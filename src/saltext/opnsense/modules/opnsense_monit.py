# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense monit wrappers.

Generated from controllers.json for module monit.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/monit/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_monit"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_check(data=None, uuid=None):
    """
    Execute check in monit/service.

    Wraps: /api/monit/service/check

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("monit", "service", "check", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in monit/service.

    Wraps: POST /api/monit/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("monit", "service", action, data)


# --- settings controller ---

def search_alert(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search alert entries in monit/settings.

    Wraps: POST /api/monit/settings/searchAlert

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("monit", "settings", "alert", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_alert(uuid=None):
    """
    Get alert entry in monit/settings.

    Wraps: GET /api/monit/settings/getAlert/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("monit", "settings", "alert", uuid)


def add_alert(data):
    """
    Add alert entry in monit/settings.

    Wraps: POST /api/monit/settings/addAlert

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("monit", "settings", "alert", data)


def set_alert(uuid, data):
    """
    Set/update alert entry in monit/settings.

    Wraps: POST /api/monit/settings/setAlert/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("monit", "settings", "alert", uuid, data)


def del_alert(uuid):
    """
    Delete alert entry in monit/settings.

    Wraps: POST /api/monit/settings/delAlert/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("monit", "settings", "alert", uuid)


def toggle_alert(uuid, enabled=None):
    """
    Toggle alert entry in monit/settings.

    Wraps: POST /api/monit/settings/toggleAlert/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("monit", "settings", "alert", uuid, enabled)


def search_service(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search service entries in monit/settings.

    Wraps: POST /api/monit/settings/searchService

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("monit", "settings", "service", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_service(uuid=None):
    """
    Get service entry in monit/settings.

    Wraps: GET /api/monit/settings/getService/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("monit", "settings", "service", uuid)


def add_service(data):
    """
    Add service entry in monit/settings.

    Wraps: POST /api/monit/settings/addService

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("monit", "settings", "service", data)


def set_service(uuid, data):
    """
    Set/update service entry in monit/settings.

    Wraps: POST /api/monit/settings/setService/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("monit", "settings", "service", uuid, data)


def del_service(uuid):
    """
    Delete service entry in monit/settings.

    Wraps: POST /api/monit/settings/delService/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("monit", "settings", "service", uuid)


def toggle_service(uuid, enabled=None):
    """
    Toggle service entry in monit/settings.

    Wraps: POST /api/monit/settings/toggleService/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("monit", "settings", "service", uuid, enabled)


def search_test(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search test entries in monit/settings.

    Wraps: POST /api/monit/settings/searchTest

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("monit", "settings", "test", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_test(uuid=None):
    """
    Get test entry in monit/settings.

    Wraps: GET /api/monit/settings/getTest/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("monit", "settings", "test", uuid)


def add_test(data):
    """
    Add test entry in monit/settings.

    Wraps: POST /api/monit/settings/addTest

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("monit", "settings", "test", data)


def set_test(uuid, data):
    """
    Set/update test entry in monit/settings.

    Wraps: POST /api/monit/settings/setTest/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("monit", "settings", "test", uuid, data)


def del_test(uuid):
    """
    Delete test entry in monit/settings.

    Wraps: POST /api/monit/settings/delTest/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("monit", "settings", "test", uuid)


def settings_get_general(data=None, uuid=None):
    """
    Execute getGeneral in monit/settings.

    Wraps: /api/monit/settings/getGeneral

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("monit", "settings", "getGeneral", uuid=uuid, data=data)


# --- status controller ---

def get_status():
    """
    Get status singleton config in monit/status.

    Wraps: GET /api/monit/status/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("monit", "status")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for monit.

    Wraps: POST /api/monit/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("monit", controller, action, data)
