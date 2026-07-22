# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense acmeclient state wrappers.

Generated from controllers.json for module acmeclient.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_acmeclient"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- accounts controller ---

def account_present(name, data=None, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure account accounts present in acmeclient.

    Wraps opnsense.item_present for /api/acmeclient/accounts/searchAccount

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default acmeclient/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "acmeclient", "accounts", "account", data, match=match, reconfigure=reconfigure, search_field=search_field)


def account_absent(name, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure account accounts absent in acmeclient.

    Wraps opnsense.item_absent for /api/acmeclient/accounts/searchAccount

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "acmeclient", "accounts", "account", match=match, reconfigure=reconfigure, search_field=search_field)


# --- actions controller ---

def action_present(name, data=None, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure action actions present in acmeclient.

    Wraps opnsense.item_present for /api/acmeclient/actions/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default acmeclient/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "acmeclient", "actions", "action", data, match=match, reconfigure=reconfigure, search_field=search_field)


def action_absent(name, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure action actions absent in acmeclient.

    Wraps opnsense.item_absent for /api/acmeclient/actions/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "acmeclient", "actions", "action", match=match, reconfigure=reconfigure, search_field=search_field)


# --- certificates controller ---

def certificate_present(name, data=None, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure certificate certificates present in acmeclient.

    Wraps opnsense.item_present for /api/acmeclient/certificates/searchCertificate

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default acmeclient/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "acmeclient", "certificates", "certificate", data, match=match, reconfigure=reconfigure, search_field=search_field)


def certificate_absent(name, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure certificate certificates absent in acmeclient.

    Wraps opnsense.item_absent for /api/acmeclient/certificates/searchCertificate

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "acmeclient", "certificates", "certificate", match=match, reconfigure=reconfigure, search_field=search_field)


# --- validations controller ---

def validation_present(name, data=None, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure validation validations present in acmeclient.

    Wraps opnsense.item_present for /api/acmeclient/validations/searchValidation

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default acmeclient/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "acmeclient", "validations", "validation", data, match=match, reconfigure=reconfigure, search_field=search_field)


def validation_absent(name, match=None, reconfigure="acmeclient/service/reconfigure", search_field=None):
    """
    Ensure validation validations absent in acmeclient.

    Wraps opnsense.item_absent for /api/acmeclient/validations/searchValidation

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "acmeclient", "validations", "validation", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for acmeclient.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("acmeclient", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured acmeclient/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"acmeclient/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
