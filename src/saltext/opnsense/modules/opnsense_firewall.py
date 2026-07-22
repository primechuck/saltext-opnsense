# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense firewall wrappers.

Generated from controllers.json for module firewall.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/firewall/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_firewall"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- alias controller ---

def search_alias_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in firewall/alias.

    Wraps: POST /api/firewall/alias/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "alias", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_alias_item(uuid=None):
    """
    Get item entry in firewall/alias.

    Wraps: GET /api/firewall/alias/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "alias", "item", uuid)


def add_alias_item(data):
    """
    Add item entry in firewall/alias.

    Wraps: POST /api/firewall/alias/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "alias", "item", data)


def set_alias_item(uuid, data):
    """
    Set/update item entry in firewall/alias.

    Wraps: POST /api/firewall/alias/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "alias", "item", uuid, data)


def del_alias_item(uuid):
    """
    Delete item entry in firewall/alias.

    Wraps: POST /api/firewall/alias/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "alias", "item", uuid)


def toggle_alias_item(uuid, enabled=None):
    """
    Toggle item entry in firewall/alias.

    Wraps: POST /api/firewall/alias/toggleItem/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("firewall", "alias", "item", uuid, enabled)


def alias_export(data=None, uuid=None):
    """
    Execute export in firewall/alias.

    Wraps: /api/firewall/alias/export

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "export", uuid=uuid, data=data)


def alias_get_alias_uuid(data=None, uuid=None):
    """
    Execute getAliasUUID in firewall/alias.

    Wraps: /api/firewall/alias/getAliasUUID

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "getAliasUUID", uuid=uuid, data=data)


def alias_get_geo_ip(data=None, uuid=None):
    """
    Execute getGeoIP in firewall/alias.

    Wraps: /api/firewall/alias/getGeoIP

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "getGeoIP", uuid=uuid, data=data)


def alias_get_table_size(data=None, uuid=None):
    """
    Execute getTableSize in firewall/alias.

    Wraps: /api/firewall/alias/getTableSize

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "getTableSize", uuid=uuid, data=data)


def alias_import(data=None, uuid=None):
    """
    Execute import in firewall/alias.

    Wraps: /api/firewall/alias/import

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "import", uuid=uuid, data=data)


def alias_list_categories(data=None, uuid=None):
    """
    Execute listCategories in firewall/alias.

    Wraps: /api/firewall/alias/listCategories

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "listCategories", uuid=uuid, data=data)


def alias_list_countries(data=None, uuid=None):
    """
    Execute listCountries in firewall/alias.

    Wraps: /api/firewall/alias/listCountries

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "listCountries", uuid=uuid, data=data)


def alias_list_network_aliases(data=None, uuid=None):
    """
    Execute listNetworkAliases in firewall/alias.

    Wraps: /api/firewall/alias/listNetworkAliases

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "listNetworkAliases", uuid=uuid, data=data)


def alias_list_user_groups(data=None, uuid=None):
    """
    Execute listUserGroups in firewall/alias.

    Wraps: /api/firewall/alias/listUserGroups

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "listUserGroups", uuid=uuid, data=data)


def alias_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in firewall/alias.

    Wraps: POST /api/firewall/alias/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("firewall", "alias", action, data)


def alias_update(data=None, uuid=None):
    """
    Execute update in firewall/alias.

    Wraps: /api/firewall/alias/update

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "alias", "update", uuid=uuid, data=data)


# --- aliasutil controller ---

def aliasutil_add(data=None, uuid=None):
    """
    Execute add in firewall/aliasutil.

    Wraps: /api/firewall/aliasutil/add

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "aliasutil", "add", uuid=uuid, data=data)


def aliasutil_aliases(data=None, uuid=None):
    """
    Execute aliases in firewall/aliasutil.

    Wraps: /api/firewall/aliasutil/aliases

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "aliasutil", "aliases", uuid=uuid, data=data)


def aliasutil_delete(data=None, uuid=None):
    """
    Execute delete in firewall/aliasutil.

    Wraps: /api/firewall/aliasutil/delete

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "aliasutil", "delete", uuid=uuid, data=data)


