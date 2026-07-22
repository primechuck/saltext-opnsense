# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ftpproxy wrappers.

Generated from controllers.json for module ftpproxy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/ftpproxy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ftpproxy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_config(data=None, uuid=None):
    """
    Execute config in ftpproxy/service.

    Wraps: /api/ftpproxy/service/config

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ftpproxy", "service", "config", uuid=uuid, data=data)


def service_reload(data=None, uuid=None):
    """
    Execute reload in ftpproxy/service.

    Wraps: /api/ftpproxy/service/reload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ftpproxy", "service", "reload", uuid=uuid, data=data)


def service_restart(data=None):
    """
    Execute restart in ftpproxy/service.

    Wraps: POST /api/ftpproxy/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("ftpproxy", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in ftpproxy/service.

    Wraps: POST /api/ftpproxy/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("ftpproxy", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in ftpproxy/service.

    Wraps: POST /api/ftpproxy/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("ftpproxy", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in ftpproxy/service.

    Wraps: POST /api/ftpproxy/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("ftpproxy", "service", "stop", data=data, method="POST")


# --- settings controller ---

def search_proxy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search proxy entries in ftpproxy/settings.

    Wraps: POST /api/ftpproxy/settings/searchProxy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ftpproxy", "settings", "proxy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_proxy(uuid=None):
    """
    Get proxy entry in ftpproxy/settings.

    Wraps: GET /api/ftpproxy/settings/getProxy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ftpproxy", "settings", "proxy", uuid)


def add_proxy(data):
    """
    Add proxy entry in ftpproxy/settings.

    Wraps: POST /api/ftpproxy/settings/addProxy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ftpproxy", "settings", "proxy", data)


def set_proxy(uuid, data):
    """
    Set/update proxy entry in ftpproxy/settings.

    Wraps: POST /api/ftpproxy/settings/setProxy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ftpproxy", "settings", "proxy", uuid, data)


def del_proxy(uuid):
    """
    Delete proxy entry in ftpproxy/settings.

    Wraps: POST /api/ftpproxy/settings/delProxy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ftpproxy", "settings", "proxy", uuid)


def toggle_proxy(uuid, enabled=None):
    """
    Toggle proxy entry in ftpproxy/settings.

    Wraps: POST /api/ftpproxy/settings/toggleProxy/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ftpproxy", "settings", "proxy", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for ftpproxy.

    Wraps: POST /api/ftpproxy/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ftpproxy", controller, action, data)
