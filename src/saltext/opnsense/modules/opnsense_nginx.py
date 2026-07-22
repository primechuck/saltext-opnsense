# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense nginx wrappers.

Generated from controllers.json for module nginx.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/nginx/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_nginx"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- bans controller ---

def search_ban(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ban entries in nginx/bans.

    Wraps: POST /api/nginx/bans/searchban

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "bans", "ban", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def del_ban(uuid):
    """
    Delete ban entry in nginx/bans.

    Wraps: POST /api/nginx/bans/delban/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "bans", "ban", uuid)


# --- logs controller ---

def logs_accesses(data=None, uuid=None):
    """
    Execute accesses in nginx/logs.

    Wraps: /api/nginx/logs/accesses

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "logs", "accesses", uuid=uuid, data=data)


def logs_errors(data=None, uuid=None):
    """
    Execute errors in nginx/logs.

    Wraps: /api/nginx/logs/errors

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "logs", "errors", uuid=uuid, data=data)


def logs_streamaccesses(data=None, uuid=None):
    """
    Execute streamaccesses in nginx/logs.

    Wraps: /api/nginx/logs/streamaccesses

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "logs", "streamaccesses", uuid=uuid, data=data)


def logs_streamerrors(data=None, uuid=None):
    """
    Execute streamerrors in nginx/logs.

    Wraps: /api/nginx/logs/streamerrors

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "logs", "streamerrors", uuid=uuid, data=data)


def logs_tls_handshakes(data=None, uuid=None):
    """
    Execute tlsHandshakes in nginx/logs.

    Wraps: /api/nginx/logs/tlsHandshakes

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "logs", "tlsHandshakes", uuid=uuid, data=data)


# --- service controller ---

def service_status(data=None):
    """
    Execute status in nginx/service.

    Wraps: POST /api/nginx/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in nginx/service.

    Wraps: POST /api/nginx/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "service", "stop", data=data, method="POST")


def service_vts(data=None, uuid=None):
    """
    Execute vts in nginx/service.

    Wraps: /api/nginx/service/vts

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "service", "vts", uuid=uuid, data=data)


# --- settings controller ---

def search_cache_path(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search cache_path entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchcachePath

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "cache_path", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_cache_path(uuid=None):
    """
    Get cache_path entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getcachePath/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "cache_path", uuid)


def add_cache_path(data):
    """
    Add cache_path entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addcachePath

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "cache_path", data)


def set_cache_path(uuid, data):
    """
    Set/update cache_path entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setcachePath/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "cache_path", uuid, data)


def del_cache_path(uuid):
    """
    Delete cache_path entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delcachePath/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "cache_path", uuid)


def search_credential(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search credential entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchcredential

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "credential", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_credential(uuid=None):
    """
    Get credential entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getcredential/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "credential", uuid)


def add_credential(data):
    """
    Add credential entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addcredential

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "credential", data)


def set_credential(uuid, data):
    """
    Set/update credential entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setcredential/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "credential", uuid, data)


def del_credential(uuid):
    """
    Delete credential entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delcredential/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "credential", uuid)


def search_custompolicy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search custompolicy entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchcustompolicy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "custompolicy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_custompolicy(uuid=None):
    """
    Get custompolicy entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getcustompolicy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "custompolicy", uuid)


def add_custompolicy(data):
    """
    Add custompolicy entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addcustompolicy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "custompolicy", data)


def set_custompolicy(uuid, data):
    """
    Set/update custompolicy entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setcustompolicy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "custompolicy", uuid, data)


def del_custompolicy(uuid):
    """
    Delete custompolicy entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delcustompolicy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "custompolicy", uuid)


def search_errorpage(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search errorpage entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searcherrorpage

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "errorpage", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_errorpage(uuid=None):
    """
    Get errorpage entry in nginx/settings.

    Wraps: GET /api/nginx/settings/geterrorpage/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "errorpage", uuid)


def add_errorpage(data):
    """
    Add errorpage entry in nginx/settings.

    Wraps: POST /api/nginx/settings/adderrorpage

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "errorpage", data)


