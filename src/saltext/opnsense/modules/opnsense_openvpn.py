# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense openvpn wrappers.

Generated from controllers.json for module openvpn.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/openvpn/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_openvpn"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- clientoverwrites controller ---

def search_clientoverwrite(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search clientoverwrite entries in openvpn/clientoverwrites.

    Wraps: POST /api/openvpn/clientoverwrites/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("openvpn", "clientoverwrites", "clientoverwrite", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_clientoverwrite(uuid=None):
    """
    Get clientoverwrite entry in openvpn/clientoverwrites.

    Wraps: GET /api/openvpn/clientoverwrites/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("openvpn", "clientoverwrites", "clientoverwrite", uuid)


def add_clientoverwrite(data):
    """
    Add clientoverwrite entry in openvpn/clientoverwrites.

    Wraps: POST /api/openvpn/clientoverwrites/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("openvpn", "clientoverwrites", "clientoverwrite", data)


def set_clientoverwrite(uuid, data):
    """
    Set/update clientoverwrite entry in openvpn/clientoverwrites.

    Wraps: POST /api/openvpn/clientoverwrites/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("openvpn", "clientoverwrites", "clientoverwrite", uuid, data)


def del_clientoverwrite(uuid):
    """
    Delete clientoverwrite entry in openvpn/clientoverwrites.

    Wraps: POST /api/openvpn/clientoverwrites/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("openvpn", "clientoverwrites", "clientoverwrite", uuid)


def toggle_clientoverwrite(uuid, enabled=None):
    """
    Toggle clientoverwrite entry in openvpn/clientoverwrites.

    Wraps: POST /api/openvpn/clientoverwrites/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("openvpn", "clientoverwrites", "clientoverwrite", uuid, enabled)


# --- export controller ---

def export_accounts(data=None, uuid=None):
    """
    Execute accounts in openvpn/export.

    Wraps: /api/openvpn/export/accounts

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "export", "accounts", uuid=uuid, data=data)


def export_download(data=None, uuid=None):
    """
    Execute download in openvpn/export.

    Wraps: /api/openvpn/export/download

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "export", "download", uuid=uuid, data=data)


def export_providers(data=None, uuid=None):
    """
    Execute providers in openvpn/export.

    Wraps: /api/openvpn/export/providers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "export", "providers", uuid=uuid, data=data)


def export_store_presets(data=None, uuid=None):
    """
    Execute storePresets in openvpn/export.

    Wraps: /api/openvpn/export/storePresets

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "export", "storePresets", uuid=uuid, data=data)


def export_templates(data=None, uuid=None):
    """
    Execute templates in openvpn/export.

    Wraps: /api/openvpn/export/templates

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "export", "templates", uuid=uuid, data=data)


def export_validate_presets(data=None, uuid=None):
    """
    Execute validatePresets in openvpn/export.

    Wraps: /api/openvpn/export/validatePresets

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "export", "validatePresets", uuid=uuid, data=data)


# --- instances controller ---

def search_static_key(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search static_key entries in openvpn/instances.

    Wraps: POST /api/openvpn/instances/searchStaticKey

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("openvpn", "instances", "static_key", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_static_key(uuid=None):
    """
    Get static_key entry in openvpn/instances.

    Wraps: GET /api/openvpn/instances/getStaticKey/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("openvpn", "instances", "static_key", uuid)


def add_static_key(data):
    """
    Add static_key entry in openvpn/instances.

    Wraps: POST /api/openvpn/instances/addStaticKey

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("openvpn", "instances", "static_key", data)


def set_static_key(uuid, data):
    """
    Set/update static_key entry in openvpn/instances.

    Wraps: POST /api/openvpn/instances/setStaticKey/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("openvpn", "instances", "static_key", uuid, data)


def del_static_key(uuid):
    """
    Delete static_key entry in openvpn/instances.

    Wraps: POST /api/openvpn/instances/delStaticKey/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("openvpn", "instances", "static_key", uuid)


def toggle_static_key(uuid, enabled=None):
    """
    Toggle static_key entry in openvpn/instances.

    Wraps: POST /api/openvpn/instances/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("openvpn", "instances", "static_key", uuid, enabled)


def instances_gen_key(data=None, uuid=None):
    """
    Execute genKey in openvpn/instances.

    Wraps: /api/openvpn/instances/genKey

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "instances", "genKey", uuid=uuid, data=data)


# --- service controller ---

def search_routes(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search routes entries in openvpn/service.

    Wraps: POST /api/openvpn/service/searchRoutes

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("openvpn", "service", "routes", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_sessions(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search sessions entries in openvpn/service.

    Wraps: POST /api/openvpn/service/searchSessions

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("openvpn", "service", "sessions", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def service_kill_session(data=None, uuid=None):
    """
    Execute killSession in openvpn/service.

    Wraps: /api/openvpn/service/killSession

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "service", "killSession", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in openvpn/service.

    Wraps: POST /api/openvpn/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("openvpn", "service", action, data)


def service_restart_service(data=None, uuid=None):
    """
    Execute restartService in openvpn/service.

    Wraps: /api/openvpn/service/restartService

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "service", "restartService", uuid=uuid, data=data)


def service_start_service(data=None, uuid=None):
    """
    Execute startService in openvpn/service.

    Wraps: /api/openvpn/service/startService

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "service", "startService", uuid=uuid, data=data)


def service_stop_service(data=None, uuid=None):
    """
    Execute stopService in openvpn/service.

    Wraps: /api/openvpn/service/stopService

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("openvpn", "service", "stopService", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for openvpn.

    Wraps: POST /api/openvpn/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("openvpn", controller, action, data)
