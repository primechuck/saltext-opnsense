# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense zabbixagent state wrappers.

Generated from controllers.json for module zabbixagent.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_zabbixagent"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def alias_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure alias settings present in zabbixagent.

    Wraps opnsense.item_present for /api/zabbixagent/settings/searchAlias

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "zabbixagent", "settings", "alias", data, match=match, reconfigure=reconfigure, search_field=search_field)


def alias_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure alias settings absent in zabbixagent.

    Wraps opnsense.item_absent for /api/zabbixagent/settings/searchAlias

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "zabbixagent", "settings", "alias", match=match, reconfigure=reconfigure, search_field=search_field)


def aliases_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure aliases settings present in zabbixagent.

    Wraps opnsense.item_present for /api/zabbixagent/settings/searchAliases

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "zabbixagent", "settings", "aliases", data, match=match, reconfigure=reconfigure, search_field=search_field)


def aliases_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure aliases settings absent in zabbixagent.

    Wraps opnsense.item_absent for /api/zabbixagent/settings/searchAliases

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "zabbixagent", "settings", "aliases", match=match, reconfigure=reconfigure, search_field=search_field)


def userparameter_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure userparameter settings present in zabbixagent.

    Wraps opnsense.item_present for /api/zabbixagent/settings/searchUserparameter

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "zabbixagent", "settings", "userparameter", data, match=match, reconfigure=reconfigure, search_field=search_field)


def userparameter_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure userparameter settings absent in zabbixagent.

    Wraps opnsense.item_absent for /api/zabbixagent/settings/searchUserparameter

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "zabbixagent", "settings", "userparameter", match=match, reconfigure=reconfigure, search_field=search_field)


def userparameters_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure userparameters settings present in zabbixagent.

    Wraps opnsense.item_present for /api/zabbixagent/settings/searchUserparameters

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "zabbixagent", "settings", "userparameters", data, match=match, reconfigure=reconfigure, search_field=search_field)


def userparameters_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure userparameters settings absent in zabbixagent.

    Wraps opnsense.item_absent for /api/zabbixagent/settings/searchUserparameters

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "zabbixagent", "settings", "userparameters", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="settings", action="reconfigure"):
    """
    Trigger reconfigure for zabbixagent.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("zabbixagent", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured zabbixagent/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"zabbixagent/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
