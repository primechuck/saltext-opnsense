# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense crowdsec wrappers.

Generated from controllers.json for module crowdsec.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/crowdsec/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_crowdsec"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- alerts controller ---

def search_alert(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search alert entries in crowdsec/alerts.

    Wraps: POST /api/crowdsec/alerts/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "alerts", "alert", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- appsecconfigs controller ---

def search_appsecconfig(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search appsecconfig entries in crowdsec/appsecconfigs.

    Wraps: POST /api/crowdsec/appsecconfigs/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "appsecconfigs", "appsecconfig", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- appsecrules controller ---

def search_appsecrule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search appsecrule entries in crowdsec/appsecrules.

    Wraps: POST /api/crowdsec/appsecrules/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "appsecrules", "appsecrule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- bouncers controller ---

def search_bouncer(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search bouncer entries in crowdsec/bouncers.

    Wraps: POST /api/crowdsec/bouncers/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "bouncers", "bouncer", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- collections controller ---

def search_collection(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search collection entries in crowdsec/collections.

    Wraps: POST /api/crowdsec/collections/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "collections", "collection", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- decisions controller ---

def search_decision(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search decision entries in crowdsec/decisions.

    Wraps: POST /api/crowdsec/decisions/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "decisions", "decision", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def del_decision(uuid):
    """
    Delete decision entry in crowdsec/decisions.

    Wraps: POST /api/crowdsec/decisions/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("crowdsec", "decisions", "decision", uuid)


# --- machines controller ---

def search_machine(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search machine entries in crowdsec/machines.

    Wraps: POST /api/crowdsec/machines/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "machines", "machine", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- parsers controller ---

def search_parser(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search parser entries in crowdsec/parsers.

    Wraps: POST /api/crowdsec/parsers/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "parsers", "parser", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- postoverflows controller ---

def search_postoverflow(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search postoverflow entries in crowdsec/postoverflows.

    Wraps: POST /api/crowdsec/postoverflows/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "postoverflows", "postoverflow", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- scenarios controller ---

def search_scenario(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search scenario entries in crowdsec/scenarios.

    Wraps: POST /api/crowdsec/scenarios/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("crowdsec", "scenarios", "scenario", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in crowdsec/service.

    Wraps: POST /api/crowdsec/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("crowdsec", "service", action, data)


# --- version controller ---

def get_version():
    """
    Get version singleton config in crowdsec/version.

    Wraps: GET /api/crowdsec/version/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("crowdsec", "version")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for crowdsec.

    Wraps: POST /api/crowdsec/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("crowdsec", controller, action, data)
