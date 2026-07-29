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

__virtualname__ = "opnsense_unbound"


def __virtual__():
    if "opnsense.search" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


def _get_reconfigure(reconfigure):
    return _common_get_reconfigure(reconfigure, "unbound")


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
        return None, f"parent {parent} must be FQDN like cluster.example.com or UUID"
    hn, dom = parent.split(".", 1)
    rows = _do_search("host_override", search_phrase=hn)
    for r in rows:
        if r.get("hostname") == hn and r.get("domain") == dom:
            uuid = r.get("uuid")
            if uuid:
                return uuid, None
    rows_all = _do_search("host_override")
    for r in rows_all:
        if r.get("hostname") == hn and r.get("domain") == dom:
            uuid = r.get("uuid")
            if uuid:
                return uuid, None
        if f"{r.get('hostname')}.{r.get('domain')}" == parent:
            uuid = r.get("uuid")
            if uuid:
                return uuid, None
    return None, f"parent host_override {parent} not found — ensure unbound host_override exists"


def _find_alias(hostname, domain):
    rows = _do_search("host_alias", search_phrase=hostname)
    for r in rows:
        if r.get("hostname") == hostname and r.get("domain") == domain:
            return r
    rows_all = _do_search("host_alias")
    for r in rows_all:
        if r.get("hostname") == hostname and r.get("domain") == domain:
            return r
    return None


