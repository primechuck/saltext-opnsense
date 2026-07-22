# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense haproxy wrappers.

Generated from controllers.json for module haproxy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/haproxy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_haproxy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- export controller ---

def export_config(data=None, uuid=None):
    """
    Execute config in haproxy/export.

    Wraps: /api/haproxy/export/config

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "export", "config", uuid=uuid, data=data)


def export_diff(data=None, uuid=None):
    """
    Execute diff in haproxy/export.

    Wraps: /api/haproxy/export/diff

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "export", "diff", uuid=uuid, data=data)


def export_download(data=None, uuid=None):
    """
    Execute download in haproxy/export.

    Wraps: /api/haproxy/export/download

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "export", "download", uuid=uuid, data=data)


# --- maintenance controller ---

def search_certificate_diff(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search certificate_diff entries in haproxy/maintenance.

    Wraps: POST /api/haproxy/maintenance/searchCertificateDiff

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "maintenance", "certificate_diff", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_maintenance_server(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search server entries in haproxy/maintenance.

    Wraps: POST /api/haproxy/maintenance/searchServer

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "maintenance", "server", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def maintenance_cert_actions(data=None, uuid=None):
    """
    Execute certActions in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/certActions

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "certActions", uuid=uuid, data=data)


def maintenance_cert_diff(data=None, uuid=None):
    """
    Execute certDiff in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/certDiff

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "certDiff", uuid=uuid, data=data)


def maintenance_cert_sync(data=None, uuid=None):
    """
    Execute certSync in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/certSync

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "certSync", uuid=uuid, data=data)


def maintenance_cert_sync_bulk(data=None, uuid=None):
    """
    Execute certSyncBulk in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/certSyncBulk

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "certSyncBulk", uuid=uuid, data=data)


def maintenance_fetch_cron_integration(data=None, uuid=None):
    """
    Execute fetchCronIntegration in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/fetchCronIntegration

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "fetchCronIntegration", uuid=uuid, data=data)


def maintenance_server_state(data=None, uuid=None):
    """
    Execute serverState in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/serverState

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "serverState", uuid=uuid, data=data)


def maintenance_server_state_bulk(data=None, uuid=None):
    """
    Execute serverStateBulk in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/serverStateBulk

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "serverStateBulk", uuid=uuid, data=data)


def maintenance_server_weight(data=None, uuid=None):
    """
    Execute serverWeight in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/serverWeight

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "serverWeight", uuid=uuid, data=data)


def maintenance_server_weight_bulk(data=None, uuid=None):
    """
    Execute serverWeightBulk in haproxy/maintenance.

    Wraps: /api/haproxy/maintenance/serverWeightBulk

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "maintenance", "serverWeightBulk", uuid=uuid, data=data)


# --- service controller ---

def service_configtest(data=None, uuid=None):
    """
    Execute configtest in haproxy/service.

    Wraps: /api/haproxy/service/configtest

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "service", "configtest", uuid=uuid, data=data)


# --- settings controller ---

def get_acl(uuid=None):
    """
    Get acl entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getAcl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "acl", uuid)


def add_acl(data):
    """
    Add acl entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addAcl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "acl", data)


def set_acl(uuid, data):
    """
    Set/update acl entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setAcl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "acl", uuid, data)


def del_acl(uuid):
    """
    Delete acl entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delAcl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "acl", uuid)


def search_acls(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search acls entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchAcls

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "acls", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_action(uuid=None):
    """
    Get action entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getAction/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "action", uuid)


def add_action(data):
    """
    Add action entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addAction

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "action", data)


def set_action(uuid, data):
    """
    Set/update action entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setAction/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "action", uuid, data)


def del_action(uuid):
    """
    Delete action entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delAction/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "action", uuid)


def toggle_action(uuid, enabled=None):
    """
    Toggle action entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleAction/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "action", uuid, enabled)


def search_actions(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search actions entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchActions

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "actions", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_backend(uuid=None):
    """
    Get backend entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getBackend/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "backend", uuid)


def add_backend(data):
    """
    Add backend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addBackend

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "backend", data)