def set_errorpage(uuid, data):
    """
    Set/update errorpage entry in nginx/settings.

    Wraps: POST /api/nginx/settings/seterrorpage/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "errorpage", uuid, data)


def del_errorpage(uuid):
    """
    Delete errorpage entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delerrorpage/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "errorpage", uuid)


def search_httprewrite(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search httprewrite entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchhttprewrite

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "httprewrite", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_httprewrite(uuid=None):
    """
    Get httprewrite entry in nginx/settings.

    Wraps: GET /api/nginx/settings/gethttprewrite/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "httprewrite", uuid)


def add_httprewrite(data):
    """
    Add httprewrite entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addhttprewrite

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "httprewrite", data)


def set_httprewrite(uuid, data):
    """
    Set/update httprewrite entry in nginx/settings.

    Wraps: POST /api/nginx/settings/sethttprewrite/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "httprewrite", uuid, data)


def del_httprewrite(uuid):
    """
    Delete httprewrite entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delhttprewrite/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "httprewrite", uuid)


def search_httpserver(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search httpserver entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchhttpserver

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "httpserver", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_httpserver(uuid=None):
    """
    Get httpserver entry in nginx/settings.

    Wraps: GET /api/nginx/settings/gethttpserver/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "httpserver", uuid)


def add_httpserver(data):
    """
    Add httpserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addhttpserver

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "httpserver", data)


def set_httpserver(uuid, data):
    """
    Set/update httpserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/sethttpserver/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "httpserver", uuid, data)


def del_httpserver(uuid):
    """
    Delete httpserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delhttpserver/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "httpserver", uuid)


def search_ipacl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ipacl entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchipacl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "ipacl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ipacl(uuid=None):
    """
    Get ipacl entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getipacl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "ipacl", uuid)


def add_ipacl(data):
    """
    Add ipacl entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addipacl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "ipacl", data)


def set_ipacl(uuid, data):
    """
    Set/update ipacl entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setipacl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "ipacl", uuid, data)


def del_ipacl(uuid):
    """
    Delete ipacl entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delipacl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "ipacl", uuid)


def search_limit_request_connection(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search limit_request_connection entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchlimitRequestConnection

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "limit_request_connection", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_limit_request_connection(uuid=None):
    """
    Get limit_request_connection entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getlimitRequestConnection/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "limit_request_connection", uuid)


def add_limit_request_connection(data):
    """
    Add limit_request_connection entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addlimitRequestConnection

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "limit_request_connection", data)


def set_limit_request_connection(uuid, data):
    """
    Set/update limit_request_connection entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setlimitRequestConnection/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "limit_request_connection", uuid, data)


def del_limit_request_connection(uuid):
    """
    Delete limit_request_connection entry in nginx/settings.

    Wraps: POST /api/nginx/settings/dellimitRequestConnection/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "limit_request_connection", uuid)


def search_limit_zone(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search limit_zone entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchlimitZone

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "limit_zone", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_limit_zone(uuid=None):
    """
    Get limit_zone entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getlimitZone/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "limit_zone", uuid)


def add_limit_zone(data):
    """
    Add limit_zone entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addlimitZone

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "limit_zone", data)


def set_limit_zone(uuid, data):
    """
    Set/update limit_zone entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setlimitZone/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "limit_zone", uuid, data)


def del_limit_zone(uuid):
    """
    Delete limit_zone entry in nginx/settings.

    Wraps: POST /api/nginx/settings/dellimitZone/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "limit_zone", uuid)


def search_location(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search location entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchlocation

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "location", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_location(uuid=None):
    """
    Get location entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getlocation/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "location", uuid)


def add_location(data):
    """
    Add location entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addlocation

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "location", data)


def set_location(uuid, data):
    """
    Set/update location entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setlocation/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "location", uuid, data)


def del_location(uuid):
    """
    Delete location entry in nginx/settings.

    Wraps: POST /api/nginx/settings/dellocation/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "location", uuid)


