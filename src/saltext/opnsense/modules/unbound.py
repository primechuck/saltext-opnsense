import logging

from saltext.opnsense.utils.common import is_uuid

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_unbound"


def __virtual__():
    """
    Only load if base opnsense execution module is available.
    """
    try:
        salt_dunder = __salt__
    except NameError:
        return True
    if (
        "opnsense.search" in salt_dunder
        or "opnsense.call" in salt_dunder
        or "opnsense_unbound.list_aliases" in salt_dunder
    ):
        return True
    return (False, "opnsense execution module not loaded")


def _search(type_name, search_phrase="", row_count=-1):
    try:
        fn = __salt__["opnsense.search"]
        res = fn("unbound", "settings", type_name, search_phrase=search_phrase, row_count=row_count)
        if isinstance(res, dict):
            return res.get("rows", [])
        return []
    except Exception as exc:
        log.debug("unbound search %s failed: %s", type_name, exc)
        return []


def _list_host_overrides_raw():
    return _search("host_override", row_count=-1)


def _list_aliases_raw():
    return _search("host_alias", row_count=-1)


def _build_host_map():
    rows = _list_host_overrides_raw()
    uuid_to_fqdn = {}
    fqdn_to_uuid = {}
    fqdn_to_row = {}
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
            fqdn_to_row[fqdn] = r
    return uuid_to_fqdn, fqdn_to_uuid, fqdn_to_row


