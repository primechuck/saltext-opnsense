# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense syslog wrappers.

Generated from controllers.json for module syslog.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/syslog/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_syslog"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reset(data=None, uuid=None):
    """
    Execute reset in syslog/service.

    Wraps: /api/syslog/service/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("syslog", "service", "reset", uuid=uuid, data=data)


def service_stats(data=None, uuid=None):
    """
    Execute stats in syslog/service.

    Wraps: /api/syslog/service/stats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("syslog", "service", "stats", uuid=uuid, data=data)


# --- settings controller ---

def get_destination(uuid=None):
    """
    Get destination entry in syslog/settings.

    Wraps: GET /api/syslog/settings/getDestination/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("syslog", "settings", "destination", uuid)


def add_destination(data):
    """
    Add destination entry in syslog/settings.

    Wraps: POST /api/syslog/settings/addDestination

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("syslog", "settings", "destination", data)


def set_destination(uuid, data):
    """
    Set/update destination entry in syslog/settings.

    Wraps: POST /api/syslog/settings/setDestination/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("syslog", "settings", "destination", uuid, data)


def del_destination(uuid):
    """
    Delete destination entry in syslog/settings.

    Wraps: POST /api/syslog/settings/delDestination/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("syslog", "settings", "destination", uuid)


def toggle_destination(uuid, enabled=None):
    """
    Toggle destination entry in syslog/settings.

    Wraps: POST /api/syslog/settings/toggleDestination/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("syslog", "settings", "destination", uuid, enabled)


def search_destinations(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search destinations entries in syslog/settings.

    Wraps: POST /api/syslog/settings/searchDestinations

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("syslog", "settings", "destinations", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for syslog.

    Wraps: POST /api/syslog/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("syslog", controller, action, data)
