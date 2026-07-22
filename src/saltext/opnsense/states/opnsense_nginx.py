# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense nginx state wrappers.

Generated from controllers.json for module nginx.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_nginx"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- bans controller ---

def ban_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure ban bans present in nginx.

    Wraps opnsense.item_present for /api/nginx/bans/searchban

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "bans", "ban", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ban_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure ban bans absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/bans/searchban

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "bans", "ban", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def cache_path_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure cache_path settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchcachePath

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "cache_path", data, match=match, reconfigure=reconfigure, search_field=search_field)


def cache_path_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure cache_path settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchcachePath

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "cache_path", match=match, reconfigure=reconfigure, search_field=search_field)


def credential_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure credential settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchcredential

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "credential", data, match=match, reconfigure=reconfigure, search_field=search_field)


def credential_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure credential settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchcredential

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "credential", match=match, reconfigure=reconfigure, search_field=search_field)


def custompolicy_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure custompolicy settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchcustompolicy

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "custompolicy", data, match=match, reconfigure=reconfigure, search_field=search_field)


def custompolicy_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure custompolicy settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchcustompolicy

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "custompolicy", match=match, reconfigure=reconfigure, search_field=search_field)


def errorpage_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure errorpage settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searcherrorpage

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "errorpage", data, match=match, reconfigure=reconfigure, search_field=search_field)


def errorpage_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure errorpage settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searcherrorpage

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "errorpage", match=match, reconfigure=reconfigure, search_field=search_field)


def httprewrite_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure httprewrite settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchhttprewrite

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "httprewrite", data, match=match, reconfigure=reconfigure, search_field=search_field)


def httprewrite_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure httprewrite settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchhttprewrite

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "httprewrite", match=match, reconfigure=reconfigure, search_field=search_field)


def httpserver_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure httpserver settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchhttpserver

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "httpserver", data, match=match, reconfigure=reconfigure, search_field=search_field)


def httpserver_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure httpserver settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchhttpserver

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "httpserver", match=match, reconfigure=reconfigure, search_field=search_field)


def ipacl_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure ipacl settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchipacl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "ipacl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ipacl_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure ipacl settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchipacl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "ipacl", match=match, reconfigure=reconfigure, search_field=search_field)


def limit_request_connection_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure limit_request_connection settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchlimitRequestConnection

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "limit_request_connection", data, match=match, reconfigure=reconfigure, search_field=search_field)


def limit_request_connection_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure limit_request_connection settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchlimitRequestConnection

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "limit_request_connection", match=match, reconfigure=reconfigure, search_field=search_field)


def limit_zone_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure limit_zone settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchlimitZone

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "limit_zone", data, match=match, reconfigure=reconfigure, search_field=search_field)


def limit_zone_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure limit_zone settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchlimitZone

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "limit_zone", match=match, reconfigure=reconfigure, search_field=search_field)


def location_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure location settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchlocation

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "location", data, match=match, reconfigure=reconfigure, search_field=search_field)


def location_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure location settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchlocation

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "location", match=match, reconfigure=reconfigure, search_field=search_field)


def naxsirule_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure naxsirule settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchnaxsirule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "naxsirule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def naxsirule_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure naxsirule settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchnaxsirule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "naxsirule", match=match, reconfigure=reconfigure, search_field=search_field)


def proxy_cache_valid_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure proxy_cache_valid settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchproxyCacheValid

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "proxy_cache_valid", data, match=match, reconfigure=reconfigure, search_field=search_field)


def proxy_cache_valid_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure proxy_cache_valid settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchproxyCacheValid

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "proxy_cache_valid", match=match, reconfigure=reconfigure, search_field=search_field)


def resolver_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure resolver settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchresolver

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "resolver", data, match=match, reconfigure=reconfigure, search_field=search_field)


def resolver_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure resolver settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchresolver

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "resolver", match=match, reconfigure=reconfigure, search_field=search_field)


def security_header_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure security_header settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchsecurityHeader

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "security_header", data, match=match, reconfigure=reconfigure, search_field=search_field)


def security_header_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure security_header settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchsecurityHeader

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "security_header", match=match, reconfigure=reconfigure, search_field=search_field)


def snifwd_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure snifwd settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchsnifwd

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "snifwd", data, match=match, reconfigure=reconfigure, search_field=search_field)


def snifwd_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure snifwd settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchsnifwd

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "snifwd", match=match, reconfigure=reconfigure, search_field=search_field)


def streamserver_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure streamserver settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchstreamserver

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "streamserver", data, match=match, reconfigure=reconfigure, search_field=search_field)


def streamserver_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure streamserver settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchstreamserver

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "streamserver", match=match, reconfigure=reconfigure, search_field=search_field)


def syslog_target_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure syslog_target settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchsyslogTarget

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "syslog_target", data, match=match, reconfigure=reconfigure, search_field=search_field)


def syslog_target_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure syslog_target settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchsyslogTarget

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "syslog_target", match=match, reconfigure=reconfigure, search_field=search_field)


def tls_fingerprint_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure tls_fingerprint settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchtlsFingerprint

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "tls_fingerprint", data, match=match, reconfigure=reconfigure, search_field=search_field)


def tls_fingerprint_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure tls_fingerprint settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchtlsFingerprint

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "tls_fingerprint", match=match, reconfigure=reconfigure, search_field=search_field)


def upstream_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure upstream settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchupstream

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "upstream", data, match=match, reconfigure=reconfigure, search_field=search_field)


def upstream_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure upstream settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchupstream

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "upstream", match=match, reconfigure=reconfigure, search_field=search_field)


def upstreamserver_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure upstreamserver settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchupstreamserver

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "upstreamserver", data, match=match, reconfigure=reconfigure, search_field=search_field)


def upstreamserver_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure upstreamserver settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchupstreamserver

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "upstreamserver", match=match, reconfigure=reconfigure, search_field=search_field)


def userlist_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure userlist settings present in nginx.

    Wraps opnsense.item_present for /api/nginx/settings/searchuserlist

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "nginx", "settings", "userlist", data, match=match, reconfigure=reconfigure, search_field=search_field)


def userlist_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure userlist settings absent in nginx.

    Wraps opnsense.item_absent for /api/nginx/settings/searchuserlist

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "nginx", "settings", "userlist", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="bans", action="reconfigure"):
    """
    Trigger reconfigure for nginx.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("nginx", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured nginx/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"nginx/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
