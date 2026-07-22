# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense proxy state wrappers.

Generated from controllers.json for module proxy.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_proxy"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- acl controller ---

def custom_policy_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure custom_policy acl present in proxy.

    Wraps opnsense.item_present for /api/proxy/acl/searchCustomPolicy

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "acl", "custom_policy", data, match=match, reconfigure=reconfigure, search_field=search_field)


def custom_policy_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure custom_policy acl absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/acl/searchCustomPolicy

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "acl", "custom_policy", match=match, reconfigure=reconfigure, search_field=search_field)


def policy_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure policy acl present in proxy.

    Wraps opnsense.item_present for /api/proxy/acl/searchPolicy

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "acl", "policy", data, match=match, reconfigure=reconfigure, search_field=search_field)


def policy_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure policy acl absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/acl/searchPolicy

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "acl", "policy", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def pac_match_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure pac_match settings present in proxy.

    Wraps opnsense.item_present for /api/proxy/settings/searchPacMatch

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "settings", "pac_match", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pac_match_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure pac_match settings absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/settings/searchPacMatch

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "settings", "pac_match", match=match, reconfigure=reconfigure, search_field=search_field)


def pac_proxy_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure pac_proxy settings present in proxy.

    Wraps opnsense.item_present for /api/proxy/settings/searchPacProxy

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "settings", "pac_proxy", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pac_proxy_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure pac_proxy settings absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/settings/searchPacProxy

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "settings", "pac_proxy", match=match, reconfigure=reconfigure, search_field=search_field)


def pac_rule_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure pac_rule settings present in proxy.

    Wraps opnsense.item_present for /api/proxy/settings/searchPacRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "settings", "pac_rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pac_rule_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure pac_rule settings absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/settings/searchPacRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "settings", "pac_rule", match=match, reconfigure=reconfigure, search_field=search_field)


def remote_blacklist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure remote_blacklist settings present in proxy.

    Wraps opnsense.item_present for /api/proxy/settings/searchRemoteBlacklist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "settings", "remote_blacklist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def remote_blacklist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure remote_blacklist settings absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/settings/searchRemoteBlacklist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "settings", "remote_blacklist", match=match, reconfigure=reconfigure, search_field=search_field)


def remote_blacklists_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure remote_blacklists settings present in proxy.

    Wraps opnsense.item_present for /api/proxy/settings/searchRemoteBlacklists

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "proxy", "settings", "remote_blacklists", data, match=match, reconfigure=reconfigure, search_field=search_field)


def remote_blacklists_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure remote_blacklists settings absent in proxy.

    Wraps opnsense.item_absent for /api/proxy/settings/searchRemoteBlacklists

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "proxy", "settings", "remote_blacklists", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="acl", action="reconfigure"):
    """
    Trigger reconfigure for proxy.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("proxy", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured proxy/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"proxy/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
