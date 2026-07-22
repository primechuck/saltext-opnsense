# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense quagga state wrappers.

Generated from controllers.json for module quagga.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_quagga"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- bfd controller ---

def bfd_neighbor_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure neighbor bfd present in quagga.

    Wraps opnsense.item_present for /api/quagga/bfd/searchNeighbor

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bfd", "neighbor", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bfd_neighbor_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure neighbor bfd absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bfd/searchNeighbor

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bfd", "neighbor", match=match, reconfigure=reconfigure, search_field=search_field)


# --- bgp controller ---

def aspath_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure aspath bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchAspath

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "aspath", data, match=match, reconfigure=reconfigure, search_field=search_field)


def aspath_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure aspath bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchAspath

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "aspath", match=match, reconfigure=reconfigure, search_field=search_field)


def communitylist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure communitylist bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchCommunitylist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "communitylist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def communitylist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure communitylist bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchCommunitylist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "communitylist", match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_neighbor_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure neighbor bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchNeighbor

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "neighbor", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_neighbor_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure neighbor bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchNeighbor

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "neighbor", match=match, reconfigure=reconfigure, search_field=search_field)


def peergroup_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure peergroup bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchPeergroup

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "peergroup", data, match=match, reconfigure=reconfigure, search_field=search_field)


def peergroup_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure peergroup bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchPeergroup

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "peergroup", match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_prefixlist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure prefixlist bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchPrefixlist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "prefixlist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_prefixlist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure prefixlist bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchPrefixlist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "prefixlist", match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_redistribution_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure redistribution bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchRedistribution

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "redistribution", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_redistribution_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure redistribution bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchRedistribution

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "redistribution", match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_routemap_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure routemap bgp present in quagga.

    Wraps opnsense.item_present for /api/quagga/bgp/searchRoutemap

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "bgp", "routemap", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bgp_routemap_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure routemap bgp absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/bgp/searchRoutemap

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "bgp", "routemap", match=match, reconfigure=reconfigure, search_field=search_field)


# --- diagnostics controller ---

def bgproute4_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure bgproute4 diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchBgproute4

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "bgproute4", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bgproute4_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure bgproute4 diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchBgproute4

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "bgproute4", match=match, reconfigure=reconfigure, search_field=search_field)


def bgproute6_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure bgproute6 diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchBgproute6

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "bgproute6", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bgproute6_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure bgproute6 diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchBgproute6

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "bgproute6", match=match, reconfigure=reconfigure, search_field=search_field)


def generalroute4_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure generalroute4 diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchGeneralroute4

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "generalroute4", data, match=match, reconfigure=reconfigure, search_field=search_field)


def generalroute4_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure generalroute4 diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchGeneralroute4

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "generalroute4", match=match, reconfigure=reconfigure, search_field=search_field)


def generalroute6_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure generalroute6 diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchGeneralroute6

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "generalroute6", data, match=match, reconfigure=reconfigure, search_field=search_field)


def generalroute6_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure generalroute6 diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchGeneralroute6

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "generalroute6", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfneighbor_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfneighbor diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchOspfneighbor

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "ospfneighbor", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfneighbor_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfneighbor diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchOspfneighbor

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "ospfneighbor", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfroute_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfroute diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchOspfroute

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "ospfroute", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfroute_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfroute diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchOspfroute

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "ospfroute", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfv3database_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfv3database diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchOspfv3database

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "ospfv3database", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfv3database_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfv3database diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchOspfv3database

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "ospfv3database", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfv3route_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfv3route diagnostics present in quagga.

    Wraps opnsense.item_present for /api/quagga/diagnostics/searchOspfv3route

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "diagnostics", "ospfv3route", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfv3route_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure ospfv3route diagnostics absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/diagnostics/searchOspfv3route

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "diagnostics", "ospfv3route", match=match, reconfigure=reconfigure, search_field=search_field)


# --- ospf6settings controller ---

def ospf6settings_interface_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure interface ospf6settings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospf6settings/searchInterface

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospf6settings", "interface", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_interface_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure interface ospf6settings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospf6settings/searchInterface

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospf6settings", "interface", match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_network_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure network ospf6settings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospf6settings/searchNetwork

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospf6settings", "network", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_network_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure network ospf6settings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospf6settings/searchNetwork

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospf6settings", "network", match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_prefixlist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure prefixlist ospf6settings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospf6settings/searchPrefixlist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospf6settings", "prefixlist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_prefixlist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure prefixlist ospf6settings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospf6settings/searchPrefixlist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospf6settings", "prefixlist", match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_redistribution_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure redistribution ospf6settings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospf6settings/searchRedistribution

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospf6settings", "redistribution", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_redistribution_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure redistribution ospf6settings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospf6settings/searchRedistribution

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospf6settings", "redistribution", match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_routemap_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure routemap ospf6settings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospf6settings/searchRoutemap

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospf6settings", "routemap", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospf6settings_routemap_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure routemap ospf6settings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospf6settings/searchRoutemap

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospf6settings", "routemap", match=match, reconfigure=reconfigure, search_field=search_field)


# --- ospfsettings controller ---

def area_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure area ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchArea

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "area", data, match=match, reconfigure=reconfigure, search_field=search_field)


def area_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure area ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchArea

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "area", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_interface_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure interface ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchInterface

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "interface", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_interface_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure interface ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchInterface

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "interface", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_neighbor_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure neighbor ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchNeighbor

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "neighbor", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_neighbor_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure neighbor ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchNeighbor

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "neighbor", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_network_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure network ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchNetwork

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "network", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_network_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure network ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchNetwork

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "network", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_prefixlist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure prefixlist ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchPrefixlist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "prefixlist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_prefixlist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure prefixlist ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchPrefixlist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "prefixlist", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_redistribution_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure redistribution ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchRedistribution

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "redistribution", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_redistribution_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure redistribution ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchRedistribution

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "redistribution", match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_routemap_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure routemap ospfsettings present in quagga.

    Wraps opnsense.item_present for /api/quagga/ospfsettings/searchRoutemap

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "ospfsettings", "routemap", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ospfsettings_routemap_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure routemap ospfsettings absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/ospfsettings/searchRoutemap

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "ospfsettings", "routemap", match=match, reconfigure=reconfigure, search_field=search_field)


# --- static controller ---

def route_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure route static present in quagga.

    Wraps opnsense.item_present for /api/quagga/static/searchRoute

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "quagga", "static", "route", data, match=match, reconfigure=reconfigure, search_field=search_field)


def route_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure route static absent in quagga.

    Wraps opnsense.item_absent for /api/quagga/static/searchRoute

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "quagga", "static", "route", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="bfd", action="reconfigure"):
    """
    Trigger reconfigure for quagga.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("quagga", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured quagga/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"quagga/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
