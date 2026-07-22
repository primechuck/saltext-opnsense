# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense caddy state wrappers.

Generated from controllers.json for module caddy.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_caddy"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- reverseproxy controller ---

def access_list_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure access_list reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchAccessList

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "access_list", data, match=match, reconfigure=reconfigure, search_field=search_field)


def access_list_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure access_list reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchAccessList

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "access_list", match=match, reconfigure=reconfigure, search_field=search_field)


def basic_auth_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure basic_auth reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchBasicAuth

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "basic_auth", data, match=match, reconfigure=reconfigure, search_field=search_field)


def basic_auth_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure basic_auth reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchBasicAuth

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "basic_auth", match=match, reconfigure=reconfigure, search_field=search_field)


def handle_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure handle reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchHandle

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "handle", data, match=match, reconfigure=reconfigure, search_field=search_field)


def handle_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure handle reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchHandle

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "handle", match=match, reconfigure=reconfigure, search_field=search_field)


def header_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure header reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchHeader

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "header", data, match=match, reconfigure=reconfigure, search_field=search_field)


def header_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure header reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchHeader

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "header", match=match, reconfigure=reconfigure, search_field=search_field)


def layer4_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure layer4 reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchLayer4

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "layer4", data, match=match, reconfigure=reconfigure, search_field=search_field)


def layer4_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure layer4 reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchLayer4

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "layer4", match=match, reconfigure=reconfigure, search_field=search_field)


def layer4_openvpn_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure layer4_openvpn reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchLayer4Openvpn

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "layer4_openvpn", data, match=match, reconfigure=reconfigure, search_field=search_field)


def layer4_openvpn_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure layer4_openvpn reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchLayer4Openvpn

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "layer4_openvpn", match=match, reconfigure=reconfigure, search_field=search_field)


def reverse_proxy_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure reverse_proxy reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchReverseProxy

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "reverse_proxy", data, match=match, reconfigure=reconfigure, search_field=search_field)


def reverse_proxy_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure reverse_proxy reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchReverseProxy

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "reverse_proxy", match=match, reconfigure=reconfigure, search_field=search_field)


def subdomain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure subdomain reverseproxy present in caddy.

    Wraps opnsense.item_present for /api/caddy/reverseproxy/searchSubdomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "caddy", "reverseproxy", "subdomain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def subdomain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure subdomain reverseproxy absent in caddy.

    Wraps opnsense.item_absent for /api/caddy/reverseproxy/searchSubdomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "caddy", "reverseproxy", "subdomain", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="diagnostics", action="reconfigure"):
    """
    Trigger reconfigure for caddy.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("caddy", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured caddy/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"caddy/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