def set_backend(uuid, data):
    """
    Set/update backend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setBackend/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "backend", uuid, data)


def del_backend(uuid):
    """
    Delete backend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delBackend/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "backend", uuid)


def toggle_backend(uuid, enabled=None):
    """
    Toggle backend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleBackend/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "backend", uuid, enabled)


def search_backends(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search backends entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchBackends

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "backends", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_cpu(uuid=None):
    """
    Get cpu entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getCpu/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "cpu", uuid)


def add_cpu(data):
    """
    Add cpu entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addCpu

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "cpu", data)


def set_cpu(uuid, data):
    """
    Set/update cpu entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setCpu/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "cpu", uuid, data)


def del_cpu(uuid):
    """
    Delete cpu entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delCpu/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "cpu", uuid)


def toggle_cpu(uuid, enabled=None):
    """
    Toggle cpu entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleCpu/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "cpu", uuid, enabled)


def search_cpus(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search cpus entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchCpus

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "cpus", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_errorfile(uuid=None):
    """
    Get errorfile entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getErrorfile/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "errorfile", uuid)


def add_errorfile(data):
    """
    Add errorfile entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addErrorfile

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "errorfile", data)


def set_errorfile(uuid, data):
    """
    Set/update errorfile entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setErrorfile/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "errorfile", uuid, data)


def del_errorfile(uuid):
    """
    Delete errorfile entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delErrorfile/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "errorfile", uuid)


def search_errorfiles(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search errorfiles entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchErrorfiles

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "errorfiles", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_fcgi(uuid=None):
    """
    Get fcgi entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getFcgi/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "fcgi", uuid)


def add_fcgi(data):
    """
    Add fcgi entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addFcgi

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "fcgi", data)


def set_fcgi(uuid, data):
    """
    Set/update fcgi entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setFcgi/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "fcgi", uuid, data)


def del_fcgi(uuid):
    """
    Delete fcgi entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delFcgi/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "fcgi", uuid)


def search_fcgis(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search fcgis entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchFcgis

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "fcgis", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_frontend(uuid=None):
    """
    Get frontend entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getFrontend/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "frontend", uuid)


def add_frontend(data):
    """
    Add frontend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addFrontend

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "frontend", data)


def set_frontend(uuid, data):
    """
    Set/update frontend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setFrontend/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "frontend", uuid, data)


def del_frontend(uuid):
    """
    Delete frontend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delFrontend/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "frontend", uuid)


def toggle_frontend(uuid, enabled=None):
    """
    Toggle frontend entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleFrontend/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "frontend", uuid, enabled)


def search_frontends(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search frontends entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchFrontends

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "frontends", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_group(uuid=None):
    """
    Get group entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getGroup/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "group", uuid)


def add_group(data):
    """
    Add group entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addGroup

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "group", data)


def set_group(uuid, data):
    """
    Set/update group entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setGroup/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "group", uuid, data)


def del_group(uuid):
    """
    Delete group entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delGroup/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "group", uuid)


def toggle_group(uuid, enabled=None):
    """
    Toggle group entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleGroup/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "group", uuid, enabled)


def search_groups(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search groups entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchGroups

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "groups", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_healthcheck(uuid=None):
    """
    Get healthcheck entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getHealthcheck/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "healthcheck", uuid)


def add_healthcheck(data):
    """
    Add healthcheck entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addHealthcheck

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "healthcheck", data)


def set_healthcheck(uuid, data):
    """
    Set/update healthcheck entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setHealthcheck/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "healthcheck", uuid, data)


def del_healthcheck(uuid):
    """
    Delete healthcheck entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delHealthcheck/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "healthcheck", uuid)


def search_healthchecks(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search healthchecks entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchHealthchecks

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "healthchecks", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_lua(uuid=None):
    """
    Get lua entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getLua/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "lua", uuid)


def add_lua(data):
    """
    Add lua entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addLua

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "lua", data)


def set_lua(uuid, data):
    """
    Set/update lua entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setLua/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "lua", uuid, data)


def del_lua(uuid):
    """
    Delete lua entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delLua/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "lua", uuid)


