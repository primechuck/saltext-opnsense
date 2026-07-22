# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense haproxy state wrappers.

Generated from controllers.json for module haproxy.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_haproxy"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- maintenance controller ---

def certificate_diff_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure certificate_diff maintenance present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/maintenance/searchCertificateDiff

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "maintenance", "certificate_diff", data, match=match, reconfigure=reconfigure, search_field=search_field)


def certificate_diff_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure certificate_diff maintenance absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/maintenance/searchCertificateDiff

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "maintenance", "certificate_diff", match=match, reconfigure=reconfigure, search_field=search_field)


def maintenance_server_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure server maintenance present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/maintenance/searchServer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "maintenance", "server", data, match=match, reconfigure=reconfigure, search_field=search_field)


def maintenance_server_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure server maintenance absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/maintenance/searchServer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "maintenance", "server", match=match, reconfigure=reconfigure, search_field=search_field)


# --- settings controller ---

def acl_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure acl settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchAcl

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "acl", data, match=match, reconfigure=reconfigure, search_field=search_field)


def acl_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure acl settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchAcl

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "acl", match=match, reconfigure=reconfigure, search_field=search_field)


def acls_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure acls settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchAcls

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "acls", data, match=match, reconfigure=reconfigure, search_field=search_field)


def acls_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure acls settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchAcls

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "acls", match=match, reconfigure=reconfigure, search_field=search_field)


def action_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure action settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchAction

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "action", data, match=match, reconfigure=reconfigure, search_field=search_field)


def action_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure action settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchAction

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "action", match=match, reconfigure=reconfigure, search_field=search_field)


def actions_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure actions settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchActions

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "actions", data, match=match, reconfigure=reconfigure, search_field=search_field)


def actions_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure actions settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchActions

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "actions", match=match, reconfigure=reconfigure, search_field=search_field)


def backend_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure backend settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchBackend

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "backend", data, match=match, reconfigure=reconfigure, search_field=search_field)


def backend_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure backend settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchBackend

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "backend", match=match, reconfigure=reconfigure, search_field=search_field)


def backends_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure backends settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchBackends

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "backends", data, match=match, reconfigure=reconfigure, search_field=search_field)


def backends_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure backends settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchBackends

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "backends", match=match, reconfigure=reconfigure, search_field=search_field)


def cpu_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure cpu settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchCpu

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "cpu", data, match=match, reconfigure=reconfigure, search_field=search_field)


def cpu_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure cpu settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchCpu

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "cpu", match=match, reconfigure=reconfigure, search_field=search_field)


def cpus_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure cpus settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchCpus

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "cpus", data, match=match, reconfigure=reconfigure, search_field=search_field)


def cpus_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure cpus settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchCpus

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "cpus", match=match, reconfigure=reconfigure, search_field=search_field)


def errorfile_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure errorfile settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchErrorfile

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "errorfile", data, match=match, reconfigure=reconfigure, search_field=search_field)


def errorfile_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure errorfile settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchErrorfile

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "errorfile", match=match, reconfigure=reconfigure, search_field=search_field)


def errorfiles_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure errorfiles settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchErrorfiles

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "errorfiles", data, match=match, reconfigure=reconfigure, search_field=search_field)


def errorfiles_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure errorfiles settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchErrorfiles

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "errorfiles", match=match, reconfigure=reconfigure, search_field=search_field)


def fcgi_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure fcgi settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchFcgi

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "fcgi", data, match=match, reconfigure=reconfigure, search_field=search_field)


def fcgi_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure fcgi settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchFcgi

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "fcgi", match=match, reconfigure=reconfigure, search_field=search_field)


def fcgis_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure fcgis settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchFcgis

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "fcgis", data, match=match, reconfigure=reconfigure, search_field=search_field)


def fcgis_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure fcgis settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchFcgis

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "fcgis", match=match, reconfigure=reconfigure, search_field=search_field)


def frontend_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure frontend settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchFrontend

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "frontend", data, match=match, reconfigure=reconfigure, search_field=search_field)


def frontend_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure frontend settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchFrontend

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "frontend", match=match, reconfigure=reconfigure, search_field=search_field)


def frontends_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure frontends settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchFrontends

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "frontends", data, match=match, reconfigure=reconfigure, search_field=search_field)


def frontends_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure frontends settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchFrontends

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "frontends", match=match, reconfigure=reconfigure, search_field=search_field)