def aliasutil_find_references(data=None, uuid=None):
    """
    Execute findReferences in firewall/aliasutil.

    Wraps: /api/firewall/aliasutil/findReferences

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "aliasutil", "findReferences", uuid=uuid, data=data)


def aliasutil_flush(data=None, uuid=None):
    """
    Execute flush in firewall/aliasutil.

    Wraps: /api/firewall/aliasutil/flush

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "aliasutil", "flush", uuid=uuid, data=data)


def aliasutil_list(data=None, uuid=None):
    """
    Execute list in firewall/aliasutil.

    Wraps: /api/firewall/aliasutil/list

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "aliasutil", "list", uuid=uuid, data=data)


# --- category controller ---

def search_category_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in firewall/category.

    Wraps: POST /api/firewall/category/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "category", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_category_item(uuid=None):
    """
    Get item entry in firewall/category.

    Wraps: GET /api/firewall/category/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "category", "item", uuid)


def add_category_item(data):
    """
    Add item entry in firewall/category.

    Wraps: POST /api/firewall/category/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "category", "item", data)


def set_category_item(uuid, data):
    """
    Set/update item entry in firewall/category.

    Wraps: POST /api/firewall/category/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "category", "item", uuid, data)


def del_category_item(uuid):
    """
    Delete item entry in firewall/category.

    Wraps: POST /api/firewall/category/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "category", "item", uuid)


def category_download(data=None, uuid=None):
    """
    Execute download in firewall/category.

    Wraps: /api/firewall/category/download

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "category", "download", uuid=uuid, data=data)


def category_upload(data=None, uuid=None):
    """
    Execute upload in firewall/category.

    Wraps: /api/firewall/category/upload

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "category", "upload", uuid=uuid, data=data)


# --- dnat controller ---

def search_dnat_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search rule entries in firewall/dnat.

    Wraps: POST /api/firewall/dnat/searchRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "dnat", "rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dnat_rule(uuid=None):
    """
    Get rule entry in firewall/dnat.

    Wraps: GET /api/firewall/dnat/getRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "dnat", "rule", uuid)


def add_dnat_rule(data):
    """
    Add rule entry in firewall/dnat.

    Wraps: POST /api/firewall/dnat/addRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "dnat", "rule", data)


def set_dnat_rule(uuid, data):
    """
    Set/update rule entry in firewall/dnat.

    Wraps: POST /api/firewall/dnat/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "dnat", "rule", uuid, data)


def del_dnat_rule(uuid):
    """
    Delete rule entry in firewall/dnat.

    Wraps: POST /api/firewall/dnat/delRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "dnat", "rule", uuid)


def toggle_dnat_rule(uuid, enabled=None):
    """
    Toggle rule entry in firewall/dnat.

    Wraps: POST /api/firewall/dnat/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("firewall", "dnat", "rule", uuid, enabled)


def dnat_download_rules(data=None, uuid=None):
    """
    Execute downloadRules in firewall/dnat.

    Wraps: /api/firewall/dnat/downloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "dnat", "downloadRules", uuid=uuid, data=data)


def dnat_move_rule_before(data=None, uuid=None):
    """
    Execute moveRuleBefore in firewall/dnat.

    Wraps: /api/firewall/dnat/moveRuleBefore

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "dnat", "moveRuleBefore", uuid=uuid, data=data)


def dnat_toggle_rule_log(data=None, uuid=None):
    """
    Execute toggleRuleLog in firewall/dnat.

    Wraps: /api/firewall/dnat/toggleRuleLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "dnat", "toggleRuleLog", uuid=uuid, data=data)


def dnat_upload_rules(data=None, uuid=None):
    """
    Execute uploadRules in firewall/dnat.

    Wraps: /api/firewall/dnat/uploadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "dnat", "uploadRules", uuid=uuid, data=data)


# --- filter controller ---

def search_filter_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search rule entries in firewall/filter.

    Wraps: POST /api/firewall/filter/searchRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "filter", "rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_filter_rule(uuid=None):
    """
    Get rule entry in firewall/filter.

    Wraps: GET /api/firewall/filter/getRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "filter", "rule", uuid)


def add_filter_rule(data):
    """
    Add rule entry in firewall/filter.

    Wraps: POST /api/firewall/filter/addRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "filter", "rule", data)


