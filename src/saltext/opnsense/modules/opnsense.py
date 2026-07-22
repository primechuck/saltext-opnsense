import logging
from typing import Any

import salt.utils.platform

log = logging.getLogger(__name__)

def _try_import():
    import importlib
    candidates = [
        ("saltext.opnsense.utils.opnsense", "saltext.opnsense.utils.api_spec"),
        ("saltext.opnsense.utils.opnsense", "opnsense_api_spec"),
        ("opnsense", "opnsense_api_spec"),
        ("salt.utils.opnsense", "salt.utils.opnsense_api_spec"),
    ]
    last_err = None
    for mod_client, mod_spec in candidates:
        try:
            c = importlib.import_module(mod_client)
            s = importlib.import_module(mod_spec)
            return (
                getattr(c, "get_client_from_opts"),
                getattr(c, "OPNsenseClient"),
                getattr(s, "list_modules"),
                getattr(s, "list_controllers"),
                getattr(s, "list_actions"),
                getattr(s, "load_spec"),
                None,
            )
        except Exception as e:
            last_err = e
            continue
    try:
        from saltext.opnsense.utils.opnsense import get_client_from_opts as _g, OPNsenseClient as _C
        from saltext.opnsense.utils.api_spec import list_modules as _lm, list_controllers as _lc, list_actions as _la, load_spec as _ls
        return _g, _C, _lm, _lc, _la, _ls, None
    except Exception as e:
        return None, None, None, None, None, None, str(e) if last_err is None else f"{last_err}; {e}"

_get_client_from_opts, OPNsenseClient, list_modules, list_controllers, list_actions, load_spec, _import_err = _try_import()

if _get_client_from_opts is not None:
    get_client_from_opts = _get_client_from_opts
    HAS_UTILS = True
    HAS_UTILS_ERROR = ""
else:
    HAS_UTILS = False
    HAS_UTILS_ERROR = _import_err or "unknown import error"
    get_client_from_opts = None
    OPNsenseClient = None
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
    if salt.utils.platform.is_proxy():
        if "__proxy__" in globals() and "opnsense.call" in __proxy__:
            raise RuntimeError("proxy mode: use __proxy__ directly")
    try:
        client = get_client_from_opts(__opts__, pillar=__pillar__ if "__pillar__" in globals() else None)
        return client
    except Exception as exc:
        if "__proxy__" in globals() and f"{__virtualname__}.call" in __proxy__:
            return None
        raise


def _proxy_or_direct(func_name, *args, **kwargs):
    if salt.utils.platform.is_proxy() and "__proxy__" in globals():
        proxy_func = f"{__virtualname__}.{func_name}"
        if proxy_func in __proxy__:
            return __proxy__[proxy_func](*args, **kwargs)
    client = _get_client()
    if client is None:
        proxy_func = f"{__virtualname__}.{func_name}"
        return __proxy__[proxy_func](*args, **kwargs)

    method_map = {
        "call": lambda: client.call(*args, **kwargs),
        "search": lambda: client.search(*args, **kwargs),
        "get": lambda: client.get(*args, **kwargs),
        "add": lambda: client.add(*args, **kwargs),
        "set_item": lambda: client.set(*args, **kwargs),
        "delete": lambda: client.delete(*args, **kwargs),
        "toggle": lambda: client.toggle(*args, **kwargs),
        "reconfigure": lambda: client.reconfigure(*args, **kwargs),
    }
    if func_name in method_map:
        return method_map[func_name]()
    raise NotImplementedError(f"func {func_name} not mapped for direct mode")


def call(module, controller, action, uuid=None, data=None, method=None):
    if salt.utils.platform.is_proxy() and "opnsense.call" in __proxy__:
        return __proxy__["opnsense.call"](module, controller, action, uuid, data, method)
    client = _get_client()
    return client.call(module, controller, action, uuid=uuid, data=data, method=method)


def search(module, controller, type_name=None, search_phrase="", row_count=-1, **kwargs):
    if salt.utils.platform.is_proxy() and "opnsense.search" in __proxy__:
        return __proxy__["opnsense.search"](module, controller, type_name, search_phrase=search_phrase, row_count=row_count, **kwargs)
    client = _get_client()
    return client.search(module, controller, type_name, search_phrase=search_phrase, row_count=row_count, **kwargs)


def get(module, controller, type_name=None, uuid=None):
    if salt.utils.platform.is_proxy() and "opnsense.get" in __proxy__:
        return __proxy__["opnsense.get"](module, controller, type_name, uuid)
    client = _get_client()
    return client.get(module, controller, type_name, uuid=uuid)


