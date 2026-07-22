# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense wol wrappers.

Generated from controllers.json for module wol.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/wol/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_wol"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- wol controller ---

def search_host(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search host entries in wol/wol.

    Wraps: POST /api/wol/wol/searchHost

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("wol", "wol", "host", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_host(uuid=None):
    """
    Get host entry in wol/wol.

    Wraps: GET /api/wol/wol/getHost/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("wol", "wol", "host", uuid)


def add_host(data):
    """
    Add host entry in wol/wol.

    Wraps: POST /api/wol/wol/addHost

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("wol", "wol", "host", data)


def set_host(uuid, data):
    """
    Set/update host entry in wol/wol.

    Wraps: POST /api/wol/wol/setHost/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("wol", "wol", "host", uuid, data)


def del_host(uuid):
    """
    Delete host entry in wol/wol.

    Wraps: POST /api/wol/wol/delHost/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("wol", "wol", "host", uuid)


def wol_getwake(data=None, uuid=None):
    """
    Execute getwake in wol/wol.

    Wraps: /api/wol/wol/getwake

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wol", "wol", "getwake", uuid=uuid, data=data)


def wol_wakeall(data=None, uuid=None):
    """
    Execute wakeall in wol/wol.

    Wraps: /api/wol/wol/wakeall

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wol", "wol", "wakeall", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="wol", action="reconfigure", data=None):
    """
    Generic reconfigure for wol.

    Wraps: POST /api/wol/{controller}/{action}

    :param controller: Controller name, default wol
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("wol", controller, action, data)
