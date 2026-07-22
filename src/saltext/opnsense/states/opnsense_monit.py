# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense monit state wrappers.

Generated from controllers.json for module monit.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_monit"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def alert_present(name, data=None, match=None, reconfigure="monit/service/reconfigure", search_field=None):
    """
    Ensure alert settings present in monit.

    Wraps opnsense.item_present for /api/monit/settings/searchAlert

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default monit/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "monit", "settings", "alert", data, match=match, reconfigure=reconfigure, search_field=search_field)


def alert_absent(name, match=None, reconfigure="monit/service/reconfigure", search_field=None):
    """
    Ensure alert settings absent in monit.

    Wraps opnsense.item_absent for /api/monit/settings/searchAlert

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "monit", "settings", "alert", match=match, reconfigure=reconfigure, search_field=search_field)


def service_present(name, data=None, match=None, reconfigure="monit/service/reconfigure", search_field=None):
    """
    Ensure service settings present in monit.

    Wraps opnsense.item_present for /api/monit/settings/searchService

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default monit/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "monit", "settings", "service", data, match=match, reconfigure=reconfigure, search_field=search_field)


def service_absent(name, match=None, reconfigure="monit/service/reconfigure", search_field=None):
    """
    Ensure service settings absent in monit.

    Wraps opnsense.item_absent for /api/monit/settings/searchService

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "monit", "settings", "service", match=match, reconfigure=reconfigure, search_field=search_field)


def test_present(name, data=None, match=None, reconfigure="monit/service/reconfigure", search_field=None):
    """
    Ensure test settings present in monit.

    Wraps opnsense.item_present for /api/monit/settings/searchTest

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default monit/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "monit", "settings", "test", data, match=match, reconfigure=reconfigure, search_field=search_field)


def test_absent(name, match=None, reconfigure="monit/service/reconfigure", search_field=None):
    """
    Ensure test settings absent in monit.

    Wraps opnsense.item_absent for /api/monit/settings/searchTest

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "monit", "settings", "test", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for monit.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("monit", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured monit/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"monit/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