def alias_present(name, parent, domain=None, description=None, enabled=True, reconfigure=True):
    """
    Ensure a single unbound host alias exists.

    Delightful single-alias state — human parent FQDN, not UUID. Reconfigure
    auto-inferred to unbound/service/reconfigure.

    Args:
        name: hostname or FQDN (e.g. www or www.example.com)
        parent: parent host override FQDN (e.g. cluster.example.com) or UUID.
                Human FQDN is auto-resolved to UUID via search.
        domain: domain part (e.g. example.com). Required when name is a bare
                hostname; auto-extracted from name when name is a FQDN.
        description: optional description, default "managed by salt - fqdn"
        enabled: bool or "1"/"0", default True
        reconfigure: True/None = auto-infer unbound/service/reconfigure,
                     False = skip, str path = explicit.

    Example SLS - single:
        www:
          opnsense_unbound.alias_present:
            - parent: cluster.example.com
            - domain: example.com

    Example SLS - explicit FQDN:
        www.example.com:
          opnsense_unbound.alias_present:
            - parent: cluster.example.com
            - description: "www dashboard"

    CLI:
        salt opnsense-router state.apply opnsense.aliases_delightful
        salt opnsense-router opnsense_unbound.list_aliases_pretty --out=table

    sys.doc:
        salt opnsense-router sys.doc opnsense_unbound.alias_present
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    hostname = name.strip().strip(".")
    if "." in name:
        parts = name.split(".", 1)
        if len(parts) == 2 and parts[1]:
            hostname = parts[0]
            if domain is None:
                domain = parts[1]
    else:
        if domain is None:
            ret["comment"] = "domain is required when name is a bare hostname"
            return ret

    if not hostname:
        ret["comment"] = "hostname empty"
        return ret

    parent_uuid, err = _resolve_parent(parent)
    if not parent_uuid:
        ret["comment"] = f"failed to resolve parent {parent}: {err}"
        return ret

    existing = _find_alias(hostname, domain)

    desc = description or f"managed by salt - {hostname}.{domain}"
    enabled_str = "1" if enabled else "0"
    if isinstance(enabled, str):
        enabled_str = "1" if enabled in ("1", "true", "True", "yes", "enabled") else "0"
    if isinstance(enabled, int):
        enabled_str = "1" if enabled else "0"

    desired_data = {
        "enabled": enabled_str,
        "host": parent_uuid,
        "hostname": hostname,
        "domain": domain,
        "description": desc,
    }
    payload = {"alias": desired_data}

    if existing is None:
        if __opts__.get("test"):
            ret["result"] = None
            ret["comment"] = f"alias {hostname}.{domain} would be created -> {parent}"
            ret["changes"] = {"added": f"{hostname}.{domain} -> {parent}"}
            return ret
        try:
            __salt__["opnsense.add"]("unbound", "settings", "host_alias", payload)
            ret["changes"] = {"added": f"{hostname}.{domain} -> {parent}"}
            ret["result"] = True
            ret["comment"] = f"alias {hostname}.{domain} created -> {parent}"
            rc = _get_reconfigure(reconfigure)
            if rc:
                pr = _parse_reconfigure(rc)
                if pr:
                    try:
                        __salt__["opnsense.reconfigure"](
                            pr["module"], pr["controller"], pr["action"]
                        )
                        ret["comment"] += f" and reconfigured {rc}"
                    except Exception as e:
                        ret["comment"] += f" but reconfigure {rc} failed: {e}"
                        ret["result"] = False
            return ret
        except Exception as exc:
            ret["comment"] = f"add failed: {exc}"
            return ret

    diff = diff_models(existing, desired_data, parent_human=parent)

    if not diff:
        ret["result"] = True
        ret["comment"] = f"alias {hostname}.{domain} already present -> {parent}"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"alias {hostname}.{domain} would be updated"
        ret["changes"] = diff
        return ret

    try:
        uuid = existing.get("uuid")
        __salt__["opnsense.set_item"]("unbound", "settings", "host_alias", uuid, payload)
        ret["changes"] = diff
        ret["result"] = True
        ret["comment"] = f"alias {hostname}.{domain} updated"
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                try:
                    __salt__["opnsense.reconfigure"](pr["module"], pr["controller"], pr["action"])
                    ret["comment"] += f" and reconfigured {rc}"
                except Exception as e:
                    ret["comment"] += f" but reconfigure {rc} failed: {e}"
                    ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"set failed: {exc}"
        return ret


def alias_absent(name, domain=None, reconfigure=True):
    """
    Ensure an unbound host alias is absent.

    Args:
        name: hostname or FQDN to remove
        domain: domain if name is bare hostname; auto-extracted from name when
                name is a FQDN
        reconfigure: auto-inferred by default

    Example:
        remove_old_old-git:
          opnsense_unbound.alias_absent:
            - name: old-git
            - domain: example.com

        # or full FQDN:
        remove_old:
          opnsense_unbound.alias_absent:
            - name: old-git.example.com

    sys.doc:
        salt opnsense-router sys.doc opnsense_unbound.alias_absent
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    hostname = name.strip().strip(".")
    if "." in hostname:
        parts = hostname.split(".", 1)
        hn = parts[0]
        dom = parts[1] if parts[1] else domain
        hostname = hn
        domain = dom
    elif domain is None:
        ret["comment"] = "domain is required when name is a bare hostname"
        return ret
    if not hostname:
        ret["comment"] = "hostname empty"
        return ret

    existing = _find_alias(hostname, domain)
    if existing is None:
        ret["result"] = True
        ret["comment"] = f"alias {hostname}.{domain} already absent"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"alias {hostname}.{domain} would be deleted"
        ret["changes"] = {"deleted": existing.get("uuid")}
        return ret

    try:
        uuid = existing.get("uuid")
        __salt__["opnsense.delete"]("unbound", "settings", "host_alias", uuid)
        ret["changes"] = {"deleted": f"{hostname}.{domain}"}
        ret["result"] = True
        ret["comment"] = f"alias {hostname}.{domain} deleted"
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                try:
                    __salt__["opnsense.reconfigure"](pr["module"], pr["controller"], pr["action"])
                    ret["comment"] += f" and reconfigured {rc}"
                except Exception as e:
                    ret["comment"] += f" but reconfigure failed: {e}"
                    ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"delete failed: {exc}"
        return ret


