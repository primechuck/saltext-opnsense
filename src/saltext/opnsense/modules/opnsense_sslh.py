# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense sslh wrappers.

Generated from controllers.json for module sslh.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/sslh/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_sslh"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- settings controller ---

def settings_index(data=None, uuid=None):
    """
    Execute index in sslh/settings.

    Wraps: /api/sslh/settings/index

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("sslh", "settings", "index", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="settings", action="reconfigure", data=None):
    """
    Generic reconfigure for sslh.

    Wraps: POST /api/sslh/{controller}/{action}

    :param controller: Controller name, default settings
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("sslh", controller, action, data)