def search_naxsirule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search naxsirule entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchnaxsirule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "naxsirule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_naxsirule(uuid=None):
    """
    Get naxsirule entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getnaxsirule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "naxsirule", uuid)


def add_naxsirule(data):
    """
    Add naxsirule entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addnaxsirule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "naxsirule", data)


def set_naxsirule(uuid, data):
    """
    Set/update naxsirule entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setnaxsirule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "naxsirule", uuid, data)


def del_naxsirule(uuid):
    """
    Delete naxsirule entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delnaxsirule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "naxsirule", uuid)


def search_proxy_cache_valid(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search proxy_cache_valid entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchproxyCacheValid

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "proxy_cache_valid", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_proxy_cache_valid(uuid=None):
    """
    Get proxy_cache_valid entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getproxyCacheValid/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "proxy_cache_valid", uuid)


def add_proxy_cache_valid(data):
    """
    Add proxy_cache_valid entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addproxyCacheValid

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "proxy_cache_valid", data)


def set_proxy_cache_valid(uuid, data):
    """
    Set/update proxy_cache_valid entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setproxyCacheValid/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "proxy_cache_valid", uuid, data)


def del_proxy_cache_valid(uuid):
    """
    Delete proxy_cache_valid entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delproxyCacheValid/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "proxy_cache_valid", uuid)


def search_resolver(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search resolver entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchresolver

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "resolver", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_resolver(uuid=None):
    """
    Get resolver entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getresolver/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "resolver", uuid)


def add_resolver(data):
    """
    Add resolver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addresolver

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "resolver", data)


def set_resolver(uuid, data):
    """
    Set/update resolver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setresolver/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "resolver", uuid, data)


def del_resolver(uuid):
    """
    Delete resolver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delresolver/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "resolver", uuid)


def search_security_header(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search security_header entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchsecurityHeader

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "security_header", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_security_header(uuid=None):
    """
    Get security_header entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getsecurityHeader/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "security_header", uuid)


def add_security_header(data):
    """
    Add security_header entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addsecurityHeader

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "security_header", data)


def set_security_header(uuid, data):
    """
    Set/update security_header entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setsecurityHeader/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "security_header", uuid, data)


def del_security_header(uuid):
    """
    Delete security_header entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delsecurityHeader/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "security_header", uuid)


def search_snifwd(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search snifwd entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchsnifwd

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "snifwd", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_snifwd(uuid=None):
    """
    Get snifwd entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getsnifwd/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "snifwd", uuid)


def add_snifwd(data):
    """
    Add snifwd entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addsnifwd

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "snifwd", data)


def set_snifwd(uuid, data):
    """
    Set/update snifwd entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setsnifwd/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "snifwd", uuid, data)


def del_snifwd(uuid):
    """
    Delete snifwd entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delsnifwd/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "snifwd", uuid)


def search_streamserver(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search streamserver entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchstreamserver

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "streamserver", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_streamserver(uuid=None):
    """
    Get streamserver entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getstreamserver/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "streamserver", uuid)


def add_streamserver(data):
    """
    Add streamserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addstreamserver

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "streamserver", data)


def set_streamserver(uuid, data):
    """
    Set/update streamserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setstreamserver/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "streamserver", uuid, data)


def del_streamserver(uuid):
    """
    Delete streamserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delstreamserver/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "streamserver", uuid)


def search_syslog_target(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search syslog_target entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchsyslogTarget

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "syslog_target", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_syslog_target(uuid=None):
    """
    Get syslog_target entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getsyslogTarget/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "syslog_target", uuid)


def add_syslog_target(data):
    """
    Add syslog_target entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addsyslogTarget

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "syslog_target", data)


