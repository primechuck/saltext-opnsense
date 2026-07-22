# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense diagnostics state wrappers.

Generated from controllers.json for module diagnostics.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_diagnostics"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- interface controller ---

def arp_present(name, data=None, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure arp interface present in diagnostics.

    Wraps opnsense.item_present for /api/diagnostics/interface/searchArp

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default diagnostics/netflow/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "diagnostics", "interface", "arp", data, match=match, reconfigure=reconfigure, search_field=search_field)


def arp_absent(name, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure arp interface absent in diagnostics.

    Wraps opnsense.item_absent for /api/diagnostics/interface/searchArp

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "diagnostics", "interface", "arp", match=match, reconfigure=reconfigure, search_field=search_field)


def ndp_present(name, data=None, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure ndp interface present in diagnostics.

    Wraps opnsense.item_present for /api/diagnostics/interface/searchNdp

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default diagnostics/netflow/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "diagnostics", "interface", "ndp", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ndp_absent(name, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure ndp interface absent in diagnostics.

    Wraps opnsense.item_absent for /api/diagnostics/interface/searchNdp

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "diagnostics", "interface", "ndp", match=match, reconfigure=reconfigure, search_field=search_field)


# --- lvtemplate controller ---

def item_present(name, data=None, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure item lvtemplate present in diagnostics.

    Wraps opnsense.item_present for /api/diagnostics/lvtemplate/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default diagnostics/netflow/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "diagnostics", "lvtemplate", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def item_absent(name, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure item lvtemplate absent in diagnostics.

    Wraps opnsense.item_absent for /api/diagnostics/lvtemplate/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "diagnostics", "lvtemplate", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- netflow controller ---

def config_present(name, data=None, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure config netflow present in diagnostics.

    Wraps opnsense.item_present for /api/diagnostics/netflow/searchconfig

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default diagnostics/netflow/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "diagnostics", "netflow", "config", data, match=match, reconfigure=reconfigure, search_field=search_field)


def config_absent(name, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure config netflow absent in diagnostics.

    Wraps opnsense.item_absent for /api/diagnostics/netflow/searchconfig

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "diagnostics", "netflow", "config", match=match, reconfigure=reconfigure, search_field=search_field)


# --- packetcapture controller ---

def packetcapture_jobs_present(name, data=None, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure jobs packetcapture present in diagnostics.

    Wraps opnsense.item_present for /api/diagnostics/packetcapture/searchJobs

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default diagnostics/netflow/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "diagnostics", "packetcapture", "jobs", data, match=match, reconfigure=reconfigure, search_field=search_field)


def packetcapture_jobs_absent(name, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure jobs packetcapture absent in diagnostics.

    Wraps opnsense.item_absent for /api/diagnostics/packetcapture/searchJobs

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "diagnostics", "packetcapture", "jobs", match=match, reconfigure=reconfigure, search_field=search_field)


# --- ping controller ---

def ping_jobs_present(name, data=None, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure jobs ping present in diagnostics.

    Wraps opnsense.item_present for /api/diagnostics/ping/searchJobs

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default diagnostics/netflow/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "diagnostics", "ping", "jobs", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ping_jobs_absent(name, match=None, reconfigure="diagnostics/netflow/reconfigure", search_field=None):
    """
    Ensure jobs ping absent in diagnostics.

    Wraps opnsense.item_absent for /api/diagnostics/ping/searchJobs

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "diagnostics", "ping", "jobs", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="activity", action="reconfigure"):
    """
    Trigger reconfigure for diagnostics.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("diagnostics", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured diagnostics/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"diagnostics/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
