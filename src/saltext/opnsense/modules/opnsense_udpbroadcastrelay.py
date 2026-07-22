# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense udpbroadcastrelay wrappers.

Generated from controllers.json for module udpbroadcastrelay.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/udpbroadcastrelay/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_udpbroadcastrelay"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_config(data=None, uuid=None):
    """
    Execute config in udpbroadcastrelay/service.

    Wraps: /api/udpbroadcastrelay/service/config

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("udpbroadcastrelay", "service", "config", uuid=uuid, data=data)


def service_reload(data=None, uuid=None):
    """
    Execute reload in udpbroadcastrelay/service.

    Wraps: /api/udpbroadcastrelay/service/reload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("udpbroadcastrelay", "service", "reload", uuid=uuid, data=data)


def service_restart(data=None):
    """
    Execute restart in udpbroadcastrelay/service.

    Wraps: POST /api/udpbroadcastrelay/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("udpbroadcastrelay", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in udpbroadcastrelay/service.

    Wraps: POST /api/udpbroadcastrelay/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("udpbroadcastrelay", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in udpbroadcastrelay/service.

    Wraps: POST /api/udpbroadcastrelay/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("udpbroadcastrelay", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in udpbroadcastrelay/service.

    Wraps: POST /api/udpbroadcastrelay/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("udpbroadcastrelay", "service", "stop", data=data, method="POST")


# --- settings controller ---

def search_relay(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search relay entries in udpbroadcastrelay/settings.

    Wraps: POST /api/udpbroadcastrelay/settings/searchRelay

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("udpbroadcastrelay", "settings", "relay", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_relay(uuid=None):
    """
    Get relay entry in udpbroadcastrelay/settings.

    Wraps: GET /api/udpbroadcastrelay/settings/getRelay/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("udpbroadcastrelay", "settings", "relay", uuid)


def add_relay(data):
    """
    Add relay entry in udpbroadcastrelay/settings.

    Wraps: POST /api/udpbroadcastrelay/settings/addRelay

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("udpbroadcastrelay", "settings", "relay", data)


def set_relay(uuid, data):
    """
    Set/update relay entry in udpbroadcastrelay/settings.

    Wraps: POST /api/udpbroadcastrelay/settings/setRelay/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("udpbroadcastrelay", "settings", "relay", uuid, data)


def del_relay(uuid):
    """
    Delete relay entry in udpbroadcastrelay/settings.

    Wraps: POST /api/udpbroadcastrelay/settings/delRelay/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("udpbroadcastrelay", "settings", "relay", uuid)


def toggle_relay(uuid, enabled=None):
    """
    Toggle relay entry in udpbroadcastrelay/settings.

    Wraps: POST /api/udpbroadcastrelay/settings/toggleRelay/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("udpbroadcastrelay", "settings", "relay", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for udpbroadcastrelay.

    Wraps: POST /api/udpbroadcastrelay/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("udpbroadcastrelay", controller, action, data)
