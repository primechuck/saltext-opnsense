# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense hostdiscovery wrappers.

Generated from controllers.json for module hostdiscovery.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/hostdiscovery/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_hostdiscovery"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def search_service(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search service entries in hostdiscovery/service.

    Wraps: POST /api/hostdiscovery/service/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("hostdiscovery", "service", "service", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for hostdiscovery.

    Wraps: POST /api/hostdiscovery/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("hostdiscovery", controller, action, data)