def set_filter_rule(uuid, data):
    """
    Set/update rule entry in firewall/filter.

    Wraps: POST /api/firewall/filter/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "filter", "rule", uuid, data)


def del_filter_rule(uuid):
    """
    Delete rule entry in firewall/filter.

    Wraps: POST /api/firewall/filter/delRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "filter", "rule", uuid)


def toggle_filter_rule(uuid, enabled=None):
    """
    Toggle rule entry in firewall/filter.

    Wraps: POST /api/firewall/filter/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("firewall", "filter", "rule", uuid, enabled)


def filter_download_rules(data=None, uuid=None):
    """
    Execute downloadRules in firewall/filter.

    Wraps: /api/firewall/filter/downloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filter", "downloadRules", uuid=uuid, data=data)


def filter_flush_inspect_cache(data=None, uuid=None):
    """
    Execute flushInspectCache in firewall/filter.

    Wraps: /api/firewall/filter/flushInspectCache

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filter", "flushInspectCache", uuid=uuid, data=data)


def filter_get_interface_list(data=None, uuid=None):
    """
    Execute getInterfaceList in firewall/filter.

    Wraps: /api/firewall/filter/getInterfaceList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filter", "getInterfaceList", uuid=uuid, data=data)


def filter_move_rule_before(data=None, uuid=None):
    """
    Execute moveRuleBefore in firewall/filter.

    Wraps: /api/firewall/filter/moveRuleBefore

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filter", "moveRuleBefore", uuid=uuid, data=data)


def filter_toggle_rule_log(data=None, uuid=None):
    """
    Execute toggleRuleLog in firewall/filter.

    Wraps: /api/firewall/filter/toggleRuleLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filter", "toggleRuleLog", uuid=uuid, data=data)


def filter_upload_rules(data=None, uuid=None):
    """
    Execute uploadRules in firewall/filter.

    Wraps: /api/firewall/filter/uploadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filter", "uploadRules", uuid=uuid, data=data)


# --- filterbase controller ---

def filterbase_apply(data=None):
    """
    Execute apply in firewall/filterbase.

    Wraps: POST /api/firewall/filterbase/apply

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filterbase", "apply", data=data, method="POST")


def filterbase_list_categories(data=None, uuid=None):
    """
    Execute listCategories in firewall/filterbase.

    Wraps: /api/firewall/filterbase/listCategories

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filterbase", "listCategories", uuid=uuid, data=data)


def filterbase_list_network_select_options(data=None, uuid=None):
    """
    Execute listNetworkSelectOptions in firewall/filterbase.

    Wraps: /api/firewall/filterbase/listNetworkSelectOptions

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filterbase", "listNetworkSelectOptions", uuid=uuid, data=data)


def filterbase_list_port_select_options(data=None, uuid=None):
    """
    Execute listPortSelectOptions in firewall/filterbase.

    Wraps: /api/firewall/filterbase/listPortSelectOptions

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filterbase", "listPortSelectOptions", uuid=uuid, data=data)


# --- filterutil controller ---

def filterutil_rule_stats(data=None, uuid=None):
    """
    Execute ruleStats in firewall/filterutil.

    Wraps: /api/firewall/filterutil/ruleStats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "filterutil", "ruleStats", uuid=uuid, data=data)


# --- group controller ---

def search_group_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in firewall/group.

    Wraps: POST /api/firewall/group/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "group", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_group_item(uuid=None):
    """
    Get item entry in firewall/group.

    Wraps: GET /api/firewall/group/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "group", "item", uuid)


def add_group_item(data):
    """
    Add item entry in firewall/group.

    Wraps: POST /api/firewall/group/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "group", "item", data)


def set_group_item(uuid, data):
    """
    Set/update item entry in firewall/group.

    Wraps: POST /api/firewall/group/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "group", "item", uuid, data)


def del_group_item(uuid):
    """
    Delete item entry in firewall/group.

    Wraps: POST /api/firewall/group/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "group", "item", uuid)


