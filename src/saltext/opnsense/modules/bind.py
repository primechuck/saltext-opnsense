import logging

from saltext.opnsense.utils.common import is_uuid

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_bind"


def __virtual__():
    if "opnsense.search" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


def _search(controller, type_name, search_phrase="", row_count=-1):
    try:
        fn = __salt__["opnsense.search"]
        res = fn("bind", controller, type_name, search_phrase=search_phrase, row_count=row_count)
        if isinstance(res, dict):
            return res.get("rows", [])
        return []
    except Exception as exc:
        log.debug("bind search %s/%s failed: %s", controller, type_name, exc)
        return []


def _search_domain_all():
    all_rows = []
    for c in ("domain",):
        for t in (
            "primary_domain",
            "secondary_domain",
            "forward_domain",
            "master_domain",
            "slave_domain",
            "domain",
        ):
            try:
                rows = _search(c, t, row_count=-1)
                if rows:
                    for r in rows:
                        r["_bind_type"] = t
                        r["_bind_controller"] = c
                    all_rows.extend(rows)
            except Exception:
                continue
    dedup = {}
    for r in all_rows:
        uuid = r.get("uuid")
        if uuid and uuid not in dedup:
            dedup[uuid] = r
        elif not uuid:
            key = r.get("domainname") or r.get("domain") or r.get("name")
            if key and key not in dedup:
                dedup[key] = r
    return list(dedup.values())


def list_domains(domain_type=None):
    rows = _search_domain_all()
    result = {}
    for r in rows:
        dname = r.get("domainname") or r.get("domain") or r.get("name") or ""
        if not dname:
            continue
        btype = r.get("_bind_type", "primary_domain")
        if domain_type and domain_type not in btype and domain_type != "all":
            if domain_type == "primary" and "primary" not in btype:
                continue
            if domain_type == "secondary" and "secondary" not in btype:
                continue
            if domain_type == "forward" and "forward" not in btype:
                continue
        result[dname] = {
            "domainname": dname,
            "type": btype,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_domains_simple():
    return {k: v["uuid"] for k, v in list_domains().items()}


def list_domains_pretty(domain_type=None):
    data = list_domains(domain_type=domain_type)
    lines = []
    for dname in sorted(data):
        info = data[dname]
        en = "enabled" if info.get("enabled") else "disabled"
        lines.append(f"{dname} [{info.get('type')}] ({en}) {info.get('uuid', '')[:8]}")
    return lines


def _resolve_domain_uuid(domain):
    if not domain:
        return None
    if is_uuid(domain):
        return domain
    domains = list_domains()
    if domain in domains:
        return domains[domain]["uuid"]
    for rows in [_search_domain_all()]:
        for r in rows:
            if r.get("domainname") == domain:
                return r.get("uuid")
    return None


def list_records(domain=None, domain_filter=None, record_type=None, name=None):
    if domain is None and domain_filter is not None:
        domain = domain_filter
    rows = _search("record", "record", row_count=-1)
    domain_uuid_filter = None
    domain_name_filter = None
    if domain:
        domain_uuid_filter = _resolve_domain_uuid(domain)
        if domain_uuid_filter:
            domains_map = {v["uuid"]: k for k, v in list_domains().items() if v.get("uuid")}
            domain_name_filter = domains_map.get(domain_uuid_filter, domain)
            if domain_name_filter is None or domain_name_filter == domain_uuid_filter:
                domain_name_filter = domain if "." in str(domain) else None
        else:
            domain_uuid_filter = domain if domain and len(domain) > 20 else None
            domain_name_filter = domain if "." in str(domain) else None

    result = {}
    for r in rows:
        r_domain = r.get("domain") or r.get("domain_uuid") or ""
        r_name = r.get("name") or ""
        r_type = r.get("type") or ""
        r_value = r.get("value") or r.get("server") or ""

        if domain_uuid_filter:
            if r_domain != domain_uuid_filter and r_domain != domain:
                if domain_uuid_filter and r_domain != domain_uuid_filter:
                    continue
        if record_type and r_type != record_type:
            continue
        if name and r_name != name:
            continue

        key = f"{r_name}.{domain_name_filter or r_domain}" if r_name else r.get("uuid", "")
        if not key:
            key = r.get("uuid", "")

        result[key] = {
            "name": r_name,
            "domain": domain_name_filter or r_domain,
            "domain_uuid": r_domain,
            "type": r_type,
            "value": r_value,
            "ttl": r.get("ttl", ""),
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_records_simple(domain=None, domain_filter=None):
    if domain is None and domain_filter is not None:
        domain = domain_filter
    return list_records(domain=domain)


def list_records_pretty(domain=None, domain_filter=None, record_type=None):
    if domain is None and domain_filter is not None:
        domain = domain_filter
    data = list_records(domain=domain, record_type=record_type)
    lines = []
    for key in sorted(data):
        info = data[key]
        lines.append(f"{info.get('name')} {info.get('type')} {info.get('value')}")
    return lines


def list_records_as_strings(domain=None, domain_filter=None):
    return list_records_pretty(domain=domain, domain_filter=domain_filter)


def list_acls():
    rows = _search("acl", "acl", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("name") or r.get("uuid") or ""
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "enabled": r.get("enabled") in ("1", True, 1),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_acls_pretty():
    data = list_acls()
    lines = []
    for name in sorted(data):
        info = data[name]
        lines.append(
            f"{name} ({'enabled' if info.get('enabled') else 'disabled'}) {info.get('uuid', '')[:8]}"
        )
    return lines


def get_domain(name):
    domains = list_domains()
    return domains.get(name)


def get_record(name, domain=None):
    records = list_records(domain=domain, name=name)
    for k, v in records.items():
        if v["name"] == name:
            return v
    return None


def resolve_domain(name_or_uuid):
    return _resolve_domain_uuid(name_or_uuid)


def get_domain_uuid(name_or_uuid):
    return _resolve_domain_uuid(name_or_uuid)
