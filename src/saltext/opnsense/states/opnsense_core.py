# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense core state wrappers.

Generated from controllers.json for module core.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_core"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- menu controller ---

def menu_present(name, data=None, match=None, reconfigure="core/hasync/reconfigure", search_field=None):
    """
    Ensure menu menu present in core.

    Wraps opnsense.item_present for /api/core/menu/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default core/hasync/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "core", "menu", "menu", data, match=match, reconfigure=reconfigure, search_field=search_field)


def menu_absent(name, match=None, reconfigure="core/hasync/reconfigure", search_field=None):
    """
    Ensure menu menu absent in core.

    Wraps opnsense.item_absent for /api/core/menu/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "core", "menu", "menu", match=match, reconfigure=reconfigure, search_field=search_field)


# --- service controller ---

def service_present(name, data=None, match=None, reconfigure="core/hasync/reconfigure", search_field=None):
    """
    Ensure service service present in core.

    Wraps opnsense.item_present for /api/core/service/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default core/hasync/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "core", "service", "service", data, match=match, reconfigure=reconfigure, search_field=search_field)


def service_absent(name, match=None, reconfigure="core/hasync/reconfigure", search_field=None):
    """
    Ensure service service absent in core.

    Wraps opnsense.item_absent for /api/core/service/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "core", "service", "service", match=match, reconfigure=reconfigure, search_field=search_field)


# --- snapshots controller ---

def snapshot_present(name, data=None, match=None, reconfigure="core/hasync/reconfigure", search_field=None):
    """
    Ensure snapshot snapshots present in core.

    Wraps opnsense.item_present for /api/core/snapshots/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default core/hasync/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "core", "snapshots", "snapshot", data, match=match, reconfigure=reconfigure, search_field=search_field)


def snapshot_absent(name, match=None, reconfigure="core/hasync/reconfigure", search_field=None):
    """
    Ensure snapshot snapshots absent in core.

    Wraps opnsense.item_absent for /api/core/snapshots/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "core", "snapshots", "snapshot", match=match, reconfigure=reconfigure, search_field=search_field)


# --- tunables controller ---

def item_present(name, data=None, match=None, reconfigure="core/tunables/reconfigure", search_field=None):
    """
    Ensure item tunables present in core.

    Wraps opnsense.item_present for /api/core/tunables/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default core/tunables/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "core", "tunables", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def item_absent(name, match=None, reconfigure="core/tunables/reconfigure", search_field=None):
    """
    Ensure item tunables absent in core.

    Wraps opnsense.item_absent for /api/core/tunables/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "core", "tunables", "item", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="backup", action="reconfigure"):
    """
    Trigger reconfigure for core.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("core", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured core/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"core/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