def group_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in firewall/group.

    Wraps: POST /api/firewall/group/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("firewall", "group", action, data)


# --- migration controller ---

def migration_count_outbound(data=None, uuid=None):
    """
    Execute countOutbound in firewall/migration.

    Wraps: /api/firewall/migration/countOutbound

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "migration", "countOutbound", uuid=uuid, data=data)


def migration_count_rules(data=None, uuid=None):
    """
    Execute countRules in firewall/migration.

    Wraps: /api/firewall/migration/countRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "migration", "countRules", uuid=uuid, data=data)


def migration_download_outbound(data=None, uuid=None):
    """
    Execute downloadOutbound in firewall/migration.

    Wraps: /api/firewall/migration/downloadOutbound

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "migration", "downloadOutbound", uuid=uuid, data=data)


def migration_download_rules(data=None, uuid=None):
    """
    Execute downloadRules in firewall/migration.

    Wraps: /api/firewall/migration/downloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "migration", "downloadRules", uuid=uuid, data=data)


def migration_flush(data=None, uuid=None):
    """
    Execute flush in firewall/migration.

    Wraps: /api/firewall/migration/flush

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "migration", "flush", uuid=uuid, data=data)


def migration_flush_outbound(data=None, uuid=None):
    """
    Execute flushOutbound in firewall/migration.

    Wraps: /api/firewall/migration/flushOutbound

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "migration", "flushOutbound", uuid=uuid, data=data)


# --- npt controller ---

def search_npt_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search rule entries in firewall/npt.

    Wraps: POST /api/firewall/npt/searchRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "npt", "rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_npt_rule(uuid=None):
    """
    Get rule entry in firewall/npt.

    Wraps: GET /api/firewall/npt/getRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "npt", "rule", uuid)


def add_npt_rule(data):
    """
    Add rule entry in firewall/npt.

    Wraps: POST /api/firewall/npt/addRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "npt", "rule", data)


def set_npt_rule(uuid, data):
    """
    Set/update rule entry in firewall/npt.

    Wraps: POST /api/firewall/npt/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "npt", "rule", uuid, data)


def del_npt_rule(uuid):
    """
    Delete rule entry in firewall/npt.

    Wraps: POST /api/firewall/npt/delRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "npt", "rule", uuid)


def toggle_npt_rule(uuid, enabled=None):
    """
    Toggle rule entry in firewall/npt.

    Wraps: POST /api/firewall/npt/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("firewall", "npt", "rule", uuid, enabled)


def npt_download_rules(data=None, uuid=None):
    """
    Execute downloadRules in firewall/npt.

    Wraps: /api/firewall/npt/downloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "npt", "downloadRules", uuid=uuid, data=data)


def npt_move_rule_before(data=None, uuid=None):
    """
    Execute moveRuleBefore in firewall/npt.

    Wraps: /api/firewall/npt/moveRuleBefore

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "npt", "moveRuleBefore", uuid=uuid, data=data)


def npt_toggle_rule_log(data=None, uuid=None):
    """
    Execute toggleRuleLog in firewall/npt.

    Wraps: /api/firewall/npt/toggleRuleLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "npt", "toggleRuleLog", uuid=uuid, data=data)


def npt_upload_rules(data=None, uuid=None):
    """
    Execute uploadRules in firewall/npt.

    Wraps: /api/firewall/npt/uploadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "npt", "uploadRules", uuid=uuid, data=data)


# --- onetoone controller ---

def search_onetoone_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search rule entries in firewall/onetoone.

    Wraps: POST /api/firewall/onetoone/searchRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "onetoone", "rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_onetoone_rule(uuid=None):
    """
    Get rule entry in firewall/onetoone.

    Wraps: GET /api/firewall/onetoone/getRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "onetoone", "rule", uuid)


def add_onetoone_rule(data):
    """
    Add rule entry in firewall/onetoone.

    Wraps: POST /api/firewall/onetoone/addRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "onetoone", "rule", data)


def set_onetoone_rule(uuid, data):
    """
    Set/update rule entry in firewall/onetoone.

    Wraps: POST /api/firewall/onetoone/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "onetoone", "rule", uuid, data)


