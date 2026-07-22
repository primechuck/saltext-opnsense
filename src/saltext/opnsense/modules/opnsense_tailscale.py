# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense tailscale wrappers.

Generated from controllers.json for module tailscale.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/tailscale/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_tailscale"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- settings controller ---

def search_subnet(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search subnet entries in tailscale/settings.

    Wraps: POST /api/tailscale/settings/searchSubnet

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tailscale", "settings", "subnet", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_subnet(uuid=None):
    """
    Get subnet entry in tailscale/settings.

    Wraps: GET /api/tailscale/settings/getSubnet/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tailscale", "settings", "subnet", uuid)


def add_subnet(data):
    """
    Add subnet entry in tailscale/settings.

    Wraps: POST /api/tailscale/settings/addSubnet

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tailscale", "settings", "subnet", data)


def set_subnet(uuid, data):
    """
    Set/update subnet entry in tailscale/settings.

    Wraps: POST /api/tailscale/settings/setSubnet/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tailscale", "settings", "subnet", uuid, data)


def del_subnet(uuid):
    """
    Delete subnet entry in tailscale/settings.

    Wraps: POST /api/tailscale/settings/delSubnet/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tailscale", "settings", "subnet", uuid)


def settings_reload(data=None, uuid=None):
    """
    Execute reload in tailscale/settings.

    Wraps: /api/tailscale/settings/reload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("tailscale", "settings", "reload", uuid=uuid, data=data)


# --- status controller ---

def status_ip(data=None, uuid=None):
    """
    Execute ip in tailscale/status.

    Wraps: /api/tailscale/status/ip

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("tailscale", "status", "ip", uuid=uuid, data=data)


def status_net(data=None, uuid=None):
    """
    Execute net in tailscale/status.

    Wraps: /api/tailscale/status/net

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("tailscale", "status", "net", uuid=uuid, data=data)


def status_status(data=None):
    """
    Execute status in tailscale/status.

    Wraps: POST /api/tailscale/status/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tailscale", "status", "status", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="settings", action="reconfigure", data=None):
    """
    Generic reconfigure for tailscale.

    Wraps: POST /api/tailscale/{controller}/{action}

    :param controller: Controller name, default settings
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("tailscale", controller, action, data)
