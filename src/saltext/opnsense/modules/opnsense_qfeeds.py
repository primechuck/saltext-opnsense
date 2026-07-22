# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense qfeeds wrappers.

Generated from controllers.json for module qfeeds.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/qfeeds/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_qfeeds"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- settings controller ---

def search_events(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search events entries in qfeeds/settings.

    Wraps: POST /api/qfeeds/settings/searchEvents

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("qfeeds", "settings", "events", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_feeds(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search feeds entries in qfeeds/settings.

    Wraps: POST /api/qfeeds/settings/searchFeeds

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("qfeeds", "settings", "feeds", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def settings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in qfeeds/settings.

    Wraps: POST /api/qfeeds/settings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("qfeeds", "settings", action, data)


def settings_stats(data=None, uuid=None):
    """
    Execute stats in qfeeds/settings.

    Wraps: /api/qfeeds/settings/stats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("qfeeds", "settings", "stats", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="settings", action="reconfigure", data=None):
    """
    Generic reconfigure for qfeeds.

    Wraps: POST /api/qfeeds/{controller}/{action}

    :param controller: Controller name, default settings
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("qfeeds", controller, action, data)
