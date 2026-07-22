# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense chrony wrappers.

Generated from controllers.json for module chrony.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/chrony/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_chrony"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_chronyauthdata(data=None, uuid=None):
    """
    Execute chronyauthdata in chrony/service.

    Wraps: /api/chrony/service/chronyauthdata

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("chrony", "service", "chronyauthdata", uuid=uuid, data=data)


def service_chronysources(data=None, uuid=None):
    """
    Execute chronysources in chrony/service.

    Wraps: /api/chrony/service/chronysources

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("chrony", "service", "chronysources", uuid=uuid, data=data)


def service_chronysourcestats(data=None, uuid=None):
    """
    Execute chronysourcestats in chrony/service.

    Wraps: /api/chrony/service/chronysourcestats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("chrony", "service", "chronysourcestats", uuid=uuid, data=data)


def service_chronytracking(data=None, uuid=None):
    """
    Execute chronytracking in chrony/service.

    Wraps: /api/chrony/service/chronytracking

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("chrony", "service", "chronytracking", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for chrony.

    Wraps: POST /api/chrony/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("chrony", controller, action, data)
