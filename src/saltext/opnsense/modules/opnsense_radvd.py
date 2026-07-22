# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense radvd wrappers.

Generated from controllers.json for module radvd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/radvd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_radvd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in radvd/service.

    Wraps: POST /api/radvd/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("radvd", "service", action, data)


# --- settings controller ---

def search_entry(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search entry entries in radvd/settings.

    Wraps: POST /api/radvd/settings/searchEntry

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("radvd", "settings", "entry", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_entry(uuid=None):
    """
    Get entry entry in radvd/settings.

    Wraps: GET /api/radvd/settings/getEntry/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("radvd", "settings", "entry", uuid)


def add_entry(data):
    """
    Add entry entry in radvd/settings.

    Wraps: POST /api/radvd/settings/addEntry

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("radvd", "settings", "entry", data)


def set_entry(uuid, data):
    """
    Set/update entry entry in radvd/settings.

    Wraps: POST /api/radvd/settings/setEntry/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("radvd", "settings", "entry", uuid, data)


def del_entry(uuid):
    """
    Delete entry entry in radvd/settings.

    Wraps: POST /api/radvd/settings/delEntry/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("radvd", "settings", "entry", uuid)


def toggle_entry(uuid, enabled=None):
    """
    Toggle entry entry in radvd/settings.

    Wraps: POST /api/radvd/settings/toggleEntry/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("radvd", "settings", "entry", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for radvd.

    Wraps: POST /api/radvd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("radvd", controller, action, data)
