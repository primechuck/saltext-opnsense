# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense qfeeds state wrappers.

Generated from controllers.json for module qfeeds.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_qfeeds"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def events_present(name, data=None, match=None, reconfigure="qfeeds/settings/reconfigure", search_field=None):
    """
    Ensure events settings present in qfeeds.

    Wraps opnsense.item_present for /api/qfeeds/settings/searchEvents

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default qfeeds/settings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "qfeeds", "settings", "events", data, match=match, reconfigure=reconfigure, search_field=search_field)


def events_absent(name, match=None, reconfigure="qfeeds/settings/reconfigure", search_field=None):
    """
    Ensure events settings absent in qfeeds.

    Wraps opnsense.item_absent for /api/qfeeds/settings/searchEvents

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "qfeeds", "settings", "events", match=match, reconfigure=reconfigure, search_field=search_field)


def feeds_present(name, data=None, match=None, reconfigure="qfeeds/settings/reconfigure", search_field=None):
    """
    Ensure feeds settings present in qfeeds.

    Wraps opnsense.item_present for /api/qfeeds/settings/searchFeeds

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default qfeeds/settings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "qfeeds", "settings", "feeds", data, match=match, reconfigure=reconfigure, search_field=search_field)


def feeds_absent(name, match=None, reconfigure="qfeeds/settings/reconfigure", search_field=None):
    """
    Ensure feeds settings absent in qfeeds.

    Wraps opnsense.item_absent for /api/qfeeds/settings/searchFeeds

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "qfeeds", "settings", "feeds", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="settings", action="reconfigure"):
    """
    Trigger reconfigure for qfeeds.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("qfeeds", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured qfeeds/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"qfeeds/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
