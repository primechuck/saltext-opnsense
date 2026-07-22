# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dhcrelay state wrappers.

Generated from controllers.json for module dhcrelay.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dhcrelay"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def dest_present(name, data=None, match=None, reconfigure="dhcrelay/service/reconfigure", search_field=None):
    """
    Ensure dest settings present in dhcrelay.

    Wraps opnsense.item_present for /api/dhcrelay/settings/searchDest

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default dhcrelay/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dhcrelay", "settings", "dest", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dest_absent(name, match=None, reconfigure="dhcrelay/service/reconfigure", search_field=None):
    """
    Ensure dest settings absent in dhcrelay.

    Wraps opnsense.item_absent for /api/dhcrelay/settings/searchDest

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dhcrelay", "settings", "dest", match=match, reconfigure=reconfigure, search_field=search_field)


def relay_present(name, data=None, match=None, reconfigure="dhcrelay/service/reconfigure", search_field=None):
    """
    Ensure relay settings present in dhcrelay.

    Wraps opnsense.item_present for /api/dhcrelay/settings/searchRelay

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default dhcrelay/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dhcrelay", "settings", "relay", data, match=match, reconfigure=reconfigure, search_field=search_field)


def relay_absent(name, match=None, reconfigure="dhcrelay/service/reconfigure", search_field=None):
    """
    Ensure relay settings absent in dhcrelay.

    Wraps opnsense.item_absent for /api/dhcrelay/settings/searchRelay

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dhcrelay", "settings", "relay", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for dhcrelay.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("dhcrelay", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured dhcrelay/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"dhcrelay/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
