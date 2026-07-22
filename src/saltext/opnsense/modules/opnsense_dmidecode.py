# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dmidecode wrappers.

Generated from controllers.json for module dmidecode.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dmidecode/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dmidecode"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def get_service():
    """
    Get service singleton config in dmidecode/service.

    Wraps: GET /api/dmidecode/service/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("dmidecode", "service")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for dmidecode.

    Wraps: POST /api/dmidecode/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dmidecode", controller, action, data)
