# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense apcupsd wrappers.

Generated from controllers.json for module apcupsd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/apcupsd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_apcupsd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_get_ups_status(data=None, uuid=None):
    """
    Execute getUpsStatus in apcupsd/service.

    Wraps: /api/apcupsd/service/getUpsStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("apcupsd", "service", "getUpsStatus", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for apcupsd.

    Wraps: POST /api/apcupsd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("apcupsd", controller, action, data)
