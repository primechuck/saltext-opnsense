# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ntopng wrappers.

Generated from controllers.json for module ntopng.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/ntopng/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ntopng"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_checkredis(data=None, uuid=None):
    """
    Execute checkredis in ntopng/service.

    Wraps: /api/ntopng/service/checkredis

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ntopng", "service", "checkredis", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for ntopng.

    Wraps: POST /api/ntopng/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ntopng", controller, action, data)
