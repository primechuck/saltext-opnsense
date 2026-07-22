# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense gridexample wrappers.

Generated from controllers.json for module gridexample.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/gridexample/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_gridexample"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in gridexample/service.

    Wraps: POST /api/gridexample/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("gridexample", "service", action, data)


# --- settings controller ---

def search_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in gridexample/settings.

    Wraps: POST /api/gridexample/settings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("gridexample", "settings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_item(uuid=None):
    """
    Get item entry in gridexample/settings.

    Wraps: GET /api/gridexample/settings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("gridexample", "settings", "item", uuid)


def add_item(data):
    """
    Add item entry in gridexample/settings.

    Wraps: POST /api/gridexample/settings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("gridexample", "settings", "item", data)


def set_item(uuid, data):
    """
    Set/update item entry in gridexample/settings.

    Wraps: POST /api/gridexample/settings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("gridexample", "settings", "item", uuid, data)


def del_item(uuid):
    """
    Delete item entry in gridexample/settings.

    Wraps: POST /api/gridexample/settings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("gridexample", "settings", "item", uuid)


def toggle_item(uuid, enabled=None):
    """
    Toggle item entry in gridexample/settings.

    Wraps: POST /api/gridexample/settings/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("gridexample", "settings", "item", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for gridexample.

    Wraps: POST /api/gridexample/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("gridexample", controller, action, data)
