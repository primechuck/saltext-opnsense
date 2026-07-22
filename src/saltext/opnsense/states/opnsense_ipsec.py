# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ipsec state wrappers.

Generated from controllers.json for module ipsec.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ipsec"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- connections controller ---

def child_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure child connections present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/connections/searchChild

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "connections", "child", data, match=match, reconfigure=reconfigure, search_field=search_field)


def child_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure child connections absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/connections/searchChild

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "connections", "child", match=match, reconfigure=reconfigure, search_field=search_field)


def connection_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure connection connections present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/connections/searchConnection

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "connections", "connection", data, match=match, reconfigure=reconfigure, search_field=search_field)


def connection_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure connection connections absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/connections/searchConnection

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "connections", "connection", match=match, reconfigure=reconfigure, search_field=search_field)


def local_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure local connections present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/connections/searchLocal

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "connections", "local", data, match=match, reconfigure=reconfigure, search_field=search_field)


def local_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure local connections absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/connections/searchLocal

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "connections", "local", match=match, reconfigure=reconfigure, search_field=search_field)


def remote_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure remote connections present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/connections/searchRemote

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "connections", "remote", data, match=match, reconfigure=reconfigure, search_field=search_field)


def remote_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure remote connections absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/connections/searchRemote

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "connections", "remote", match=match, reconfigure=reconfigure, search_field=search_field)


# --- keypairs controller ---

def keypairs_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item keypairs present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/keypairs/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "keypairs", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def keypairs_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item keypairs absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/keypairs/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "keypairs", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- leases controller ---

def lease_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/leases/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "leases", "lease", data, match=match, reconfigure=reconfigure, search_field=search_field)


def lease_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure lease leases absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/leases/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "leases", "lease", match=match, reconfigure=reconfigure, search_field=search_field)


# --- manualspd controller ---

def manualspd_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure manualspd manualspd present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/manualspd/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "manualspd", "manualspd", data, match=match, reconfigure=reconfigure, search_field=search_field)


def manualspd_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure manualspd manualspd absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/manualspd/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "manualspd", "manualspd", match=match, reconfigure=reconfigure, search_field=search_field)


# --- pools controller ---

def pool_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure pool pools present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/pools/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "pools", "pool", data, match=match, reconfigure=reconfigure, search_field=search_field)


def pool_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure pool pools absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/pools/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "pools", "pool", match=match, reconfigure=reconfigure, search_field=search_field)


# --- presharedkeys controller ---

def presharedkeys_item_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure item presharedkeys present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/presharedkeys/searchItem

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "presharedkeys", "item", data, match=match, reconfigure=reconfigure, search_field=search_field)


def presharedkeys_item_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure item presharedkeys absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/presharedkeys/searchItem

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "presharedkeys", "item", match=match, reconfigure=reconfigure, search_field=search_field)


# --- sad controller ---

def sad_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure sad sad present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/sad/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "sad", "sad", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sad_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure sad sad absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/sad/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "sad", "sad", match=match, reconfigure=reconfigure, search_field=search_field)


# --- sessions controller ---

def sessions_phase1_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase1 sessions present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/sessions/searchPhase1

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "sessions", "phase1", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sessions_phase1_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase1 sessions absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/sessions/searchPhase1

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "sessions", "phase1", match=match, reconfigure=reconfigure, search_field=search_field)


def sessions_phase2_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase2 sessions present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/sessions/searchPhase2

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "sessions", "phase2", data, match=match, reconfigure=reconfigure, search_field=search_field)


def sessions_phase2_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase2 sessions absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/sessions/searchPhase2

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "sessions", "phase2", match=match, reconfigure=reconfigure, search_field=search_field)


# --- spd controller ---

def spd_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure spd spd present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/spd/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "spd", "spd", data, match=match, reconfigure=reconfigure, search_field=search_field)


def spd_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure spd spd absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/spd/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "spd", "spd", match=match, reconfigure=reconfigure, search_field=search_field)


# --- tunnel controller ---

def tunnel_phase1_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase1 tunnel present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/tunnel/searchPhase1

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "tunnel", "phase1", data, match=match, reconfigure=reconfigure, search_field=search_field)


def tunnel_phase1_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase1 tunnel absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/tunnel/searchPhase1

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "tunnel", "phase1", match=match, reconfigure=reconfigure, search_field=search_field)


def tunnel_phase2_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase2 tunnel present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/tunnel/searchPhase2

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "tunnel", "phase2", data, match=match, reconfigure=reconfigure, search_field=search_field)


def tunnel_phase2_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure phase2 tunnel absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/tunnel/searchPhase2

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "tunnel", "phase2", match=match, reconfigure=reconfigure, search_field=search_field)


# --- vti controller ---

def vti_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure vti vti present in ipsec.

    Wraps opnsense.item_present for /api/ipsec/vti/search

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "ipsec", "vti", "vti", data, match=match, reconfigure=reconfigure, search_field=search_field)


def vti_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure vti vti absent in ipsec.

    Wraps opnsense.item_absent for /api/ipsec/vti/search

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "ipsec", "vti", "vti", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="connections", action="reconfigure"):
    """
    Trigger reconfigure for ipsec.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("ipsec", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured ipsec/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"ipsec/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
