from __future__ import annotations

import logging
import socket

log = logging.getLogger(__name__)
from saltext.opnsense.utils.common import is_uuid as _is_uuid
from saltext.opnsense.utils.common import parse_reconfigure_path as _parse_rc
from saltext.opnsense.utils.diff import diff_models

__virtualname__ = "opnsense"

# Minimal reconfigure defaults – needed for auto reconfigure
_RECONFIGURE_DEFAULTS = {
    "unbound": "unbound/service/reconfigure",
    "bind": "bind/service/reconfigure",
    "kea": "kea/service/reconfigure",
    "acmeclient": "acmeclient/service/reconfigure",
    "firewall": "firewall/alias/reconfigure",
}
_RECONFIGURE_OVERRIDES = {
    ("unbound", "settings"): "unbound/service/reconfigure",
    ("bind", "domain"): "bind/service/reconfigure",
    ("bind", "record"): "bind/service/reconfigure",
    ("kea", "dhcpv4"): "kea/service/reconfigure",
    ("kea", "dhcpv6"): "kea/service/reconfigure",
    ("acmeclient", "accounts"): "acmeclient/service/reconfigure",
    ("acmeclient", "validations"): "acmeclient/service/reconfigure",
    ("acmeclient", "certificates"): "acmeclient/service/reconfigure",
    ("firewall", "alias"): "firewall/alias/reconfigure",
    ("firewall", "filter"): "firewall/filter_base/apply",
    ("firewall", "filter", "rule"): "firewall/filter_base/apply",
}

_RESOLVE_MAP = {
    "host": {
        "module": "unbound",
        "controller": "settings",
        "type": "host_override",
        "field": "hostname",
    },
    "subnet": {"module": "kea", "controller": "dhcpv4", "type": "subnet", "field": "subnet"},
    "domain": {
        "module": "bind",
        "controller": "domain",
        "type": "primary_domain",
        "field": "domainname",
    },
    "account": {
        "module": "acmeclient",
        "controller": "accounts",
        "type": "account",
        "field": "name",
    },
    "validationMethod": {
        "module": "acmeclient",
        "controller": "validations",
        "type": "validation",
        "field": "name",
    },
    "validation": {
        "module": "acmeclient",
        "controller": "validations",
        "type": "validation",
        "field": "name",
    },
    "action": {"module": "acmeclient", "controller": "actions", "type": "action", "field": "name"},
}


def __virtual__():
    from saltext.opnsense.utils.common import is_salt_version_ok as _ok

    v = _ok((3008,))
    if v is not True:
        return v
    try:
        sd = __salt__
    except NameError:
        return True
    if not sd:
        return True
    if "opnsense.call" in sd or "opnsense.search" in sd:
        return True
    return (False, "opnsense execution module not loaded")


def _search_fn():
    try:
        return __salt__["opnsense.search"]  # type: ignore[name-defined]
    except Exception:
        try:
            return globals().get("__salt__", {}).get("opnsense.search")
        except Exception:
            return None


def _do_search(module: str, controller: str, typ: str, phrase: str = ""):
    fn = _search_fn()
    if not fn:
        return []
    try:
        res = fn(module, controller, typ, search_phrase=phrase, row_count=-1)
        return res.get("rows", []) if isinstance(res, dict) else []
    except Exception as exc:
        log.debug("search %s/%s/%s failed: %s", module, controller, typ, exc)
        return []


def _resolve_host_single(value):
    cfg = _RESOLVE_MAP["host"]
    if isinstance(value, dict):
        hn = value.get("hostname")
        dom = value.get("domain")
        if not hn or not dom:
            return value
        for phrase in (hn, "", f"{hn}.{dom}"):
            for row in _do_search(cfg["module"], cfg["controller"], cfg["type"], phrase):
                if row.get("hostname") == hn and row.get("domain") == dom and row.get("uuid"):
                    return row["uuid"]
        return value
    if not isinstance(value, str):
        return value
    if _is_uuid(value):
        return value
    if "." in value:
        hn, dom = value.split(".", 1)
        for phrase in (hn, "", value):
            for row in _do_search(cfg["module"], cfg["controller"], cfg["type"], phrase):
                if row.get("hostname") == hn and row.get("domain") == dom and row.get("uuid"):
                    return row["uuid"]
    return value


