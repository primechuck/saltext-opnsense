# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense telegraf state wrappers.

Generated from controllers.json for module telegraf.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_telegraf"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- key controller ---

def key_present(name, data=None, match=None, reconfigure="telegraf/service/reconfigure", search_field=None):
    """
    Ensure key key present in telegraf.

    Wraps opnsense.item_present for /api/telegraf/key/searchKey

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default telegraf/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "telegraf", "key", "key", data, match=match, reconfigure=reconfigure, search_field=search_field)


def key_absent(name, match=None, reconfigure="telegraf/service/reconfigure", search_field=None):
    """
    Ensure key key absent in telegraf.

    Wraps opnsense.item_absent for /api/telegraf/key/searchKey

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "telegraf", "key", "key", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for telegraf.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("telegraf", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured telegraf/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"telegraf/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