def del_onetoone_rule(uuid):
    """
    Delete rule entry in firewall/onetoone.

    Wraps: POST /api/firewall/onetoone/delRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "onetoone", "rule", uuid)


def toggle_onetoone_rule(uuid, enabled=None):
    """
    Toggle rule entry in firewall/onetoone.

    Wraps: POST /api/firewall/onetoone/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("firewall", "onetoone", "rule", uuid, enabled)


def onetoone_download_rules(data=None, uuid=None):
    """
    Execute downloadRules in firewall/onetoone.

    Wraps: /api/firewall/onetoone/downloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "onetoone", "downloadRules", uuid=uuid, data=data)


def onetoone_move_rule_before(data=None, uuid=None):
    """
    Execute moveRuleBefore in firewall/onetoone.

    Wraps: /api/firewall/onetoone/moveRuleBefore

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "onetoone", "moveRuleBefore", uuid=uuid, data=data)


def onetoone_toggle_rule_log(data=None, uuid=None):
    """
    Execute toggleRuleLog in firewall/onetoone.

    Wraps: /api/firewall/onetoone/toggleRuleLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "onetoone", "toggleRuleLog", uuid=uuid, data=data)


def onetoone_upload_rules(data=None, uuid=None):
    """
    Execute uploadRules in firewall/onetoone.

    Wraps: /api/firewall/onetoone/uploadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "onetoone", "uploadRules", uuid=uuid, data=data)


# --- sourcenat controller ---

def search_sourcenat_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search rule entries in firewall/sourcenat.

    Wraps: POST /api/firewall/sourcenat/searchRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("firewall", "sourcenat", "rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_sourcenat_rule(uuid=None):
    """
    Get rule entry in firewall/sourcenat.

    Wraps: GET /api/firewall/sourcenat/getRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("firewall", "sourcenat", "rule", uuid)


def add_sourcenat_rule(data):
    """
    Add rule entry in firewall/sourcenat.

    Wraps: POST /api/firewall/sourcenat/addRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("firewall", "sourcenat", "rule", data)


def set_sourcenat_rule(uuid, data):
    """
    Set/update rule entry in firewall/sourcenat.

    Wraps: POST /api/firewall/sourcenat/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("firewall", "sourcenat", "rule", uuid, data)


def del_sourcenat_rule(uuid):
    """
    Delete rule entry in firewall/sourcenat.

    Wraps: POST /api/firewall/sourcenat/delRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("firewall", "sourcenat", "rule", uuid)


def toggle_sourcenat_rule(uuid, enabled=None):
    """
    Toggle rule entry in firewall/sourcenat.

    Wraps: POST /api/firewall/sourcenat/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("firewall", "sourcenat", "rule", uuid, enabled)


def sourcenat_download_rules(data=None, uuid=None):
    """
    Execute downloadRules in firewall/sourcenat.

    Wraps: /api/firewall/sourcenat/downloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "sourcenat", "downloadRules", uuid=uuid, data=data)


def sourcenat_move_rule_before(data=None, uuid=None):
    """
    Execute moveRuleBefore in firewall/sourcenat.

    Wraps: /api/firewall/sourcenat/moveRuleBefore

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "sourcenat", "moveRuleBefore", uuid=uuid, data=data)


def sourcenat_toggle_rule_log(data=None, uuid=None):
    """
    Execute toggleRuleLog in firewall/sourcenat.

    Wraps: /api/firewall/sourcenat/toggleRuleLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "sourcenat", "toggleRuleLog", uuid=uuid, data=data)


def sourcenat_upload_rules(data=None, uuid=None):
    """
    Execute uploadRules in firewall/sourcenat.

    Wraps: /api/firewall/sourcenat/uploadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("firewall", "sourcenat", "uploadRules", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="alias", action="reconfigure", data=None):
    """
    Generic reconfigure for firewall.

    Wraps: POST /api/firewall/{controller}/{action}

    :param controller: Controller name, default alias
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("firewall", controller, action, data)
