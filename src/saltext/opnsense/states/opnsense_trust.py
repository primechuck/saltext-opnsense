# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense trust state wrappers.

Generated from controllers.json for module trust.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_trust"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- ca controller ---

def ca_present(name, data=None, match=None, reconfigure="trust/settings/reconfigure", search_field=None):
    """
    Ensure ca ca present in trust.

    Wraps opnsense.item_present for /api/trust/ca/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trust/settings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trust", "ca", "ca", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ca_absent(name, match=None, reconfigure="trust/settings/reconfigure", search_field=None):
    """
    Ensure ca ca absent in trust.

    Wraps opnsense.item_absent for /api/trust/ca/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trust", "ca", "ca", match=match, reconfigure=reconfigure, search_field=search_field)


# --- cert controller ---

def cert_present(name, data=None, match=None, reconfigure="trust/settings/reconfigure", search_field=None):
    """
    Ensure cert cert present in trust.

    Wraps opnsense.item_present for /api/trust/cert/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trust/settings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trust", "cert", "cert", data, match=match, reconfigure=reconfigure, search_field=search_field)


def cert_absent(name, match=None, reconfigure="trust/settings/reconfigure", search_field=None):
    """
    Ensure cert cert absent in trust.

    Wraps opnsense.item_absent for /api/trust/cert/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trust", "cert", "cert", match=match, reconfigure=reconfigure, search_field=search_field)


# --- crl controller ---

def crl_present(name, data=None, match=None, reconfigure="trust/settings/reconfigure", search_field=None):
    """
    Ensure crl crl present in trust.

    Wraps opnsense.item_present for /api/trust/crl/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default trust/settings/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "trust", "crl", "crl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def crl_absent(name, match=None, reconfigure="trust/settings/reconfigure", search_field=None):
    """
    Ensure crl crl absent in trust.

    Wraps opnsense.item_absent for /api/trust/crl/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "trust", "crl", "crl", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="ca", action="reconfigure"):
    """
    Trigger reconfigure for trust.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("trust", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured trust/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"trust/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
