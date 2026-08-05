"""
Execution module override for opnsense resource type – API-only.

Thin delegation to connection module via __resource_funcs__.
Per Salt resources execution_modules docs: this file's location enforces the slot,
do NOT redefine __virtualname__ – filename wins.

__resource_funcs__["opnsense.call"] etc are functions defined in
resources/opnsense/__init__.py (connection module). They use
__resource__["id"] to select cached OPNsenseClient.

All other modules (bind, unbound, firewall, kea, etc) that call
__salt__["opnsense.search"] will automatically dispatch here via
per-resource merged loader.
"""

from saltext.opnsense.utils.common import strip_salt_internal_kwargs


def _strip(kw):
    return strip_salt_internal_kwargs(kw)


def call(module, controller, action, uuid=None, data=None, method=None, **kwargs):
    return __resource_funcs__["opnsense.call"](module, controller, action, uuid, data, method)  # type: ignore[name-defined]


def search(module, controller, type_name=None, search_phrase="", row_count=-1, current=1, sort=None, extra=None, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.search"](module, controller, type_name, search_phrase, row_count, current, sort, extra)  # type: ignore[name-defined]


def get(module, controller, type_name=None, uuid=None, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.get"](module, controller, type_name, uuid)  # type: ignore[name-defined]


def add(module, controller, type_name, data, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.add"](module, controller, type_name, data)  # type: ignore[name-defined]


def set_item(module, controller, type_name, uuid, data, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.set_item"](module, controller, type_name, uuid, data)  # type: ignore[name-defined]


def delete(module, controller, type_name, uuid, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.delete"](module, controller, type_name, uuid)  # type: ignore[name-defined]


def toggle(module, controller, type_name, uuid, enabled=None, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.toggle"](module, controller, type_name, uuid, enabled)  # type: ignore[name-defined]


def reconfigure(module, controller, action="reconfigure", data=None, **kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.reconfigure"](module, controller, action, data)  # type: ignore[name-defined]


def ping(**kwargs):
    _strip(kwargs)
    return __resource_funcs__["opnsense.ping"]()  # type: ignore[name-defined]


# Compatibility wrappers – same naming as execution module opnsense.py top-level also used
# Dynamic doc will be resolved via __resource__ path; keep alias for backward compat


def spec(**kwargs):
    _strip(kwargs)
    # spec is not per-resource – delegate to standard utils if available via __salt__ or load directly
    try:
        from saltext.opnsense.utils.api_spec import load_spec

        return load_spec()
    except Exception:
        return {}


def list_api_modules(**kwargs):
    _strip(kwargs)
    try:
        from saltext.opnsense.utils.api_spec import list_modules

        return list_modules()
    except Exception:
        return []


def list_api_controllers(module, **kwargs):
    _strip(kwargs)
    try:
        from saltext.opnsense.utils.api_spec import list_controllers

        return list_controllers(module)
    except Exception:
        return []


def list_api_actions(module, controller, **kwargs):
    _strip(kwargs)
    try:
        from saltext.opnsense.utils.api_spec import list_actions

        return list_actions(module, controller)
    except Exception:
        return []


def doctor(**kwargs):
    _strip(kwargs)
    try:
        client_res = __resource_funcs__["opnsense.call"]("core", "firmware", "status", data={}, method="POST")  # type: ignore[name-defined]
        return {"status": "OK", "firmware_status": client_res, "resource_id": __resource__["id"]}  # type: ignore[name-defined]
    except Exception as exc:
        return {"status": "ERROR", "error": str(exc), "resource_id": __resource__["id"] if "__resource__" in globals() else "unknown"}  # type: ignore[name-defined]