def _resolve_subnet_single(value):
    if not isinstance(value, str) or _is_uuid(value) or "/" not in value:
        return value
    cfg = _RESOLVE_MAP["subnet"]
    for phrase in (value, ""):
        for row in _do_search(cfg["module"], cfg["controller"], cfg["type"], phrase):
            if row.get("subnet") == value and row.get("uuid"):
                return row["uuid"]
        rows = _do_search(cfg["module"], cfg["controller"], cfg["type"], value)
        if len(rows) == 1 and rows[0].get("uuid"):
            return rows[0]["uuid"]
    return value


def _resolve_generic_single(value, cfg):
    if not isinstance(value, str) or _is_uuid(value) or not value:
        return value
    sf = cfg.get("field", "name")
    for phrase in (value, ""):
        for row in _do_search(cfg["module"], cfg["controller"], cfg["type"], phrase):
            if str(row.get(sf, "")) == value or str(row.get("name", "")) == value:
                if row.get("uuid"):
                    return row["uuid"]
        if phrase == value:
            rows = _do_search(cfg["module"], cfg["controller"], cfg["type"], "")
            if (
                len(rows) == 1
                and rows[0].get("uuid")
                and value.lower() in str(rows[0].get(sf, "")).lower()
            ):
                return rows[0]["uuid"]
    return value


def _should_resolve(field: str, module: str) -> bool:
    base = field[:-5] if field.endswith("_uuid") else field
    cfg = _RESOLVE_MAP.get(field) or _RESOLVE_MAP.get(base)
    if not cfg:
        if field == "host":
            return module == "unbound"
        if field == "subnet":
            return module == "kea"
        return False
    # module gating per type
    t = cfg["type"]
    if t == "host_override":
        return module == "unbound"
    if t == "subnet":
        return module == "kea"
    if t == "primary_domain":
        return module == "bind"
    if t in ("account", "validation", "action"):
        return module == "acmeclient"
    return True


def _resolve_ref(field: str, value, module: str = ""):
    if value is None:
        return value
    if isinstance(value, str) and _is_uuid(value):
        return value
    if not _should_resolve(field, module):
        return value
    base = field[:-5] if field.endswith("_uuid") else field
    cfg = _RESOLVE_MAP.get(field) or _RESOLVE_MAP.get(base)
    if not cfg:
        return value
    if cfg["type"] == "host_override":
        return _resolve_host_single(value)
    if cfg["type"] == "subnet":
        return _resolve_subnet_single(value)
    return _resolve_generic_single(value, cfg)


def _auto_resolve(data: dict, module: str = "") -> dict:
    if not isinstance(data, dict):
        return data
    for k, v in list(data.items()):
        if k == "uuid":
            continue
        if isinstance(v, (str, dict)):
            rv = _resolve_ref(k, v, module)
            if rv != v:
                data[k] = rv
    return data


def _infer_reconfigure(module: str, controller: str, type_name: str | None = None):
    for key in [(module, controller, type_name), (module, controller), (module,)]:
        if key in _RECONFIGURE_OVERRIDES:
            return _parse_rc(_RECONFIGURE_OVERRIDES[key])
    if module in _RECONFIGURE_DEFAULTS:
        return _parse_rc(_RECONFIGURE_DEFAULTS[module])
    # fallback heuristics
    try:
        from saltext.opnsense.utils.api_spec import list_controllers

        ctrls = list_controllers(module)
        if "service" in ctrls:
            return {"module": module, "controller": "service", "action": "reconfigure"}
    except Exception:
        pass
    return {"module": module, "controller": controller or "service", "action": "reconfigure"}


