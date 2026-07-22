# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense auth state wrappers.

Generated from controllers.json for module auth.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_auth"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- group controller ---

def group_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure group group present in auth.

    Wraps opnsense.item_present for /api/auth/group/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "auth", "group", "group", data, match=match, reconfigure=reconfigure, search_field=search_field)


def group_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure group group absent in auth.

    Wraps opnsense.item_absent for /api/auth/group/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "auth", "group", "group", match=match, reconfigure=reconfigure, search_field=search_field)


# --- priv controller ---

def item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item priv present in auth.

    Wraps opnsense.item_present for /api/auth/priv/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "auth", "priv", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item priv absent in auth.

    Wraps opnsense.item_absent for /api/auth/priv/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "auth", "priv", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- user controller ---

def api_key_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure api_key user present in auth.

    Wraps opnsense.item_present for /api/auth/user/searchApiKey

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "auth", "user", "api_key", data, match=match, reconfigure=reconfigure, search_field=search_field)


def api_key_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure api_key user absent in auth.

    Wraps opnsense.item_absent for /api/auth/user/searchApiKey

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "auth", "user", "api_key", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="group", action="reconfigure"):
    """
    Trigger reconfigure for auth.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("auth", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured auth/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"auth/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
