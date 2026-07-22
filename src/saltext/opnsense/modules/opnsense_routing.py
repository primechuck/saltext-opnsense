# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense routing wrappers.

Generated from controllers.json for module routing.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/routing/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_routing"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- groupsettings controller ---

def search_groupsetting(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search groupsetting entries in routing/groupsettings.

    Wraps: POST /api/routing/groupsettings/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("routing", "groupsettings", "groupsetting", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_groupsetting(uuid=None):
    """
    Get groupsetting entry in routing/groupsettings.

    Wraps: GET /api/routing/groupsettings/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("routing", "groupsettings", "groupsetting", uuid)


def add_groupsetting(data):
    """
    Add groupsetting entry in routing/groupsettings.

    Wraps: POST /api/routing/groupsettings/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("routing", "groupsettings", "groupsetting", data)


def set_groupsetting(uuid, data):
    """
    Set/update groupsetting entry in routing/groupsettings.

    Wraps: POST /api/routing/groupsettings/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("routing", "groupsettings", "groupsetting", uuid, data)


def del_groupsetting(uuid):
    """
    Delete groupsetting entry in routing/groupsettings.

    Wraps: POST /api/routing/groupsettings/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("routing", "groupsettings", "groupsetting", uuid)


def groupsettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in routing/groupsettings.

    Wraps: POST /api/routing/groupsettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("routing", "groupsettings", action, data)


# --- settings controller ---

def search_gateway(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search gateway entries in routing/settings.

    Wraps: POST /api/routing/settings/searchGateway

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("routing", "settings", "gateway", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_gateway(uuid=None):
    """
    Get gateway entry in routing/settings.

    Wraps: GET /api/routing/settings/getGateway/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("routing", "settings", "gateway", uuid)


def add_gateway(data):
    """
    Add gateway entry in routing/settings.

    Wraps: POST /api/routing/settings/addGateway

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("routing", "settings", "gateway", data)


def set_gateway(uuid, data):
    """
    Set/update gateway entry in routing/settings.

    Wraps: POST /api/routing/settings/setGateway/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("routing", "settings", "gateway", uuid, data)


def del_gateway(uuid):
    """
    Delete gateway entry in routing/settings.

    Wraps: POST /api/routing/settings/delGateway/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("routing", "settings", "gateway", uuid)


def toggle_gateway(uuid, enabled=None):
    """
    Toggle gateway entry in routing/settings.

    Wraps: POST /api/routing/settings/toggleGateway/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("routing", "settings", "gateway", uuid, enabled)


def settings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in routing/settings.

    Wraps: POST /api/routing/settings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("routing", "settings", action, data)



# Generic module-level helpers

def reconfigure(controller="groupsettings", action="reconfigure", data=None):
    """
    Generic reconfigure for routing.

    Wraps: POST /api/routing/{controller}/{action}

    :param controller: Controller name, default groupsettings
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("routing", controller, action, data)
