import logging

from saltext.opnsense.utils.common import (
    get_reconfigure as _common_get_reconfigure,
)
from saltext.opnsense.utils.common import (
    is_uuid as _is_uuid,
)
from saltext.opnsense.utils.common import (
    parse_reconfigure_path as _parse_reconfigure,
)
from saltext.opnsense.utils.diff import diff_models

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dns"


def __virtual__():
    if "opnsense.search" in __salt__ or "opnsense_unbound.list_aliases" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


def _get_reconfigure(reconfigure):
    return _common_get_reconfigure(reconfigure, "unbound")


def _verify_reconfigure_call(module: str, controller: str, action: str = "reconfigure"):
    try:
        res = __salt__["opnsense.reconfigure"](module, controller, action)
        if isinstance(res, dict):
            status = str(res.get("status", "")).lower()
            result = str(res.get("result", "")).lower()
            if status in ("failed", "error") or result in ("failed", "error"):
                msg = res.get("message") or res.get("error") or res.get("validations") or res
                return False, str(msg)
        elif isinstance(res, str):
            if res.lower() in ("failed", "error"):
                return False, res
        return True, ""
    except Exception as exc:
        return False, str(exc)


def _do_search(type_name, search_phrase=""):
    try:
        res = __salt__["opnsense.search"](
            "unbound", "settings", type_name, search_phrase=search_phrase, row_count=-1
        )
        return res.get("rows", []) if isinstance(res, dict) else []
    except Exception as exc:
        log.debug("search %s failed: %s", type_name, exc)
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
        return None, f"parent {parent} must be FQDN like cluster.example.com"
    hn, dom = parent.split(".", 1)
    rows = _do_search("host_override", search_phrase=hn)
    for r in rows:
        if r.get("hostname") == hn and r.get("domain") == dom:
            uuid = r.get("uuid")
            if uuid:
                return uuid, None
    rows_all = _do_search("host_override")
    for r in rows_all:
        if f"{r.get('hostname')}.{r.get('domain')}" == parent:
            uuid = r.get("uuid")
            if uuid:
                return uuid, None
    return None, f"parent host_override {parent} not found"


