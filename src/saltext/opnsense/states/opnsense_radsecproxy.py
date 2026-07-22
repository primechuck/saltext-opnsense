# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense radsecproxy state wrappers.

Generated from controllers.json for module radsecproxy.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_radsecproxy"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- clients controller ---

def clients_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item clients present in radsecproxy.

    Wraps opnsense.item_present for /api/radsecproxy/clients/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "radsecproxy", "clients", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def clients_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item clients absent in radsecproxy.

    Wraps opnsense.item_absent for /api/radsecproxy/clients/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "radsecproxy", "clients", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- realms controller ---

def realms_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item realms present in radsecproxy.

    Wraps opnsense.item_present for /api/radsecproxy/realms/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "radsecproxy", "realms", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def realms_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item realms absent in radsecproxy.

    Wraps opnsense.item_absent for /api/radsecproxy/realms/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "radsecproxy", "realms", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- rewrites controller ---

def rewrites_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item rewrites present in radsecproxy.

    Wraps opnsense.item_present for /api/radsecproxy/rewrites/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "radsecproxy", "rewrites", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def rewrites_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item rewrites absent in radsecproxy.

    Wraps opnsense.item_absent for /api/radsecproxy/rewrites/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "radsecproxy", "rewrites", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- servers controller ---

def servers_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item servers present in radsecproxy.

    Wraps opnsense.item_present for /api/radsecproxy/servers/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "radsecproxy", "servers", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def servers_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item servers absent in radsecproxy.

    Wraps opnsense.item_absent for /api/radsecproxy/servers/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "radsecproxy", "servers", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- tls controller ---

def tls_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item tls present in radsecproxy.

    Wraps opnsense.item_present for /api/radsecproxy/tls/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "radsecproxy", "tls", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def tls_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item tls absent in radsecproxy.

    Wraps opnsense.item_absent for /api/radsecproxy/tls/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "radsecproxy", "tls", "item", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="clients", action="reconfigure"):
    """
    Trigger reconfigure for radsecproxy.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("radsecproxy", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured radsecproxy/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"radsecproxy/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
