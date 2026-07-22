# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense wireguard state wrappers.

Generated from controllers.json for module wireguard.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_wireguard"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- client controller ---

def client_present(name, data=None, match=None, reconfigure="wireguard/service/reconfigure", search_field=None):
    """
    Ensure client client present in wireguard.

    Wraps opnsense.item_present for /api/wireguard/client/searchClient

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default wireguard/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "wireguard", "client", "client", data, match=match, reconfigure=reconfigure, search_field=search_field)


def client_absent(name, match=None, reconfigure="wireguard/service/reconfigure", search_field=None):
    """
    Ensure client client absent in wireguard.

    Wraps opnsense.item_absent for /api/wireguard/client/searchClient

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "wireguard", "client", "client", match=match, reconfigure=reconfigure, search_field=search_field)


def client_builder_present(name, data=None, match=None, reconfigure="wireguard/service/reconfigure", search_field=None):
    """
    Ensure client_builder client present in wireguard.

    Wraps opnsense.item_present for /api/wireguard/client/searchClientBuilder

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default wireguard/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "wireguard", "client", "client_builder", data, match=match, reconfigure=reconfigure, search_field=search_field)


def client_builder_absent(name, match=None, reconfigure="wireguard/service/reconfigure", search_field=None):
    """
    Ensure client_builder client absent in wireguard.

    Wraps opnsense.item_absent for /api/wireguard/client/searchClientBuilder

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "wireguard", "client", "client_builder", match=match, reconfigure=reconfigure, search_field=search_field)


# --- server controller ---

def server_present(name, data=None, match=None, reconfigure="wireguard/service/reconfigure", search_field=None):
    """
    Ensure server server present in wireguard.

    Wraps opnsense.item_present for /api/wireguard/server/searchServer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default wireguard/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "wireguard", "server", "server", data, match=match, reconfigure=reconfigure, search_field=search_field)


def server_absent(name, match=None, reconfigure="wireguard/service/reconfigure", search_field=None):
    """
    Ensure server server absent in wireguard.

    Wraps opnsense.item_absent for /api/wireguard/server/searchServer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "wireguard", "server", "server", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for wireguard.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("wireguard", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured wireguard/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"wireguard/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
