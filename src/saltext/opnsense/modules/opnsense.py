from __future__ import annotations

import logging
from typing import Any, Final

log = logging.getLogger(__name__)

from saltext.opnsense.utils.common import strip_salt_internal_kwargs as _strip

try:
    from saltext.opnsense.utils.api_spec import (
        list_actions,
        list_controllers,
        list_modules,
        load_spec,
    )

    HAS_API_SPEC: Final[bool] = True
except ImportError:
    HAS_API_SPEC = False  # type: ignore[no-redef]

    def list_modules() -> list[str]:
        return []

    def list_controllers(m: str) -> list[str]:
        return []

    def list_actions(m: str, c: str) -> list[str]:
        return []

    def load_spec() -> dict[str, Any]:
        return {}


try:
    from saltext.opnsense.utils.opnsense import OPNsenseClient, get_client_from_opts

    HAS_UTILS: Final[bool] = True
    HAS_UTILS_ERROR: Final[str] = ""
except Exception as exc:
    HAS_UTILS = False  # type: ignore[no-redef]
    HAS_UTILS_ERROR = str(exc)  # type: ignore[no-redef]
    OPNsenseClient = None  # type: ignore
    get_client_from_opts = None  # type: ignore

__virtualname__: Final[str] = "opnsense"


def __virtual__() -> bool | tuple[bool, str]:
    from saltext.opnsense.utils.common import is_salt_version_ok as _ok

    v = _ok((3008,))
    if v is not True:
        return v
    if not HAS_API_SPEC:
        return (False, "api_spec missing")
    if not HAS_UTILS:
        return (False, f"utils missing: {HAS_UTILS_ERROR}")
    return True


def _get_client():
    try:
        from salt.exceptions import SaltInvocationError
    except ImportError:
        SaltInvocationError = RuntimeError  # type: ignore  # noqa
    try:
        client = get_client_from_opts(
            __opts__, pillar=__pillar__ if "__pillar__" in globals() else None
        )  # type: ignore[name-defined]
    except Exception as exc:
        raise SaltInvocationError(str(exc)) from exc
    if not client:
        raise SaltInvocationError(
            "Failed to create OPNsense client – check pillar resources:opnsense:hosts:fw-01:host"
        )
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
    kwargs = _strip(kwargs)
    return _get_client().call(module, controller, action, uuid=uuid, data=data, method=method)


def search(
    module: str,
    controller: str,
    type_name: str | None = None,
    search_phrase: str = "",
    row_count: int = -1,
    **kwargs: Any,
) -> Any:
    filtered = _strip(kwargs)
    return _get_client().search(
        module, controller, type_name, search_phrase=search_phrase, row_count=row_count, **filtered
    )


def get(
    module: str,
    controller: str,
    type_name: str | None = None,
    uuid: str | None = None,
    **kwargs: Any,
) -> Any:
    _strip(kwargs)
    return _get_client().get(module, controller, type_name, uuid=uuid)


def add(module: str, controller: str, type_name: str, data: dict[str, Any], **kwargs: Any) -> Any:
    _strip(kwargs)
    return _get_client().add(module, controller, type_name, data)


def set_item(
    module: str, controller: str, type_name: str, uuid: str, data: dict[str, Any], **kwargs: Any
) -> Any:
    _strip(kwargs)
    return _get_client().set(module, controller, type_name, uuid, data)


def delete(module: str, controller: str, type_name: str, uuid: str, **kwargs: Any) -> Any:
    _strip(kwargs)
    return _get_client().delete(module, controller, type_name, uuid)


def toggle(
    module: str,
    controller: str,
    type_name: str,
    uuid: str,
    enabled: bool | None = None,
    **kwargs: Any,
) -> Any:
    _strip(kwargs)
    return _get_client().toggle(module, controller, type_name, uuid, enabled)


