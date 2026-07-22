# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dnscryptproxy state wrappers.

Generated from controllers.json for module dnscryptproxy.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dnscryptproxy"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- cloak controller ---

def cloak_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure cloak cloak present in dnscryptproxy.

    Wraps opnsense.item_present for /api/dnscryptproxy/cloak/searchCloak

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnscryptproxy", "cloak", "cloak", data, match=match, reconfigure=reconfigure, search_field=search_field)


def cloak_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure cloak cloak absent in dnscryptproxy.

    Wraps opnsense.item_absent for /api/dnscryptproxy/cloak/searchCloak

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnscryptproxy", "cloak", "cloak", match=match, reconfigure=reconfigure, search_field=search_field)


# --- forward controller ---

def forward_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure forward forward present in dnscryptproxy.

    Wraps opnsense.item_present for /api/dnscryptproxy/forward/searchForward

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnscryptproxy", "forward", "forward", data, match=match, reconfigure=reconfigure, search_field=search_field)


def forward_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure forward forward absent in dnscryptproxy.

    Wraps opnsense.item_absent for /api/dnscryptproxy/forward/searchForward

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnscryptproxy", "forward", "forward", match=match, reconfigure=reconfigure, search_field=search_field)


# --- server controller ---

def server_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure server server present in dnscryptproxy.

    Wraps opnsense.item_present for /api/dnscryptproxy/server/searchServer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnscryptproxy", "server", "server", data, match=match, reconfigure=reconfigure, search_field=search_field)


def server_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure server server absent in dnscryptproxy.

    Wraps opnsense.item_absent for /api/dnscryptproxy/server/searchServer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnscryptproxy", "server", "server", match=match, reconfigure=reconfigure, search_field=search_field)


# --- whitelist controller ---

def whitelist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure whitelist whitelist present in dnscryptproxy.

    Wraps opnsense.item_present for /api/dnscryptproxy/whitelist/searchWhitelist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnscryptproxy", "whitelist", "whitelist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def whitelist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure whitelist whitelist absent in dnscryptproxy.

    Wraps opnsense.item_absent for /api/dnscryptproxy/whitelist/searchWhitelist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnscryptproxy", "whitelist", "whitelist", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="cloak", action="reconfigure"):
    """
    Trigger reconfigure for dnscryptproxy.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("dnscryptproxy", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured dnscryptproxy/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"dnscryptproxy/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
