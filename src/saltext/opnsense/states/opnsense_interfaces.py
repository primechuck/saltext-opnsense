# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense interfaces state wrappers.

Generated from controllers.json for module interfaces.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_interfaces"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- assignment controller ---

def assignment_item_present(name, data=None, match=None, reconfigure="interfaces/assignment/reconfigure", search_field=None):
    """
    Ensure item assignment present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/assignment/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/assignment/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "assignment", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def assignment_item_absent(name, match=None, reconfigure="interfaces/assignment/reconfigure", search_field=None):
    """
    Ensure item assignment absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/assignment/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "assignment", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- bridgesettings controller ---

def bridgesettings_item_present(name, data=None, match=None, reconfigure="interfaces/bridgesettings/reconfigure", search_field=None):
    """
    Ensure item bridgesettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/bridgesettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/bridgesettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "bridgesettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bridgesettings_item_absent(name, match=None, reconfigure="interfaces/bridgesettings/reconfigure", search_field=None):
    """
    Ensure item bridgesettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/bridgesettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "bridgesettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- gifsettings controller ---

def gifsettings_item_present(name, data=None, match=None, reconfigure="interfaces/gifsettings/reconfigure", search_field=None):
    """
    Ensure item gifsettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/gifsettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/gifsettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "gifsettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def gifsettings_item_absent(name, match=None, reconfigure="interfaces/gifsettings/reconfigure", search_field=None):
    """
    Ensure item gifsettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/gifsettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "gifsettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- gresettings controller ---

def gresettings_item_present(name, data=None, match=None, reconfigure="interfaces/gresettings/reconfigure", search_field=None):
    """
    Ensure item gresettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/gresettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/gresettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "gresettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def gresettings_item_absent(name, match=None, reconfigure="interfaces/gresettings/reconfigure", search_field=None):
    """
    Ensure item gresettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/gresettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "gresettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- laggsettings controller ---

def laggsettings_item_present(name, data=None, match=None, reconfigure="interfaces/laggsettings/reconfigure", search_field=None):
    """
    Ensure item laggsettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/laggsettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/laggsettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "laggsettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def laggsettings_item_absent(name, match=None, reconfigure="interfaces/laggsettings/reconfigure", search_field=None):
    """
    Ensure item laggsettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/laggsettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "laggsettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- loopbacksettings controller ---

def loopbacksettings_item_present(name, data=None, match=None, reconfigure="interfaces/loopbacksettings/reconfigure", search_field=None):
    """
    Ensure item loopbacksettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/loopbacksettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/loopbacksettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "loopbacksettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def loopbacksettings_item_absent(name, match=None, reconfigure="interfaces/loopbacksettings/reconfigure", search_field=None):
    """
    Ensure item loopbacksettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/loopbacksettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "loopbacksettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- neighborsettings controller ---

def neighborsettings_item_present(name, data=None, match=None, reconfigure="interfaces/neighborsettings/reconfigure", search_field=None):
    """
    Ensure item neighborsettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/neighborsettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/neighborsettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "neighborsettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def neighborsettings_item_absent(name, match=None, reconfigure="interfaces/neighborsettings/reconfigure", search_field=None):
    """
    Ensure item neighborsettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/neighborsettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "neighborsettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- vipsettings controller ---

def vipsettings_item_present(name, data=None, match=None, reconfigure="interfaces/vipsettings/reconfigure", search_field=None):
    """
    Ensure item vipsettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/vipsettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/vipsettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "vipsettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def vipsettings_item_absent(name, match=None, reconfigure="interfaces/vipsettings/reconfigure", search_field=None):
    """
    Ensure item vipsettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/vipsettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "vipsettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- vlansettings controller ---

def vlansettings_item_present(name, data=None, match=None, reconfigure="interfaces/vlansettings/reconfigure", search_field=None):
    """
    Ensure item vlansettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/vlansettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/vlansettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "vlansettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def vlansettings_item_absent(name, match=None, reconfigure="interfaces/vlansettings/reconfigure", search_field=None):
    """
    Ensure item vlansettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/vlansettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "vlansettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- vxlansettings controller ---

def vxlansettings_item_present(name, data=None, match=None, reconfigure="interfaces/vxlansettings/reconfigure", search_field=None):
    """
    Ensure item vxlansettings present in interfaces.

    Wraps opnsense.item_present for /api/interfaces/vxlansettings/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default interfaces/vxlansettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "interfaces", "vxlansettings", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def vxlansettings_item_absent(name, match=None, reconfigure="interfaces/vxlansettings/reconfigure", search_field=None):
    """
    Ensure item vxlansettings absent in interfaces.

    Wraps opnsense.item_absent for /api/interfaces/vxlansettings/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "interfaces", "vxlansettings", "item", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="assignment", action="reconfigure"):
    """
    Trigger reconfigure for interfaces.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("interfaces", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured interfaces/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"interfaces/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
