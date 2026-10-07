import logging

log = logging.getLogger(__name__)
__virtualname__ = "opnsense_dns"


def __virtual__():
    try:
        dunder = __salt__
    except NameError:
        return True
    if "opnsense.search" in dunder or "opnsense.call" in dunder:
        return True
    return (False, "opnsense execution module not loaded")


def _pillar():
    try:
        p = __pillar__ or {}
        return p.get("opnsense", {}) if isinstance(p, dict) else {}
    except Exception:
        return {}


def _search(t: str):
    try:
        fn = __salt__["opnsense.search"]
        res = fn("unbound", "settings", t, row_count=-1)
        return res.get("rows", []) if isinstance(res, dict) else []
    except Exception as exc:
        log.debug("search %s failed: %s", t, exc)
        return []


def _host_map():
    rows = _search("host_override")
    uuid_to_fqdn = {}
    fqdn_to_uuid = {}
    for r in rows:
        hn = r.get("hostname", "")
        dom = r.get("domain", "")
        if not hn or not dom:
            continue
        fqdn = f"{hn}.{dom}"
        uuid = r.get("uuid")
        if uuid:
            uuid_to_fqdn[uuid] = fqdn
            fqdn_to_uuid[fqdn] = uuid
    return uuid_to_fqdn, fqdn_to_uuid


def list_aliases(domain=None, parent=None):
    uuid_to_fqdn, fqdn_to_uuid = _host_map()
    rows = _search("host_alias")
    result = {}
    pf_uuid = None
    pf_fqdn = None
    if parent:
        from saltext.opnsense.utils.common import is_uuid as _is_uuid

        if _is_uuid(parent):
            pf_uuid = parent
        else:
            pf_fqdn = parent
            pf_uuid = fqdn_to_uuid.get(parent)
    for r in rows:
        hn = r.get("hostname")
        dom = r.get("domain")
        if not hn or not dom:
            continue
        if domain and dom != domain:
            continue
        fqdn = f"{hn}.{dom}"
        hu = r.get("host") or ""
        pf = uuid_to_fqdn.get(hu, hu)
        if pf_uuid and hu != pf_uuid and (not pf_fqdn or pf != pf_fqdn):
            continue
        if pf_fqdn and not pf_uuid and pf != pf_fqdn:
            continue
        result[fqdn] = {
            "hostname": hn,
            "domain": dom,
            "parent": pf,
            "parent_uuid": hu,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
        }
    return dict(sorted(result.items()))


def list_aliases_detailed(domain=None, parent=None):
    return list_aliases(domain=domain, parent=parent)


def list_aliases_simple(domain=None, parent=None):
    data = list_aliases(domain=domain, parent=parent)
    return {fqdn: info.get("parent") for fqdn, info in data.items()}


def managed_preview(parent=None, aliases=None, purge=None):
    p = _pillar()
    aliases_p = p.get("aliases", {}) if aliases is None else aliases
    purge_p = p.get("purge_aliases", {}) if purge is None else purge
    parent_p = p.get("cluster_parent", {}) if parent is None else parent
    if parent is None:
        if isinstance(parent_p, dict) and parent_p.get("hostname"):
            parent = f"{parent_p['hostname']}.{parent_p.get('domain', 'example.com')}"
        else:
            parent = parent_p
    live = list_aliases()
    desired = {f"{h}.{dom}" for dom, hosts in (aliases_p or {}).items() for h in (hosts or [])}
    purged = {f"{h}.{dom}" for dom, hosts in (purge_p or {}).items() for h in (hosts or [])}
    return {
        "parent": parent,
        "desired": sorted(desired),
        "purge": sorted(purged),
        "live_count": len(live),
        "live": live,
    }
