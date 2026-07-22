# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense trafficshaper wrappers.

Generated from controllers.json for module trafficshaper.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/trafficshaper/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_trafficshaper"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_flushreload(data=None, uuid=None):
    """
    Execute flushreload in trafficshaper/service.

    Wraps: /api/trafficshaper/service/flushreload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trafficshaper", "service", "flushreload", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in trafficshaper/service.

    Wraps: POST /api/trafficshaper/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("trafficshaper", "service", action, data)


def service_statistics(data=None, uuid=None):
    """
    Execute statistics in trafficshaper/service.

    Wraps: /api/trafficshaper/service/statistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trafficshaper", "service", "statistics", uuid=uuid, data=data)


# --- settings controller ---

def get_pipe(uuid=None):
    """
    Get pipe entry in trafficshaper/settings.

    Wraps: GET /api/trafficshaper/settings/getPipe/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("trafficshaper", "settings", "pipe", uuid)


def add_pipe(data):
    """
    Add pipe entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/addPipe

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("trafficshaper", "settings", "pipe", data)


def set_pipe(uuid, data):
    """
    Set/update pipe entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/setPipe/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("trafficshaper", "settings", "pipe", uuid, data)


def del_pipe(uuid):
    """
    Delete pipe entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/delPipe/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("trafficshaper", "settings", "pipe", uuid)


def toggle_pipe(uuid, enabled=None):
    """
    Toggle pipe entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/togglePipe/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("trafficshaper", "settings", "pipe", uuid, enabled)


def search_pipes(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search pipes entries in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/searchPipes

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("trafficshaper", "settings", "pipes", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_queue(uuid=None):
    """
    Get queue entry in trafficshaper/settings.

    Wraps: GET /api/trafficshaper/settings/getQueue/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("trafficshaper", "settings", "queue", uuid)


def add_queue(data):
    """
    Add queue entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/addQueue

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("trafficshaper", "settings", "queue", data)


def set_queue(uuid, data):
    """
    Set/update queue entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/setQueue/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("trafficshaper", "settings", "queue", uuid, data)


def del_queue(uuid):
    """
    Delete queue entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/delQueue/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("trafficshaper", "settings", "queue", uuid)


def toggle_queue(uuid, enabled=None):
    """
    Toggle queue entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/toggleQueue/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("trafficshaper", "settings", "queue", uuid, enabled)


def search_queues(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search queues entries in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/searchQueues

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("trafficshaper", "settings", "queues", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_rule(uuid=None):
    """
    Get rule entry in trafficshaper/settings.

    Wraps: GET /api/trafficshaper/settings/getRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("trafficshaper", "settings", "rule", uuid)


def add_rule(data):
    """
    Add rule entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/addRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("trafficshaper", "settings", "rule", data)


def set_rule(uuid, data):
    """
    Set/update rule entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("trafficshaper", "settings", "rule", uuid, data)


def del_rule(uuid):
    """
    Delete rule entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/delRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("trafficshaper", "settings", "rule", uuid)


def toggle_rule(uuid, enabled=None):
    """
    Toggle rule entry in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("trafficshaper", "settings", "rule", uuid, enabled)


def search_rules(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search rules entries in trafficshaper/settings.

    Wraps: POST /api/trafficshaper/settings/searchRules

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("trafficshaper", "settings", "rules", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def settings_download_pipes(data=None, uuid=None):
    """
    Execute downloadPipes in trafficshaper/settings.

    Wraps: /api/trafficshaper/settings/downloadPipes

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trafficshaper", "settings", "downloadPipes", uuid=uuid, data=data)


def settings_download_queues(data=None, uuid=None):
    """
    Execute downloadQueues in trafficshaper/settings.

    Wraps: /api/trafficshaper/settings/downloadQueues

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trafficshaper", "settings", "downloadQueues", uuid=uuid, data=data)


def settings_upload_pipes(data=None, uuid=None):
    """
    Execute uploadPipes in trafficshaper/settings.

    Wraps: /api/trafficshaper/settings/uploadPipes

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trafficshaper", "settings", "uploadPipes", uuid=uuid, data=data)


def settings_upload_queues(data=None, uuid=None):
    """
    Execute uploadQueues in trafficshaper/settings.

    Wraps: /api/trafficshaper/settings/uploadQueues

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trafficshaper", "settings", "uploadQueues", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for trafficshaper.

    Wraps: POST /api/trafficshaper/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("trafficshaper", controller, action, data)
