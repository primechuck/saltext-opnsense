import logging

from saltext.opnsense.utils.common import is_uuid as _is_uuid

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_firewall"


def __virtual__():
    if "opnsense.search" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


def _search(controller, type_name, search_phrase="", row_count=-1):
    try:
        fn = __salt__["opnsense.search"]
        res = fn("firewall", controller, type_name, search_phrase=search_phrase, row_count=row_count)
        if isinstance(res, dict):
            return res.get("rows", [])
        return []
    except Exception as exc:
        log.debug("firewall search %s/%s failed: %s", controller, type_name, exc)
        return []




def list_aliases(search_phrase="", row_count=-1):
    rows = _search("alias", "item", search_phrase=search_phrase, row_count=row_count)
    result = {}
    for r in rows:
        name = r.get("name") or r.get("uuid") or ""
        if not name:
            continue
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "type": r.get("type") or "",
            "content": r.get("content") or r.get("address") or "",
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_aliases_simple(search_phrase=""):
    return {k: v["content"] for k, v in list_aliases(search_phrase=search_phrase).items()}


def list_aliases_pretty(search_phrase=""):
    data = list_aliases(search_phrase=search_phrase)
    lines = []
    for name in sorted(data):
        info = data[name]
        lines.append(f"{name} type={info.get('type')} content={info.get('content')} ({'enabled' if info.get('enabled') else 'disabled'})")
    return lines


def list_rules(search_phrase="", row_count=-1):
    rows = _search("filter", "rule", search_phrase=search_phrase, row_count=row_count)
    result = {}
    for r in rows:
        descr = r.get("description") or r.get("descr") or r.get("uuid") or ""
        key = descr or r.get("uuid") or str(id(r))
        result[key] = {
            "description": descr,
            "uuid": r.get("uuid"),
            "action": r.get("action") or "",
            "interface": r.get("interface") or "",
            "protocol": r.get("protocol") or "",
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_rules_pretty(search_phrase=""):
    data = list_rules(search_phrase=search_phrase)
    lines = []
    for descr in sorted(data):
        info = data[descr]
        lines.append(f"{descr} action={info.get('action')} iface={info.get('interface')} proto={info.get('protocol')}")
    return lines


def get_alias(name):
    return list_aliases().get(name)


def resolve_alias(name_or_uuid):
    if not name_or_uuid:
        return None
    if _is_uuid(name_or_uuid):
        return name_or_uuid
    aliases = list_aliases()
    if name_or_uuid in aliases:
        return aliases[name_or_uuid]["uuid"]
    rows = _search("alias", "item", search_phrase=name_or_uuid, row_count=-1)
    for r in rows:
        if r.get("name") == name_or_uuid and r.get("uuid"):
            return r["uuid"]
    return None