def _get_reconfigure(module: str, controller: str, type_name: str | None, reconfigure_arg):
    if reconfigure_arg is False:
        return None
    if reconfigure_arg is None or reconfigure_arg is True:
        return _infer_reconfigure(module, controller, type_name)
    if isinstance(reconfigure_arg, str):
        s = reconfigure_arg.strip()
        if s.lower() in ("auto", "infer", "true", "yes", ""):
            return _infer_reconfigure(module, controller, type_name)
        parsed = _parse_rc(s)
        return parsed or _infer_reconfigure(module, controller, type_name)
    if isinstance(reconfigure_arg, dict):
        return reconfigure_arg
    return _infer_reconfigure(module, controller, type_name)


def _verify_reconfigure(module: str, controller: str, action: str = "reconfigure"):
    try:
        res = __salt__["opnsense.reconfigure"](module, controller, action)  # type: ignore[name-defined]
        if isinstance(res, dict):
            status = str(res.get("status", "")).lower()
            result = str(res.get("result", "")).lower()
            if status in ("failed", "error") or result in ("failed", "error"):
                msg = res.get("message") or res.get("error") or res.get("validations") or res
                return False, str(msg)
        elif isinstance(res, str) and res.lower() in ("failed", "error"):
            return False, res
        return True, ""
    except Exception as exc:
        return False, str(exc)


def _extract_payload(type_name: str, data: dict) -> dict:
    if not isinstance(data, dict):
        return {}
    if type_name in data and isinstance(data[type_name], dict):
        return data
    # OPNsense model name mapping: host_alias->alias, host_override->host, primary_domain->domain, etc.
    mapping = {
        "host_alias": "alias",
        "host_override": "host",
        "primary_domain": "domain",
        "reservation": "reservation",
        "subnet": "subnet",
        "account": "account",
        "validation": "validation",
        "certificate": "certificate",
        "action": "action",
        "record": "record",
        "item": "alias",
        "rule": "rule",
    }
    key = mapping.get(type_name, type_name)
    # also handle generic: if type contains '_' take last part
    if key == type_name and "_" in type_name:
        key = type_name.split("_")[-1]
    return {key: data}


def item_present(
    name, module, controller, type, data=None, match=None, reconfigure=None, search_field=None
):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    data = data or {}
    match = match or {}
    # unwrap if payload already wrapped
    if len(data) == 1 and isinstance(list(data.values())[0], dict):
        flat = list(data.values())[0]
    else:
        flat = data
    if not isinstance(flat, dict):
        ret["comment"] = "data must be dict"
        return ret
    # auto-resolve relations host/subnet/account etc
    flat = _auto_resolve(dict(flat), module)

    fn_search = _search_fn()
    found = None
    try:
        if fn_search:
            rows = []
            # try search_field or match
            search_phrase = ""
            if search_field and isinstance(flat, dict) and search_field in flat:
                search_phrase = str(flat.get(search_field) or "")
            elif match:
                # use first match value as phrase for efficiency
                for v in match.values():
                    if isinstance(v, str) and v:
                        search_phrase = v
                        break
            res = fn_search(module, controller, type, search_phrase=search_phrase, row_count=-1)
            rows = res.get("rows", []) if isinstance(res, dict) else []
            if not rows and search_phrase:
                res2 = fn_search(module, controller, type, search_phrase="", row_count=-1)
                rows = res2.get("rows", []) if isinstance(res2, dict) else []
            for row in rows:
                ok = True
                for k, v in (match or {}).items():
                    if str(row.get(k, "")) != str(v):
                        ok = False
                        break
                if ok:
                    found = row
                    break
            if not found and not match:
                # if no match provided, use flat keys
                for row in rows:
                    ok = True
                    for k, v in flat.items():
                        if k in ("enabled",):
                            continue
                        if k in row and str(row.get(k)) != str(v):
                            ok = False
                            break
                    if ok:
                        found = row
                        break
    except Exception as exc:
        log.debug("item_present search failed: %s", exc)

    if __opts__.get("test"):  # type: ignore[name-defined]
        if found:
            diff = diff_models(found, flat)
            if not diff:
                ret["result"] = True
                ret["comment"] = f"{name} already present"
                return ret
            ret["result"] = None
            ret["comment"] = f"{name} would be updated"
            ret["changes"] = diff
            return ret
        ret["result"] = None
        ret["comment"] = f"{name} would be created"
        ret["changes"] = {"new": flat}
        return ret

    try:
        if not found:
            # create
            payload = _extract_payload(type, flat)
            res = __salt__["opnsense.add"](module, controller, type, payload)  # type: ignore[name-defined]
            ret["changes"] = {"added": res}
        else:
            diff = diff_models(found, flat)
            if not diff:
                ret["result"] = True
                ret["comment"] = f"{name} already present"
                return ret
            payload = _extract_payload(type, flat)
            res = __salt__["opnsense.set_item"](
                module, controller, type, found.get("uuid"), payload
            )  # type: ignore[name-defined]
            ret["changes"] = diff
        rc = _get_reconfigure(module, controller, type, reconfigure)
        if rc:
            ok, err = _verify_reconfigure(rc["module"], rc["controller"], rc["action"])
            if not ok:
                ret["result"] = False
                ret["comment"] = (
                    f"reconfigure {rc['module']}/{rc['controller']}/{rc['action']} failed: {err}"
                )
                return ret
        ret["result"] = True
        ret["comment"] = f"{name} present"
        return ret
    except Exception as exc:
        ret["comment"] = str(exc)
        ret["result"] = False
        return ret


