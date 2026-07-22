# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense unbound wrappers.

Generated from controllers.json for module unbound.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/unbound/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_unbound"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- diagnostics controller ---

def diagnostics_dumpcache(data=None, uuid=None):
    """
    Execute dumpcache in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/dumpcache

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "dumpcache", uuid=uuid, data=data)


def diagnostics_dumpinfra(data=None, uuid=None):
    """
    Execute dumpinfra in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/dumpinfra

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "dumpinfra", uuid=uuid, data=data)


def diagnostics_listinsecure(data=None, uuid=None):
    """
    Execute listinsecure in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/listinsecure

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "listinsecure", uuid=uuid, data=data)


def diagnostics_listlocaldata(data=None, uuid=None):
    """
    Execute listlocaldata in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/listlocaldata

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "listlocaldata", uuid=uuid, data=data)


def diagnostics_listlocalzones(data=None, uuid=None):
    """
    Execute listlocalzones in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/listlocalzones

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "listlocalzones", uuid=uuid, data=data)


def diagnostics_stats(data=None, uuid=None):
    """
    Execute stats in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/stats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "stats", uuid=uuid, data=data)


def diagnostics_test_blocklist(data=None, uuid=None):
    """
    Execute testBlocklist in unbound/diagnostics.

    Wraps: /api/unbound/diagnostics/testBlocklist

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "diagnostics", "testBlocklist", uuid=uuid, data=data)


# --- overview controller ---

def search_queries(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search queries entries in unbound/overview.

    Wraps: POST /api/unbound/overview/searchQueries

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("unbound", "overview", "queries", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def overview_get_policies(data=None, uuid=None):
    """
    Execute getPolicies in unbound/overview.

    Wraps: /api/unbound/overview/getPolicies

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "overview", "getPolicies", uuid=uuid, data=data)


def overview_is_block_list_enabled(data=None, uuid=None):
    """
    Execute isBlockListEnabled in unbound/overview.

    Wraps: /api/unbound/overview/isBlockListEnabled

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "overview", "isBlockListEnabled", uuid=uuid, data=data)


def overview_is_enabled(data=None, uuid=None):
    """
    Execute isEnabled in unbound/overview.

    Wraps: /api/unbound/overview/isEnabled

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "overview", "isEnabled", uuid=uuid, data=data)


def overview_reset(data=None, uuid=None):
    """
    Execute reset in unbound/overview.

    Wraps: /api/unbound/overview/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "overview", "reset", uuid=uuid, data=data)


def overview_rolling(data=None, uuid=None):
    """
    Execute Rolling in unbound/overview.

    Wraps: /api/unbound/overview/Rolling

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "overview", "Rolling", uuid=uuid, data=data)


def overview_totals(data=None, uuid=None):
    """
    Execute totals in unbound/overview.

    Wraps: /api/unbound/overview/totals

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "overview", "totals", uuid=uuid, data=data)


# --- service controller ---

def service_dnsbl(data=None, uuid=None):
    """
    Execute dnsbl in unbound/service.

    Wraps: /api/unbound/service/dnsbl

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "service", "dnsbl", uuid=uuid, data=data)


def service_reconfigure_general(action="reconfigureGeneral", data=None):
    """
    reconfigureGeneral action in unbound/service.

    Wraps: POST /api/unbound/service/reconfigureGeneral

    :param action: Action override, default reconfigureGeneral
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("unbound", "service", action, data)


# --- settings controller ---

def search_acl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search acl entries in unbound/settings.

    Wraps: POST /api/unbound/settings/searchAcl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("unbound", "settings", "acl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_acl(uuid=None):
    """
    Get acl entry in unbound/settings.

    Wraps: GET /api/unbound/settings/getAcl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("unbound", "settings", "acl", uuid)


def add_acl(data):
    """
    Add acl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/addAcl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("unbound", "settings", "acl", data)


def set_acl(uuid, data):
    """
    Set/update acl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/setAcl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("unbound", "settings", "acl", uuid, data)


def del_acl(uuid):
    """
    Delete acl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/delAcl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("unbound", "settings", "acl", uuid)


def toggle_acl(uuid, enabled=None):
    """
    Toggle acl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/toggleAcl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("unbound", "settings", "acl", uuid, enabled)


