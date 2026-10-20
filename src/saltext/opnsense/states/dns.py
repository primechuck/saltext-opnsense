import logging

log = logging.getLogger(__name__)
from saltext.opnsense.utils.common import get_reconfigure as _get_rc
from saltext.opnsense.utils.common import is_uuid as _is_uuid
from saltext.opnsense.utils.common import normalize_enabled as _norm_en
from saltext.opnsense.utils.common import parse_reconfigure_path as _parse_rc
from saltext.opnsense.utils.diff import diff_models

__virtualname__ = "opnsense_dns"


def __virtual__():
    try:
        sd = __salt__
    except NameError:
        return True
    if "opnsense.search" in sd or "opnsense.call" in sd:
        return True
    return (False, "opnsense execution module not loaded")


def _search(t: str, phrase: str = ""):
    try:
        fn = __salt__["opnsense.search"]  # type: ignore
        res = fn("unbound", "settings", t, search_phrase=phrase, row_count=-1)
        return res.get("rows", []) if isinstance(res, dict) else []
    except Exception as exc:
        log.debug("search %s failed: %s", t, exc)
        return []


def _resolve_parent(parent):
    if not parent:
        return None, "parent required"
    if _is_uuid(parent):
        return parent, None
    if isinstance(parent, dict):
        if parent.get("uuid") and _is_uuid(parent["uuid"]):
            return parent["uuid"], None
        hn = parent.get("hostname")
        dom = parent.get("domain")
        if hn and dom:
            return _resolve_parent(f"{hn}.{dom}")
    if not isinstance(parent, str):
        return None, f"unsupported parent type {type(parent)}"
    parent = parent.strip()
    if _is_uuid(parent):
        return parent, None
    if "." not in parent:
        return None, f"parent {parent} must be FQDN"
    hn, dom = parent.split(".", 1)
    for row in _search("host_override", hn):
        if row.get("hostname") == hn and row.get("domain") == dom:
            if row.get("uuid"):
                return row["uuid"], None
    for row in _search("host_override"):
        if f"{row.get('hostname')}.{row.get('domain')}" == parent and row.get("uuid"):
            return row["uuid"], None
    return None, f"parent {parent} not found"


def _verify_rc(module: str, controller: str, action: str = "reconfigure"):
    try:
        res = __salt__["opnsense.reconfigure"](module, controller, action)  # type: ignore
        if isinstance(res, dict):
            st = str(res.get("status", "")).lower()
            rs = str(res.get("result", "")).lower()
            if st in ("failed", "error") or rs in ("failed", "error"):
                return False, str(res.get("message") or res.get("error") or res)
        elif isinstance(res, str) and res.lower() in ("failed", "error"):
            return False, res
        return True, ""
    except Exception as exc:
        return False, str(exc)


