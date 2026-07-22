# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense captiveportal state wrappers.

Generated from controllers.json for module captiveportal.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_captiveportal"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- session controller ---

def session_present(name, data=None, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure session session present in captiveportal.

    Wraps opnsense.item_present for /api/captiveportal/session/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default captiveportal/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "captiveportal", "session", "session", data, match=match, reconfigure=reconfigure, search_field=search_field)


def session_absent(name, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure session session absent in captiveportal.

    Wraps opnsense.item_absent for /api/captiveportal/session/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "captiveportal", "session", "session", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def zone_present(name, data=None, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure zone settings present in captiveportal.

    Wraps opnsense.item_present for /api/captiveportal/settings/searchZone

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default captiveportal/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "captiveportal", "settings", "zone", data, match=match, reconfigure=reconfigure, search_field=search_field)


def zone_absent(name, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure zone settings absent in captiveportal.

    Wraps opnsense.item_absent for /api/captiveportal/settings/searchZone

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "captiveportal", "settings", "zone", match=match, reconfigure=reconfigure, search_field=search_field)


def zones_present(name, data=None, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure zones settings present in captiveportal.

    Wraps opnsense.item_present for /api/captiveportal/settings/searchZones

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default captiveportal/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "captiveportal", "settings", "zones", data, match=match, reconfigure=reconfigure, search_field=search_field)


def zones_absent(name, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure zones settings absent in captiveportal.

    Wraps opnsense.item_absent for /api/captiveportal/settings/searchZones

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "captiveportal", "settings", "zones", match=match, reconfigure=reconfigure, search_field=search_field)


# --- template controller ---

def template_present(name, data=None, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure template template present in captiveportal.

    Wraps opnsense.item_present for /api/captiveportal/template/searchTemplate

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default captiveportal/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "captiveportal", "template", "template", data, match=match, reconfigure=reconfigure, search_field=search_field)


def template_absent(name, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure template template absent in captiveportal.

    Wraps opnsense.item_absent for /api/captiveportal/template/searchTemplate

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "captiveportal", "template", "template", match=match, reconfigure=reconfigure, search_field=search_field)


def templates_present(name, data=None, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure templates template present in captiveportal.

    Wraps opnsense.item_present for /api/captiveportal/template/searchTemplates

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default captiveportal/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "captiveportal", "template", "templates", data, match=match, reconfigure=reconfigure, search_field=search_field)


def templates_absent(name, match=None, reconfigure="captiveportal/service/reconfigure", search_field=None):
    """
    Ensure templates template absent in captiveportal.

    Wraps opnsense.item_absent for /api/captiveportal/template/searchTemplates

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "captiveportal", "template", "templates", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for captiveportal.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("captiveportal", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured captiveportal/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"captiveportal/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
