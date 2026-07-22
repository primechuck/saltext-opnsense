# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense netsnmp wrappers.

Generated from controllers.json for module netsnmp.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/netsnmp/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_netsnmp"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- user controller ---

def search_user(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search user entries in netsnmp/user.

    Wraps: POST /api/netsnmp/user/searchUser

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("netsnmp", "user", "user", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_user(uuid=None):
    """
    Get user entry in netsnmp/user.

    Wraps: GET /api/netsnmp/user/getUser/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("netsnmp", "user", "user", uuid)


def add_user(data):
    """
    Add user entry in netsnmp/user.

    Wraps: POST /api/netsnmp/user/addUser

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("netsnmp", "user", "user", data)


def set_user(uuid, data):
    """
    Set/update user entry in netsnmp/user.

    Wraps: POST /api/netsnmp/user/setUser/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("netsnmp", "user", "user", uuid, data)


def del_user(uuid):
    """
    Delete user entry in netsnmp/user.

    Wraps: POST /api/netsnmp/user/delUser/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("netsnmp", "user", "user", uuid)


def toggle_user(uuid, enabled=None):
    """
    Toggle user entry in netsnmp/user.

    Wraps: POST /api/netsnmp/user/toggleUser/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("netsnmp", "user", "user", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="user", action="reconfigure", data=None):
    """
    Generic reconfigure for netsnmp.

    Wraps: POST /api/netsnmp/{controller}/{action}

    :param controller: Controller name, default user
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("netsnmp", controller, action, data)
