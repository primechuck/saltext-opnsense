# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dyndns wrappers.

Generated from controllers.json for module dyndns.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dyndns/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dyndns"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- accounts controller ---

def search_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in dyndns/accounts.

    Wraps: POST /api/dyndns/accounts/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dyndns", "accounts", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_item(uuid=None):
    """
    Get item entry in dyndns/accounts.

    Wraps: GET /api/dyndns/accounts/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dyndns", "accounts", "item", uuid)


def add_item(data):
    """
    Add item entry in dyndns/accounts.

    Wraps: POST /api/dyndns/accounts/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dyndns", "accounts", "item", data)


def set_item(uuid, data):
    """
    Set/update item entry in dyndns/accounts.

    Wraps: POST /api/dyndns/accounts/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dyndns", "accounts", "item", uuid, data)


def del_item(uuid):
    """
    Delete item entry in dyndns/accounts.

    Wraps: POST /api/dyndns/accounts/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dyndns", "accounts", "item", uuid)


def toggle_item(uuid, enabled=None):
    """
    Toggle item entry in dyndns/accounts.

    Wraps: POST /api/dyndns/accounts/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("dyndns", "accounts", "item", uuid, enabled)


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in dyndns/settings.

    Wraps: GET /api/dyndns/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("dyndns", "settings")



# Generic module-level helpers

def reconfigure(controller="accounts", action="reconfigure", data=None):
    """
    Generic reconfigure for dyndns.

    Wraps: POST /api/dyndns/{controller}/{action}

    :param controller: Controller name, default accounts
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dyndns", controller, action, data)