def aliases_managed(
    name, parent, aliases=None, purge=None, descriptions=None, enabled=True, reconfigure=True
):
    """
    Batch manage many unbound aliases — one state, one reconfigure.

    Replaces Jinja loops: previously 2 loops × N hosts = N states + N reconfigures.
    Now 1 state, single reconfigure, parent as human FQDN.

    Args:
        name: arbitrary state name (e.g. dns)
        parent: parent host FQDN like cluster.example.com or UUID. Also auto-read
                from pillar opnsense:cluster_parent if None.
        aliases: dict domain->[hostnames] like {"example.com": [www, git]}.
                 If None, reads pillar opnsense:aliases.
        purge: dict domain->[hostnames] to delete. Reads pillar opnsense:purge_aliases if None.
        descriptions: optional dict fqdn->description
        enabled: bool
        reconfigure: auto-inferred by default, single reconfigure at end

    Pillar-driven delightful:
        opnsense:
          cluster_parent: {hostname: cluster, domain: example.com}
          aliases:
            example.com: [git, www]
            internal.example.com: [code]
          purge_aliases:
            example.com: [old-git]

    Example SLS explicit:
        dns_batch:
          opnsense_unbound.aliases_managed:
            - parent: cluster.example.com
            - aliases:
                example.com:
                  - www
                  - git
            - purge:
                example.com:
                  - old-git

    Example SLS pillar-direct (zero Jinja):
        dns:
          opnsense_dns.managed:
            - name: dns
            # parent/aliases/purge auto-read from pillar

    CLI preview:
        salt opnsense-router opnsense_dns.managed_preview
        salt opnsense-router state.apply opnsense.aliases_delightful test=True

    sys.doc:
        salt opnsense-router sys.doc opnsense_unbound.aliases_managed
        salt opnsense-router sys.doc opnsense_dns.managed
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    descriptions = descriptions or {}

    if aliases is None:
        try:
            pillar = __pillar__ or {}
            aliases = pillar.get("opnsense", {}).get("aliases", {})
        except Exception:
            aliases = {}
    if purge is None:
        try:
            pillar = __pillar__ or {}
            purge = pillar.get("opnsense", {}).get("purge_aliases", {})
        except Exception:
            purge = {}

    if parent is None:
        try:
            pillar = __pillar__ or {}
            cp = pillar.get("opnsense", {}).get("cluster_parent", {})
            if isinstance(cp, dict) and cp.get("uuid"):
                parent = cp["uuid"]
            elif isinstance(cp, dict) and cp.get("hostname"):
                parent = f"{cp['hostname']}.{cp.get('domain', 'example.com')}"
        except Exception:
            pass

    if not parent:
        ret["comment"] = (
            "parent required — provide parent: cluster.example.com or from pillar opnsense:cluster_parent"
        )
        return ret

    parent_uuid, err = _resolve_parent(parent)
    if not parent_uuid:
        ret["comment"] = f"parent resolve failed {parent}: {err}"
        return ret

    if not isinstance(aliases, dict):
        ret["comment"] = f"aliases must be dict domain->list, got {type(aliases)}"
        return ret
    if not isinstance(purge, dict):
        purge = {}

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
            if not hn:
                continue
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
            f"would manage {len(desired)} aliases ({len(to_add)} to add, {len(to_upd)} to update, {len(to_del)} to purge)"
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
    if total_changed:
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                try:
                    __salt__["opnsense.reconfigure"](pr["module"], pr["controller"], pr["action"])
                    ret["comment"] = (
                        f"managed {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged and reconfigured {rc}"
                    )
                except Exception as exc:
                    ret["comment"] = f"managed aliases but reconfigure {rc} failed: {exc}"
                    ret["result"] = False
                    ret["changes"] = changes
                    return ret
            else:
                ret["comment"] = (
                    f"managed {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged"
                )
        else:
            ret["comment"] = (
                f"managed {len(desired)} aliases, {len(added)} added, {len(updated)} updated, {len(deleted)} purged"
            )
        ret["changes"] = changes
        ret["result"] = True
    else:
        ret["comment"] = (
            f"{len(desired)} aliases already present, {len(deleted)} purged already absent"
        )
        ret["result"] = True

    return ret
