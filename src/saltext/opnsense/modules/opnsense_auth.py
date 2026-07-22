# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense auth wrappers.

Generated from controllers.json for module auth.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/auth/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_auth"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- group controller ---

def search_group(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search group entries in auth/group.

    Wraps: POST /api/auth/group/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("auth", "group", "group", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_group(uuid=None):
    """
    Get group entry in auth/group.

    Wraps: GET /api/auth/group/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("auth", "group", "group", uuid)


def add_group(data):
    """
    Add group entry in auth/group.

    Wraps: POST /api/auth/group/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("auth", "group", "group", data)


def set_group(uuid, data):
    """
    Set/update group entry in auth/group.

    Wraps: POST /api/auth/group/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("auth", "group", "group", uuid, data)


def del_group(uuid):
    """
    Delete group entry in auth/group.

    Wraps: POST /api/auth/group/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("auth", "group", "group", uuid)


# --- priv controller ---

def search_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in auth/priv.

    Wraps: POST /api/auth/priv/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("auth", "priv", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_item(uuid=None):
    """
    Get item entry in auth/priv.

    Wraps: GET /api/auth/priv/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("auth", "priv", "item", uuid)


def set_item(uuid, data):
    """
    Set/update item entry in auth/priv.

    Wraps: POST /api/auth/priv/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("auth", "priv", "item", uuid, data)


# --- user controller ---

def search_api_key(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search api_key entries in auth/user.

    Wraps: POST /api/auth/user/searchApiKey

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("auth", "user", "api_key", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_api_key(uuid=None):
    """
    Get api_key entry in auth/user.

    Wraps: GET /api/auth/user/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("auth", "user", "api_key", uuid)


def add_api_key(data):
    """
    Add api_key entry in auth/user.

    Wraps: POST /api/auth/user/addApiKey

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("auth", "user", "api_key", data)


def set_api_key(uuid, data):
    """
    Set/update api_key entry in auth/user.

    Wraps: POST /api/auth/user/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("auth", "user", "api_key", uuid, data)


def del_api_key(uuid):
    """
    Delete api_key entry in auth/user.

    Wraps: POST /api/auth/user/delApiKey/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("auth", "user", "api_key", uuid)


def user_download(data=None, uuid=None):
    """
    Execute download in auth/user.

    Wraps: /api/auth/user/download

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("auth", "user", "download", uuid=uuid, data=data)


def user_new_otp_seed(data=None, uuid=None):
    """
    Execute newOtpSeed in auth/user.

    Wraps: /api/auth/user/newOtpSeed

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("auth", "user", "newOtpSeed", uuid=uuid, data=data)


def user_upload(data=None, uuid=None):
    """
    Execute upload in auth/user.

    Wraps: /api/auth/user/upload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("auth", "user", "upload", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="group", action="reconfigure", data=None):
    """
    Generic reconfigure for auth.

    Wraps: POST /api/auth/{controller}/{action}

    :param controller: Controller name, default group
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("auth", controller, action, data)
