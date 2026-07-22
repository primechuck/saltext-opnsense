# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense wireguard wrappers.

Generated from controllers.json for module wireguard.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/wireguard/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_wireguard"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- client controller ---

def search_client(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search client entries in wireguard/client.

    Wraps: POST /api/wireguard/client/searchClient

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("wireguard", "client", "client", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_client(uuid=None):
    """
    Get client entry in wireguard/client.

    Wraps: GET /api/wireguard/client/getClient/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("wireguard", "client", "client", uuid)


def add_client(data):
    """
    Add client entry in wireguard/client.

    Wraps: POST /api/wireguard/client/addClient

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("wireguard", "client", "client", data)


def set_client(uuid, data):
    """
    Set/update client entry in wireguard/client.

    Wraps: POST /api/wireguard/client/setClient/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("wireguard", "client", "client", uuid, data)


def del_client(uuid):
    """
    Delete client entry in wireguard/client.

    Wraps: POST /api/wireguard/client/delClient/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("wireguard", "client", "client", uuid)


def toggle_client(uuid, enabled=None):
    """
    Toggle client entry in wireguard/client.

    Wraps: POST /api/wireguard/client/toggleClient/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("wireguard", "client", "client", uuid, enabled)


def get_client_builder(uuid=None):
    """
    Get client_builder entry in wireguard/client.

    Wraps: GET /api/wireguard/client/getClientBuilder/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("wireguard", "client", "client_builder", uuid)


def add_client_builder(data):
    """
    Add client_builder entry in wireguard/client.

    Wraps: POST /api/wireguard/client/addClientBuilder

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("wireguard", "client", "client_builder", data)


def client_get_server_info(data=None, uuid=None):
    """
    Execute getServerInfo in wireguard/client.

    Wraps: /api/wireguard/client/getServerInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wireguard", "client", "getServerInfo", uuid=uuid, data=data)


def client_list_servers(data=None, uuid=None):
    """
    Execute listServers in wireguard/client.

    Wraps: /api/wireguard/client/listServers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wireguard", "client", "listServers", uuid=uuid, data=data)


def client_psk(data=None, uuid=None):
    """
    Execute psk in wireguard/client.

    Wraps: /api/wireguard/client/psk

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wireguard", "client", "psk", uuid=uuid, data=data)


# --- server controller ---

def search_server(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search server entries in wireguard/server.

    Wraps: POST /api/wireguard/server/searchServer

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("wireguard", "server", "server", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_server(uuid=None):
    """
    Get server entry in wireguard/server.

    Wraps: GET /api/wireguard/server/getServer/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("wireguard", "server", "server", uuid)


def add_server(data):
    """
    Add server entry in wireguard/server.

    Wraps: POST /api/wireguard/server/addServer

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("wireguard", "server", "server", data)


def set_server(uuid, data):
    """
    Set/update server entry in wireguard/server.

    Wraps: POST /api/wireguard/server/setServer/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("wireguard", "server", "server", uuid, data)


def del_server(uuid):
    """
    Delete server entry in wireguard/server.

    Wraps: POST /api/wireguard/server/delServer/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("wireguard", "server", "server", uuid)


def toggle_server(uuid, enabled=None):
    """
    Toggle server entry in wireguard/server.

    Wraps: POST /api/wireguard/server/toggleServer/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("wireguard", "server", "server", uuid, enabled)


def server_key_pair(data=None, uuid=None):
    """
    Execute keyPair in wireguard/server.

    Wraps: /api/wireguard/server/keyPair

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wireguard", "server", "keyPair", uuid=uuid, data=data)


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in wireguard/service.

    Wraps: POST /api/wireguard/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("wireguard", "service", action, data)


def service_show(data=None, uuid=None):
    """
    Execute show in wireguard/service.

    Wraps: /api/wireguard/service/show

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("wireguard", "service", "show", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for wireguard.

    Wraps: POST /api/wireguard/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("wireguard", controller, action, data)