def managed(
    name,
    parent=None,
    aliases=None,
    purge=None,
    descriptions=None,
    enabled=True,
    reconfigure=True,
    **kwargs,
):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    descriptions = descriptions or {}
    pillar = {}
    try:
        pillar = __pillar__ or {}  # type: ignore
    except Exception:
        pillar = {}
    opnsense_pillar = pillar.get("opnsense", {}) if isinstance(pillar, dict) else {}
    if aliases is None:
        aliases = opnsense_pillar.get("aliases", {})
    if purge is None:
        purge = opnsense_pillar.get("purge_aliases", {})
    if parent is None:
        cp = opnsense_pillar.get("cluster_parent", {})
        if isinstance(cp, dict) and cp.get("uuid") and _is_uuid(cp["uuid"]):
            parent = cp["uuid"]
        elif isinstance(cp, dict) and cp.get("hostname") and cp.get("domain"):
            parent = f"{cp['hostname']}.{cp['domain']}"
        elif isinstance(cp, str) and cp:
            parent = cp
    if not isinstance(aliases, dict):
        ret["comment"] = f"aliases must be dict got {type(aliases)}"
        return ret
    if not isinstance(purge, dict):
        purge = {}
    if not parent:
        ret["comment"] = (
            "parent required – set opnsense:cluster_parent in pillar or pass parent: cluster.example.com"
        )
        return ret
    parent_uuid, err = _resolve_parent(parent)
    if not parent_uuid:
        ret["comment"] = f"parent resolve failed {parent}: {err}"
        return ret

    all_rows = _search("host_alias")
    existing_map = {}
    for r in all_rows:
        hn = r.get("hostname")
        dom = r.get("domain")
        if hn and dom:
            existing_map[(hn, dom)] = r

    desired = []
    for dom, hosts in aliases.items():
        if not isinstance(hosts, (list, tuple, set)):
            continue
        for hn in hosts:
            hn = str(hn).strip()
            if hn:
                desired.append((hn, dom))

    purge_list = []
    for dom, hosts in purge.items():
        if not isinstance(hosts, (list, tuple, set)):
            continue
        for hn in hosts:
            hn = str(hn).strip()
            if hn:
                purge_list.append((hn, dom))

    enabled_str = _norm_en(enabled)

    if __opts__.get("test"):  # type: ignore
        to_add = []
        to_upd = []
        to_del = []
        for hn, dom in desired:
            key = (hn, dom)
            if key not in existing_map:
                to_add.append(f"{hn}.{dom}")
            else:
                cur = existing_map[key]
                fqdn = f"{hn}.{dom}"
                desc = descriptions.get(fqdn) or descriptions.get(hn) or f"managed by salt - {fqdn}"
                desired_data = {
                    "enabled": enabled_str,
                    "host": parent_uuid,
                    "hostname": hn,
                    "domain": dom,
                    "description": desc,
                }
                if diff_models(cur, desired_data, parent_human=parent):
                    to_upd.append(fqdn)
        for hn, dom in purge_list:
            if (hn, dom) in existing_map:
                to_del.append(f"{hn}.{dom}")
        ret["result"] = None
        ret["comment"] = (
            f"[dns managed:{name}] would ensure {len(desired)} aliases ({len(to_add)} add, {len(to_upd)} upd, {len(to_del)} purge) -> {parent}"
        )
        ch = {}
        if to_add:
            ch["would_add"] = to_add
        if to_upd:
            ch["would_update"] = to_upd
        if to_del:
            ch["would_delete"] = to_del
        ret["changes"] = ch
        return ret

    changes = {}
    added = []
    updated = []
    errors = []
    for hn, dom in desired:
        fqdn = f"{hn}.{dom}"
        desc = descriptions.get(fqdn) or descriptions.get(hn) or f"managed by salt - {fqdn}"
        desired_data = {
            "enabled": enabled_str,
            "host": parent_uuid,
            "hostname": hn,
            "domain": dom,
            "description": desc,
        }
        payload = {"alias": desired_data}
        existing = existing_map.get((hn, dom))
        try:
            if existing is None:
                __salt__["opnsense.add"]("unbound", "settings", "host_alias", payload)  # type: ignore
                added.append(fqdn)
                changes[fqdn] = {"action": "added", "parent": parent}
            else:
                if diff_models(existing, desired_data, parent_human=parent):
                    __salt__["opnsense.set_item"](
                        "unbound", "settings", "host_alias", existing.get("uuid"), payload
                    )  # type: ignore
                    updated.append(fqdn)
                    changes[fqdn] = {"action": "updated", "parent": parent}
        except Exception as exc:
            errors.append(f"{fqdn}: {exc}")

    deleted = []
    for hn, dom in purge_list:
        existing = existing_map.get((hn, dom))
        if existing:
            try:
                __salt__["opnsense.delete"](
                    "unbound", "settings", "host_alias", existing.get("uuid")
                )  # type: ignore
                fqdn = f"{hn}.{dom}"
                deleted.append(fqdn)
                changes[fqdn] = {"action": "deleted"}
            except Exception as exc:
                errors.append(f"{hn}.{dom} purge: {exc}")

    if errors:
        ret["comment"] = "; ".join(errors)
        ret["result"] = False
        ret["changes"] = changes
        return ret

    total_changed = len(added) + len(updated) + len(deleted)
    rc = _get_rc(reconfigure, "unbound")
    if total_changed and rc:
        pr = _parse_rc(rc)
        if pr:
            ok, err = _verify_rc(pr["module"], pr["controller"], pr["action"])
            if not ok:
                ret["comment"] = f"managed but reconfigure {rc} failed: {err}"
                ret["result"] = False
                ret["changes"] = changes
                return ret
    if total_changed:
        ret["comment"] = (
            f"[dns managed:{name}] {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged -> {parent}"
        )
        ret["changes"] = changes
        ret["result"] = True
    else:
        ret["comment"] = f"[dns managed:{name}] {len(desired)} aliases already present -> {parent}"
        ret["result"] = True
    return ret


def aliases_managed(
    name,
    parent,
    aliases=None,
    purge=None,
    descriptions=None,
    enabled=True,
    reconfigure=True,
    **kwargs,
):
    return managed(
        name,
        parent=parent,
        aliases=aliases,
        purge=purge,
        descriptions=descriptions,
        enabled=enabled,
        reconfigure=reconfigure,
    )
