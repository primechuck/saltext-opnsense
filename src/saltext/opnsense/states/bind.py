import logging

from saltext.opnsense.utils.common import (
    get_reconfigure as _common_get_reconfigure,
)
from saltext.opnsense.utils.common import (
    is_uuid as _is_uuid,
)
from saltext.opnsense.utils.common import (
    normalize_enabled as _normalize_enabled,
)
from saltext.opnsense.utils.common import (
    parse_reconfigure_path as _parse_reconfigure,
)
from saltext.opnsense.utils.common import (
    strip_salt_internal_kwargs as _strip_salt_internal_kwargs,
)
from saltext.opnsense.utils.diff import diff_models

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_bind"


def __virtual__():
    """
    Only load if opnsense execution module is available.
    """
    try:
        salt_dunder = __salt__
    except NameError:
        # No Salt dunder in test harness - allow import
        return True
    if "opnsense.search" in salt_dunder:
        return True
    return (False, "opnsense execution module not loaded")


def _verify_reconfigure_call(module: str, controller: str, action: str = "reconfigure"):
    """
    Consistent reconfigure verification, mirroring opnsense state.
    Returns (ok, error_message).
    """
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


def _get_reconfigure(reconfigure):
    return _common_get_reconfigure(reconfigure, "bind")


def _search(controller, type_name, search_phrase="", row_count=-1):
    try:
        res = __salt__["opnsense.search"](
            "bind", controller, type_name, search_phrase=search_phrase, row_count=row_count
        )
        return res.get("rows", []) if isinstance(res, dict) else []
    except Exception as exc:
        log.debug("bind search %s/%s failed: %s", controller, type_name, exc)
        return []


def _search_domains_all():
    all_rows = []
    for t in (
        "primary_domain",
        "secondary_domain",
        "forward_domain",
        "master_domain",
        "slave_domain",
        "domain",
    ):
        try:
            rows = _search("domain", t, row_count=-1)
            for r in rows:
                # Preserve actual bind type for correct delete - fix for domain_absent bug
                if isinstance(r, dict):
                    r = dict(r)
                    r["_bind_type"] = t
                    r.setdefault("_bind_controller", "domain")
                all_rows.append(r)
        except Exception:
            continue
    dedup = {}
    for r in all_rows:
        uuid = r.get("uuid")
        key = uuid or r.get("domainname") or r.get("domain")
        if key and key not in dedup:
            dedup[key] = r
        else:
            # If we already have entry but new entry has more specific _bind_type, keep it
            if key and key in dedup:
                existing = dedup[key]
                # Prefer keeping existing unless it lacks _bind_type
                if not existing.get("_bind_type") and r.get("_bind_type"):
                    dedup[key] = r
    return list(dedup.values())


def _resolve_domain(domain):
    if not domain:
        return None, "domain required"
    if _is_uuid(domain):
        return domain, None
    domain = str(domain).strip()
    rows = _search_domains_all()
    for r in rows:
        if r.get("domainname") == domain or r.get("domain") == domain or r.get("name") == domain:
            uuid = r.get("uuid")
            if uuid:
                return uuid, None
    return None, f"domain {domain} not found"


def _find_domain(domainname):
    rows = _search_domains_all()
    for r in rows:
        if r.get("domainname") == domainname:
            return r
    return None


