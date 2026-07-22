# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense telegraf wrappers.

Generated from controllers.json for module telegraf.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/telegraf/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_telegraf"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- general controller ---

def get_general():
    """
    Get general singleton config in telegraf/general.

    Wraps: GET /api/telegraf/general/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("telegraf", "general")


def set_general(data):
    """
    Set general singleton config in telegraf/general.

    Wraps: POST /api/telegraf/general/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("telegraf", "general", "set", data=data, method="POST")


# --- input controller ---

def get_input():
    """
    Get input singleton config in telegraf/input.

    Wraps: GET /api/telegraf/input/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("telegraf", "input")


def set_input(data):
    """
    Set input singleton config in telegraf/input.

    Wraps: POST /api/telegraf/input/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("telegraf", "input", "set", data=data, method="POST")


# --- key controller ---

def search_key(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search key entries in telegraf/key.

    Wraps: POST /api/telegraf/key/searchKey

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("telegraf", "key", "key", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_key(uuid=None):
    """
    Get key entry in telegraf/key.

    Wraps: GET /api/telegraf/key/getKey/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("telegraf", "key", "key", uuid)


def add_key(data):
    """
    Add key entry in telegraf/key.

    Wraps: POST /api/telegraf/key/addKey

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("telegraf", "key", "key", data)


def set_key(uuid, data):
    """
    Set/update key entry in telegraf/key.

    Wraps: POST /api/telegraf/key/setKey/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("telegraf", "key", "key", uuid, data)


def del_key(uuid):
    """
    Delete key entry in telegraf/key.

    Wraps: POST /api/telegraf/key/delKey/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("telegraf", "key", "key", uuid)


def toggle_key(uuid, enabled=None):
    """
    Toggle key entry in telegraf/key.

    Wraps: POST /api/telegraf/key/toggleKey/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("telegraf", "key", "key", uuid, enabled)


# --- output controller ---

def get_output():
    """
    Get output singleton config in telegraf/output.

    Wraps: GET /api/telegraf/output/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("telegraf", "output")


def set_output(data):
    """
    Set output singleton config in telegraf/output.

    Wraps: POST /api/telegraf/output/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("telegraf", "output", "set", data=data, method="POST")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in telegraf/service.

    Wraps: POST /api/telegraf/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("telegraf", "service", action, data)


def service_restart(data=None):
    """
    Execute restart in telegraf/service.

    Wraps: POST /api/telegraf/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("telegraf", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in telegraf/service.

    Wraps: POST /api/telegraf/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("telegraf", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in telegraf/service.

    Wraps: POST /api/telegraf/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("telegraf", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in telegraf/service.

    Wraps: POST /api/telegraf/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("telegraf", "service", "stop", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for telegraf.

    Wraps: POST /api/telegraf/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("telegraf", controller, action, data)
