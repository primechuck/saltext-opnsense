import logging

from saltext.opnsense.utils.common import strip_salt_internal_kwargs as _strip_salt_internal_kwargs

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_acmeclient"


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



def _search(controller, type_name, search_phrase="", row_count=-1):
    try:
        fn = __salt__["opnsense.search"]
        res = fn(
            "acmeclient", controller, type_name, search_phrase=search_phrase, row_count=row_count
        )
        if isinstance(res, dict):
            return res.get("rows", [])
        return []
    except Exception as exc:
        log.debug("acmeclient search %s/%s failed: %s", controller, type_name, exc)
        return []


def _sorted_dict(d):
    return dict(sorted(d.items()))


def list_accounts():
    rows = _search("accounts", "account", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("name") or r.get("uuid") or ""
        if not name:
            continue
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "email": r.get("email") or r.get("contact") or "",
            "ca": r.get("ca") or r.get("directoryUrl") or "",
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return _sorted_dict(result)


def list_accounts_pretty():
    data = list_accounts()
    lines = []
    for name in sorted(data):
        info = data[name]
        lines.append(f"{name} [{info.get('ca')}] uuid={info.get('uuid', '')[:8]}")
    return lines


def list_validations():
    rows = _search("validations", "validation", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("name") or r.get("uuid") or ""
        if not name:
            continue
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "method": r.get("method") or r.get("validation_type") or "",
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return _sorted_dict(result)


def list_validations_pretty():
    data = list_validations()
    lines = []
    for name in sorted(data):
        info = data[name]
        lines.append(f"{name} method={info.get('method')} uuid={info.get('uuid', '')[:8]}")
    return lines


def list_actions():
    rows = _search("actions", "action", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("name") or r.get("uuid") or ""
        if not name:
            continue
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "type": r.get("type") or r.get("action_type") or "",
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return _sorted_dict(result)


def list_actions_pretty():
    data = list_actions()
    lines = []
    for name in sorted(data):
        info = data[name]
        lines.append(f"{name} type={info.get('type')} uuid={info.get('uuid', '')[:8]}")
    return lines


def list_certificates():
    rows = _search("certificates", "certificate", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("name") or r.get("common_name") or r.get("uuid") or ""
        if not name:
            continue
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "common_name": r.get("common_name") or name,
            "status": r.get("status") or r.get("last_status") or "",
            "account": r.get("account") or "",
            "enabled": r.get("enabled") in ("1", True, 1, None),
            "raw": r,
        }
    return _sorted_dict(result)


def list_certificates_simple():
    return {k: v["status"] for k, v in list_certificates().items()}


def list_certificates_pretty():
    data = list_certificates()
    lines = []
    for name in sorted(data):
        info = data[name]
        lines.append(f"{name} status={info.get('status')} uuid={info.get('uuid', '')[:8]}")
    return lines


def list_settings():
    try:
        res = __salt__["opnsense.call"]("acmeclient", "settings", "get", method="GET")
        return res
    except Exception as exc:
        log.debug("acme settings get failed: %s", exc)
        return {}


def get_account(name):
    accounts = list_accounts()
    return accounts.get(name)


def get_validation(name):
    vals = list_validations()
    return vals.get(name)


def get_certificate(name):
    certs = list_certificates()
    return certs.get(name)


def service_status():
    try:
        res = __salt__["opnsense.call"]("acmeclient", "service", "status", method="POST", data={})
        return res
    except Exception as exc:
        log.debug("acme service status failed: %s", exc)
        return {"error": str(exc)}
