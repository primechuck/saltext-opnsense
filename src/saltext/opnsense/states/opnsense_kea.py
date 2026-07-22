# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense kea state wrappers.

Generated from controllers.json for module kea.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_kea"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- dhcpv4 controller ---

def dhcpv4_option_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure option dhcpv4 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv4/searchOption

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv4", "option", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_option_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure option dhcpv4 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv4/searchOption

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv4", "option", match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_peer_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure peer dhcpv4 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv4/searchPeer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv4", "peer", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_peer_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure peer dhcpv4 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv4/searchPeer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv4", "peer", match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_reservation_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure reservation dhcpv4 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv4/searchReservation

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv4", "reservation", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_reservation_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure reservation dhcpv4 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv4/searchReservation

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv4", "reservation", match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_subnet_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure subnet dhcpv4 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv4/searchSubnet

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv4", "subnet", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv4_subnet_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure subnet dhcpv4 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv4/searchSubnet

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv4", "subnet", match=match, reconfigure=reconfigure, search_field=search_field)


# --- dhcpv6 controller ---

def dhcpv6_option_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure option dhcpv6 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv6/searchOption

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv6", "option", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_option_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure option dhcpv6 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv6/searchOption

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv6", "option", match=match, reconfigure=reconfigure, search_field=search_field)


def pd_pool_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure pd_pool dhcpv6 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv6/searchPdPool

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv6", "pd_pool", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pd_pool_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure pd_pool dhcpv6 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv6/searchPdPool

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv6", "pd_pool", match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_peer_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure peer dhcpv6 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv6/searchPeer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv6", "peer", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_peer_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure peer dhcpv6 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv6/searchPeer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv6", "peer", match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_reservation_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure reservation dhcpv6 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv6/searchReservation

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv6", "reservation", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_reservation_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure reservation dhcpv6 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv6/searchReservation

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv6", "reservation", match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_subnet_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure subnet dhcpv6 present in kea.

    Wraps opnsense.item_present for /api/kea/dhcpv6/searchSubnet

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "dhcpv6", "subnet", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcpv6_subnet_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure subnet dhcpv6 absent in kea.

    Wraps opnsense.item_absent for /api/kea/dhcpv6/searchSubnet

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "dhcpv6", "subnet", match=match, reconfigure=reconfigure, search_field=search_field)


# --- leases controller ---

def lease_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases present in kea.

    Wraps opnsense.item_present for /api/kea/leases/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "kea", "leases", "lease", data, match=match, reconfigure=reconfigure, search_field=search_field)


def lease_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases absent in kea.

    Wraps opnsense.item_absent for /api/kea/leases/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "kea", "leases", "lease", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="ctrlagent", action="reconfigure"):
    """
    Trigger reconfigure for kea.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("kea", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured kea/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"kea/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
