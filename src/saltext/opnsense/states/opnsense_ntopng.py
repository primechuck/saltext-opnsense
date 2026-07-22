# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ntopng state wrappers.

Generated from controllers.json for module ntopng.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ntopng"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for ntopng.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("ntopng", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured ntopng/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"ntopng/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
