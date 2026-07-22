# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense freeradius state wrappers.

Generated from controllers.json for module freeradius.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_freeradius"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- avpair controller ---

def avpair_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure avpair avpair present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/avpair/searchAvpair

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "avpair", "avpair", data, match=match, reconfigure=reconfigure, search_field=search_field)


def avpair_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure avpair avpair absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/avpair/searchAvpair

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "avpair", "avpair", match=match, reconfigure=reconfigure, search_field=search_field)


# --- client controller ---

def client_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure client client present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/client/searchClient

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "client", "client", data, match=match, reconfigure=reconfigure, search_field=search_field)


def client_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure client client absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/client/searchClient

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "client", "client", match=match, reconfigure=reconfigure, search_field=search_field)


# --- dhcp controller ---

def dhcp_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure dhcp dhcp present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/dhcp/searchDhcp

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "dhcp", "dhcp", data, match=match, reconfigure=reconfigure, search_field=search_field)


def dhcp_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure dhcp dhcp absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/dhcp/searchDhcp

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "dhcp", "dhcp", match=match, reconfigure=reconfigure, search_field=search_field)


# --- ldapgroup controller ---

def ldapgroup_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure ldapgroup ldapgroup present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/ldapgroup/searchLdapgroup

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "ldapgroup", "ldapgroup", data, match=match, reconfigure=reconfigure, search_field=search_field)


def ldapgroup_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure ldapgroup ldapgroup absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/ldapgroup/searchLdapgroup

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "ldapgroup", "ldapgroup", match=match, reconfigure=reconfigure, search_field=search_field)


# --- lease controller ---

def lease_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure lease lease present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/lease/searchLease

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "lease", "lease", data, match=match, reconfigure=reconfigure, search_field=search_field)


def lease_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure lease lease absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/lease/searchLease

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "lease", "lease", match=match, reconfigure=reconfigure, search_field=search_field)


# --- proxy controller ---

def homeserver_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure homeserver proxy present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/proxy/searchHomeserver

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "proxy", "homeserver", data, match=match, reconfigure=reconfigure, search_field=search_field)


def homeserver_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure homeserver proxy absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/proxy/searchHomeserver

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "proxy", "homeserver", match=match, reconfigure=reconfigure, search_field=search_field)


def homeserverpool_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure homeserverpool proxy present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/proxy/searchHomeserverpool

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "proxy", "homeserverpool", data, match=match, reconfigure=reconfigure, search_field=search_field)


def homeserverpool_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure homeserverpool proxy absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/proxy/searchHomeserverpool

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "proxy", "homeserverpool", match=match, reconfigure=reconfigure, search_field=search_field)


def realm_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure realm proxy present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/proxy/searchRealm

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "proxy", "realm", data, match=match, reconfigure=reconfigure, search_field=search_field)


def realm_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure realm proxy absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/proxy/searchRealm

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "proxy", "realm", match=match, reconfigure=reconfigure, search_field=search_field)


# --- user controller ---

def user_present(name, data=None, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure user user present in freeradius.

    Wraps opnsense.item_present for /api/freeradius/user/searchUser

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default freeradius/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "freeradius", "user", "user", data, match=match, reconfigure=reconfigure, search_field=search_field)


def user_absent(name, match=None, reconfigure="freeradius/service/reconfigure", search_field=None):
    """
    Ensure user user absent in freeradius.

    Wraps opnsense.item_absent for /api/freeradius/user/searchUser

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "freeradius", "user", "user", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for freeradius.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("freeradius", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured freeradius/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"freeradius/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
