# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense firewall state wrappers.

Generated from controllers.json for module firewall.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_firewall"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- alias controller ---

def alias_item_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure item alias present in firewall.

    Wraps opnsense.item_present for /api/firewall/alias/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "alias", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def alias_item_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure item alias absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/alias/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "alias", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- category controller ---

def category_item_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure item category present in firewall.

    Wraps opnsense.item_present for /api/firewall/category/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "category", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def category_item_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure item category absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/category/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "category", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- dnat controller ---

def dnat_rule_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule dnat present in firewall.

    Wraps opnsense.item_present for /api/firewall/dnat/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "dnat", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dnat_rule_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule dnat absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/dnat/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "dnat", "rule", match=match, reconfigure=reconfigure, search_field=search_field)


# --- filter controller ---

def filter_rule_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule filter present in firewall.

    Wraps opnsense.item_present for /api/firewall/filter/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "filter", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def filter_rule_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule filter absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/filter/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "filter", "rule", match=match, reconfigure=reconfigure, search_field=search_field)


# --- group controller ---

def group_item_present(name, data=None, match=None, reconfigure="firewall/group/reconfigure", search_field=None):
    """
    Ensure item group present in firewall.

    Wraps opnsense.item_present for /api/firewall/group/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/group/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "group", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def group_item_absent(name, match=None, reconfigure="firewall/group/reconfigure", search_field=None):
    """
    Ensure item group absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/group/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "group", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- npt controller ---

def npt_rule_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule npt present in firewall.

    Wraps opnsense.item_present for /api/firewall/npt/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "npt", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def npt_rule_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule npt absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/npt/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "npt", "rule", match=match, reconfigure=reconfigure, search_field=search_field)


# --- onetoone controller ---

def onetoone_rule_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule onetoone present in firewall.

    Wraps opnsense.item_present for /api/firewall/onetoone/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "onetoone", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def onetoone_rule_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule onetoone absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/onetoone/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "onetoone", "rule", match=match, reconfigure=reconfigure, search_field=search_field)


# --- sourcenat controller ---

def sourcenat_rule_present(name, data=None, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule sourcenat present in firewall.

    Wraps opnsense.item_present for /api/firewall/sourcenat/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default firewall/alias/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "firewall", "sourcenat", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sourcenat_rule_absent(name, match=None, reconfigure="firewall/alias/reconfigure", search_field=None):
    """
    Ensure rule sourcenat absent in firewall.

    Wraps opnsense.item_absent for /api/firewall/sourcenat/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "firewall", "sourcenat", "rule", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="alias", action="reconfigure"):
    """
    Trigger reconfigure for firewall.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("firewall", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured firewall/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"firewall/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