def add(module, controller, type_name, data):
    if salt.utils.platform.is_proxy() and "opnsense.add" in __proxy__:
        return __proxy__["opnsense.add"](module, controller, type_name, data)
    client = _get_client()
    return client.add(module, controller, type_name, data)


def set_item(module, controller, type_name, uuid, data):
    if salt.utils.platform.is_proxy() and "opnsense.set_item" in __proxy__:
        return __proxy__["opnsense.set_item"](module, controller, type_name, uuid, data)
    client = _get_client()
    return client.set(module, controller, type_name, uuid, data)


def delete(module, controller, type_name, uuid):
    if salt.utils.platform.is_proxy() and "opnsense.delete" in __proxy__:
        return __proxy__["opnsense.delete"](module, controller, type_name, uuid)
    client = _get_client()
    return client.delete(module, controller, type_name, uuid)


def toggle(module, controller, type_name, uuid, enabled=None):
    if salt.utils.platform.is_proxy() and "opnsense.toggle" in __proxy__:
        return __proxy__["opnsense.toggle"](module, controller, type_name, uuid, enabled)
    client = _get_client()
    return client.toggle(module, controller, type_name, uuid, enabled)


def reconfigure(module, controller, action="reconfigure", data=None):
    if salt.utils.platform.is_proxy() and "opnsense.reconfigure" in __proxy__:
        return __proxy__["opnsense.reconfigure"](module, controller, action, data)
    client = _get_client()
    return client.reconfigure(module, controller, action, data=data)


def ping():
    if salt.utils.platform.is_proxy() and "opnsense.ping" in __proxy__:
        return __proxy__["opnsense.ping"]()
    client = _get_client()
    try:
        client.call("core", "firmware", "status", method="GET")
        return True
    except Exception:
        try:
            client.call("unbound", "overview", "isEnabled", method="GET")
            return True
        except Exception as exc:
            log.debug("ping failed: %s", exc)
            return False


def list_api_modules():
    return list_modules()


def list_api_controllers(module):
    return list_controllers(module)


def list_api_actions(module, controller):
    return list_actions(module, controller)


def spec():
    return load_spec()


def _find_existing(module, controller, type_name, match):
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


def ensure_present(module, controller, type_name, data, match=None, reconfigure_path=None):
    existing = _find_existing(module, controller, type_name, match) if match else None
    if existing is None:
        result = add(module, controller, type_name, data)
        if reconfigure_path:
            mod, ctrl, act = _parse_reconfigure(reconfigure_path)
            reconfigure(mod, ctrl, act)
        return {"result": result, "changed": True, "action": "added"}

    diff = {}
    for k, v in (data.get(list(data.keys())[0]) if len(data) == 1 and isinstance(list(data.values())[0], dict) else data).items():
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


def ensure_absent(module, controller, type_name, match, reconfigure_path=None):
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


def _camel_to_snake(name: str):
    import re

    name = name.replace("-", "_")
    s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    s1 = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s1)
    s1 = s1.lower()
    s1 = re.sub(r"__+", "_", s1)
    s1 = re.sub(r"[^0-9a-z_]+", "_", s1)
    return s1.strip("_")


def _inject_dynamic_wrappers():
    try:
        spec_data = load_spec() or {}
        modules_dict = spec_data.get("modules") or {}
        if not modules_dict:
            return

        existing = set(globals().keys())

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
                    if func_name in existing:
                        continue

                    orig_action = action

                    def _make_wrapper(m=mod_name, c=ctrl_name, a=orig_action):
                        def wrapper(data=None, uuid=None, search_phrase="", row_count=-1, **kwargs):
                            if a.lower().startswith("search"):
                                return call(m, c, a, data={"current": 1, "rowCount": row_count, "searchPhrase": search_phrase, **kwargs}, method="POST")
                            if a.lower().startswith("get") and data is None:
                                return call(m, c, a, uuid=uuid, method="GET")
                            if data is not None:
                                return call(m, c, a, uuid=uuid, data=data, method="POST")
                            return call(m, c, a, uuid=uuid, method="POST")

                        wrapper.__name__ = func_name
                        wrapper.__doc__ = f"""Auto-generated from spec: /api/{m}/{c}/{a}\n\nWraps opnsense.call for {m}/{c}/{a}.\n\nThis function is dynamically injected at import time from controllers.json to ensure complete API coverage without hand-coding. For explicit reconfigure, pass reconfigure path via separate call.\n\nRegenerate spec: python tools/generate_spec.py"""
                        return wrapper

                    globals()[func_name] = _make_wrapper()
                    existing.add(func_name)

        log.debug("Dynamic opnsense wrappers injected: %s new functions", len(existing) - len(globals().keys()))

    except Exception as exc:
        log.debug("Dynamic wrapper injection failed: %s", exc)


_inject_dynamic_wrappers()
