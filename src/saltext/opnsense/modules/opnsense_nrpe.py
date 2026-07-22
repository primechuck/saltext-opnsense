# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense nrpe wrappers.

Generated from controllers.json for module nrpe.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/nrpe/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_nrpe"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- command controller ---

def search_command(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search command entries in nrpe/command.

    Wraps: POST /api/nrpe/command/searchCommand

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("nrpe", "command", "command", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_command(uuid=None):
    """
    Get command entry in nrpe/command.

    Wraps: GET /api/nrpe/command/getCommand/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("nrpe", "command", "command", uuid)


def add_command(data):
    """
    Add command entry in nrpe/command.

    Wraps: POST /api/nrpe/command/addCommand

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("nrpe", "command", "command", data)


def set_command(uuid, data):
    """
    Set/update command entry in nrpe/command.

    Wraps: POST /api/nrpe/command/setCommand/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("nrpe", "command", "command", uuid, data)


def del_command(uuid):
    """
    Delete command entry in nrpe/command.

    Wraps: POST /api/nrpe/command/delCommand/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("nrpe", "command", "command", uuid)


def toggle_command(uuid, enabled=None):
    """
    Toggle command entry in nrpe/command.

    Wraps: POST /api/nrpe/command/toggleCommand/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("nrpe", "command", "command", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="command", action="reconfigure", data=None):
    """
    Generic reconfigure for nrpe.

    Wraps: POST /api/nrpe/{controller}/{action}

    :param controller: Controller name, default command
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("nrpe", controller, action, data)
