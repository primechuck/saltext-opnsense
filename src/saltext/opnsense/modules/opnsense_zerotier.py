# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense zerotier wrappers.

Generated from controllers.json for module zerotier.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/zerotier/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_zerotier"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- network controller ---

def search_network(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search network entries in zerotier/network.

    Wraps: POST /api/zerotier/network/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("zerotier", "network", "network", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_network(uuid=None):
    """
    Get network entry in zerotier/network.

    Wraps: GET /api/zerotier/network/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("zerotier", "network", "network", uuid)


def add_network(data):
    """
    Add network entry in zerotier/network.

    Wraps: POST /api/zerotier/network/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("zerotier", "network", "network", data)


def set_network(uuid, data):
    """
    Set/update network entry in zerotier/network.

    Wraps: POST /api/zerotier/network/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("zerotier", "network", "network", uuid, data)


def del_network(uuid):
    """
    Delete network entry in zerotier/network.

    Wraps: POST /api/zerotier/network/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("zerotier", "network", "network", uuid)


def toggle_network(uuid, enabled=None):
    """
    Toggle network entry in zerotier/network.

    Wraps: POST /api/zerotier/network/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("zerotier", "network", "network", uuid, enabled)


def network_info(data=None, uuid=None):
    """
    Execute info in zerotier/network.

    Wraps: /api/zerotier/network/info

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("zerotier", "network", "info", uuid=uuid, data=data)


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in zerotier/settings.

    Wraps: GET /api/zerotier/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("zerotier", "settings")


def set_settings(data):
    """
    Set settings singleton config in zerotier/settings.

    Wraps: POST /api/zerotier/settings/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("zerotier", "settings", "set", data=data, method="POST")


def settings_status(data=None):
    """
    Execute status in zerotier/settings.

    Wraps: POST /api/zerotier/settings/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("zerotier", "settings", "status", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="network", action="reconfigure", data=None):
    """
    Generic reconfigure for zerotier.

    Wraps: POST /api/zerotier/{controller}/{action}

    :param controller: Controller name, default network
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("zerotier", controller, action, data)
