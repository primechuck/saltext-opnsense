# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense tinc state wrappers.

Generated from controllers.json for module tinc.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_tinc"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def host_present(name, data=None, match=None, reconfigure="tinc/service/reconfigure", search_field=None):
    """
    Ensure host settings present in tinc.

    Wraps opnsense.item_present for /api/tinc/settings/searchHost

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tinc/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tinc", "settings", "host", data, match=match, reconfigure=reconfigure, search_field=search_field)


def host_absent(name, match=None, reconfigure="tinc/service/reconfigure", search_field=None):
    """
    Ensure host settings absent in tinc.

    Wraps opnsense.item_absent for /api/tinc/settings/searchHost

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tinc", "settings", "host", match=match, reconfigure=reconfigure, search_field=search_field)


def network_present(name, data=None, match=None, reconfigure="tinc/service/reconfigure", search_field=None):
    """
    Ensure network settings present in tinc.

    Wraps opnsense.item_present for /api/tinc/settings/searchNetwork

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tinc/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tinc", "settings", "network", data, match=match, reconfigure=reconfigure, search_field=search_field)


def network_absent(name, match=None, reconfigure="tinc/service/reconfigure", search_field=None):
    """
    Ensure network settings absent in tinc.

    Wraps opnsense.item_absent for /api/tinc/settings/searchNetwork

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tinc", "settings", "network", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for tinc.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("tinc", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured tinc/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"tinc/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
