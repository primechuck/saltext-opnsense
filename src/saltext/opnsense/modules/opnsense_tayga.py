# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense tayga wrappers.

Generated from controllers.json for module tayga.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/tayga/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_tayga"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- mapping controller ---

def search_staticmapping(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search staticmapping entries in tayga/mapping.

    Wraps: POST /api/tayga/mapping/searchStaticmapping

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tayga", "mapping", "staticmapping", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_staticmapping(uuid=None):
    """
    Get staticmapping entry in tayga/mapping.

    Wraps: GET /api/tayga/mapping/getStaticmapping/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tayga", "mapping", "staticmapping", uuid)


def add_staticmapping(data):
    """
    Add staticmapping entry in tayga/mapping.

    Wraps: POST /api/tayga/mapping/addStaticmapping

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tayga", "mapping", "staticmapping", data)


def set_staticmapping(uuid, data):
    """
    Set/update staticmapping entry in tayga/mapping.

    Wraps: POST /api/tayga/mapping/setStaticmapping/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tayga", "mapping", "staticmapping", uuid, data)


def del_staticmapping(uuid):
    """
    Delete staticmapping entry in tayga/mapping.

    Wraps: POST /api/tayga/mapping/delStaticmapping/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tayga", "mapping", "staticmapping", uuid)


def toggle_staticmapping(uuid, enabled=None):
    """
    Toggle staticmapping entry in tayga/mapping.

    Wraps: POST /api/tayga/mapping/toggleStaticmapping/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tayga", "mapping", "staticmapping", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="mapping", action="reconfigure", data=None):
    """
    Generic reconfigure for tayga.

    Wraps: POST /api/tayga/{controller}/{action}

    :param controller: Controller name, default mapping
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("tayga", controller, action, data)
