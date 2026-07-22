# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense zabbixagent wrappers.

Generated from controllers.json for module zabbixagent.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/zabbixagent/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_zabbixagent"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- settings controller ---

def get_alias(uuid=None):
    """
    Get alias entry in zabbixagent/settings.

    Wraps: GET /api/zabbixagent/settings/getAlias/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("zabbixagent", "settings", "alias", uuid)


def add_alias(data):
    """
    Add alias entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/addAlias

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("zabbixagent", "settings", "alias", data)


def set_alias(uuid, data):
    """
    Set/update alias entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/setAlias/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("zabbixagent", "settings", "alias", uuid, data)


def del_alias(uuid):
    """
    Delete alias entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/delAlias/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("zabbixagent", "settings", "alias", uuid)


def toggle_alias(uuid, enabled=None):
    """
    Toggle alias entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/toggleAlias/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("zabbixagent", "settings", "alias", uuid, enabled)


def search_aliases(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search aliases entries in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/searchAliases

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("zabbixagent", "settings", "aliases", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_userparameter(uuid=None):
    """
    Get userparameter entry in zabbixagent/settings.

    Wraps: GET /api/zabbixagent/settings/getUserparameter/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("zabbixagent", "settings", "userparameter", uuid)


def add_userparameter(data):
    """
    Add userparameter entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/addUserparameter

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("zabbixagent", "settings", "userparameter", data)


def set_userparameter(uuid, data):
    """
    Set/update userparameter entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/setUserparameter/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("zabbixagent", "settings", "userparameter", uuid, data)


def del_userparameter(uuid):
    """
    Delete userparameter entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/delUserparameter/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("zabbixagent", "settings", "userparameter", uuid)


def toggle_userparameter(uuid, enabled=None):
    """
    Toggle userparameter entry in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/toggleUserparameter/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("zabbixagent", "settings", "userparameter", uuid, enabled)


def search_userparameters(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search userparameters entries in zabbixagent/settings.

    Wraps: POST /api/zabbixagent/settings/searchUserparameters

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("zabbixagent", "settings", "userparameters", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)



# Generic module-level helpers

def reconfigure(controller="settings", action="reconfigure", data=None):
    """
    Generic reconfigure for zabbixagent.

    Wraps: POST /api/zabbixagent/{controller}/{action}

    :param controller: Controller name, default settings
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("zabbixagent", controller, action, data)