def toggle_lua(uuid, enabled=None):
    """
    Toggle lua entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleLua/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "lua", uuid, enabled)


def search_luas(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search luas entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchLuas

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "luas", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_mailer(uuid=None):
    """
    Get mailer entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getmailer/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "mailer", uuid)


def add_mailer(data):
    """
    Add mailer entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addmailer

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "mailer", data)


def set_mailer(uuid, data):
    """
    Set/update mailer entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setmailer/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "mailer", uuid, data)


def del_mailer(uuid):
    """
    Delete mailer entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delmailer/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "mailer", uuid)


def toggle_mailer(uuid, enabled=None):
    """
    Toggle mailer entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/togglemailer/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "mailer", uuid, enabled)


def search_mailers(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search mailers entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchmailers

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "mailers", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_mapfile(uuid=None):
    """
    Get mapfile entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getMapfile/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "mapfile", uuid)


def add_mapfile(data):
    """
    Add mapfile entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addMapfile

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "mapfile", data)


def set_mapfile(uuid, data):
    """
    Set/update mapfile entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setMapfile/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "mapfile", uuid, data)


def del_mapfile(uuid):
    """
    Delete mapfile entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delMapfile/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "mapfile", uuid)


def search_mapfiles(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search mapfiles entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchMapfiles

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "mapfiles", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_resolver(uuid=None):
    """
    Get resolver entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getresolver/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "resolver", uuid)


def add_resolver(data):
    """
    Add resolver entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addresolver

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "resolver", data)


def set_resolver(uuid, data):
    """
    Set/update resolver entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setresolver/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "resolver", uuid, data)


def del_resolver(uuid):
    """
    Delete resolver entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delresolver/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "resolver", uuid)


def toggle_resolver(uuid, enabled=None):
    """
    Toggle resolver entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleresolver/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "resolver", uuid, enabled)


def search_resolvers(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search resolvers entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchresolvers

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "resolvers", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_settings_server(uuid=None):
    """
    Get server entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getServer/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "server", uuid)


def add_settings_server(data):
    """
    Add server entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addServer

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "server", data)


def set_settings_server(uuid, data):
    """
    Set/update server entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setServer/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "server", uuid, data)


def del_settings_server(uuid):
    """
    Delete server entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delServer/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "server", uuid)


def toggle_settings_server(uuid, enabled=None):
    """
    Toggle server entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleServer/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "server", uuid, enabled)


def search_servers(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search servers entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchServers

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "servers", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_user(uuid=None):
    """
    Get user entry in haproxy/settings.

    Wraps: GET /api/haproxy/settings/getUser/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("haproxy", "settings", "user", uuid)


def add_user(data):
    """
    Add user entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/addUser

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("haproxy", "settings", "user", data)


def set_user(uuid, data):
    """
    Set/update user entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/setUser/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("haproxy", "settings", "user", uuid, data)


def del_user(uuid):
    """
    Delete user entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/delUser/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("haproxy", "settings", "user", uuid)


def toggle_user(uuid, enabled=None):
    """
    Toggle user entry in haproxy/settings.

    Wraps: POST /api/haproxy/settings/toggleUser/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("haproxy", "settings", "user", uuid, enabled)


def search_users(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search users entries in haproxy/settings.

    Wraps: POST /api/haproxy/settings/searchUsers

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("haproxy", "settings", "users", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- statistics controller ---

def statistics_counters(data=None, uuid=None):
    """
    Execute counters in haproxy/statistics.

    Wraps: /api/haproxy/statistics/counters

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "statistics", "counters", uuid=uuid, data=data)


def statistics_info(data=None, uuid=None):
    """
    Execute info in haproxy/statistics.

    Wraps: /api/haproxy/statistics/info

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "statistics", "info", uuid=uuid, data=data)


def statistics_tables(data=None, uuid=None):
    """
    Execute tables in haproxy/statistics.

    Wraps: /api/haproxy/statistics/tables

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("haproxy", "statistics", "tables", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="export", action="reconfigure", data=None):
    """
    Generic reconfigure for haproxy.

    Wraps: POST /api/haproxy/{controller}/{action}

    :param controller: Controller name, default export
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("haproxy", controller, action, data)
