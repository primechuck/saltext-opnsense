# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense cron wrappers.

Generated from controllers.json for module cron.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/cron/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_cron"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in cron/service.

    Wraps: POST /api/cron/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("cron", "service", action, data)


# --- settings controller ---

def get_job(uuid=None):
    """
    Get job entry in cron/settings.

    Wraps: GET /api/cron/settings/getJob/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("cron", "settings", "job", uuid)


def add_job(data):
    """
    Add job entry in cron/settings.

    Wraps: POST /api/cron/settings/addJob

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("cron", "settings", "job", data)


def set_job(uuid, data):
    """
    Set/update job entry in cron/settings.

    Wraps: POST /api/cron/settings/setJob/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("cron", "settings", "job", uuid, data)


def del_job(uuid):
    """
    Delete job entry in cron/settings.

    Wraps: POST /api/cron/settings/delJob/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("cron", "settings", "job", uuid)


def toggle_job(uuid, enabled=None):
    """
    Toggle job entry in cron/settings.

    Wraps: POST /api/cron/settings/toggleJob/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("cron", "settings", "job", uuid, enabled)


def search_jobs(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search jobs entries in cron/settings.

    Wraps: POST /api/cron/settings/searchJobs

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("cron", "settings", "jobs", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for cron.

    Wraps: POST /api/cron/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("cron", controller, action, data)
