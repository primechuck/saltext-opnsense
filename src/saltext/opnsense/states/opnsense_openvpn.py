# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense openvpn state wrappers.

Generated from controllers.json for module openvpn.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_openvpn"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- clientoverwrites controller ---

def clientoverwrite_present(name, data=None, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure clientoverwrite clientoverwrites present in openvpn.

    Wraps opnsense.item_present for /api/openvpn/clientoverwrites/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default openvpn/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "openvpn", "clientoverwrites", "clientoverwrite", data, match=match, reconfigure=reconfigure, search_field=search_field)


def clientoverwrite_absent(name, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure clientoverwrite clientoverwrites absent in openvpn.

    Wraps opnsense.item_absent for /api/openvpn/clientoverwrites/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "openvpn", "clientoverwrites", "clientoverwrite", match=match, reconfigure=reconfigure, search_field=search_field)


# --- instances controller ---

def static_key_present(name, data=None, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure static_key instances present in openvpn.

    Wraps opnsense.item_present for /api/openvpn/instances/searchStaticKey

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default openvpn/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "openvpn", "instances", "static_key", data, match=match, reconfigure=reconfigure, search_field=search_field)


def static_key_absent(name, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure static_key instances absent in openvpn.

    Wraps opnsense.item_absent for /api/openvpn/instances/searchStaticKey

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "openvpn", "instances", "static_key", match=match, reconfigure=reconfigure, search_field=search_field)


# --- service controller ---

def routes_present(name, data=None, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure routes service present in openvpn.

    Wraps opnsense.item_present for /api/openvpn/service/searchRoutes

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default openvpn/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "openvpn", "service", "routes", data, match=match, reconfigure=reconfigure, search_field=search_field)


def routes_absent(name, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure routes service absent in openvpn.

    Wraps opnsense.item_absent for /api/openvpn/service/searchRoutes

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "openvpn", "service", "routes", match=match, reconfigure=reconfigure, search_field=search_field)


def sessions_present(name, data=None, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure sessions service present in openvpn.

    Wraps opnsense.item_present for /api/openvpn/service/searchSessions

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default openvpn/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "openvpn", "service", "sessions", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sessions_absent(name, match=None, reconfigure="openvpn/service/reconfigure", search_field=None):
    """
    Ensure sessions service absent in openvpn.

    Wraps opnsense.item_absent for /api/openvpn/service/searchSessions

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "openvpn", "service", "sessions", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for openvpn.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("openvpn", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured openvpn/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"openvpn/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
