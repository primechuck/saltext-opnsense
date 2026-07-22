# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dnscryptproxy wrappers.

Generated from controllers.json for module dnscryptproxy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/dnscryptproxy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dnscryptproxy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- cloak controller ---

def search_cloak(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search cloak entries in dnscryptproxy/cloak.

    Wraps: POST /api/dnscryptproxy/cloak/searchCloak

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnscryptproxy", "cloak", "cloak", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_cloak(uuid=None):
    """
    Get cloak entry in dnscryptproxy/cloak.

    Wraps: GET /api/dnscryptproxy/cloak/getCloak/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnscryptproxy", "cloak", "cloak", uuid)


def add_cloak(data):
    """
    Add cloak entry in dnscryptproxy/cloak.

    Wraps: POST /api/dnscryptproxy/cloak/addCloak

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnscryptproxy", "cloak", "cloak", data)


def set_cloak(uuid, data):
    """
    Set/update cloak entry in dnscryptproxy/cloak.

    Wraps: POST /api/dnscryptproxy/cloak/setCloak/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnscryptproxy", "cloak", "cloak", uuid, data)


def del_cloak(uuid):
    """
    Delete cloak entry in dnscryptproxy/cloak.

    Wraps: POST /api/dnscryptproxy/cloak/delCloak/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnscryptproxy", "cloak", "cloak", uuid)


def toggle_cloak(uuid, enabled=None):
    """
    Toggle cloak entry in dnscryptproxy/cloak.

    Wraps: POST /api/dnscryptproxy/cloak/toggleCloak/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("dnscryptproxy", "cloak", "cloak", uuid, enabled)


# --- forward controller ---

def search_forward(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search forward entries in dnscryptproxy/forward.

    Wraps: POST /api/dnscryptproxy/forward/searchForward

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnscryptproxy", "forward", "forward", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_forward(uuid=None):
    """
    Get forward entry in dnscryptproxy/forward.

    Wraps: GET /api/dnscryptproxy/forward/getForward/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnscryptproxy", "forward", "forward", uuid)


def add_forward(data):
    """
    Add forward entry in dnscryptproxy/forward.

    Wraps: POST /api/dnscryptproxy/forward/addForward

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnscryptproxy", "forward", "forward", data)


def set_forward(uuid, data):
    """
    Set/update forward entry in dnscryptproxy/forward.

    Wraps: POST /api/dnscryptproxy/forward/setForward/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnscryptproxy", "forward", "forward", uuid, data)


def del_forward(uuid):
    """
    Delete forward entry in dnscryptproxy/forward.

    Wraps: POST /api/dnscryptproxy/forward/delForward/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnscryptproxy", "forward", "forward", uuid)


def toggle_forward(uuid, enabled=None):
    """
    Toggle forward entry in dnscryptproxy/forward.

    Wraps: POST /api/dnscryptproxy/forward/toggleForward/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("dnscryptproxy", "forward", "forward", uuid, enabled)


# --- server controller ---

def search_server(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search server entries in dnscryptproxy/server.

    Wraps: POST /api/dnscryptproxy/server/searchServer

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnscryptproxy", "server", "server", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_server(uuid=None):
    """
    Get server entry in dnscryptproxy/server.

    Wraps: GET /api/dnscryptproxy/server/getServer/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnscryptproxy", "server", "server", uuid)


def add_server(data):
    """
    Add server entry in dnscryptproxy/server.

    Wraps: POST /api/dnscryptproxy/server/addServer

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnscryptproxy", "server", "server", data)


def set_server(uuid, data):
    """
    Set/update server entry in dnscryptproxy/server.

    Wraps: POST /api/dnscryptproxy/server/setServer/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnscryptproxy", "server", "server", uuid, data)


def del_server(uuid):
    """
    Delete server entry in dnscryptproxy/server.

    Wraps: POST /api/dnscryptproxy/server/delServer/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnscryptproxy", "server", "server", uuid)


def toggle_server(uuid, enabled=None):
    """
    Toggle server entry in dnscryptproxy/server.

    Wraps: POST /api/dnscryptproxy/server/toggleServer/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("dnscryptproxy", "server", "server", uuid, enabled)


# --- service controller ---

def service_dnsbl(data=None, uuid=None):
    """
    Execute dnsbl in dnscryptproxy/service.

    Wraps: /api/dnscryptproxy/service/dnsbl

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("dnscryptproxy", "service", "dnsbl", uuid=uuid, data=data)


# --- whitelist controller ---

def search_whitelist(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search whitelist entries in dnscryptproxy/whitelist.

    Wraps: POST /api/dnscryptproxy/whitelist/searchWhitelist

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("dnscryptproxy", "whitelist", "whitelist", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_whitelist(uuid=None):
    """
    Get whitelist entry in dnscryptproxy/whitelist.

    Wraps: GET /api/dnscryptproxy/whitelist/getWhitelist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("dnscryptproxy", "whitelist", "whitelist", uuid)


def add_whitelist(data):
    """
    Add whitelist entry in dnscryptproxy/whitelist.

    Wraps: POST /api/dnscryptproxy/whitelist/addWhitelist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("dnscryptproxy", "whitelist", "whitelist", data)


def set_whitelist(uuid, data):
    """
    Set/update whitelist entry in dnscryptproxy/whitelist.

    Wraps: POST /api/dnscryptproxy/whitelist/setWhitelist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("dnscryptproxy", "whitelist", "whitelist", uuid, data)


def del_whitelist(uuid):
    """
    Delete whitelist entry in dnscryptproxy/whitelist.

    Wraps: POST /api/dnscryptproxy/whitelist/delWhitelist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("dnscryptproxy", "whitelist", "whitelist", uuid)


def toggle_whitelist(uuid, enabled=None):
    """
    Toggle whitelist entry in dnscryptproxy/whitelist.

    Wraps: POST /api/dnscryptproxy/whitelist/toggleWhitelist/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("dnscryptproxy", "whitelist", "whitelist", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="cloak", action="reconfigure", data=None):
    """
    Generic reconfigure for dnscryptproxy.

    Wraps: POST /api/dnscryptproxy/{controller}/{action}

    :param controller: Controller name, default cloak
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("dnscryptproxy", controller, action, data)
