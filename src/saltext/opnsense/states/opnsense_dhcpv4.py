# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dhcpv4 state wrappers.

Generated from controllers.json for module dhcpv4.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dhcpv4"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- leases controller ---

def lease_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases present in dhcpv4.

    Wraps opnsense.item_present for /api/dhcpv4/leases/searchLease

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dhcpv4", "leases", "lease", data, match=match, reconfigure=reconfigure, search_field=search_field)


def lease_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases absent in dhcpv4.

    Wraps opnsense.item_absent for /api/dhcpv4/leases/searchLease

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dhcpv4", "leases", "lease", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="leases", action="reconfigure"):
    """
    Trigger reconfigure for dhcpv4.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("dhcpv4", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured dhcpv4/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"dhcpv4/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
