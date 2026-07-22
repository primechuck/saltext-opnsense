# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense crowdsec state wrappers.

Generated from controllers.json for module crowdsec.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_crowdsec"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- alerts controller ---

def alert_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure alert alerts present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/alerts/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "alerts", "alert", data, match=match, reconfigure=reconfigure, search_field=search_field)


def alert_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure alert alerts absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/alerts/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "alerts", "alert", match=match, reconfigure=reconfigure, search_field=search_field)


# --- appsecconfigs controller ---

def appsecconfig_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure appsecconfig appsecconfigs present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/appsecconfigs/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "appsecconfigs", "appsecconfig", data, match=match, reconfigure=reconfigure, search_field=search_field)


def appsecconfig_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure appsecconfig appsecconfigs absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/appsecconfigs/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "appsecconfigs", "appsecconfig", match=match, reconfigure=reconfigure, search_field=search_field)


# --- appsecrules controller ---

def appsecrule_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure appsecrule appsecrules present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/appsecrules/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "appsecrules", "appsecrule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def appsecrule_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure appsecrule appsecrules absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/appsecrules/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "appsecrules", "appsecrule", match=match, reconfigure=reconfigure, search_field=search_field)


# --- bouncers controller ---

def bouncer_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure bouncer bouncers present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/bouncers/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "bouncers", "bouncer", data, match=match, reconfigure=reconfigure, search_field=search_field)


def bouncer_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure bouncer bouncers absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/bouncers/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "bouncers", "bouncer", match=match, reconfigure=reconfigure, search_field=search_field)


# --- collections controller ---

def collection_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure collection collections present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/collections/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "collections", "collection", data, match=match, reconfigure=reconfigure, search_field=search_field)


def collection_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure collection collections absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/collections/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "collections", "collection", match=match, reconfigure=reconfigure, search_field=search_field)


# --- decisions controller ---

def decision_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure decision decisions present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/decisions/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "decisions", "decision", data, match=match, reconfigure=reconfigure, search_field=search_field)


def decision_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure decision decisions absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/decisions/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "decisions", "decision", match=match, reconfigure=reconfigure, search_field=search_field)


# --- machines controller ---

def machine_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure machine machines present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/machines/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "machines", "machine", data, match=match, reconfigure=reconfigure, search_field=search_field)


def machine_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure machine machines absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/machines/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "machines", "machine", match=match, reconfigure=reconfigure, search_field=search_field)


# --- parsers controller ---

def parser_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure parser parsers present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/parsers/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "parsers", "parser", data, match=match, reconfigure=reconfigure, search_field=search_field)


def parser_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure parser parsers absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/parsers/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "parsers", "parser", match=match, reconfigure=reconfigure, search_field=search_field)


# --- postoverflows controller ---

def postoverflow_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure postoverflow postoverflows present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/postoverflows/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "postoverflows", "postoverflow", data, match=match, reconfigure=reconfigure, search_field=search_field)


def postoverflow_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure postoverflow postoverflows absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/postoverflows/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "postoverflows", "postoverflow", match=match, reconfigure=reconfigure, search_field=search_field)


# --- scenarios controller ---

def scenario_present(name, data=None, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure scenario scenarios present in crowdsec.

    Wraps opnsense.item_present for /api/crowdsec/scenarios/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default crowdsec/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "crowdsec", "scenarios", "scenario", data, match=match, reconfigure=reconfigure, search_field=search_field)


def scenario_absent(name, match=None, reconfigure="crowdsec/service/reconfigure", search_field=None):
    """
    Ensure scenario scenarios absent in crowdsec.

    Wraps opnsense.item_absent for /api/crowdsec/scenarios/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "crowdsec", "scenarios", "scenario", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for crowdsec.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("crowdsec", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured crowdsec/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"crowdsec/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
