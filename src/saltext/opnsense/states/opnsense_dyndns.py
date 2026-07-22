# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense dyndns state wrappers.

Generated from controllers.json for module dyndns.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_dyndns"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- accounts controller ---

def item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item accounts present in dyndns.

    Wraps opnsense.item_present for /api/dyndns/accounts/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "dyndns", "accounts", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item accounts absent in dyndns.

    Wraps opnsense.item_absent for /api/dyndns/accounts/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "dyndns", "accounts", "item", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="accounts", action="reconfigure"):
    """
    Trigger reconfigure for dyndns.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("dyndns", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured dyndns/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"dyndns/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
