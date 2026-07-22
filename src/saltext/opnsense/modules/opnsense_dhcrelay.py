# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dhcrelay wrappers.

Generated from controllers.json for module dhcrelay.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dhcrelay/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dhcrelay"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in dhcrelay/service.

    Wraps: POST /api/dhcrelay/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dhcrelay", "service", action, data)


# --- settings controller ---

def search_dest(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search dest entries in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/searchDest

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dhcrelay", "settings", "dest", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dest(uuid=None):
    """
    Get dest entry in dhcrelay/settings.

    Wraps: GET /api/dhcrelay/settings/getDest/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dhcrelay", "settings", "dest", uuid)


def add_dest(data):
    """
    Add dest entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/addDest

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dhcrelay", "settings", "dest", data)


def set_dest(uuid, data):
    """
    Set/update dest entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/setDest/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dhcrelay", "settings", "dest", uuid, data)


def del_dest(uuid):
    """
    Delete dest entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/delDest/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dhcrelay", "settings", "dest", uuid)


def search_relay(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search relay entries in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/searchRelay

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dhcrelay", "settings", "relay", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_relay(uuid=None):
    """
    Get relay entry in dhcrelay/settings.

    Wraps: GET /api/dhcrelay/settings/getRelay/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dhcrelay", "settings", "relay", uuid)


def add_relay(data):
    """
    Add relay entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/addRelay

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dhcrelay", "settings", "relay", data)


def set_relay(uuid, data):
    """
    Set/update relay entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/setRelay/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dhcrelay", "settings", "relay", uuid, data)


def del_relay(uuid):
    """
    Delete relay entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/delRelay/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dhcrelay", "settings", "relay", uuid)


def toggle_relay(uuid, enabled=None):
    """
    Toggle relay entry in dhcrelay/settings.

    Wraps: POST /api/dhcrelay/settings/toggleRelay/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("dhcrelay", "settings", "relay", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for dhcrelay.

    Wraps: POST /api/dhcrelay/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dhcrelay", controller, action, data)
