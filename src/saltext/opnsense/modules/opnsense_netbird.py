# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense netbird wrappers.

Generated from controllers.json for module netbird.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/netbird/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_netbird"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- authentication controller ---

def get_authentication():
    """
    Get authentication singleton config in netbird/authentication.

    Wraps: GET /api/netbird/authentication/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("netbird", "authentication")


def authentication_down(data=None, uuid=None):
    """
    Execute down in netbird/authentication.

    Wraps: /api/netbird/authentication/down

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("netbird", "authentication", "down", uuid=uuid, data=data)


def authentication_up(data=None, uuid=None):
    """
    Execute up in netbird/authentication.

    Wraps: /api/netbird/authentication/up

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("netbird", "authentication", "up", uuid=uuid, data=data)


# --- settings controller ---

def settings_sync(data=None, uuid=None):
    """
    Execute sync in netbird/settings.

    Wraps: /api/netbird/settings/sync

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("netbird", "settings", "sync", uuid=uuid, data=data)


# --- status controller ---

def status_status(data=None):
    """
    Execute status in netbird/status.

    Wraps: POST /api/netbird/status/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("netbird", "status", "status", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="authentication", action="reconfigure", data=None):
    """
    Generic reconfigure for netbird.

    Wraps: POST /api/netbird/{controller}/{action}

    :param controller: Controller name, default authentication
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("netbird", controller, action, data)