def managed(
    name, parent=None, aliases=None, purge=None, descriptions=None, enabled=True, reconfigure=True
):
    """
    Pillar-driven Unbound host alias management — no Jinja loops required.

    Reads parent, aliases, and purge lists from pillar opnsense:* when not
    passed explicitly. A single state block with no args manages all DNS
    aliases declaratively from pillar.

    Pillar example (pillars/hosts/opnsense-router.sls):
        opnsense:
          cluster_parent:
            hostname: cluster
            domain: example.com
          aliases:
            example.com: [git, www, auth]
            internal.example.com: [code, ide]
          purge_aliases:
            example.com: [old-git, old-service]

    Args:
        name: State name (arbitrary, e.g. dns)
        parent: parent host override FQDN or UUID. If omitted, reads
                pillar opnsense:cluster_parent (dict with hostname/domain,
                plain string FQDN, or UUID). Required if pillar key absent.
        aliases: dict domain->list[hostname]. If omitted, reads pillar opnsense:aliases.
        purge: dict domain->list to remove. If omitted, reads pillar opnsense:purge_aliases.
        descriptions: optional dict fqdn->description
        enabled: bool, default True
        reconfigure: True/None = auto-infer unbound/service/reconfigure, False = skip

    Example SLS - fully pillar-driven (zero args, zero Jinja):
        dns:
          opnsense_dns.managed:
            - name: dns
          # reads everything from pillar

    Example SLS - explicit parent, pillar aliases:
        dns_convenience:
          opnsense_dns.managed:
            - name: dns
            - parent: cluster.example.com   # required if not in pillar
            # aliases/purge auto-read from pillar

    Example SLS - explicit everything:
        dns_batch:
          opnsense_dns.managed:
            - name: dns
            - parent: cluster.example.com
            - aliases:
                example.com:
                  - www
                  - git
            - purge:
                example.com:
                  - old-git

    CLI:
        salt opnsense-router state.apply opnsense.convenience_aliases
        salt opnsense-router state.apply opnsense.convenience_aliases test=True --out=table
        # deprecated shim still works: aliases_delightful
        salt opnsense-router opnsense_dns.managed_preview
        salt opnsense-router opnsense_dns.list_aliases_pretty --out=table

    Prometheus metrics integration (see docs/METRICS.md):
        metrics are exposed via grains opnsense_unbound_alias_count and
        opnsense_version, then written to node_exporter textfile by state
        opnsense.metrics or examples/states/metrics.sls.

    sys.doc:
        salt opnsense-router sys.doc opnsense_dns.managed
        salt opnsense-router sys.doc opnsense_dns.aliases_managed
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    descriptions = descriptions or {}

    pillar = {}
    try:
        pillar = __pillar__ or {}
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
        ret["comment"] = f"aliases must be dict domain->list, got {type(aliases)}"
        return ret
    if not isinstance(purge, dict):
        purge = {}

    if not parent:
        ret["comment"] = (
            "parent required — set opnsense:cluster_parent in pillar or pass parent: cluster.example.com"
        )
        return ret

    parent_uuid, err = _resolve_parent(parent)
    if not parent_uuid:
        ret["comment"] = f"parent resolve failed {parent}: {err}"
        return ret

    all_rows = _do_search("host_alias")
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
            if not hn:
                continue
            desired.append((hn, dom))

    purge_list = []
    for dom, hosts in purge.items():
        if not isinstance(hosts, (list, tuple, set)):
            continue
        for hn in hosts:
            hn = str(hn).strip()
            if hn:
                purge_list.append((hn, dom))

    enabled_str = "1" if enabled else "0"
    if isinstance(enabled, str):
        enabled_str = "1" if enabled in ("1", "true", "yes") else "0"

    if __opts__.get("test"):
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
                    to_upd.append(f"{hn}.{dom}")
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
                __salt__["opnsense.add"]("unbound", "settings", "host_alias", payload)
                added.append(fqdn)
                changes[fqdn] = {"action": "added", "parent": parent}
            else:
                diff = diff_models(existing, desired_data, parent_human=parent)
                if diff:
                    __salt__["opnsense.set_item"](
                        "unbound", "settings", "host_alias", existing.get("uuid"), payload
                    )
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
                )
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
    rc = _get_reconfigure(reconfigure)
    if total_changed:
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                if not ok:
                    ret["comment"] = f"managed but reconfigure {rc} failed: {err}"
                    ret["result"] = False
                    ret["changes"] = changes
                    return ret
                ret["comment"] = (
                    f"[dns managed:{name}] {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged -> {parent} and reconfigured {rc}"
                )
            else:
                ret["comment"] = (
                    f"[dns managed:{name}] {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged -> {parent}"
                )
        else:
            ret["comment"] = (
                f"[dns managed:{name}] {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged -> {parent}"
            )
        ret["changes"] = changes
        ret["result"] = True
    else:
        ret["comment"] = (
            f"[dns managed:{name}] {len(desired)} aliases already present -> {parent}, {len(deleted)} purged already absent"
        )
        ret["result"] = True

    return ret


def aliases_managed(
    name, parent, aliases=None, purge=None, descriptions=None, enabled=True, reconfigure=True
):
    """
    Alias to managed() for backward compat with opnsense_unbound.aliases_managed naming.

    See opnsense_dns.managed for full convenience docs.

    Example:
        dns_batch:
          opnsense_dns.aliases_managed:
            - parent: cluster.example.com
            - aliases:
                example.com: [www, git]

    sys.doc:
        salt opnsense-router sys.doc opnsense_dns.aliases_managed
    """
    return managed(
        name,
        parent=parent,
        aliases=aliases,
        purge=purge,
        descriptions=descriptions,
        enabled=enabled,
        reconfigure=reconfigure,
    )
