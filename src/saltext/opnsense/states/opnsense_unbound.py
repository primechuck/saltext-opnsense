# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense unbound state wrappers.

Generated from controllers.json for module unbound.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_unbound"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- overview controller ---

def queries_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure queries overview present in unbound.

    Wraps opnsense.item_present for /api/unbound/overview/searchQueries

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "unbound", "overview", "queries", data, match=match, reconfigure=reconfigure, search_field=search_field)


def queries_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure queries overview absent in unbound.

    Wraps opnsense.item_absent for /api/unbound/overview/searchQueries

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "unbound", "overview", "queries", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def acl_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure acl settings present in unbound.

    Wraps opnsense.item_present for /api/unbound/settings/searchAcl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "unbound", "settings", "acl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def acl_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure acl settings absent in unbound.

    Wraps opnsense.item_absent for /api/unbound/settings/searchAcl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "unbound", "settings", "acl", match=match, reconfigure=reconfigure, search_field=search_field)


def dnsbl_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure dnsbl settings present in unbound.

    Wraps opnsense.item_present for /api/unbound/settings/searchDnsbl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "unbound", "settings", "dnsbl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dnsbl_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure dnsbl settings absent in unbound.

    Wraps opnsense.item_absent for /api/unbound/settings/searchDnsbl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "unbound", "settings", "dnsbl", match=match, reconfigure=reconfigure, search_field=search_field)


def forward_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure forward settings present in unbound.

    Wraps opnsense.item_present for /api/unbound/settings/searchForward

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "unbound", "settings", "forward", data, match=match, reconfigure=reconfigure, search_field=search_field)


def forward_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure forward settings absent in unbound.

    Wraps opnsense.item_absent for /api/unbound/settings/searchForward

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "unbound", "settings", "forward", match=match, reconfigure=reconfigure, search_field=search_field)


def host_alias_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure host_alias settings present in unbound.

    Wraps opnsense.item_present for /api/unbound/settings/searchHostAlias

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "unbound", "settings", "host_alias", data, match=match, reconfigure=reconfigure, search_field=search_field)


def host_alias_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure host_alias settings absent in unbound.

    Wraps opnsense.item_absent for /api/unbound/settings/searchHostAlias

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "unbound", "settings", "host_alias", match=match, reconfigure=reconfigure, search_field=search_field)


def host_override_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure host_override settings present in unbound.

    Wraps opnsense.item_present for /api/unbound/settings/searchHostOverride

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "unbound", "settings", "host_override", data, match=match, reconfigure=reconfigure, search_field=search_field)


def host_override_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure host_override settings absent in unbound.

    Wraps opnsense.item_absent for /api/unbound/settings/searchHostOverride

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "unbound", "settings", "host_override", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="diagnostics", action="reconfigure"):
    """
    Trigger reconfigure for unbound.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("unbound", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured unbound/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"unbound/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
