# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense radvd state wrappers.

Generated from controllers.json for module radvd.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_radvd"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def entry_present(name, data=None, match=None, reconfigure="radvd/service/reconfigure", search_field=None):
    """
    Ensure entry settings present in radvd.

    Wraps opnsense.item_present for /api/radvd/settings/searchEntry

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default radvd/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "radvd", "settings", "entry", data, match=match, reconfigure=reconfigure, search_field=search_field)


def entry_absent(name, match=None, reconfigure="radvd/service/reconfigure", search_field=None):
    """
    Ensure entry settings absent in radvd.

    Wraps opnsense.item_absent for /api/radvd/settings/searchEntry

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "radvd", "settings", "entry", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for radvd.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("radvd", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured radvd/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"radvd/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
