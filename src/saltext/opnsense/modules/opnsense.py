import logging

import salt.utils.platform

log = logging.getLogger(__name__)

try:
    from saltext.opnsense.utils.common import (
        camel_to_snake as _camel_to_snake,
    )
    from saltext.opnsense.utils.common import (
        strip_salt_internal_kwargs as _strip_pub_kwargs,
    )
except Exception:

    def _camel_to_snake(name: str) -> str:
        import re

        name = name.replace("-", "_")
        s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
        s1 = s1.lower()
        return re.sub(r"__+", "_", s1).strip("_")

    def _strip_pub_kwargs(kwargs: dict) -> dict:
        return {k: v for k, v in kwargs.items() if not k.startswith("__")}


def _try_import():
    import importlib

    for client_mod, spec_mod in [
        ("saltext.opnsense.utils.opnsense", "saltext.opnsense.utils.api_spec"),
        ("saltext.opnsense.utils.opnsense", "opnsense_api_spec"),
        ("opnsense", "opnsense_api_spec"),
        ("salt.utils.opnsense", "salt.utils.opnsense_api_spec"),
    ]:
        try:
            c = importlib.import_module(client_mod)
            s = importlib.import_module(spec_mod)
            return (
                getattr(c, "get_client_from_opts"),
                getattr(c, "OPNsenseClient"),
                getattr(s, "list_modules"),
                getattr(s, "list_controllers"),
                getattr(s, "list_actions"),
                getattr(s, "load_spec"),
                None,
            )
        except Exception as exc:
            _ = exc
            continue
    try:
        from saltext.opnsense.utils.api_spec import (
            list_actions as _la,
        )
        from saltext.opnsense.utils.api_spec import (
            list_controllers as _lc,
        )
        from saltext.opnsense.utils.api_spec import (
            list_modules as _lm,
        )
        from saltext.opnsense.utils.api_spec import (
            load_spec as _ls,
        )
        from saltext.opnsense.utils.opnsense import OPNsenseClient as _C
        from saltext.opnsense.utils.opnsense import get_client_from_opts as _g

        return _g, _C, _lm, _lc, _la, _ls, None
    except Exception as exc:
        return None, None, None, None, None, None, str(exc)


(
    _get_client_from_opts,
    OPNsenseClient,
    list_modules,
    list_controllers,
    list_actions,
    load_spec,
    _import_err,
) = _try_import()

if _get_client_from_opts is not None:
    get_client_from_opts = _get_client_from_opts
    HAS_UTILS = True
    HAS_UTILS_ERROR = ""
else:
    HAS_UTILS = False
    HAS_UTILS_ERROR = _import_err or "import failed"
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


def _inject_dynamic_wrappers():
    try:
        spec_data = load_spec() or {}
        modules_dict = spec_data.get("modules") or {}
        if not modules_dict:
            return

        initial_count = len(globals())
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
                            kwargs = _strip_pub_kwargs(kwargs)
                            if a.lower().startswith("search"):
                                return call(
                                    m,
                                    c,
                                    a,
                                    data={
                                        "current": 1,
                                        "rowCount": row_count,
                                        "searchPhrase": search_phrase,
                                        **kwargs,
                                    },
                                    method="POST",
                                )
                            if data is not None:
                                return call(m, c, a, uuid=uuid, data=data, method="POST")
                            return call(m, c, a, uuid=uuid, data={}, method="POST")

                        action_low = a.lower()
                        verb_word = {
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
                        for k, v in verb_word.items():
                            if action_low.startswith(k):
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
                        if clean in [
                            "search",
                            "get",
                            "add",
                            "set",
                            "del",
                            "delete",
                            "toggle",
                            "reconfigure",
                            "",
                        ]:
                            type_human = f"{ctrl_snake} {mod_snake}".replace("_", " ").strip()
                            if not type_human:
                                type_human = ctrl_snake.replace("_", " ") or mod_snake.replace(
                                    "_", " "
                                )
                        else:
                            type_human = clean.replace("_", " ").strip() or ctrl_snake.replace(
                                "_", " "
                            )
                        if not type_human:
                            type_human = f"{mod_snake} {ctrl_snake}"
                        ctrl_human = ctrl_snake.replace("_", " ")
                        mod_human = mod_snake.replace("_", " ")
                        wrapper.__name__ = func_name
                        wrapper.__doc__ = f"""{verb} {type_human} in {mod_human} {ctrl_human}.

Auto-generated from upstream OPNsense spec.
Endpoint: POST /api/{m}/{c}/{a}

CLI (read-only):
    salt opnsense-router opnsense.{func_name} row_count=1 --out=table

Docs: https://docs.opnsense.org/development/api/core/{m}.html"""
                        return wrapper

                    globals()[func_name] = _make_wrapper()
                    existing.add(func_name)

        injected_count = len(globals()) - initial_count
        log.debug("Dynamic opnsense wrappers injected: %d new functions", injected_count)

    except Exception as exc:
        log.debug("Dynamic wrapper injection failed: %s", exc)


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
        if salt.utils.platform.is_proxy() and "__proxy__" in globals() and "opnsense.call" in __proxy__:
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


_inject_dynamic_wrappers()