def set_syslog_target(uuid, data):
    """
    Set/update syslog_target entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setsyslogTarget/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "syslog_target", uuid, data)


def del_syslog_target(uuid):
    """
    Delete syslog_target entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delsyslogTarget/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "syslog_target", uuid)


def search_tls_fingerprint(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search tls_fingerprint entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchtlsFingerprint

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "tls_fingerprint", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_tls_fingerprint(uuid=None):
    """
    Get tls_fingerprint entry in nginx/settings.

    Wraps: GET /api/nginx/settings/gettlsFingerprint/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "tls_fingerprint", uuid)


def add_tls_fingerprint(data):
    """
    Add tls_fingerprint entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addtlsFingerprint

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "tls_fingerprint", data)


def set_tls_fingerprint(uuid, data):
    """
    Set/update tls_fingerprint entry in nginx/settings.

    Wraps: POST /api/nginx/settings/settlsFingerprint/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "tls_fingerprint", uuid, data)


def del_tls_fingerprint(uuid):
    """
    Delete tls_fingerprint entry in nginx/settings.

    Wraps: POST /api/nginx/settings/deltlsFingerprint/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "tls_fingerprint", uuid)


def search_upstream(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search upstream entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchupstream

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "upstream", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_upstream(uuid=None):
    """
    Get upstream entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getupstream/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "upstream", uuid)


def add_upstream(data):
    """
    Add upstream entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addupstream

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "upstream", data)


def set_upstream(uuid, data):
    """
    Set/update upstream entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setupstream/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "upstream", uuid, data)


def del_upstream(uuid):
    """
    Delete upstream entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delupstream/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "upstream", uuid)


def search_upstreamserver(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search upstreamserver entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchupstreamserver

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "upstreamserver", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_upstreamserver(uuid=None):
    """
    Get upstreamserver entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getupstreamserver/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "upstreamserver", uuid)


def add_upstreamserver(data):
    """
    Add upstreamserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/addupstreamserver

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "upstreamserver", data)


def set_upstreamserver(uuid, data):
    """
    Set/update upstreamserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setupstreamserver/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "upstreamserver", uuid, data)


def del_upstreamserver(uuid):
    """
    Delete upstreamserver entry in nginx/settings.

    Wraps: POST /api/nginx/settings/delupstreamserver/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "upstreamserver", uuid)


def search_userlist(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search userlist entries in nginx/settings.

    Wraps: POST /api/nginx/settings/searchuserlist

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nginx", "settings", "userlist", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_userlist(uuid=None):
    """
    Get userlist entry in nginx/settings.

    Wraps: GET /api/nginx/settings/getuserlist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nginx", "settings", "userlist", uuid)


def add_userlist(data):
    """
    Add userlist entry in nginx/settings.

    Wraps: POST /api/nginx/settings/adduserlist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nginx", "settings", "userlist", data)


def set_userlist(uuid, data):
    """
    Set/update userlist entry in nginx/settings.

    Wraps: POST /api/nginx/settings/setuserlist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nginx", "settings", "userlist", uuid, data)


def del_userlist(uuid):
    """
    Delete userlist entry in nginx/settings.

    Wraps: POST /api/nginx/settings/deluserlist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nginx", "settings", "userlist", uuid)


def settings_downloadrules(data=None, uuid=None):
    """
    Execute downloadrules in nginx/settings.

    Wraps: /api/nginx/settings/downloadrules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "settings", "downloadrules", uuid=uuid, data=data)


def settings_showconfig(data=None, uuid=None):
    """
    Execute showconfig in nginx/settings.

    Wraps: /api/nginx/settings/showconfig

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "settings", "showconfig", uuid=uuid, data=data)


def settings_testconfig(data=None, uuid=None):
    """
    Execute testconfig in nginx/settings.

    Wraps: /api/nginx/settings/testconfig

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("nginx", "settings", "testconfig", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="bans", action="reconfigure", data=None):
    """
    Generic reconfigure for nginx.

    Wraps: POST /api/nginx/{controller}/{action}

    :param controller: Controller name, default bans
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("nginx", controller, action, data)
