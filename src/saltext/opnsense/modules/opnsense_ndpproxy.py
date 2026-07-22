# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ndpproxy wrappers.

Generated from controllers.json for module ndpproxy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/ndpproxy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ndpproxy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- general controller ---

def search_alias(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search alias entries in ndpproxy/general.

    Wraps: POST /api/ndpproxy/general/searchAlias

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ndpproxy", "general", "alias", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_alias(uuid=None):
    """
    Get alias entry in ndpproxy/general.

    Wraps: GET /api/ndpproxy/general/getAlias/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ndpproxy", "general", "alias", uuid)


def add_alias(data):
    """
    Add alias entry in ndpproxy/general.

    Wraps: POST /api/ndpproxy/general/addAlias

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ndpproxy", "general", "alias", data)


def set_alias(uuid, data):
    """
    Set/update alias entry in ndpproxy/general.

    Wraps: POST /api/ndpproxy/general/setAlias/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ndpproxy", "general", "alias", uuid, data)


def del_alias(uuid):
    """
    Delete alias entry in ndpproxy/general.

    Wraps: POST /api/ndpproxy/general/delAlias/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ndpproxy", "general", "alias", uuid)



# Generic module-level helpers

def reconfigure(controller="general", action="reconfigure", data=None):
    """
    Generic reconfigure for ndpproxy.

    Wraps: POST /api/ndpproxy/{controller}/{action}

    :param controller: Controller name, default general
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ndpproxy", controller, action, data)