def domain_present(
    name, domain_type="primary", description=None, enabled=True, reconfigure=True, **kwargs
):
    """
    Ensure a BIND primary/secondary/forward domain exists.

    Args:
        name: domain name like example.com
        domain_type: primary, secondary, forward — default primary
        description: optional description
        enabled: bool
        reconfigure: auto-inferred to bind/service/reconfigure by default

    Example:
        example.com domain:
          opnsense_bind.domain_present:
            - name: example.com
            - description: "example.com primary"

        internal.example.com:
          opnsense_bind.domain_present:
            - name: internal.example.com
            - domain_type: primary

    sys.doc:
        salt opnsense-router sys.doc opnsense_bind.domain_present
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    # Strip Salt internal kwargs (__pub_*, etc.) - salty best practice
    if kwargs:
        kwargs = _strip_salt_internal_kwargs(kwargs)
    existing = _find_domain(name)

    type_name = "primary_domain"
    if domain_type in ("primary", "primary_domain"):
        type_name = "primary_domain"
    elif domain_type in ("secondary", "secondary_domain"):
        type_name = "secondary_domain"
    elif domain_type in ("forward", "forward_domain"):
        type_name = "forward_domain"
    else:
        type_name = domain_type

    enabled_str = _normalize_enabled(enabled)

    desc = description or f"managed by salt - {name}"
    data = {
        "enabled": enabled_str,
        "domainname": name,
        "description": desc,
    }
    data.update(kwargs)

    payload = (
        {"domain": data}
        if type_name in ("domain", "primary_domain", "secondary_domain")
        else {type_name: data}
    )
    if type_name == "primary_domain":
        payload = {"domain": data}

    if existing is None:
        if __opts__.get("test"):
            ret["result"] = None
            ret["comment"] = f"domain {name} would be created"
            ret["changes"] = {"added": name}
            return ret
        try:
            __salt__["opnsense.add"]("bind", "domain", type_name, payload)
            ret["changes"] = {"added": name}
            ret["result"] = True
            ret["comment"] = f"domain {name} created"
            rc = _get_reconfigure(reconfigure)
            if rc:
                pr = _parse_reconfigure(rc)
                if pr:
                    ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                    if ok:
                        ret["comment"] += f" and reconfigured {rc}"
                    else:
                        ret["comment"] += f" but reconfigure {rc} failed: {err}"
                        ret["result"] = False
            return ret
        except Exception as exc:
            ret["comment"] = f"add failed: {exc}"
            return ret

    diff = diff_models(existing, data)

    if not diff:
        ret["result"] = True
        ret["comment"] = f"domain {name} already present"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"domain {name} would be updated"
        ret["changes"] = diff
        return ret

    try:
        uuid = existing.get("uuid")
        __salt__["opnsense.set_item"]("bind", "domain", type_name, uuid, payload)
        ret["changes"] = diff
        ret["result"] = True
        ret["comment"] = f"domain {name} updated"
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                if ok:
                    ret["comment"] += f" and reconfigured {rc}"
                else:
                    ret["comment"] += f" but reconfigure {rc} failed: {err}"
                    ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"set failed: {exc}"
        return ret


def domain_absent(name, reconfigure=True):
    """
    Ensure a BIND domain is absent.

    Example:
        remove_old:
          opnsense_bind.domain_absent:
            - name: old.example.com

    sys.doc:
        salt opnsense-router sys.doc opnsense_bind.domain_absent
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    existing = _find_domain(name)
    if existing is None:
        ret["result"] = True
        ret["comment"] = f"domain {name} already absent"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"domain {name} would be deleted"
        ret["changes"] = {"deleted": existing.get("uuid")}
        return ret

    try:
        uuid = existing.get("uuid")
        # Fix bug: use actual _bind_type instead of always primary_domain
        actual_type = (
            existing.get("_bind_type") or existing.get("_bind_type_original") or "primary_domain"
        )
        # Normalize type - ensure it's one of known types, fallback to primary_domain if invalid
        if actual_type not in (
            "primary_domain",
            "secondary_domain",
            "forward_domain",
            "master_domain",
            "slave_domain",
            "domain",
        ):
            # If type looks like domain_type string (primary/secondary/forward), map it
            mapping = {
                "primary": "primary_domain",
                "secondary": "secondary_domain",
                "forward": "forward_domain",
                "master": "master_domain",
                "slave": "slave_domain",
            }
            actual_type = mapping.get(actual_type, "primary_domain")
        __salt__["opnsense.delete"]("bind", "domain", actual_type, uuid)
        ret["changes"] = {"deleted": name}
        ret["result"] = True
        ret["comment"] = f"domain {name} deleted (type {actual_type})"
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                if ok:
                    ret["comment"] += f" and reconfigured {rc}"
                else:
                    ret["comment"] += f" but reconfigure {rc} failed: {err}"
                    ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"delete failed: {exc}"
        return ret


