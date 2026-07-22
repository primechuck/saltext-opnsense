# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense siproxd state wrappers.

Generated from controllers.json for module siproxd.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_siproxd"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- domain controller ---

def domain_present(name, data=None, match=None, reconfigure="siproxd/service/reconfigure", search_field=None):
    """
    Ensure domain domain present in siproxd.

    Wraps opnsense.item_present for /api/siproxd/domain/searchDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default siproxd/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "siproxd", "domain", "domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def domain_absent(name, match=None, reconfigure="siproxd/service/reconfigure", search_field=None):
    """
    Ensure domain domain absent in siproxd.

    Wraps opnsense.item_absent for /api/siproxd/domain/searchDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "siproxd", "domain", "domain", match=match, reconfigure=reconfigure, search_field=search_field)


# --- user controller ---

def user_present(name, data=None, match=None, reconfigure="siproxd/service/reconfigure", search_field=None):
    """
    Ensure user user present in siproxd.

    Wraps opnsense.item_present for /api/siproxd/user/searchUser

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default siproxd/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "siproxd", "user", "user", data, match=match, reconfigure=reconfigure, search_field=search_field)


def user_absent(name, match=None, reconfigure="siproxd/service/reconfigure", search_field=None):
    """
    Ensure user user absent in siproxd.

    Wraps opnsense.item_absent for /api/siproxd/user/searchUser

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "siproxd", "user", "user", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for siproxd.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("siproxd", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured siproxd/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"siproxd/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
