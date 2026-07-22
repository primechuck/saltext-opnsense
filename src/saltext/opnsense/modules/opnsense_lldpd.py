# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense lldpd wrappers.

Generated from controllers.json for module lldpd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/lldpd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_lldpd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_neighbor(data=None, uuid=None):
    """
    Execute neighbor in lldpd/service.

    Wraps: /api/lldpd/service/neighbor

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("lldpd", "service", "neighbor", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for lldpd.

    Wraps: POST /api/lldpd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("lldpd", controller, action, data)
