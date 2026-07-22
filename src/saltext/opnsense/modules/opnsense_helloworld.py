# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense helloworld wrappers.

Generated from controllers.json for module helloworld.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/helloworld/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_helloworld"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reload(data=None, uuid=None):
    """
    Execute reload in helloworld/service.

    Wraps: /api/helloworld/service/reload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("helloworld", "service", "reload", uuid=uuid, data=data)


def service_test(data=None, uuid=None):
    """
    Execute test in helloworld/service.

    Wraps: /api/helloworld/service/test

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("helloworld", "service", "test", uuid=uuid, data=data)


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in helloworld/settings.

    Wraps: GET /api/helloworld/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("helloworld", "settings")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for helloworld.

    Wraps: POST /api/helloworld/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("helloworld", controller, action, data)
