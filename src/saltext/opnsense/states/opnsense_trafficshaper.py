# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense trafficshaper state wrappers.

Generated from controllers.json for module trafficshaper.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_trafficshaper"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def pipe_present(name, data=None, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure pipe settings present in trafficshaper.

    Wraps opnsense.item_present for /api/trafficshaper/settings/searchPipe

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trafficshaper/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trafficshaper", "settings", "pipe", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pipe_absent(name, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure pipe settings absent in trafficshaper.

    Wraps opnsense.item_absent for /api/trafficshaper/settings/searchPipe

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trafficshaper", "settings", "pipe", match=match, reconfigure=reconfigure, search_field=search_field)


def pipes_present(name, data=None, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure pipes settings present in trafficshaper.

    Wraps opnsense.item_present for /api/trafficshaper/settings/searchPipes

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trafficshaper/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trafficshaper", "settings", "pipes", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pipes_absent(name, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure pipes settings absent in trafficshaper.

    Wraps opnsense.item_absent for /api/trafficshaper/settings/searchPipes

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trafficshaper", "settings", "pipes", match=match, reconfigure=reconfigure, search_field=search_field)


def queue_present(name, data=None, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure queue settings present in trafficshaper.

    Wraps opnsense.item_present for /api/trafficshaper/settings/searchQueue

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trafficshaper/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trafficshaper", "settings", "queue", data, match=match, reconfigure=reconfigure, search_field=search_field)


def queue_absent(name, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure queue settings absent in trafficshaper.

    Wraps opnsense.item_absent for /api/trafficshaper/settings/searchQueue

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trafficshaper", "settings", "queue", match=match, reconfigure=reconfigure, search_field=search_field)


def queues_present(name, data=None, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure queues settings present in trafficshaper.

    Wraps opnsense.item_present for /api/trafficshaper/settings/searchQueues

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trafficshaper/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trafficshaper", "settings", "queues", data, match=match, reconfigure=reconfigure, search_field=search_field)


def queues_absent(name, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure queues settings absent in trafficshaper.

    Wraps opnsense.item_absent for /api/trafficshaper/settings/searchQueues

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trafficshaper", "settings", "queues", match=match, reconfigure=reconfigure, search_field=search_field)


def rule_present(name, data=None, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure rule settings present in trafficshaper.

    Wraps opnsense.item_present for /api/trafficshaper/settings/searchRule

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trafficshaper/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trafficshaper", "settings", "rule", data, match=match, reconfigure=reconfigure, search_field=search_field)


def rule_absent(name, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure rule settings absent in trafficshaper.

    Wraps opnsense.item_absent for /api/trafficshaper/settings/searchRule

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trafficshaper", "settings", "rule", match=match, reconfigure=reconfigure, search_field=search_field)


def rules_present(name, data=None, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure rules settings present in trafficshaper.

    Wraps opnsense.item_present for /api/trafficshaper/settings/searchRules

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trafficshaper/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trafficshaper", "settings", "rules", data, match=match, reconfigure=reconfigure, search_field=search_field)


def rules_absent(name, match=None, reconfigure="trafficshaper/service/reconfigure", search_field=None):
    """
    Ensure rules settings absent in trafficshaper.

    Wraps opnsense.item_absent for /api/trafficshaper/settings/searchRules

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trafficshaper", "settings", "rules", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for trafficshaper.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("trafficshaper", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured trafficshaper/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"trafficshaper/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
