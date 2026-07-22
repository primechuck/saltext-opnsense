# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense caddy wrappers.

Generated from controllers.json for module caddy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/caddy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_caddy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- diagnostics controller ---

def diagnostics_caddyfile(data=None, uuid=None):
    """
    Execute caddyfile in caddy/diagnostics.

    Wraps: /api/caddy/diagnostics/caddyfile

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("caddy", "diagnostics", "caddyfile", uuid=uuid, data=data)


def diagnostics_config(data=None, uuid=None):
    """
    Execute config in caddy/diagnostics.

    Wraps: /api/caddy/diagnostics/config

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("caddy", "diagnostics", "config", uuid=uuid, data=data)


# --- reverseproxy controller ---

def search_access_list(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search access_list entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchAccessList

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "access_list", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_access_list(uuid=None):
    """
    Get access_list entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getAccessList/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "access_list", uuid)


def add_access_list(data):
    """
    Add access_list entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addAccessList

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "access_list", data)


def set_access_list(uuid, data):
    """
    Set/update access_list entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setAccessList/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "access_list", uuid, data)


def del_access_list(uuid):
    """
    Delete access_list entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delAccessList/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "access_list", uuid)


def search_basic_auth(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search basic_auth entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchBasicAuth

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "basic_auth", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_basic_auth(uuid=None):
    """
    Get basic_auth entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getBasicAuth/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "basic_auth", uuid)


def add_basic_auth(data):
    """
    Add basic_auth entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addBasicAuth

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "basic_auth", data)


def set_basic_auth(uuid, data):
    """
    Set/update basic_auth entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setBasicAuth/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "basic_auth", uuid, data)


def del_basic_auth(uuid):
    """
    Delete basic_auth entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delBasicAuth/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "basic_auth", uuid)


def search_handle(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search handle entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchHandle

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "handle", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_handle(uuid=None):
    """
    Get handle entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getHandle/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "handle", uuid)


def add_handle(data):
    """
    Add handle entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addHandle

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "handle", data)


def set_handle(uuid, data):
    """
    Set/update handle entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setHandle/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "handle", uuid, data)


def del_handle(uuid):
    """
    Delete handle entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delHandle/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "handle", uuid)


def toggle_handle(uuid, enabled=None):
    """
    Toggle handle entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/toggleHandle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("caddy", "reverseproxy", "handle", uuid, enabled)


def search_header(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search header entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchHeader

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "header", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_header(uuid=None):
    """
    Get header entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getHeader/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "header", uuid)


def add_header(data):
    """
    Add header entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addHeader

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "header", data)


def set_header(uuid, data):
    """
    Set/update header entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setHeader/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "header", uuid, data)


def del_header(uuid):
    """
    Delete header entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delHeader/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "header", uuid)


def search_layer4(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search layer4 entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchLayer4

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "layer4", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_layer4(uuid=None):
    """
    Get layer4 entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getLayer4/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "layer4", uuid)


def add_layer4(data):
    """
    Add layer4 entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addLayer4

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "layer4", data)


def set_layer4(uuid, data):
    """
    Set/update layer4 entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setLayer4/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "layer4", uuid, data)


def del_layer4(uuid):
    """
    Delete layer4 entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delLayer4/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "layer4", uuid)


def toggle_layer4(uuid, enabled=None):
    """
    Toggle layer4 entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/toggleLayer4/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("caddy", "reverseproxy", "layer4", uuid, enabled)


def search_layer4_openvpn(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search layer4_openvpn entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchLayer4Openvpn

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "layer4_openvpn", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_layer4_openvpn(uuid=None):
    """
    Get layer4_openvpn entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getLayer4Openvpn/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "layer4_openvpn", uuid)


def add_layer4_openvpn(data):
    """
    Add layer4_openvpn entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addLayer4Openvpn

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "layer4_openvpn", data)


def set_layer4_openvpn(uuid, data):
    """
    Set/update layer4_openvpn entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setLayer4Openvpn/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "layer4_openvpn", uuid, data)


def del_layer4_openvpn(uuid):
    """
    Delete layer4_openvpn entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delLayer4Openvpn/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "layer4_openvpn", uuid)


def toggle_layer4_openvpn(uuid, enabled=None):
    """
    Toggle layer4_openvpn entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/toggleLayer4Openvpn/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("caddy", "reverseproxy", "layer4_openvpn", uuid, enabled)


def search_reverse_proxy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search reverse_proxy entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchReverseProxy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "reverse_proxy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_reverse_proxy(uuid=None):
    """
    Get reverse_proxy entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getReverseProxy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "reverse_proxy", uuid)


def add_reverse_proxy(data):
    """
    Add reverse_proxy entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addReverseProxy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "reverse_proxy", data)


def set_reverse_proxy(uuid, data):
    """
    Set/update reverse_proxy entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setReverseProxy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "reverse_proxy", uuid, data)


def del_reverse_proxy(uuid):
    """
    Delete reverse_proxy entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delReverseProxy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "reverse_proxy", uuid)


def toggle_reverse_proxy(uuid, enabled=None):
    """
    Toggle reverse_proxy entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/toggleReverseProxy/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("caddy", "reverseproxy", "reverse_proxy", uuid, enabled)


def search_subdomain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search subdomain entries in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/searchSubdomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("caddy", "reverseproxy", "subdomain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_subdomain(uuid=None):
    """
    Get subdomain entry in caddy/reverseproxy.

    Wraps: GET /api/caddy/reverseproxy/getSubdomain/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("caddy", "reverseproxy", "subdomain", uuid)


def add_subdomain(data):
    """
    Add subdomain entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/addSubdomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("caddy", "reverseproxy", "subdomain", data)


def set_subdomain(uuid, data):
    """
    Set/update subdomain entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/setSubdomain/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("caddy", "reverseproxy", "subdomain", uuid, data)


def del_subdomain(uuid):
    """
    Delete subdomain entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/delSubdomain/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("caddy", "reverseproxy", "subdomain", uuid)


def toggle_subdomain(uuid, enabled=None):
    """
    Toggle subdomain entry in caddy/reverseproxy.

    Wraps: POST /api/caddy/reverseproxy/toggleSubdomain/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("caddy", "reverseproxy", "subdomain", uuid, enabled)


def reverseproxy_get_all_reverse_domains(data=None, uuid=None):
    """
    Execute getAllReverseDomains in caddy/reverseproxy.

    Wraps: /api/caddy/reverseproxy/getAllReverseDomains

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("caddy", "reverseproxy", "getAllReverseDomains", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="diagnostics", action="reconfigure", data=None):
    """
    Generic reconfigure for caddy.

    Wraps: POST /api/caddy/{controller}/{action}

    :param controller: Controller name, default diagnostics
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("caddy", controller, action, data)
