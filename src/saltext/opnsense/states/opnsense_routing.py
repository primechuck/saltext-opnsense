# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense routing state wrappers.

Generated from controllers.json for module routing.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_routing"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- groupsettings controller ---

def groupsetting_present(name, data=None, match=None, reconfigure="routing/groupsettings/reconfigure", search_field=None):
    """
    Ensure groupsetting groupsettings present in routing.

    Wraps opnsense.item_present for /api/routing/groupsettings/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default routing/groupsettings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "routing", "groupsettings", "groupsetting", data, match=match, reconfigure=reconfigure, search_field=search_field)


def groupsetting_absent(name, match=None, reconfigure="routing/groupsettings/reconfigure", search_field=None):
    """
    Ensure groupsetting groupsettings absent in routing.

    Wraps opnsense.item_absent for /api/routing/groupsettings/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "routing", "groupsettings", "groupsetting", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def gateway_present(name, data=None, match=None, reconfigure="routing/settings/reconfigure", search_field=None):
    """
    Ensure gateway settings present in routing.

    Wraps opnsense.item_present for /api/routing/settings/searchGateway

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default routing/settings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "routing", "settings", "gateway", data, match=match, reconfigure=reconfigure, search_field=search_field)


def gateway_absent(name, match=None, reconfigure="routing/settings/reconfigure", search_field=None):
    """
    Ensure gateway settings absent in routing.

    Wraps opnsense.item_absent for /api/routing/settings/searchGateway

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "routing", "settings", "gateway", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="groupsettings", action="reconfigure"):
    """
    Trigger reconfigure for routing.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("routing", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured routing/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"routing/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
