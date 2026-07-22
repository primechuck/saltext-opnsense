# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense clamav wrappers.

Generated from controllers.json for module clamav.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/clamav/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_clamav"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_freshclam(data=None, uuid=None):
    """
    Execute freshclam in clamav/service.

    Wraps: /api/clamav/service/freshclam

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("clamav", "service", "freshclam", uuid=uuid, data=data)


def service_version(data=None, uuid=None):
    """
    Execute version in clamav/service.

    Wraps: /api/clamav/service/version

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("clamav", "service", "version", uuid=uuid, data=data)


# --- url controller ---

def search_url(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search url entries in clamav/url.

    Wraps: POST /api/clamav/url/searchUrl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("clamav", "url", "url", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_url(uuid=None):
    """
    Get url entry in clamav/url.

    Wraps: GET /api/clamav/url/getUrl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("clamav", "url", "url", uuid)


def add_url(data):
    """
    Add url entry in clamav/url.

    Wraps: POST /api/clamav/url/addUrl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("clamav", "url", "url", data)


def set_url(uuid, data):
    """
    Set/update url entry in clamav/url.

    Wraps: POST /api/clamav/url/setUrl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("clamav", "url", "url", uuid, data)


def del_url(uuid):
    """
    Delete url entry in clamav/url.

    Wraps: POST /api/clamav/url/delUrl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("clamav", "url", "url", uuid)


def toggle_url(uuid, enabled=None):
    """
    Toggle url entry in clamav/url.

    Wraps: POST /api/clamav/url/toggleUrl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("clamav", "url", "url", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for clamav.

    Wraps: POST /api/clamav/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("clamav", controller, action, data)