def list_host_overrides():
    """
    List unbound host overrides keyed by FQDN with IP and metadata.

    CLI:
        salt opnsense-router opnsense_unbound.list_host_overrides
        salt opnsense-router opnsense_unbound.list_host_overrides --out=yaml
    """
    rows = _list_host_overrides_raw()
    result = {}
    for r in rows:
        hn = r.get("hostname", "")
        dom = r.get("domain", "")
        if not hn or not dom:
            continue
        fqdn = f"{hn}.{dom}"
        result[fqdn] = {
            "hostname": hn,
            "domain": dom,
            "ip": r.get("server") or r.get("ip") or r.get("address") or "",
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_host_overrides_simple():
    """
    Simple mapping FQDN -> IP. Perfect for table outputter.

    CLI:
        salt opnsense-router opnsense_unbound.list_host_overrides_simple --out=table
    """
    data = list_host_overrides()
    return {fqdn: info["ip"] for fqdn, info in data.items()}


def list_host_overrides_pretty():
    """
    Pretty list of "fqdn -> ip (enabled) [uuid8]" for humans.

    CLI:
        salt opnsense-router opnsense_unbound.list_host_overrides_pretty --out=table
        salt opnsense-router opnsense_unbound.list_host_overrides_pretty | xargs -I{} echo {}
    """
    data = list_host_overrides()
    lines = []
    for fqdn in sorted(data):
        info = data[fqdn]
        en = "enabled" if info.get("enabled") else "disabled"
        lines.append(f"{fqdn} -> {info.get('ip')} ({en}) [{info.get('uuid', '')[:8]}]")
    return lines


def list_aliases(domain=None, parent=None):
    """
    List unbound host aliases keyed by FQDN with parent resolution.

    Args:
        domain: filter by domain like example.com
        parent: filter by parent FQDN or UUID like cluster.example.com

    CLI:
        salt opnsense-router opnsense_unbound.list_aliases
        salt opnsense-router opnsense_unbound.list_aliases domain=example.com
        salt opnsense-router opnsense_unbound.list_aliases parent=cluster.example.com --out=table
    """
    uuid_to_fqdn, fqdn_to_uuid, _ = _build_host_map()
    rows = _list_aliases_raw()
    result = {}
    parent_filter_uuid = None
    parent_filter_fqdn = None
    if parent:
        if is_uuid(parent):
            parent_filter_uuid = parent
        else:
            parent_filter_fqdn = parent
            if parent in fqdn_to_uuid:
                parent_filter_uuid = fqdn_to_uuid[parent]

    for r in rows:
        hn = r.get("hostname", "")
        dom = r.get("domain", "")
        if not hn or not dom:
            continue
        if domain and dom != domain:
            continue
        fqdn = f"{hn}.{dom}"
        host_uuid = r.get("host") or r.get("host_uuid") or ""
        parent_fqdn = uuid_to_fqdn.get(host_uuid, host_uuid)

        if parent_filter_uuid and host_uuid != parent_filter_uuid:
            if parent_filter_fqdn and parent_fqdn != parent_filter_fqdn:
                continue
            elif not parent_filter_fqdn:
                continue
        if parent_filter_fqdn and not parent_filter_uuid:
            if parent_fqdn != parent_filter_fqdn:
                continue

        result[fqdn] = {
            "hostname": hn,
            "domain": dom,
            "parent": parent_fqdn,
            "parent_uuid": host_uuid,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
        }
    return dict(sorted(result.items()))


def list_aliases_simple(domain=None, parent=None):
    """
    Simple mapping FQDN -> parent FQDN. Chef/Puppet friendly, easy table output.

    CLI:
        salt opnsense-router opnsense_unbound.list_aliases_simple --out=table
        salt opnsense-router opnsense_unbound.list_aliases_simple domain=example.com parent=cluster.example.com
    """
    data = list_aliases(domain=domain, parent=parent)
    return {fqdn: info["parent"] for fqdn, info in data.items()}


def list_aliases_mapping():
    """
    Alias to list_aliases_simple for backward compatibility.
    """
    return list_aliases_simple()


def list_aliases_pretty(domain=None, parent=None):
    """
    Pretty list of "fqdn -> parent (enabled)" for humans. Use with --out=table.

    This is the convenience CLI helper that users expect:
        salt opnsense-router opnsense_unbound.list_aliases_pretty --out=table
        salt opnsense-router opnsense_dns.list_aliases_pretty --out=table

    Returns list of strings like "www.example.com -> cluster.example.com (enabled)"
    Salt's table outputter formats it nicely.
    """
    data = list_aliases(domain=domain, parent=parent)
    lines = []
    for fqdn in sorted(data):
        info = data[fqdn]
        en = "enabled" if info.get("enabled") else "disabled"
        lines.append(f"{fqdn} -> {info.get('parent')} ({en})")
    return lines


def list_aliases_simple_pretty(domain=None, parent=None):
    """
    Alias to list_aliases_pretty for backward compat.
    """
    return list_aliases_pretty(domain=domain, parent=parent)


def list_forwards():
    rows = _search("forward", row_count=-1)
    result = {}
    for r in rows:
        dom = r.get("domain", "") or r.get("zone", "")
        srv = r.get("server", "") or r.get("address", "")
        result[dom] = {
            "domain": dom,
            "server": srv,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
            "raw": r,
        }
    return result


def list_dots():
    rows = _search("dot", row_count=-1)
    result = {}
    for r in rows:
        dom = r.get("domain", "") or r.get("zone", "") or r.get("name", "")
        result[dom] = {
            "domain": dom,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
            "raw": r,
        }
    return result


def list_acls():
    rows = _search("acl", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("name", "") or r.get("network", "") or r.get("uuid", "")
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
            "raw": r,
        }
    return result


def get_alias(hostname, domain):
    aliases = list_aliases(domain=domain)
    fqdn = f"{hostname}.{domain}"
    return aliases.get(fqdn)


def get_host_override(hostname, domain):
    overrides = list_host_overrides()
    fqdn = f"{hostname}.{domain}"
    return overrides.get(fqdn)


def resolve_parent(parent):
    if not parent:
        return None
    if is_uuid(parent):
        return parent
    _, fqdn_to_uuid, _ = _build_host_map()
    if parent in fqdn_to_uuid:
        return fqdn_to_uuid[parent]
    if "." in parent:
        hn, dom = parent.split(".", 1)
        rows = _list_host_overrides_raw()
        for r in rows:
            if r.get("hostname") == hn and r.get("domain") == dom:
                return r.get("uuid")
    return None


def list_overrides():
    return list_host_overrides()


def list_overrides_pretty():
    return list_host_overrides_pretty()
