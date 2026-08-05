from __future__ import annotations

import logging
import threading
from typing import Any, Final

log = logging.getLogger(__name__)

from saltext.opnsense.utils.common import camel_to_snake as _camel_to_snake
from saltext.opnsense.utils.common import strip_salt_internal_kwargs as _strip_pub_kwargs

try:
    from saltext.opnsense.utils.api_spec import (
        list_actions,
        list_controllers,
        list_modules,
        load_spec,
    )
    from saltext.opnsense.utils.opnsense import OPNsenseClient, get_client_from_opts

    HAS_UTILS: Final[bool] = True
    HAS_UTILS_ERROR: Final[str] = ""
except ImportError as exc:  # pragma: no cover - fallback for missing deps
    HAS_UTILS = False  # type: ignore[no-redef]
    HAS_UTILS_ERROR = str(exc)  # type: ignore[no-redef]
    OPNsenseClient = None  # type: ignore[assignment]
    get_client_from_opts = None  # type: ignore[assignment]

    def list_modules() -> list[str]:  # type: ignore[no-redef]
        return []

    def list_controllers(module: str) -> list[str]:  # type: ignore[no-redef]
        return []

    def list_actions(module: str, controller: str) -> list[str]:  # type: ignore[no-redef]
        return []

    def load_spec() -> dict[str, Any]:  # type: ignore[no-redef]
        return {}


__virtualname__: Final[str] = "opnsense"


def __virtual__() -> bool | tuple[bool, str]:
    if not HAS_UTILS:
        return (False, f"opnsense utils missing: {HAS_UTILS_ERROR}")
    return True


def _get_client() -> OPNsenseClient:
    client = get_client_from_opts(
        __opts__, pillar=__pillar__ if "__pillar__" in globals() else None
    )
    if not client:
        raise RuntimeError("Failed to create OPNsense client from opts/pillar")
    return client


