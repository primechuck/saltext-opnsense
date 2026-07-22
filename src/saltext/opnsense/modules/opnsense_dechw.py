# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dechw wrappers.

Generated from controllers.json for module dechw.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dechw/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dechw"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- info controller ---

def info_power_status(data=None, uuid=None):
    """
    Execute powerStatus in dechw/info.

    Wraps: /api/dechw/info/powerStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("dechw", "info", "powerStatus", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="info", action="reconfigure", data=None):
    """
    Generic reconfigure for dechw.

    Wraps: POST /api/dechw/{controller}/{action}

    :param controller: Controller name, default info
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dechw", controller, action, data)