def reconfigure(
    module: str,
    controller: str,
    action: str = "reconfigure",
    data: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Any:
    _strip(kwargs)
    return _get_client().reconfigure(module, controller, action, data=data)


def ping(**kwargs: Any) -> bool:
    _strip(kwargs)
    client = _get_client()
    try:
        client.search("unbound", "settings", "host_alias", row_count=1)
        return True
    except Exception as exc:
        log.debug("ping failed: %s", exc)
        return False


def list_api_modules(**kwargs: Any) -> list[str]:
    _strip(kwargs)
    return list_modules()


def list_api_controllers(module: str, **kwargs: Any) -> list[str]:
    _strip(kwargs)
    return list_controllers(module)


def list_api_actions(module: str, controller: str, **kwargs: Any) -> list[str]:
    _strip(kwargs)
    return list_actions(module, controller)


def spec(**kwargs: Any) -> dict[str, Any]:
    _strip(kwargs)
    return load_spec()


_DYNAMIC_MAP_CACHE: dict[str, tuple[str, str, str]] | None = None


def _build_dynamic_map() -> dict[str, tuple[str, str, str]]:
    global _DYNAMIC_MAP_CACHE
    if _DYNAMIC_MAP_CACHE:
        return _DYNAMIC_MAP_CACHE
    mapping: dict[str, tuple[str, str, str]] = {}
    try:
        spec_data = load_spec() or {}
        modules_dict = spec_data.get("modules") or {}
        for mod_name, controllers in modules_dict.items():
            if not isinstance(controllers, dict):
                continue
            for ctrl_name, actions in controllers.items():
                if isinstance(actions, dict):
                    action_list = list(actions.keys())
                elif isinstance(actions, (list, tuple)):
                    action_list = list(actions)
                else:
                    continue
                for action in action_list:
                    from saltext.opnsense.utils.common import camel_to_snake as _c

                    mod_sn = _c(mod_name)
                    ctrl_sn = _c(ctrl_name)
                    act_sn = _c(action)
                    if not act_sn:
                        continue
                    func_name = f"{mod_sn}_{ctrl_sn}_{act_sn}"
                    mapping[func_name] = (mod_name, ctrl_name, action)
    except Exception as exc:
        log.debug("dynamic map build failed: %s", exc)
    if mapping:
        _DYNAMIC_MAP_CACHE = mapping
    return mapping


def _make_dynamic_wrapper(mod_name: str, ctrl_name: str, action: str, func_name: str):
    def wrapper(
        data: dict[str, Any] | None = None,
        uuid: str | None = None,
        search_phrase: str = "",
        row_count: int = -1,
        **kwargs: Any,
    ) -> Any:
        kwargs = _strip(kwargs)
        if action.lower().startswith("search"):
            return call(
                mod_name,
                ctrl_name,
                action,
                data={"current": 1, "rowCount": row_count, "searchPhrase": search_phrase, **kwargs},
                method="POST",
            )
        if data is not None:
            return call(mod_name, ctrl_name, action, uuid=uuid, data=data, method="POST")
        return call(mod_name, ctrl_name, action, uuid=uuid, data={}, method="POST")

    wrapper.__name__ = func_name
    wrapper.__doc__ = f"Auto-generated {mod_name}/{ctrl_name}/{action}. CLI: salt -C 'T@opnsense:fw-01' opnsense.{func_name}"
    return wrapper


def __getattr__(name: str):
    mapping = _build_dynamic_map()
    if name in mapping:
        mod_name, ctrl_name, action = mapping[name]
        wrapper = _make_dynamic_wrapper(mod_name, ctrl_name, action, name)
        globals()[name] = wrapper
        return wrapper
    raise AttributeError(f"module 'opnsense' has no attribute {name!r}")


def __dir__() -> list[str]:
    base = list(globals().keys())
    try:
        base.extend(_build_dynamic_map().keys())
    except Exception:
        pass
    return sorted(set(base))


def doctor() -> dict[str, Any]:
    res: dict[str, Any] = {
        "spec_version": "26.7.3",
        "loaded_modules_count": len(list_modules()),
        "status": "UNKNOWN",
        "details": {},
    }
    try:
        spec_data = load_spec()
        meta = spec_data.get("meta", {})
        if meta.get("core_ref"):
            res["spec_version"] = meta["core_ref"]
    except Exception:
        pass
    try:
        client = _get_client()
        fw = client.get("core", "firmware", "status")
        res["status"] = "OK"
        res["firmware_status"] = fw
    except Exception as exc:
        res["status"] = "ERROR"
        res["error"] = str(exc)
    return res
