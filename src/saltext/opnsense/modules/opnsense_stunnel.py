# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense stunnel wrappers.

Generated from controllers.json for module stunnel.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/stunnel/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_stunnel"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- services controller ---

def search_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in stunnel/services.

    Wraps: POST /api/stunnel/services/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("stunnel", "services", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_item(uuid=None):
    """
    Get item entry in stunnel/services.

    Wraps: GET /api/stunnel/services/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("stunnel", "services", "item", uuid)


def add_item(data):
    """
    Add item entry in stunnel/services.

    Wraps: POST /api/stunnel/services/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("stunnel", "services", "item", data)


def set_item(uuid, data):
    """
    Set/update item entry in stunnel/services.

    Wraps: POST /api/stunnel/services/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("stunnel", "services", "item", uuid, data)


def del_item(uuid):
    """
    Delete item entry in stunnel/services.

    Wraps: POST /api/stunnel/services/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("stunnel", "services", "item", uuid)


def toggle_item(uuid, enabled=None):
    """
    Toggle item entry in stunnel/services.

    Wraps: POST /api/stunnel/services/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("stunnel", "services", "item", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="services", action="reconfigure", data=None):
    """
    Generic reconfigure for stunnel.

    Wraps: POST /api/stunnel/{controller}/{action}

    :param controller: Controller name, default services
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("stunnel", controller, action, data)
