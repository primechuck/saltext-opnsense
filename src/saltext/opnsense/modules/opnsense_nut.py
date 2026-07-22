# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense nut wrappers.

Generated from controllers.json for module nut.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/nut/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_nut"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- diagnostics controller ---

def diagnostics_upsstatus(data=None, uuid=None):
    """
    Execute upsstatus in nut/diagnostics.

    Wraps: /api/nut/diagnostics/upsstatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nut", "diagnostics", "upsstatus", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="diagnostics", action="reconfigure", data=None):
    """
    Generic reconfigure for nut.

    Wraps: POST /api/nut/{controller}/{action}

    :param controller: Controller name, default diagnostics
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("nut", controller, action, data)
