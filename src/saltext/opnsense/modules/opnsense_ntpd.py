# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ntpd wrappers.

Generated from controllers.json for module ntpd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/ntpd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ntpd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_gps(data=None, uuid=None):
    """
    Execute gps in ntpd/service.

    Wraps: /api/ntpd/service/gps

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ntpd", "service", "gps", uuid=uuid, data=data)


def service_meta(data=None, uuid=None):
    """
    Execute meta in ntpd/service.

    Wraps: /api/ntpd/service/meta

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ntpd", "service", "meta", uuid=uuid, data=data)


def service_status(data=None):
    """
    Execute status in ntpd/service.

    Wraps: POST /api/ntpd/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("ntpd", "service", "status", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for ntpd.

    Wraps: POST /api/ntpd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ntpd", controller, action, data)
