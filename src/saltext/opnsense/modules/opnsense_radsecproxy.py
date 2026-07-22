# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense radsecproxy wrappers.

Generated from controllers.json for module radsecproxy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/radsecproxy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_radsecproxy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- clients controller ---

def search_clients_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in radsecproxy/clients.

    Wraps: POST /api/radsecproxy/clients/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("radsecproxy", "clients", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_clients_item(uuid=None):
    """
    Get item entry in radsecproxy/clients.

    Wraps: GET /api/radsecproxy/clients/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("radsecproxy", "clients", "item", uuid)


def add_clients_item(data):
    """
    Add item entry in radsecproxy/clients.

    Wraps: POST /api/radsecproxy/clients/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("radsecproxy", "clients", "item", data)


def set_clients_item(uuid, data):
    """
    Set/update item entry in radsecproxy/clients.

    Wraps: POST /api/radsecproxy/clients/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("radsecproxy", "clients", "item", uuid, data)


def del_clients_item(uuid):
    """
    Delete item entry in radsecproxy/clients.

    Wraps: POST /api/radsecproxy/clients/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("radsecproxy", "clients", "item", uuid)


def toggle_clients_item(uuid, enabled=None):
    """
    Toggle item entry in radsecproxy/clients.

    Wraps: POST /api/radsecproxy/clients/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("radsecproxy", "clients", "item", uuid, enabled)


# --- realms controller ---

def search_realms_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in radsecproxy/realms.

    Wraps: POST /api/radsecproxy/realms/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("radsecproxy", "realms", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_realms_item(uuid=None):
    """
    Get item entry in radsecproxy/realms.

    Wraps: GET /api/radsecproxy/realms/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("radsecproxy", "realms", "item", uuid)


def add_realms_item(data):
    """
    Add item entry in radsecproxy/realms.

    Wraps: POST /api/radsecproxy/realms/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("radsecproxy", "realms", "item", data)


def set_realms_item(uuid, data):
    """
    Set/update item entry in radsecproxy/realms.

    Wraps: POST /api/radsecproxy/realms/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("radsecproxy", "realms", "item", uuid, data)


def del_realms_item(uuid):
    """
    Delete item entry in radsecproxy/realms.

    Wraps: POST /api/radsecproxy/realms/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("radsecproxy", "realms", "item", uuid)


def toggle_realms_item(uuid, enabled=None):
    """
    Toggle item entry in radsecproxy/realms.

    Wraps: POST /api/radsecproxy/realms/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("radsecproxy", "realms", "item", uuid, enabled)


# --- rewrites controller ---

def search_rewrites_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in radsecproxy/rewrites.

    Wraps: POST /api/radsecproxy/rewrites/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("radsecproxy", "rewrites", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_rewrites_item(uuid=None):
    """
    Get item entry in radsecproxy/rewrites.

    Wraps: GET /api/radsecproxy/rewrites/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("radsecproxy", "rewrites", "item", uuid)


def add_rewrites_item(data):
    """
    Add item entry in radsecproxy/rewrites.

    Wraps: POST /api/radsecproxy/rewrites/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("radsecproxy", "rewrites", "item", data)


def set_rewrites_item(uuid, data):
    """
    Set/update item entry in radsecproxy/rewrites.

    Wraps: POST /api/radsecproxy/rewrites/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("radsecproxy", "rewrites", "item", uuid, data)


def del_rewrites_item(uuid):
    """
    Delete item entry in radsecproxy/rewrites.

    Wraps: POST /api/radsecproxy/rewrites/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("radsecproxy", "rewrites", "item", uuid)


def toggle_rewrites_item(uuid, enabled=None):
    """
    Toggle item entry in radsecproxy/rewrites.

    Wraps: POST /api/radsecproxy/rewrites/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("radsecproxy", "rewrites", "item", uuid, enabled)


# --- servers controller ---

def search_servers_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in radsecproxy/servers.

    Wraps: POST /api/radsecproxy/servers/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("radsecproxy", "servers", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_servers_item(uuid=None):
    """
    Get item entry in radsecproxy/servers.

    Wraps: GET /api/radsecproxy/servers/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("radsecproxy", "servers", "item", uuid)


def add_servers_item(data):
    """
    Add item entry in radsecproxy/servers.

    Wraps: POST /api/radsecproxy/servers/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("radsecproxy", "servers", "item", data)


def set_servers_item(uuid, data):
    """
    Set/update item entry in radsecproxy/servers.

    Wraps: POST /api/radsecproxy/servers/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("radsecproxy", "servers", "item", uuid, data)


def del_servers_item(uuid):
    """
    Delete item entry in radsecproxy/servers.

    Wraps: POST /api/radsecproxy/servers/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("radsecproxy", "servers", "item", uuid)


def toggle_servers_item(uuid, enabled=None):
    """
    Toggle item entry in radsecproxy/servers.

    Wraps: POST /api/radsecproxy/servers/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("radsecproxy", "servers", "item", uuid, enabled)


# --- tls controller ---

def search_tls_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in radsecproxy/tls.

    Wraps: POST /api/radsecproxy/tls/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("radsecproxy", "tls", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_tls_item(uuid=None):
    """
    Get item entry in radsecproxy/tls.

    Wraps: GET /api/radsecproxy/tls/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("radsecproxy", "tls", "item", uuid)


def add_tls_item(data):
    """
    Add item entry in radsecproxy/tls.

    Wraps: POST /api/radsecproxy/tls/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("radsecproxy", "tls", "item", data)


def set_tls_item(uuid, data):
    """
    Set/update item entry in radsecproxy/tls.

    Wraps: POST /api/radsecproxy/tls/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("radsecproxy", "tls", "item", uuid, data)


def del_tls_item(uuid):
    """
    Delete item entry in radsecproxy/tls.

    Wraps: POST /api/radsecproxy/tls/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("radsecproxy", "tls", "item", uuid)


def toggle_tls_item(uuid, enabled=None):
    """
    Toggle item entry in radsecproxy/tls.

    Wraps: POST /api/radsecproxy/tls/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("radsecproxy", "tls", "item", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="clients", action="reconfigure", data=None):
    """
    Generic reconfigure for radsecproxy.

    Wraps: POST /api/radsecproxy/{controller}/{action}

    :param controller: Controller name, default clients
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("radsecproxy", controller, action, data)
