# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dnsmasq state wrappers.

Generated from controllers.json for module dnsmasq.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dnsmasq"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- leases controller ---

def lease_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/leases/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "leases", "lease", data, match=match, reconfigure=reconfigure, search_field=search_field)


def lease_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/leases/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "leases", "lease", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def boot_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure boot settings present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/settings/searchBoot

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "settings", "boot", data, match=match, reconfigure=reconfigure, search_field=search_field)


def boot_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure boot settings absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/settings/searchBoot

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "settings", "boot", match=match, reconfigure=reconfigure, search_field=search_field)


def domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure domain settings present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/settings/searchDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "settings", "domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure domain settings absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/settings/searchDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "settings", "domain", match=match, reconfigure=reconfigure, search_field=search_field)


def host_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure host settings present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/settings/searchHost

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "settings", "host", data, match=match, reconfigure=reconfigure, search_field=search_field)


def host_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure host settings absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/settings/searchHost

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "settings", "host", match=match, reconfigure=reconfigure, search_field=search_field)


def option_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure option settings present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/settings/searchOption

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "settings", "option", data, match=match, reconfigure=reconfigure, search_field=search_field)


def option_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure option settings absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/settings/searchOption

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "settings", "option", match=match, reconfigure=reconfigure, search_field=search_field)


def range_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure range settings present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/settings/searchRange

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "settings", "range", data, match=match, reconfigure=reconfigure, search_field=search_field)


def range_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure range settings absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/settings/searchRange

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "settings", "range", match=match, reconfigure=reconfigure, search_field=search_field)


def tag_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure tag settings present in dnsmasq.

    Wraps opnsense.item_present for /api/dnsmasq/settings/searchTag

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dnsmasq", "settings", "tag", data, match=match, reconfigure=reconfigure, search_field=search_field)


def tag_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure tag settings absent in dnsmasq.

    Wraps opnsense.item_absent for /api/dnsmasq/settings/searchTag

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dnsmasq", "settings", "tag", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="leases", action="reconfigure"):
    """
    Trigger reconfigure for dnsmasq.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("dnsmasq", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured dnsmasq/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"dnsmasq/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