def item_absent(name, module, controller, type, match=None, reconfigure=None, search_field=None):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    match = match or {}
    fn = _search_fn()
    found = None
    try:
        if fn:
            res = fn(module, controller, type, row_count=-1)
            rows = res.get("rows", []) if isinstance(res, dict) else []
            for row in rows:
                ok = True
                for k, v in match.items():
                    if str(row.get(k, "")) != str(v):
                        ok = False
                        break
                if ok:
                    found = row
                    break
    except Exception as exc:
        log.debug("item_absent search failed: %s", exc)

    if __opts__.get("test"):  # type: ignore[name-defined]
        if not found:
            ret["result"] = True
            ret["comment"] = f"{name} already absent"
            return ret
        ret["result"] = None
        ret["comment"] = f"{name} would be deleted"
        ret["changes"] = {"deleted": found.get("uuid")}
        return ret

    if not found:
        ret["result"] = True
        ret["comment"] = f"{name} already absent"
        return ret

    try:
        res = __salt__["opnsense.delete"](module, controller, type, found.get("uuid"))  # type: ignore[name-defined]
        ret["changes"] = {"deleted": found.get("uuid")}
        rc = _get_reconfigure(module, controller, type, reconfigure)
        if rc:
            ok, err = _verify_reconfigure(rc["module"], rc["controller"], rc["action"])
            if not ok:
                ret["result"] = False
                ret["comment"] = (
                    f"reconfigure {rc['module']}/{rc['controller']}/{rc['action']} failed: {err} but {name} deleted"
                )
                return ret
        ret["result"] = True
        ret["comment"] = f"{name} deleted"
        return ret
    except Exception as exc:
        ret["comment"] = str(exc)
        ret["result"] = False
        return ret


def reconfigured(name, module, controller, action="reconfigure"):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    if __opts__.get("test"):  # type: ignore[name-defined]
        ret["result"] = None
        ret["comment"] = f"{module}/{controller}/{action} would be applied"
        return ret
    try:
        ok, err = _verify_reconfigure(module, controller, action)
        if not ok:
            ret["result"] = False
            ret["comment"] = f"{module}/{controller}/{action} failed: {err}"
            return ret
        ret["result"] = True
        ret["comment"] = f"{module}/{controller}/{action} applied"
        ret["changes"] = {"reconfigured": f"{module}/{controller}/{action}"}
        return ret
    except Exception as exc:
        ret["comment"] = str(exc)
        ret["result"] = False
        return ret


