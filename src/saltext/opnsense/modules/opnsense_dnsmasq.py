# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dnsmasq wrappers.

Generated from controllers.json for module dnsmasq.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dnsmasq/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dnsmasq"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- leases controller ---

def search_lease(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search lease entries in dnsmasq/leases.

    Wraps: POST /api/dnsmasq/leases/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "leases", "lease", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings")


def search_boot(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search boot entries in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/searchBoot

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "settings", "boot", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_boot(uuid=None):
    """
    Get boot entry in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/getBoot/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings", "boot", uuid)


def add_boot(data):
    """
    Add boot entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/addBoot

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnsmasq", "settings", "boot", data)


def set_boot(uuid, data):
    """
    Set/update boot entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/setBoot/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnsmasq", "settings", "boot", uuid, data)


def del_boot(uuid):
    """
    Delete boot entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/delBoot/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnsmasq", "settings", "boot", uuid)


def search_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search domain entries in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/searchDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "settings", "domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_domain(uuid=None):
    """
    Get domain entry in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/getDomain/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings", "domain", uuid)


def add_domain(data):
    """
    Add domain entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/addDomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnsmasq", "settings", "domain", data)


def set_domain(uuid, data):
    """
    Set/update domain entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/setDomain/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnsmasq", "settings", "domain", uuid, data)


def del_domain(uuid):
    """
    Delete domain entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/delDomain/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnsmasq", "settings", "domain", uuid)


def search_host(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search host entries in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/searchHost

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "settings", "host", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_host(uuid=None):
    """
    Get host entry in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/getHost/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings", "host", uuid)


def add_host(data):
    """
    Add host entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/addHost

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnsmasq", "settings", "host", data)


def set_host(uuid, data):
    """
    Set/update host entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/setHost/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnsmasq", "settings", "host", uuid, data)


def del_host(uuid):
    """
    Delete host entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/delHost/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnsmasq", "settings", "host", uuid)


def search_option(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search option entries in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/searchOption

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "settings", "option", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_option(uuid=None):
    """
    Get option entry in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/getOption/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings", "option", uuid)


def add_option(data):
    """
    Add option entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/addOption

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnsmasq", "settings", "option", data)


def set_option(uuid, data):
    """
    Set/update option entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/setOption/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnsmasq", "settings", "option", uuid, data)


def del_option(uuid):
    """
    Delete option entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/delOption/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnsmasq", "settings", "option", uuid)


def search_range(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search range entries in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/searchRange

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "settings", "range", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_range(uuid=None):
    """
    Get range entry in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/getRange/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings", "range", uuid)


def add_range(data):
    """
    Add range entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/addRange

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnsmasq", "settings", "range", data)


def set_range(uuid, data):
    """
    Set/update range entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/setRange/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnsmasq", "settings", "range", uuid, data)


def del_range(uuid):
    """
    Delete range entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/delRange/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnsmasq", "settings", "range", uuid)


def search_tag(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search tag entries in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/searchTag

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnsmasq", "settings", "tag", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_tag(uuid=None):
    """
    Get tag entry in dnsmasq/settings.

    Wraps: GET /api/dnsmasq/settings/getTag/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnsmasq", "settings", "tag", uuid)


def add_tag(data):
    """
    Add tag entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/addTag

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnsmasq", "settings", "tag", data)


def set_tag(uuid, data):
    """
    Set/update tag entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/setTag/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnsmasq", "settings", "tag", uuid, data)


def del_tag(uuid):
    """
    Delete tag entry in dnsmasq/settings.

    Wraps: POST /api/dnsmasq/settings/delTag/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnsmasq", "settings", "tag", uuid)


def settings_download_hosts(data=None, uuid=None):
    """
    Execute downloadHosts in dnsmasq/settings.

    Wraps: /api/dnsmasq/settings/downloadHosts

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("dnsmasq", "settings", "downloadHosts", uuid=uuid, data=data)


def settings_get_tag_list(data=None, uuid=None):
    """
    Execute getTagList in dnsmasq/settings.

    Wraps: /api/dnsmasq/settings/getTagList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("dnsmasq", "settings", "getTagList", uuid=uuid, data=data)


def settings_upload_hosts(data=None, uuid=None):
    """
    Execute uploadHosts in dnsmasq/settings.

    Wraps: /api/dnsmasq/settings/uploadHosts

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("dnsmasq", "settings", "uploadHosts", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="leases", action="reconfigure", data=None):
    """
    Generic reconfigure for dnsmasq.

    Wraps: POST /api/dnsmasq/{controller}/{action}

    :param controller: Controller name, default leases
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dnsmasq", controller, action, data)