def call(
    module: str,
    controller: str,
    action: str,
    uuid: str | None = None,
    data: dict[str, Any] | None = None,
    method: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Execute a raw REST API call to OPNsense.

    CLI Example:
        salt minion opnsense.call unbound settings searchHostAlias '{"rowCount": 1}'
    """
    kwargs = _strip_pub_kwargs(kwargs)
    if kwargs:
        log.debug("opnsense.call stripping extra kwargs %s", list(kwargs.keys()))
    client = _get_client()
    return client.call(module, controller, action, uuid=uuid, data=data, method=method)


def search(
    module: str,
    controller: str,
    type_name: str | None = None,
    search_phrase: str = "",
    row_count: int = -1,
    **kwargs: Any,
) -> Any:
    """
    Query an OPNsense search endpoint and unwrap the resulting rows.

    CLI Example:
        salt minion opnsense.search unbound settings host_alias search_phrase="www"
    """
    filtered = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.search(
        module,
        controller,
        type_name,
        search_phrase=search_phrase,
        row_count=row_count,
        **filtered,
    )


def get(
    module: str,
    controller: str,
    type_name: str | None = None,
    uuid: str | None = None,
    **kwargs: Any,
) -> Any:
    kwargs = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.get(module, controller, type_name, uuid=uuid)


def add(module: str, controller: str, type_name: str, data: dict[str, Any], **kwargs: Any) -> Any:
    kwargs = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.add(module, controller, type_name, data)


def set_item(
    module: str,
    controller: str,
    type_name: str,
    uuid: str,
    data: dict[str, Any],
    **kwargs: Any,
) -> Any:
    kwargs = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.set(module, controller, type_name, uuid, data)


def delete(module: str, controller: str, type_name: str, uuid: str, **kwargs: Any) -> Any:
    kwargs = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.delete(module, controller, type_name, uuid)


def toggle(
    module: str,
    controller: str,
    type_name: str,
    uuid: str,
    enabled: bool | None = None,
    **kwargs: Any,
) -> Any:
    kwargs = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.toggle(module, controller, type_name, uuid, enabled)


def reconfigure(
    module: str,
    controller: str,
    action: str = "reconfigure",
    data: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Any:
    kwargs = _strip_pub_kwargs(kwargs)
    client = _get_client()
    return client.reconfigure(module, controller, action, data=data)


def ping(**kwargs: Any) -> bool:
    kwargs = _strip_pub_kwargs(kwargs)
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
        except Exception as exc:  # pragma: no cover - best-effort probe
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
    except Exception as exc:  # pragma: no cover
        log.debug("ping fallback failed: %s", exc)
        return False


def list_api_modules(**kwargs: Any) -> list[str]:
    kwargs = _strip_pub_kwargs(kwargs)
    return list_modules()


def list_api_controllers(module: str, **kwargs: Any) -> list[str]:
    kwargs = _strip_pub_kwargs(kwargs)
    return list_controllers(module)


def list_api_actions(module: str, controller: str, **kwargs: Any) -> list[str]:
    kwargs = _strip_pub_kwargs(kwargs)
    return list_actions(module, controller)


def spec(**kwargs: Any) -> dict[str, Any]:
    kwargs = _strip_pub_kwargs(kwargs)
    return load_spec()


def _find_existing(
    module: str, controller: str, type_name: str, match: dict[str, Any] | None, **kwargs: Any
) -> dict[str, Any] | None:
    kwargs = _strip_pub_kwargs(kwargs)
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
    module: str,
    controller: str,
    type_name: str,
    data: dict[str, Any],
    match: dict[str, Any] | None = None,
    reconfigure_path: str | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
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

    if len(data) == 1:
        first_key = next(iter(data))
        first_val = data[first_key]
        if isinstance(first_val, dict):
            inner_data = first_val
        else:
            inner_data = data
    else:
        inner_data = data

    diff: dict[str, dict[str, Any]] = {}
    for k, v in inner_data.items():
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


def ensure_absent(
    module: str,
    controller: str,
    type_name: str,
    match: dict[str, Any],
    reconfigure_path: str | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    """
    Ensure an item is absent (execution module backend for `opnsense.item_absent`).

    CLI Example:
        salt minion opnsense.ensure_absent unbound settings host_alias \\
            match='{"hostname": "www"}'
    """
    kwargs = _strip_pub_kwargs(kwargs)
    existing = _find_existing(module, controller, type_name, match)
    if existing is None:
        return {"changed": False, "action": "absent"}
    uuid = existing.get("uuid")
    result = delete(module, controller, type_name, uuid)
    if reconfigure_path:
        mod, ctrl, act = _parse_reconfigure(reconfigure_path)
        reconfigure(mod, ctrl, act)
    return {"result": result, "changed": True, "action": "deleted"}


def _parse_reconfigure(path: str) -> tuple[str | None, str | None, str | None]:
    if not path:
        return None, None, None
    parts = path.split("/")
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    if len(parts) == 2:
        return parts[0], parts[1], "reconfigure"
    return None, None, None


_DYNAMIC_MAP_CACHE: dict[str, tuple[str, str, str, str, str, str]] | None = None
_CACHE_LOCK: Final[threading.Lock] = threading.Lock()
_CONTEXT_CACHE_KEY: Final[str] = "opnsense_dynamic_map"

VERB_MAP: Final[dict[str, str]] = {
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

ACTION_PREFIXES: Final[tuple[str, ...]] = (
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
)

GENERIC_ACTIONS: Final[frozenset[str]] = frozenset(
    {"search", "get", "add", "set", "del", "delete", "toggle", "reconfigure", ""}
)


def _build_dynamic_map() -> dict[str, tuple[str, str, str, str, str, str]]:
    ctx = globals().get("__context__")
    if isinstance(ctx, dict) and _CONTEXT_CACHE_KEY in ctx:
        cached = ctx[_CONTEXT_CACHE_KEY]
        if isinstance(cached, dict):
            return cached

    global _DYNAMIC_MAP_CACHE
    with _CACHE_LOCK:
        if isinstance(ctx, dict) and _CONTEXT_CACHE_KEY in ctx:
            return ctx[_CONTEXT_CACHE_KEY]

        if _DYNAMIC_MAP_CACHE is not None:
            return _DYNAMIC_MAP_CACHE

        mapping: dict[str, tuple[str, str, str, str, str, str]] = {}
        try:
            spec_data = load_spec() or {}
            modules_dict = spec_data.get("modules") or {}
            for mod_name, controllers in modules_dict.items():
                if not isinstance(controllers, dict):
                    continue
                mod_snake = _camel_to_snake(mod_name)
                for ctrl_name, actions in controllers.items():
                    if isinstance(actions, dict):
                        action_list = list(actions.keys())
                    elif isinstance(actions, (list, tuple)):
                        action_list = list(actions)
                    else:
                        continue
                    ctrl_snake = _camel_to_snake(ctrl_name)
                    for action in action_list:
                        action_snake = _camel_to_snake(action)
                        if not action_snake:
                            continue
                        func_name = f"{mod_snake}_{ctrl_snake}_{action_snake}"
                        mapping[func_name] = (
                            mod_name,
                            ctrl_name,
                            action,
                            mod_snake,
                            ctrl_snake,
                            action_snake,
                        )
        except Exception as exc:
            log.debug("Failed to build dynamic map: %s", exc)

        if isinstance(ctx, dict):
            ctx[_CONTEXT_CACHE_KEY] = mapping
        _DYNAMIC_MAP_CACHE = mapping
        return mapping


def _make_dynamic_wrapper(
    mod_name: str,
    ctrl_name: str,
    action: str,
    mod_snake: str,
    ctrl_snake: str,
    action_snake: str,
    func_name: str,
):
    def wrapper(
        data: dict[str, Any] | None = None,
        uuid: str | None = None,
        search_phrase: str = "",
        row_count: int = -1,
        **kwargs: Any,
    ) -> Any:
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

    verb = "Execute"
    al = action.lower()
    for k, v in VERB_MAP.items():
        if al.startswith(k):
            verb = v
            break

    clean = action_snake
    for prefix in ACTION_PREFIXES:
        if clean.startswith(prefix):
            clean = clean[len(prefix) :]
            break

    if clean in GENERIC_ACTIONS:
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


def __getattr__(name: str):  # type: ignore[no-untyped-def]
    mapping = _build_dynamic_map()
    if name in mapping:
        mod_name, ctrl_name, action, mod_snake, ctrl_snake, action_snake = mapping[name]
        wrapper = _make_dynamic_wrapper(
            mod_name, ctrl_name, action, mod_snake, ctrl_snake, action_snake, name
        )
        globals()[name] = wrapper
        return wrapper
    raise AttributeError(f"module 'opnsense' has no attribute {name!r}")


def __dir__() -> list[str]:
    base = list(globals().keys())
    try:
        base.extend(_build_dynamic_map().keys())
    except Exception:  # pragma: no cover
        pass
    return sorted(set(base))


def doctor() -> dict[str, Any]:
    """
    Test OPNsense API connectivity, spec version, and credentials.

    CLI Example:
        salt opnsense-router opnsense.doctor
    """
    res: dict[str, Any] = {
        "spec_version": "25.7",
        "loaded_modules_count": len(list_modules()),
        "status": "UNKNOWN",
        "details": {},
    }
    spec_data = load_spec()
    meta = spec_data.get("meta", {})
    if meta.get("core_ref"):
        res["spec_version"] = meta["core_ref"]

    try:
        client = _get_client()
        firmware_res = client.get("core", "firmware", "status")
        res["status"] = "OK"
        res["firmware_status"] = firmware_res
    except Exception as exc:
        res["status"] = "ERROR"
        res["error"] = str(exc)

    return res