def items_present(name, module, controller, type, items, reconfigure=None, search_field=None):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    if __opts__.get("test"):  # type: ignore[name-defined]
        ret["result"] = None
        ret["comment"] = f"{name} would manage {len(items)} items"
        return ret
    changes = {}
    errors = []
    for it in items:
        iname = it.get("name") or it.get("hostname") or str(it)
        idata = it.get("data") or {k: v for k, v in it.items() if k not in ("name",)}
        imatch = it.get("match") or {}
        res = item_present(
            iname, module, controller, type, data=idata, match=imatch, reconfigure=False
        )
        if res["result"] is False:
            errors.append(f"{iname}: {res['comment']}")
        if res["changes"]:
            changes[iname] = res["changes"]
    if errors:
        ret["comment"] = "; ".join(errors)
        ret["result"] = False
        ret["changes"] = changes
        return ret
    rc = _get_reconfigure(module, controller, type, reconfigure)
    if rc and changes:
        ok, err = _verify_reconfigure(rc["module"], rc["controller"], rc["action"])
        if not ok:
            ret["result"] = False
            ret["comment"] = f"reconfigure failed: {err}"
            ret["changes"] = changes
            return ret
    ret["result"] = True
    ret["comment"] = f"{name} {len(changes)} items managed"
    ret["changes"] = changes
    return ret


def items_absent(name, module, controller, type, items, reconfigure=None, search_field=None):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    if __opts__.get("test"):  # type: ignore[name-defined]
        ret["result"] = None
        ret["comment"] = f"{name} would delete {len(items)} items"
        return ret
    changes = {}
    errors = []
    for it in items:
        iname = it.get("name") or str(it)
        imatch = it.get("match") or it if isinstance(it, dict) else {}
        if "name" in imatch:
            imatch = {k: v for k, v in imatch.items() if k != "name"}
        res = item_absent(iname, module, controller, type, match=imatch, reconfigure=False)
        if res["result"] is False:
            errors.append(f"{iname}: {res['comment']}")
        if res["changes"]:
            changes[iname] = res["changes"]
    if errors:
        ret["comment"] = "; ".join(errors)
        ret["result"] = False
        ret["changes"] = changes
        return ret
    rc = _get_reconfigure(module, controller, type, reconfigure)
    if rc and changes:
        ok, err = _verify_reconfigure(rc["module"], rc["controller"], rc["action"])
        if not ok:
            ret["result"] = False
            ret["comment"] = f"reconfigure failed: {err}"
            ret["changes"] = changes
            return ret
    ret["result"] = True
    ret["comment"] = f"{name} {len(changes)} items absent"
    ret["changes"] = changes
    return ret


def assert_resolves(name, hostname, expected_ip, server=None, timeout=10, ttl=60):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    # try localData search first
    try:
        fn = (
            __salt__.get("opnsense.call")
            if isinstance(__salt__, dict)
            else __salt__["opnsense.call"]
        )  # type: ignore
        res = (
            fn("unbound", "diagnostics", "getLocalData", data={}, method="POST")
            if callable(fn)
            else {}
        )
        txt = str(res)
        if expected_ip in txt:
            ret["result"] = True
            ret["comment"] = f"{hostname} resolves to {expected_ip} via localData"
            return ret
    except Exception:
        pass
    try:
        ip = socket.gethostbyname(hostname)
        if ip == expected_ip:
            ret["result"] = True
            ret["comment"] = f"{hostname} -> {ip}"
        else:
            ret["comment"] = f"{hostname} -> {ip} expected {expected_ip}"
            ret["result"] = False
        return ret
    except Exception as exc:
        ret["comment"] = f"resolve {hostname} failed: {exc}"
        ret["result"] = False
        return ret
