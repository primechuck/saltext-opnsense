# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dhcpv4 wrappers.

Generated from controllers.json for module dhcpv4.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dhcpv4/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dhcpv4"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- leases controller ---

def search_lease(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search lease entries in dhcpv4/leases.

    Wraps: POST /api/dhcpv4/leases/searchLease

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dhcpv4", "leases", "lease", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def del_lease(uuid):
    """
    Delete lease entry in dhcpv4/leases.

    Wraps: POST /api/dhcpv4/leases/delLease/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dhcpv4", "leases", "lease", uuid)



# Generic module-level helpers

def reconfigure(controller="leases", action="reconfigure", data=None):
    """
    Generic reconfigure for dhcpv4.

    Wraps: POST /api/dhcpv4/{controller}/{action}

    :param controller: Controller name, default leases
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dhcpv4", controller, action, data)
