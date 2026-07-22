# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense postfix state wrappers.

Generated from controllers.json for module postfix.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_postfix"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- address controller ---

def address_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure address address present in postfix.

    Wraps opnsense.item_present for /api/postfix/address/searchAddress

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "address", "address", data, match=match, reconfigure=reconfigure, search_field=search_field)


def address_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure address address absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/address/searchAddress

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "address", "address", match=match, reconfigure=reconfigure, search_field=search_field)


# --- domain controller ---

def domain_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure domain domain present in postfix.

    Wraps opnsense.item_present for /api/postfix/domain/searchDomain

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "domain", "domain", data, match=match, reconfigure=reconfigure, search_field=search_field)


def domain_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure domain domain absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/domain/searchDomain

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "domain", "domain", match=match, reconfigure=reconfigure, search_field=search_field)


# --- headerchecks controller ---

def headercheck_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure headercheck headerchecks present in postfix.

    Wraps opnsense.item_present for /api/postfix/headerchecks/searchHeadercheck

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "headerchecks", "headercheck", data, match=match, reconfigure=reconfigure, search_field=search_field)


def headercheck_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure headercheck headerchecks absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/headerchecks/searchHeadercheck

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "headerchecks", "headercheck", match=match, reconfigure=reconfigure, search_field=search_field)


def headerchecks_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure headerchecks headerchecks present in postfix.

    Wraps opnsense.item_present for /api/postfix/headerchecks/searchHeaderchecks

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "headerchecks", "headerchecks", data, match=match, reconfigure=reconfigure, search_field=search_field)


def headerchecks_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure headerchecks headerchecks absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/headerchecks/searchHeaderchecks

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "headerchecks", "headerchecks", match=match, reconfigure=reconfigure, search_field=search_field)


# --- recipient controller ---

def recipient_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure recipient recipient present in postfix.

    Wraps opnsense.item_present for /api/postfix/recipient/searchRecipient

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "recipient", "recipient", data, match=match, reconfigure=reconfigure, search_field=search_field)


def recipient_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure recipient recipient absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/recipient/searchRecipient

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "recipient", "recipient", match=match, reconfigure=reconfigure, search_field=search_field)


# --- recipientbcc controller ---

def recipientbcc_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure recipientbcc recipientbcc present in postfix.

    Wraps opnsense.item_present for /api/postfix/recipientbcc/searchRecipientbcc

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "recipientbcc", "recipientbcc", data, match=match, reconfigure=reconfigure, search_field=search_field)


def recipientbcc_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure recipientbcc recipientbcc absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/recipientbcc/searchRecipientbcc

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "recipientbcc", "recipientbcc", match=match, reconfigure=reconfigure, search_field=search_field)


# --- sender controller ---

def sender_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure sender sender present in postfix.

    Wraps opnsense.item_present for /api/postfix/sender/searchSender

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "sender", "sender", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sender_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure sender sender absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/sender/searchSender

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "sender", "sender", match=match, reconfigure=reconfigure, search_field=search_field)


# --- senderbcc controller ---

def senderbcc_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure senderbcc senderbcc present in postfix.

    Wraps opnsense.item_present for /api/postfix/senderbcc/searchSenderbcc

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "senderbcc", "senderbcc", data, match=match, reconfigure=reconfigure, search_field=search_field)


def senderbcc_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure senderbcc senderbcc absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/senderbcc/searchSenderbcc

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "senderbcc", "senderbcc", match=match, reconfigure=reconfigure, search_field=search_field)


# --- sendercanonical controller ---

def sendercanonical_present(name, data=None, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure sendercanonical sendercanonical present in postfix.

    Wraps opnsense.item_present for /api/postfix/sendercanonical/searchSendercanonical

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default postfix/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "postfix", "sendercanonical", "sendercanonical", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sendercanonical_absent(name, match=None, reconfigure="postfix/service/reconfigure", search_field=None):
    """
    Ensure sendercanonical sendercanonical absent in postfix.

    Wraps opnsense.item_absent for /api/postfix/sendercanonical/searchSendercanonical

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "postfix", "sendercanonical", "sendercanonical", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for postfix.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("postfix", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured postfix/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"postfix/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
