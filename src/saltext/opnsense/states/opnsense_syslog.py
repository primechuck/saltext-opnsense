# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense syslog state wrappers.

Generated from controllers.json for module syslog.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_syslog"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def destination_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure destination settings present in syslog.

    Wraps opnsense.item_present for /api/syslog/settings/searchDestination

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "syslog", "settings", "destination", data, match=match, reconfigure=reconfigure, search_field=search_field)


def destination_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure destination settings absent in syslog.

    Wraps opnsense.item_absent for /api/syslog/settings/searchDestination

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "syslog", "settings", "destination", match=match, reconfigure=reconfigure, search_field=search_field)


def destinations_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure destinations settings present in syslog.

    Wraps opnsense.item_present for /api/syslog/settings/searchDestinations

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "syslog", "settings", "destinations", data, match=match, reconfigure=reconfigure, search_field=search_field)


def destinations_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure destinations settings absent in syslog.

    Wraps opnsense.item_absent for /api/syslog/settings/searchDestinations

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "syslog", "settings", "destinations", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for syslog.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("syslog", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured syslog/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"syslog/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
