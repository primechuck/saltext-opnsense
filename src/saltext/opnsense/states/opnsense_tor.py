# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense tor state wrappers.

Generated from controllers.json for module tor.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_tor"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- exitacl controller ---

def exitacl_acl_present(name, data=None, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure acl exitacl present in tor.

    Wraps opnsense.item_present for /api/tor/exitacl/searchacl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tor/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tor", "exitacl", "acl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def exitacl_acl_absent(name, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure acl exitacl absent in tor.

    Wraps opnsense.item_absent for /api/tor/exitacl/searchacl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tor", "exitacl", "acl", match=match, reconfigure=reconfigure, search_field=search_field)


# --- general controller ---

def hidservauth_present(name, data=None, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure hidservauth general present in tor.

    Wraps opnsense.item_present for /api/tor/general/searchhidservauth

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tor/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tor", "general", "hidservauth", data, match=match, reconfigure=reconfigure, search_field=search_field)


def hidservauth_absent(name, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure hidservauth general absent in tor.

    Wraps opnsense.item_absent for /api/tor/general/searchhidservauth

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tor", "general", "hidservauth", match=match, reconfigure=reconfigure, search_field=search_field)


# --- hiddenservice controller ---

def service_present(name, data=None, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure service hiddenservice present in tor.

    Wraps opnsense.item_present for /api/tor/hiddenservice/searchservice

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tor/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tor", "hiddenservice", "service", data, match=match, reconfigure=reconfigure, search_field=search_field)


def service_absent(name, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure service hiddenservice absent in tor.

    Wraps opnsense.item_absent for /api/tor/hiddenservice/searchservice

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tor", "hiddenservice", "service", match=match, reconfigure=reconfigure, search_field=search_field)


# --- hiddenserviceacl controller ---

def hiddenserviceacl_acl_present(name, data=None, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure acl hiddenserviceacl present in tor.

    Wraps opnsense.item_present for /api/tor/hiddenserviceacl/searchacl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tor/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tor", "hiddenserviceacl", "acl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def hiddenserviceacl_acl_absent(name, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure acl hiddenserviceacl absent in tor.

    Wraps opnsense.item_absent for /api/tor/hiddenserviceacl/searchacl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tor", "hiddenserviceacl", "acl", match=match, reconfigure=reconfigure, search_field=search_field)


# --- socksacl controller ---

def socksacl_acl_present(name, data=None, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure acl socksacl present in tor.

    Wraps opnsense.item_present for /api/tor/socksacl/searchacl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default tor/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "tor", "socksacl", "acl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def socksacl_acl_absent(name, match=None, reconfigure="tor/service/reconfigure", search_field=None):
    """
    Ensure acl socksacl absent in tor.

    Wraps opnsense.item_absent for /api/tor/socksacl/searchacl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "tor", "socksacl", "acl", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for tor.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("tor", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured tor/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"tor/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
