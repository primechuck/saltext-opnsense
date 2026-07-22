# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dhcpv6 wrappers.

Generated from controllers.json for module dhcpv6.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dhcpv6/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dhcpv6"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- leases controller ---

def search_lease(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search lease entries in dhcpv6/leases.

    Wraps: POST /api/dhcpv6/leases/searchLease

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dhcpv6", "leases", "lease", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def del_lease(uuid):
    """
    Delete lease entry in dhcpv6/leases.

    Wraps: POST /api/dhcpv6/leases/delLease/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dhcpv6", "leases", "lease", uuid)


def search_prefix(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search prefix entries in dhcpv6/leases.

    Wraps: POST /api/dhcpv6/leases/searchPrefix

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dhcpv6", "leases", "prefix", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)



# Generic module-level helpers

def reconfigure(controller="leases", action="reconfigure", data=None):
    """
    Generic reconfigure for dhcpv6.

    Wraps: POST /api/dhcpv6/{controller}/{action}

    :param controller: Controller name, default leases
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dhcpv6", controller, action, data)
