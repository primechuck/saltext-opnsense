# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ids state wrappers.

Generated from controllers.json for module ids.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ids"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def installed_rules_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure installed_rules settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchInstalledRules

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "installed_rules", data, match=match, reconfigure=reconfigure, search_field=search_field)


def installed_rules_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure installed_rules settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchInstalledRules

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "installed_rules", match=match, reconfigure=reconfigure, search_field=search_field)


def policy_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure policy settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchPolicy

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "policy", data, match=match, reconfigure=reconfigure, search_field=search_field)


def policy_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure policy settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchPolicy

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "policy", match=match, reconfigure=reconfigure, search_field=search_field)


def policy_rule_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure policy_rule settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchPolicyRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "policy_rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def policy_rule_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure policy_rule settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchPolicyRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "policy_rule", match=match, reconfigure=reconfigure, search_field=search_field)


def rule_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure rule settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def rule_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure rule settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "rule", match=match, reconfigure=reconfigure, search_field=search_field)


def ruleset_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure ruleset settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchRuleset

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "ruleset", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ruleset_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure ruleset settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchRuleset

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "ruleset", match=match, reconfigure=reconfigure, search_field=search_field)


def rulesetproperties_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure rulesetproperties settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchRulesetproperties

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "rulesetproperties", data, match=match, reconfigure=reconfigure, search_field=search_field)


def rulesetproperties_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure rulesetproperties settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchRulesetproperties

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "rulesetproperties", match=match, reconfigure=reconfigure, search_field=search_field)


def user_rule_present(name, data=None, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure user_rule settings present in ids.

    Wraps opnsense.item_present for /api/ids/settings/searchUserRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default ids/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ids", "settings", "user_rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def user_rule_absent(name, match=None, reconfigure="ids/service/reconfigure", search_field=None):
    """
    Ensure user_rule settings absent in ids.

    Wraps opnsense.item_absent for /api/ids/settings/searchUserRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ids", "settings", "user_rule", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for ids.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("ids", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured ids/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"ids/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