def search_dnsbl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search dnsbl entries in unbound/settings.

    Wraps: POST /api/unbound/settings/searchDnsbl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("unbound", "settings", "dnsbl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dnsbl(uuid=None):
    """
    Get dnsbl entry in unbound/settings.

    Wraps: GET /api/unbound/settings/getDnsbl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("unbound", "settings", "dnsbl", uuid)


def add_dnsbl(data):
    """
    Add dnsbl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/addDnsbl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("unbound", "settings", "dnsbl", data)


def set_dnsbl(uuid, data):
    """
    Set/update dnsbl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/setDnsbl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("unbound", "settings", "dnsbl", uuid, data)


def del_dnsbl(uuid):
    """
    Delete dnsbl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/delDnsbl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("unbound", "settings", "dnsbl", uuid)


def toggle_dnsbl(uuid, enabled=None):
    """
    Toggle dnsbl entry in unbound/settings.

    Wraps: POST /api/unbound/settings/toggleDnsbl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("unbound", "settings", "dnsbl", uuid, enabled)


def search_forward(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search forward entries in unbound/settings.

    Wraps: POST /api/unbound/settings/searchForward

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("unbound", "settings", "forward", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_forward(uuid=None):
    """
    Get forward entry in unbound/settings.

    Wraps: GET /api/unbound/settings/getForward/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("unbound", "settings", "forward", uuid)


def add_forward(data):
    """
    Add forward entry in unbound/settings.

    Wraps: POST /api/unbound/settings/addForward

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("unbound", "settings", "forward", data)


def set_forward(uuid, data):
    """
    Set/update forward entry in unbound/settings.

    Wraps: POST /api/unbound/settings/setForward/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("unbound", "settings", "forward", uuid, data)


def del_forward(uuid):
    """
    Delete forward entry in unbound/settings.

    Wraps: POST /api/unbound/settings/delForward/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("unbound", "settings", "forward", uuid)


def toggle_forward(uuid, enabled=None):
    """
    Toggle forward entry in unbound/settings.

    Wraps: POST /api/unbound/settings/toggleForward/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("unbound", "settings", "forward", uuid, enabled)


def search_host_alias(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search host_alias entries in unbound/settings.

    Wraps: POST /api/unbound/settings/searchHostAlias

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("unbound", "settings", "host_alias", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_host_alias(uuid=None):
    """
    Get host_alias entry in unbound/settings.

    Wraps: GET /api/unbound/settings/getHostAlias/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("unbound", "settings", "host_alias", uuid)


def add_host_alias(data):
    """
    Add host_alias entry in unbound/settings.

    Wraps: POST /api/unbound/settings/addHostAlias

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("unbound", "settings", "host_alias", data)


def set_host_alias(uuid, data):
    """
    Set/update host_alias entry in unbound/settings.

    Wraps: POST /api/unbound/settings/setHostAlias/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("unbound", "settings", "host_alias", uuid, data)


def del_host_alias(uuid):
    """
    Delete host_alias entry in unbound/settings.

    Wraps: POST /api/unbound/settings/delHostAlias/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("unbound", "settings", "host_alias", uuid)


def toggle_host_alias(uuid, enabled=None):
    """
    Toggle host_alias entry in unbound/settings.

    Wraps: POST /api/unbound/settings/toggleHostAlias/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("unbound", "settings", "host_alias", uuid, enabled)


def search_host_override(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search host_override entries in unbound/settings.

    Wraps: POST /api/unbound/settings/searchHostOverride

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("unbound", "settings", "host_override", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_host_override(uuid=None):
    """
    Get host_override entry in unbound/settings.

    Wraps: GET /api/unbound/settings/getHostOverride/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("unbound", "settings", "host_override", uuid)


def add_host_override(data):
    """
    Add host_override entry in unbound/settings.

    Wraps: POST /api/unbound/settings/addHostOverride

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("unbound", "settings", "host_override", data)


def set_host_override(uuid, data):
    """
    Set/update host_override entry in unbound/settings.

    Wraps: POST /api/unbound/settings/setHostOverride/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("unbound", "settings", "host_override", uuid, data)


def del_host_override(uuid):
    """
    Delete host_override entry in unbound/settings.

    Wraps: POST /api/unbound/settings/delHostOverride/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("unbound", "settings", "host_override", uuid)


def toggle_host_override(uuid, enabled=None):
    """
    Toggle host_override entry in unbound/settings.

    Wraps: POST /api/unbound/settings/toggleHostOverride/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("unbound", "settings", "host_override", uuid, enabled)


def settings_get_nameservers(data=None, uuid=None):
    """
    Execute getNameservers in unbound/settings.

    Wraps: /api/unbound/settings/getNameservers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "settings", "getNameservers", uuid=uuid, data=data)


def settings_update_blocklist(data=None, uuid=None):
    """
    Execute updateBlocklist in unbound/settings.

    Wraps: /api/unbound/settings/updateBlocklist

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("unbound", "settings", "updateBlocklist", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="diagnostics", action="reconfigure", data=None):
    """
    Generic reconfigure for unbound.

    Wraps: POST /api/unbound/{controller}/{action}

    :param controller: Controller name, default diagnostics
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("unbound", controller, action, data)
