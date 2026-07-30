import logging

import salt.utils.platform

log = logging.getLogger(__name__)

from saltext.opnsense.utils.common import (
    camel_to_snake as _camel_to_snake,
)
from saltext.opnsense.utils.common import (
    strip_salt_internal_kwargs as _strip_pub_kwargs,
)

try:
    from saltext.opnsense.utils.api_spec import (
        list_actions,
        list_controllers,
        list_modules,
        load_spec,
    )
    from saltext.opnsense.utils.opnsense import OPNsenseClient, get_client_from_opts

    HAS_UTILS = True
    HAS_UTILS_ERROR = ""
except ImportError as exc:
    HAS_UTILS = False
    HAS_UTILS_ERROR = str(exc)
    OPNsenseClient = None
    get_client_from_opts = None
    list_modules = lambda: []
    list_controllers = lambda m: []
    list_actions = lambda m, c: []
    load_spec = lambda: {}

__virtualname__ = "opnsense"


def __virtual__():
    if not HAS_UTILS:
        return (False, f"opnsense utils missing: {HAS_UTILS_ERROR}")
    return __virtualname__


def _get_client() -> OPNsenseClient:
    if salt.utils.platform.is_proxy() and "__proxy__" in globals() and "opnsense.call" in __proxy__:
        raise RuntimeError("proxy mode: use __proxy__ directly")
    try:
        client = get_client_from_opts(
            __opts__, pillar=__pillar__ if "__pillar__" in globals() else None
        )
        return client
    except Exception:
        if "__proxy__" in globals() and f"{__virtualname__}.call" in __proxy__:
            return None
        raise


def call(module, controller, action, uuid=None, data=None, method=None, **kwargs):
    """
    Execute a raw REST API call to OPNsense.

    CLI Example:
        salt minion opnsense.call unbound settings searchHostAlias '{"rowCount": 1}'
    """
    kwargs = _strip_pub_kwargs(kwargs)
    if kwargs:
        log.debug("opnsense.call stripping extra kwargs %s", list(kwargs.keys()))
    if salt.utils.platform.is_proxy() and "opnsense.call" in __proxy__:
        return __proxy__["opnsense.call"](module, controller, action, uuid, data, method)
    client = _get_client()
    return client.call(module, controller, action, uuid=uuid, data=data, method=method)


def search(module, controller, type_name=None, search_phrase="", row_count=-1, **kwargs):
    """
    Query an OPNsense search endpoint and unwrap the resulting rows.

    CLI Example:
        salt minion opnsense.search unbound settings host_alias search_phrase="www"
    """
    filtered = _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.search" in __proxy__:
        return __proxy__["opnsense.search"](
            module,
            controller,
            type_name,
            search_phrase=search_phrase,
            row_count=row_count,
            **filtered,
        )
    client = _get_client()
    return client.search(
        module, controller, type_name, search_phrase=search_phrase, row_count=row_count, **filtered
    )