def group_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure group settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchGroup

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "group", data, match=match, reconfigure=reconfigure, search_field=search_field)


def group_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure group settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchGroup

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "group", match=match, reconfigure=reconfigure, search_field=search_field)


def groups_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure groups settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchGroups

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "groups", data, match=match, reconfigure=reconfigure, search_field=search_field)


def groups_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure groups settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchGroups

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "groups", match=match, reconfigure=reconfigure, search_field=search_field)


def healthcheck_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure healthcheck settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchHealthcheck

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "healthcheck", data, match=match, reconfigure=reconfigure, search_field=search_field)


def healthcheck_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure healthcheck settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchHealthcheck

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "healthcheck", match=match, reconfigure=reconfigure, search_field=search_field)


def healthchecks_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure healthchecks settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchHealthchecks

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "healthchecks", data, match=match, reconfigure=reconfigure, search_field=search_field)


def healthchecks_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure healthchecks settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchHealthchecks

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "healthchecks", match=match, reconfigure=reconfigure, search_field=search_field)


def lua_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure lua settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchLua

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "lua", data, match=match, reconfigure=reconfigure, search_field=search_field)


def lua_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure lua settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchLua

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "lua", match=match, reconfigure=reconfigure, search_field=search_field)


def luas_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure luas settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchLuas

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "luas", data, match=match, reconfigure=reconfigure, search_field=search_field)


def luas_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure luas settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchLuas

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "luas", match=match, reconfigure=reconfigure, search_field=search_field)


def mailer_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure mailer settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchmailer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "mailer", data, match=match, reconfigure=reconfigure, search_field=search_field)


def mailer_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure mailer settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchmailer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "mailer", match=match, reconfigure=reconfigure, search_field=search_field)


def mailers_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure mailers settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchmailers

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "mailers", data, match=match, reconfigure=reconfigure, search_field=search_field)


def mailers_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure mailers settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchmailers

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "mailers", match=match, reconfigure=reconfigure, search_field=search_field)


def mapfile_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure mapfile settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchMapfile

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "mapfile", data, match=match, reconfigure=reconfigure, search_field=search_field)


def mapfile_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure mapfile settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchMapfile

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "mapfile", match=match, reconfigure=reconfigure, search_field=search_field)


def mapfiles_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure mapfiles settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchMapfiles

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "mapfiles", data, match=match, reconfigure=reconfigure, search_field=search_field)


def mapfiles_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure mapfiles settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchMapfiles

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "mapfiles", match=match, reconfigure=reconfigure, search_field=search_field)


def resolver_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure resolver settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchresolver

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "resolver", data, match=match, reconfigure=reconfigure, search_field=search_field)


def resolver_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure resolver settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchresolver

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "resolver", match=match, reconfigure=reconfigure, search_field=search_field)


def resolvers_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure resolvers settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchresolvers

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "resolvers", data, match=match, reconfigure=reconfigure, search_field=search_field)


def resolvers_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure resolvers settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchresolvers

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "resolvers", match=match, reconfigure=reconfigure, search_field=search_field)


def settings_server_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure server settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchServer

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "server", data, match=match, reconfigure=reconfigure, search_field=search_field)


def settings_server_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure server settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchServer

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "server", match=match, reconfigure=reconfigure, search_field=search_field)


def servers_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure servers settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchServers

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "servers", data, match=match, reconfigure=reconfigure, search_field=search_field)


def servers_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure servers settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchServers

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "servers", match=match, reconfigure=reconfigure, search_field=search_field)


def user_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure user settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchUser

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "user", data, match=match, reconfigure=reconfigure, search_field=search_field)


def user_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure user settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchUser

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "user", match=match, reconfigure=reconfigure, search_field=search_field)


def users_present(name, data=None, match=None, reconfigure=None, search_field=None):
    """
    Ensure users settings present in haproxy.

    Wraps opnsense.item_present for /api/haproxy/settings/searchUsers

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default None
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "haproxy", "settings", "users", data, match=match, reconfigure=reconfigure, search_field=search_field)


def users_absent(name, match=None, reconfigure=None, search_field=None):
    """
    Ensure users settings absent in haproxy.

    Wraps opnsense.item_absent for /api/haproxy/settings/searchUsers

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "haproxy", "settings", "users", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="export", action="reconfigure"):
    """
    Trigger reconfigure for haproxy.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("haproxy", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured haproxy/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"haproxy/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
