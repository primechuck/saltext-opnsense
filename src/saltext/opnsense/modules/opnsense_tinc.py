# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense tinc wrappers.

Generated from controllers.json for module tinc.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/tinc/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_tinc"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in tinc/service.

    Wraps: POST /api/tinc/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("tinc", "service", action, data)


def service_restart(data=None):
    """
    Execute restart in tinc/service.

    Wraps: POST /api/tinc/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tinc", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in tinc/service.

    Wraps: POST /api/tinc/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tinc", "service", "start", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in tinc/service.

    Wraps: POST /api/tinc/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tinc", "service", "stop", data=data, method="POST")


# --- settings controller ---

def search_host(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search host entries in tinc/settings.

    Wraps: POST /api/tinc/settings/searchHost

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tinc", "settings", "host", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_host(uuid=None):
    """
    Get host entry in tinc/settings.

    Wraps: GET /api/tinc/settings/getHost/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tinc", "settings", "host", uuid)


def set_host(uuid, data):
    """
    Set/update host entry in tinc/settings.

    Wraps: POST /api/tinc/settings/setHost/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tinc", "settings", "host", uuid, data)


def del_host(uuid):
    """
    Delete host entry in tinc/settings.

    Wraps: POST /api/tinc/settings/delHost/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tinc", "settings", "host", uuid)


def toggle_host(uuid, enabled=None):
    """
    Toggle host entry in tinc/settings.

    Wraps: POST /api/tinc/settings/toggleHost/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tinc", "settings", "host", uuid, enabled)


def search_network(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search network entries in tinc/settings.

    Wraps: POST /api/tinc/settings/searchNetwork

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tinc", "settings", "network", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_network(uuid=None):
    """
    Get network entry in tinc/settings.

    Wraps: GET /api/tinc/settings/getNetwork/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tinc", "settings", "network", uuid)


def set_network(uuid, data):
    """
    Set/update network entry in tinc/settings.

    Wraps: POST /api/tinc/settings/setNetwork/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tinc", "settings", "network", uuid, data)


def del_network(uuid):
    """
    Delete network entry in tinc/settings.

    Wraps: POST /api/tinc/settings/delNetwork/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tinc", "settings", "network", uuid)


def toggle_network(uuid, enabled=None):
    """
    Toggle network entry in tinc/settings.

    Wraps: POST /api/tinc/settings/toggleNetwork/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tinc", "settings", "network", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for tinc.

    Wraps: POST /api/tinc/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("tinc", controller, action, data)
