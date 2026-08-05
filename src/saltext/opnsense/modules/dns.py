import logging

from saltext.opnsense.utils.common import strip_salt_internal_kwargs as _strip_salt_internal_kwargs

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dns"


def __virtual__():
    """
    Only load if base opnsense execution module is available.
    """
    try:
        salt_dunder = __salt__
    except NameError:
        return True
    if "opnsense.search" in salt_dunder or "opnsense.call" in salt_dunder or "opnsense_unbound.list_aliases" in salt_dunder:
        return True
    return (False, "opnsense execution module not loaded")



def _pillar_aliases():
    try:
        pillar = __pillar__ or {}
        op = pillar.get("opnsense", {}) if isinstance(pillar, dict) else {}
        return op.get("aliases", {}), op.get("purge_aliases", {}), op.get("cluster_parent", {})
    except Exception:
        return {}, {}, {}


def list_aliases(domain=None, parent=None):
    """
    List DNS aliases as dict fqdn -> info.

    Convenience alternative to raw search. Returns sorted dict keyed by FQDN.

    Example:
        salt opnsense-router opnsense_dns.list_aliases
        salt opnsense-router opnsense_dns.list_aliases domain=example.com
        salt opnsense-router opnsense_dns.list_aliases parent=cluster.example.com
    """
    try:
        fn = __salt__["opnsense_unbound.list_aliases"]
        return fn(domain=domain, parent=parent)
    except Exception:
        try:
            fn = __salt__["opnsense.search"]
            res = fn("unbound", "settings", "host_alias", row_count=-1)
            rows = res.get("rows", []) if isinstance(res, dict) else []
            result = {}
            for r in rows:
                hn = r.get("hostname")
                dom = r.get("domain")
                if not hn or not dom:
                    continue
                if domain and dom != domain:
                    continue
                fqdn = f"{hn}.{dom}"
                result[fqdn] = r.get("host")
            return result
        except Exception as exc:
            log.debug("dns list_aliases failed: %s", exc)
            return {}


def list_aliases_detailed(domain=None, parent=None):
    """
    Alias to list_aliases returning full info dict.

    Example:
        salt opnsense-router opnsense_dns.list_aliases_detailed
    """
    try:
        fn = __salt__["opnsense_unbound.list_aliases"]
        return fn(domain=domain, parent=parent)
    except Exception:
        return list_aliases(domain=domain, parent=parent)


def list_aliases_simple(domain=None, parent=None):
    """
    Simple mapping fqdn -> parent FQDN. Great for CLI --out=table.

    Example:
        salt opnsense-router opnsense_dns.list_aliases_simple --out=table
        salt opnsense-router opnsense_dns.list_aliases_simple domain=example.com
    """
    try:
        fn = __salt__["opnsense_unbound.list_aliases_simple"]
        return fn(domain=domain, parent=parent)
    except Exception:
        try:
            fn = __salt__["opnsense_unbound.list_aliases"]
            data = fn(domain=domain, parent=parent)
            return {
                fqdn: info.get("parent") if isinstance(info, dict) else info
                for fqdn, info in data.items()
            }
        except Exception:
            data = list_aliases(domain=domain, parent=parent)
            return {
                fqdn: info.get("parent") if isinstance(info, dict) else str(info)
                for fqdn, info in data.items()
            }


def list_aliases_pretty(domain=None, parent=None):
    """
    Pretty list of "fqdn -> parent (enabled)" for human output. Works with --out=table.

    Example:
        salt opnsense-router opnsense_dns.list_aliases_pretty --out=table
        salt opnsense-router opnsense_dns.list_aliases_pretty domain=example.com --out=table
    """
    try:
        fn = __salt__["opnsense_unbound.list_aliases_pretty"]
        return fn(domain=domain, parent=parent)
    except Exception:
        pass
    try:
        fn = __salt__["opnsense_unbound.list_aliases"]
        data = fn(domain=domain, parent=parent)
    except Exception:
        data = list_aliases(domain=domain, parent=parent)
    lines = []
    for fqdn in sorted(data):
        info = data[fqdn]
        if isinstance(info, dict):
            parent_f = info.get("parent", "")
            en = (
                "enabled" if info.get("enabled") else "disabled" if "enabled" in info else "enabled"
            )
            lines.append(f"{fqdn} -> {parent_f} ({en})")
        else:
            lines.append(f"{fqdn} -> {info}")
    return lines


def list_aliases_simple_pretty(domain=None, parent=None):
    """
    Alias to list_aliases_pretty for backward compat.
    """
    return list_aliases_pretty(domain=domain, parent=parent)


def list_pillar_aliases():
    aliases, purge, parent = _pillar_aliases()
    return {
        "aliases": aliases,
        "purge_aliases": purge,
        "cluster_parent": parent,
    }


def resolve_parent(parent=None):
    if parent:
        try:
            fn = __salt__["opnsense_unbound.resolve_parent"]
            return fn(parent)
        except Exception:
            return None
    _, _, cp = _pillar_aliases()
    if isinstance(cp, dict) and cp.get("uuid"):
        return cp["uuid"]
    if isinstance(cp, dict) and cp.get("hostname"):
        try:
            fn = __salt__["opnsense_unbound.resolve_parent"]
            fqdn = f"{cp['hostname']}.{cp.get('domain', 'example.com')}"
            return fn(fqdn)
        except Exception:
            return None
    return None


def managed_preview(parent=None, aliases=None, purge=None):
    aliases_p, purge_p, parent_p = _pillar_aliases()
    if aliases is None:
        aliases = aliases_p
    if purge is None:
        purge = purge_p
    if parent is None:
        if isinstance(parent_p, dict) and parent_p.get("hostname"):
            parent = f"{parent_p['hostname']}.{parent_p.get('domain', 'example.com')}"
        else:
            parent = parent_p
    live = list_aliases()
    desired_fqdns = {f"{h}.{dom}" for dom, hosts in (aliases or {}).items() for h in (hosts or [])}
    purge_fqdns = {f"{h}.{dom}" for dom, hosts in (purge or {}).items() for h in (hosts or [])}
    return {
        "parent": parent,
        "desired": sorted(desired_fqdns),
        "purge": sorted(purge_fqdns),
        "live_count": len(live),
        "live": live,
    }
