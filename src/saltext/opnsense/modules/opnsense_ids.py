# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ids wrappers.

Generated from controllers.json for module ids.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/ids/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ids"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_drop_alert_log(data=None, uuid=None):
    """
    Execute dropAlertLog in ids/service.

    Wraps: /api/ids/service/dropAlertLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "service", "dropAlertLog", uuid=uuid, data=data)


def service_get_alert_info(data=None, uuid=None):
    """
    Execute getAlertInfo in ids/service.

    Wraps: /api/ids/service/getAlertInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "service", "getAlertInfo", uuid=uuid, data=data)


def service_get_alert_logs(data=None, uuid=None):
    """
    Execute getAlertLogs in ids/service.

    Wraps: /api/ids/service/getAlertLogs

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "service", "getAlertLogs", uuid=uuid, data=data)


def service_query_alerts(data=None, uuid=None):
    """
    Execute queryAlerts in ids/service.

    Wraps: /api/ids/service/queryAlerts

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "service", "queryAlerts", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in ids/service.

    Wraps: POST /api/ids/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ids", "service", action, data)


def service_reload_rules(data=None, uuid=None):
    """
    Execute reloadRules in ids/service.

    Wraps: /api/ids/service/reloadRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "service", "reloadRules", uuid=uuid, data=data)


def service_update_rules(data=None, uuid=None):
    """
    Execute updateRules in ids/service.

    Wraps: /api/ids/service/updateRules

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "service", "updateRules", uuid=uuid, data=data)


# --- settings controller ---

def search_installed_rules(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search installed_rules entries in ids/settings.

    Wraps: POST /api/ids/settings/searchInstalledRules

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ids", "settings", "installed_rules", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_policy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search policy entries in ids/settings.

    Wraps: POST /api/ids/settings/searchPolicy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ids", "settings", "policy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_policy(uuid=None):
    """
    Get policy entry in ids/settings.

    Wraps: GET /api/ids/settings/getPolicy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ids", "settings", "policy", uuid)


def add_policy(data):
    """
    Add policy entry in ids/settings.

    Wraps: POST /api/ids/settings/addPolicy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ids", "settings", "policy", data)


def set_policy(uuid, data):
    """
    Set/update policy entry in ids/settings.

    Wraps: POST /api/ids/settings/setPolicy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ids", "settings", "policy", uuid, data)


def del_policy(uuid):
    """
    Delete policy entry in ids/settings.

    Wraps: POST /api/ids/settings/delPolicy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ids", "settings", "policy", uuid)


def toggle_policy(uuid, enabled=None):
    """
    Toggle policy entry in ids/settings.

    Wraps: POST /api/ids/settings/togglePolicy/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ids", "settings", "policy", uuid, enabled)


def search_policy_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search policy_rule entries in ids/settings.

    Wraps: POST /api/ids/settings/searchPolicyRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ids", "settings", "policy_rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_policy_rule(uuid=None):
    """
    Get policy_rule entry in ids/settings.

    Wraps: GET /api/ids/settings/getPolicyRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ids", "settings", "policy_rule", uuid)


def add_policy_rule(data):
    """
    Add policy_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/addPolicyRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ids", "settings", "policy_rule", data)


def set_policy_rule(uuid, data):
    """
    Set/update policy_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/setPolicyRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ids", "settings", "policy_rule", uuid, data)


def del_policy_rule(uuid):
    """
    Delete policy_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/delPolicyRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ids", "settings", "policy_rule", uuid)


def toggle_policy_rule(uuid, enabled=None):
    """
    Toggle policy_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/togglePolicyRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ids", "settings", "policy_rule", uuid, enabled)


def set_rule(uuid, data):
    """
    Set/update rule entry in ids/settings.

    Wraps: POST /api/ids/settings/setRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ids", "settings", "rule", uuid, data)


def toggle_rule(uuid, enabled=None):
    """
    Toggle rule entry in ids/settings.

    Wraps: POST /api/ids/settings/toggleRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ids", "settings", "rule", uuid, enabled)


def get_ruleset(uuid=None):
    """
    Get ruleset entry in ids/settings.

    Wraps: GET /api/ids/settings/getRuleset/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ids", "settings", "ruleset", uuid)


def set_ruleset(uuid, data):
    """
    Set/update ruleset entry in ids/settings.

    Wraps: POST /api/ids/settings/setRuleset/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ids", "settings", "ruleset", uuid, data)


def toggle_ruleset(uuid, enabled=None):
    """
    Toggle ruleset entry in ids/settings.

    Wraps: POST /api/ids/settings/toggleRuleset/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ids", "settings", "ruleset", uuid, enabled)


def get_rulesetproperties(uuid=None):
    """
    Get rulesetproperties entry in ids/settings.

    Wraps: GET /api/ids/settings/getRulesetproperties/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ids", "settings", "rulesetproperties", uuid)


def set_rulesetproperties(uuid, data):
    """
    Set/update rulesetproperties entry in ids/settings.

    Wraps: POST /api/ids/settings/setRulesetproperties/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ids", "settings", "rulesetproperties", uuid, data)


def search_user_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search user_rule entries in ids/settings.

    Wraps: POST /api/ids/settings/searchUserRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ids", "settings", "user_rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_user_rule(uuid=None):
    """
    Get user_rule entry in ids/settings.

    Wraps: GET /api/ids/settings/getUserRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ids", "settings", "user_rule", uuid)


def add_user_rule(data):
    """
    Add user_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/addUserRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ids", "settings", "user_rule", data)


def set_user_rule(uuid, data):
    """
    Set/update user_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/setUserRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ids", "settings", "user_rule", uuid, data)


def del_user_rule(uuid):
    """
    Delete user_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/delUserRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ids", "settings", "user_rule", uuid)


def toggle_user_rule(uuid, enabled=None):
    """
    Toggle user_rule entry in ids/settings.

    Wraps: POST /api/ids/settings/toggleUserRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ids", "settings", "user_rule", uuid, enabled)


def settings_check_policy_rule(data=None, uuid=None):
    """
    Execute checkPolicyRule in ids/settings.

    Wraps: /api/ids/settings/checkPolicyRule

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "settings", "checkPolicyRule", uuid=uuid, data=data)


def settings_get_rule_info(data=None, uuid=None):
    """
    Execute getRuleInfo in ids/settings.

    Wraps: /api/ids/settings/getRuleInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "settings", "getRuleInfo", uuid=uuid, data=data)


def settings_list_rule_metadata(data=None, uuid=None):
    """
    Execute listRuleMetadata in ids/settings.

    Wraps: /api/ids/settings/listRuleMetadata

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "settings", "listRuleMetadata", uuid=uuid, data=data)


def settings_list_rulesets(data=None, uuid=None):
    """
    Execute listRulesets in ids/settings.

    Wraps: /api/ids/settings/listRulesets

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ids", "settings", "listRulesets", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for ids.

    Wraps: POST /api/ids/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ids", controller, action, data)