def record_present(
    name, domain, type="A", value=None, ttl=None, enabled=True, description=None, reconfigure=True
):
    """
    Ensure a BIND DNS record exists. Human domain name, not UUID — auto-resolved.

    Args:
        name: record name like www, www, @
        domain: parent zone example.com — auto-resolved to UUID
        type: record type A, AAAA, CNAME, MX, TXT etc
        value: record value like 192.0.2.10 or cname target
        ttl: optional TTL
        enabled: bool
        reconfigure: auto-inferred to bind/service/reconfigure
        description: optional description

    Example - convenience:
        www A record:
          opnsense_bind.record_present:
            - name: www
            - domain: example.com
            - type: A
            - value: 192.0.2.10

        wildcard CNAME:
          opnsense_bind.record_present:
            - name: "*.apps"
            - domain: example.com
            - type: CNAME
            - value: cluster.example.com

    Example - pillar direct:
        # pillar opnsense:bind_zone: {example.com: {A: {www: 192.0.2.10}}}

    CLI:
        salt opnsense-router opnsense_bind.list_records domain=example.com
        salt opnsense-router opnsense_bind.list_records_pretty domain=example.com --out=table

    sys.doc:
        salt opnsense-router sys.doc opnsense_bind.record_present
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    if value is None:
        ret["comment"] = "value required for record_present"
        return ret

    domain_uuid, err = _resolve_domain(domain)
    if not domain_uuid:
        ret["comment"] = f"domain resolve failed for {domain}: {err}"
        return ret

    rows = _search("record", "record", search_phrase=name)
    existing = None
    for r in rows:
        if r.get("name") == name and (r.get("domain") == domain_uuid or r.get("domain") == domain):
            if r.get("type", type) == type:
                existing = r
                break
    if not existing:
        all_rows = _search("record", "record")
        for r in all_rows:
            if r.get("name") == name and (
                r.get("domain") == domain_uuid or r.get("domain") == domain
            ):
                if r.get("type") == type:
                    existing = r
                    break

    enabled_str = _normalize_enabled(enabled)

    data = {
        "enabled": enabled_str,
        "domain": domain_uuid,
        "name": name,
        "type": type,
        "value": value,
    }
    if ttl is not None:
        data["ttl"] = str(ttl)
    if description:
        data["description"] = description

    payload = {"record": data}

    if existing is None:
        if __opts__.get("test"):
            ret["result"] = None
            ret["comment"] = f"record {name}.{domain} {type} {value} would be created"
            ret["changes"] = {"added": f"{name}.{domain}"}
            return ret
        try:
            __salt__["opnsense.add"]("bind", "record", "record", payload)
            ret["changes"] = {"added": f"{name}.{domain} {type} {value}"}
            ret["result"] = True
            ret["comment"] = f"record {name}.{domain} created"
            rc = _get_reconfigure(reconfigure)
            if rc:
                pr = _parse_reconfigure(rc)
                if pr:
                    ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                    if ok:
                        ret["comment"] += f" and reconfigured {rc}"
                    else:
                        ret["comment"] += f" but reconfigure {rc} failed: {err}"
                        ret["result"] = False
            return ret
        except Exception as exc:
            ret["comment"] = f"add failed: {exc}"
            return ret

    diff = diff_models(existing, data, parent_human=domain)

    if not diff:
        ret["result"] = True
        ret["comment"] = f"record {name}.{domain} already present"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"record {name}.{domain} would be updated"
        ret["changes"] = diff
        return ret

    try:
        uuid = existing.get("uuid")
        __salt__["opnsense.set_item"]("bind", "record", "record", uuid, payload)
        ret["changes"] = diff
        ret["result"] = True
        ret["comment"] = f"record {name}.{domain} updated"
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                if ok:
                    ret["comment"] += f" and reconfigured {rc}"
                else:
                    ret["comment"] += f" but reconfigure {rc} failed: {err}"
                    ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"set failed: {exc}"
        return ret


def record_absent(name, domain, type="A", reconfigure=True):
    """
    Ensure a BIND record is absent.

    Example:
        remove_old:
          opnsense_bind.record_absent:
            - name: old
            - domain: example.com
            - type: A

    sys.doc:
        salt opnsense-router sys.doc opnsense_bind.record_absent
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    domain_uuid, err = _resolve_domain(domain)
    if not domain_uuid:
        domain_uuid = domain

    rows = _search("record", "record", search_phrase=name)
    existing = None
    for r in rows:
        if r.get("name") == name and (r.get("domain") == domain_uuid or r.get("domain") == domain):
            if not type or r.get("type") == type:
                existing = r
                break
    if not existing:
        all_rows = _search("record", "record")
        for r in all_rows:
            if r.get("name") == name and (
                r.get("domain") == domain_uuid or r.get("domain") == domain
            ):
                if not type or r.get("type") == type:
                    existing = r
                    break

    if existing is None:
        ret["result"] = True
        ret["comment"] = f"record {name}.{domain} already absent"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"record {name}.{domain} would be deleted"
        ret["changes"] = {"deleted": existing.get("uuid")}
        return ret

    try:
        uuid = existing.get("uuid")
        __salt__["opnsense.delete"]("bind", "record", "record", uuid)
        ret["changes"] = {"deleted": f"{name}.{domain}"}
        ret["result"] = True
        ret["comment"] = f"record {name}.{domain} deleted"
        rc = _get_reconfigure(reconfigure)
        if rc:
            pr = _parse_reconfigure(rc)
            if pr:
                ok, err = _verify_reconfigure_call(pr["module"], pr["controller"], pr["action"])
                if ok:
                    ret["comment"] += f" and reconfigured {rc}"
                else:
                    ret["comment"] += f" but reconfigure {rc} failed: {err}"
                    ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"delete failed: {exc}"
        return ret
