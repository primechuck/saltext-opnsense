# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense relayd wrappers.

Generated from controllers.json for module relayd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/relayd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_relayd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_configtest(data=None, uuid=None):
    """
    Execute configtest in relayd/service.

    Wraps: /api/relayd/service/configtest

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("relayd", "service", "configtest", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in relayd/service.

    Wraps: POST /api/relayd/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("relayd", "service", action, data)


# --- settings controller ---

def search_setting(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search setting entries in relayd/settings.

    Wraps: POST /api/relayd/settings/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("relayd", "settings", "setting", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_setting(uuid=None):
    """
    Get setting entry in relayd/settings.

    Wraps: GET /api/relayd/settings/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("relayd", "settings", "setting", uuid)


def set_setting(uuid, data):
    """
    Set/update setting entry in relayd/settings.

    Wraps: POST /api/relayd/settings/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("relayd", "settings", "setting", uuid, data)


def del_setting(uuid):
    """
    Delete setting entry in relayd/settings.

    Wraps: POST /api/relayd/settings/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("relayd", "settings", "setting", uuid)


def toggle_setting(uuid, enabled=None):
    """
    Toggle setting entry in relayd/settings.

    Wraps: POST /api/relayd/settings/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("relayd", "settings", "setting", uuid, enabled)


def settings_dirty(data=None, uuid=None):
    """
    Execute dirty in relayd/settings.

    Wraps: /api/relayd/settings/dirty

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("relayd", "settings", "dirty", uuid=uuid, data=data)


# --- status controller ---

def status_sum(data=None, uuid=None):
    """
    Execute sum in relayd/status.

    Wraps: /api/relayd/status/sum

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("relayd", "status", "sum", uuid=uuid, data=data)


def status_toggle(data=None, uuid=None):
    """
    Execute toggle in relayd/status.

    Wraps: /api/relayd/status/toggle

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("relayd", "status", "toggle", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for relayd.

    Wraps: POST /api/relayd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("relayd", controller, action, data)