def get(module, controller, type_name=None, uuid=None, **kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.get" in __proxy__:
        return __proxy__["opnsense.get"](module, controller, type_name, uuid)
    client = _get_client()
    return client.get(module, controller, type_name, uuid=uuid)


def add(module, controller, type_name, data, **kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.add" in __proxy__:
        return __proxy__["opnsense.add"](module, controller, type_name, data)
    client = _get_client()
    return client.add(module, controller, type_name, data)


def set_item(module, controller, type_name, uuid, data, **kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.set_item" in __proxy__:
        return __proxy__["opnsense.set_item"](module, controller, type_name, uuid, data)
    client = _get_client()
    return client.set(module, controller, type_name, uuid, data)


def delete(module, controller, type_name, uuid, **kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.delete" in __proxy__:
        return __proxy__["opnsense.delete"](module, controller, type_name, uuid)
    client = _get_client()
    return client.delete(module, controller, type_name, uuid)


def toggle(module, controller, type_name, uuid, enabled=None, **kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.toggle" in __proxy__:
        return __proxy__["opnsense.toggle"](module, controller, type_name, uuid, enabled)
    client = _get_client()
    return client.toggle(module, controller, type_name, uuid, enabled)


def reconfigure(module, controller, action="reconfigure", data=None, **kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.reconfigure" in __proxy__:
        return __proxy__["opnsense.reconfigure"](module, controller, action, data)
    client = _get_client()
    return client.reconfigure(module, controller, action, data=data)


def ping(**kwargs):
    _strip_pub_kwargs(kwargs)
    if salt.utils.platform.is_proxy() and "opnsense.ping" in __proxy__:
        return __proxy__["opnsense.ping"]()
    client = _get_client()
    for mod, ctrl, typ in [
        ("unbound", "settings", "host_alias"),
        ("bind", "domain", "primary_domain"),
        ("firewall", "alias", "item"),
        ("unbound", "settings", "host_override"),
    ]:
        try:
            client.search(mod, ctrl, typ, row_count=1)
            return True
        except Exception as exc:
            log.debug("ping attempt %s/%s/%s failed: %s", mod, ctrl, typ, exc)
            continue
    try:
        client.call(
            "unbound",
            "settings",
            "searchHostAlias",
            data={"rowCount": 1, "current": 1, "searchPhrase": ""},
            method="POST",
        )
        return True
    except Exception as exc:
        log.debug("ping fallback failed: %s", exc)
        return False


def list_api_modules(**kwargs):
    _strip_pub_kwargs(kwargs)
    return list_modules()


def list_api_controllers(module, **kwargs):
    _strip_pub_kwargs(kwargs)
    return list_controllers(module)


def list_api_actions(module, controller, **kwargs):
    _strip_pub_kwargs(kwargs)
    return list_actions(module, controller)


def spec(**kwargs):
    _strip_pub_kwargs(kwargs)
    return load_spec()


def _find_existing(module, controller, type_name, match, **kwargs):
    _strip_pub_kwargs(kwargs)
    res = search(module, controller, type_name, row_count=-1)
    rows = res.get("rows", [])
    if not rows:
        return None
    if not match:
        return None
    for row in rows:
        matched = True
        for k, v in match.items():
            rv = row.get(k)
            if str(rv) != str(v):
                matched = False
                break
        if matched:
            return row
    return None


def ensure_present(
    module, controller, type_name, data, match=None, reconfigure_path=None, **kwargs
):
    """
    Ensure an item exists (execution module backend for `opnsense.item_present`).

    CLI Example:
        salt minion opnsense.ensure_present unbound settings host_alias \\
            data='{"hostname": "www"}' match='{"hostname": "www"}'
    """
    kwargs = _strip_pub_kwargs(kwargs)
    existing = _find_existing(module, controller, type_name, match) if match else None
    if existing is None:
        result = add(module, controller, type_name, data)
        if reconfigure_path:
            mod, ctrl, act = _parse_reconfigure(reconfigure_path)
            reconfigure(mod, ctrl, act)
        return {"result": result, "changed": True, "action": "added"}

    diff = {}
    for k, v in (
        data.get(list(data.keys())[0])
        if len(data) == 1 and isinstance(list(data.values())[0], dict)
        else data
    ).items():
        if k in existing and str(existing[k]) != str(v):
            diff[k] = {"old": existing.get(k), "new": v}
        elif k not in existing:
            diff[k] = {"old": None, "new": v}

    if not diff:
        return {"result": existing, "changed": False, "action": "present"}

    uuid = existing.get("uuid")
    result = set_item(module, controller, type_name, uuid, data)
    if reconfigure_path:
        mod, ctrl, act = _parse_reconfigure(reconfigure_path)
        reconfigure(mod, ctrl, act)
    return {"result": result, "changed": True, "action": "updated", "diff": diff}


def ensure_absent(module, controller, type_name, match, reconfigure_path=None, **kwargs):
    """
    Ensure an item is absent (execution module backend for `opnsense.item_absent`).

    CLI Example:
        salt minion opnsense.ensure_absent unbound settings host_alias \\
            match='{"hostname": "www"}'
    """
    _strip_pub_kwargs(kwargs)
    existing = _find_existing(module, controller, type_name, match)
    if existing is None:
        return {"changed": False, "action": "absent"}
    uuid = existing.get("uuid")
    result = delete(module, controller, type_name, uuid)
    if reconfigure_path:
        mod, ctrl, act = _parse_reconfigure(reconfigure_path)
        reconfigure(mod, ctrl, act)
    return {"result": result, "changed": True, "action": "deleted"}


def _parse_reconfigure(path):
    if not path:
        return None, None, None
    parts = path.split("/")
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    if len(parts) == 2:
        return parts[0], parts[1], "reconfigure"
    return None, None, None


_DYNAMIC_MAP_CACHE = None


def _build_dynamic_map():
    global _DYNAMIC_MAP_CACHE
    if _DYNAMIC_MAP_CACHE is not None:
        return _DYNAMIC_MAP_CACHE
    mapping = {}
    try:
        spec_data = load_spec() or {}
        modules_dict = spec_data.get("modules") or {}
        for mod_name, controllers in modules_dict.items():
            if not isinstance(controllers, dict):
                continue
            mod_snake = _camel_to_snake(mod_name)
            for ctrl_name, actions in controllers.items():
                if not isinstance(actions, list):
                    if isinstance(actions, dict):
                        actions = list(actions.keys())
                    else:
                        continue
                ctrl_snake = _camel_to_snake(ctrl_name)
                for action in actions:
                    action_snake = _camel_to_snake(action)
                    if not action_snake:
                        continue
                    func_name = f"{mod_snake}_{ctrl_snake}_{action_snake}"
                    mapping[func_name] = (mod_name, ctrl_name, action, mod_snake, ctrl_snake, action_snake)
    except Exception as exc:
        log.debug("Failed to build dynamic map: %s", exc)
    _DYNAMIC_MAP_CACHE = mapping
    return mapping


def _make_dynamic_wrapper(mod_name, ctrl_name, action, mod_snake, ctrl_snake, action_snake, func_name):
    def wrapper(data=None, uuid=None, search_phrase="", row_count=-1, **kwargs):
        kwargs = _strip_pub_kwargs(kwargs)
        if action.lower().startswith("search"):
            return call(
                mod_name,
                ctrl_name,
                action,
                data={
                    "current": 1,
                    "rowCount": row_count,
                    "searchPhrase": search_phrase,
                    **kwargs,
                },
                method="POST",
            )
        if data is not None:
            return call(mod_name, ctrl_name, action, uuid=uuid, data=data, method="POST")
        return call(mod_name, ctrl_name, action, uuid=uuid, data={}, method="POST")

    verb_map = {
        "search": "List and search",
        "get": "Fetch",
        "add": "Create",
        "set": "Update",
        "del": "Delete",
        "delete": "Delete",
        "toggle": "Toggle enable/disable for",
        "reconfigure": "Apply and reload (reconfigure)",
        "restart": "Restart",
        "start": "Start",
        "stop": "Stop",
        "status": "Check status of",
        "apply": "Apply",
    }
    verb = "Execute"
    al = action.lower()
    for k, v in verb_map.items():
        if al.startswith(k):
            verb = v
            break

    clean = action_snake
    for prefix in [
        "search_",
        "get_",
        "add_",
        "set_",
        "del_",
        "delete_",
        "toggle_",
        "reconfigure_",
        "restart_",
        "start_",
        "stop_",
        "status_",
        "apply_",
    ]:
        if clean.startswith(prefix):
            clean = clean[len(prefix) :]
            break
    if clean in ["search", "get", "add", "set", "del", "delete", "toggle", "reconfigure", ""]:
        type_human = f"{ctrl_snake} {mod_snake}".replace("_", " ").strip()
        if not type_human:
            type_human = ctrl_snake.replace("_", " ") or mod_snake.replace("_", " ")
    else:
        type_human = clean.replace("_", " ").strip() or ctrl_snake.replace("_", " ")
    if not type_human:
        type_human = f"{mod_snake} {ctrl_snake}"
    wrapper.__name__ = func_name
    wrapper.__doc__ = f"""{verb} {type_human} in {mod_snake} {ctrl_snake}.
Auto-generated from upstream OPNsense spec.
Endpoint: POST /api/{mod_name}/{ctrl_name}/{action}
CLI: salt opnsense-router opnsense.{func_name} row_count=1 --out=table
Docs: https://docs.opnsense.org/development/api/core/{mod_name}.html"""
    return wrapper


def __getattr__(name):
    mapping = _build_dynamic_map()
    if name in mapping:
        mod_name, ctrl_name, action, mod_snake, ctrl_snake, action_snake = mapping[name]
        wrapper = _make_dynamic_wrapper(mod_name, ctrl_name, action, mod_snake, ctrl_snake, action_snake, name)
        globals()[name] = wrapper
        return wrapper
    raise AttributeError(f"module 'opnsense' has no attribute {name!r}")


def __dir__():
    base = list(globals().keys())
    try:
        base.extend(_build_dynamic_map().keys())
    except Exception:
        pass
    return sorted(set(base))


def doctor() -> dict:
    """
    Test OPNsense API connectivity, spec version, and credentials.

    CLI Example:
        salt opnsense-router opnsense.doctor
    """
    res = {
        "spec_version": "25.7",
        "loaded_modules_count": len(list_modules()),
        "proxy_mode": salt.utils.platform.is_proxy(),
        "status": "UNKNOWN",
        "details": {},
    }
    spec = load_spec()
    meta = spec.get("meta", {})
    if meta.get("core_ref"):
        res["spec_version"] = meta["core_ref"]

    try:
        if (
            salt.utils.platform.is_proxy()
            and "__proxy__" in globals()
            and "opnsense.call" in __proxy__
        ):
            firmware_res = __proxy__["opnsense.call"]("core", "firmware", "status")
        else:
            client = _get_client()
            firmware_res = client.get("core", "firmware", "status")
        res["status"] = "OK"
        res["firmware_status"] = firmware_res
    except Exception as exc:
        res["status"] = "ERROR"
        res["error"] = str(exc)

    return res
