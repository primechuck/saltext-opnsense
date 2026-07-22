# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense bind state wrappers.

Generated from controllers.json for module bind.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_bind"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- acl controller ---

def acl_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure acl acl present in bind.

    Wraps opnsense.item_present for /api/bind/acl/searchAcl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "acl", "acl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def acl_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure acl acl absent in bind.

    Wraps opnsense.item_absent for /api/bind/acl/searchAcl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "acl", "acl", match=match, reconfigure=reconfigure, search_field=search_field)


# --- domain controller ---

def domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure domain domain present in bind.

    Wraps opnsense.item_present for /api/bind/domain/searchDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "domain", "domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure domain domain absent in bind.

    Wraps opnsense.item_absent for /api/bind/domain/searchDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "domain", "domain", match=match, reconfigure=reconfigure, search_field=search_field)


def forward_domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure forward_domain domain present in bind.

    Wraps opnsense.item_present for /api/bind/domain/searchForwardDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "domain", "forward_domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def forward_domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure forward_domain domain absent in bind.

    Wraps opnsense.item_absent for /api/bind/domain/searchForwardDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "domain", "forward_domain", match=match, reconfigure=reconfigure, search_field=search_field)


def master_domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure master_domain domain present in bind.

    Wraps opnsense.item_present for /api/bind/domain/searchMasterDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "domain", "master_domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def master_domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure master_domain domain absent in bind.

    Wraps opnsense.item_absent for /api/bind/domain/searchMasterDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "domain", "master_domain", match=match, reconfigure=reconfigure, search_field=search_field)


def primary_domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure primary_domain domain present in bind.

    Wraps opnsense.item_present for /api/bind/domain/searchPrimaryDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "domain", "primary_domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def primary_domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure primary_domain domain absent in bind.

    Wraps opnsense.item_absent for /api/bind/domain/searchPrimaryDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "domain", "primary_domain", match=match, reconfigure=reconfigure, search_field=search_field)


def secondary_domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure secondary_domain domain present in bind.

    Wraps opnsense.item_present for /api/bind/domain/searchSecondaryDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "domain", "secondary_domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def secondary_domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure secondary_domain domain absent in bind.

    Wraps opnsense.item_absent for /api/bind/domain/searchSecondaryDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "domain", "secondary_domain", match=match, reconfigure=reconfigure, search_field=search_field)


def slave_domain_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure slave_domain domain present in bind.

    Wraps opnsense.item_present for /api/bind/domain/searchSlaveDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "domain", "slave_domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def slave_domain_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure slave_domain domain absent in bind.

    Wraps opnsense.item_absent for /api/bind/domain/searchSlaveDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "domain", "slave_domain", match=match, reconfigure=reconfigure, search_field=search_field)


# --- record controller ---

def record_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure record record present in bind.

    Wraps opnsense.item_present for /api/bind/record/searchRecord

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "bind", "record", "record", data, match=match, reconfigure=reconfigure, search_field=search_field)


def record_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure record record absent in bind.

    Wraps opnsense.item_absent for /api/bind/record/searchRecord

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "bind", "record", "record", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="acl", action="reconfigure"):
    """
    Trigger reconfigure for bind.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("bind", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured bind/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"bind/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
