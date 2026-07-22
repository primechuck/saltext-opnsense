# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense ipsec wrappers.

Generated from controllers.json for module ipsec.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/ipsec/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_ipsec"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- connections controller ---

def search_child(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search child entries in ipsec/connections.

    Wraps: POST /api/ipsec/connections/searchChild

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "connections", "child", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_child(uuid=None):
    """
    Get child entry in ipsec/connections.

    Wraps: GET /api/ipsec/connections/getChild/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "connections", "child", uuid)


def add_child(data):
    """
    Add child entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/addChild

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "connections", "child", data)


def set_child(uuid, data):
    """
    Set/update child entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/setChild/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "connections", "child", uuid, data)


def del_child(uuid):
    """
    Delete child entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/delChild/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "connections", "child", uuid)


def toggle_child(uuid, enabled=None):
    """
    Toggle child entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/toggleChild/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "connections", "child", uuid, enabled)


def search_connection(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search connection entries in ipsec/connections.

    Wraps: POST /api/ipsec/connections/searchConnection

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "connections", "connection", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_connection(uuid=None):
    """
    Get connection entry in ipsec/connections.

    Wraps: GET /api/ipsec/connections/getConnection/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "connections", "connection", uuid)


def add_connection(data):
    """
    Add connection entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/addConnection

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "connections", "connection", data)


def set_connection(uuid, data):
    """
    Set/update connection entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/setConnection/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "connections", "connection", uuid, data)


def del_connection(uuid):
    """
    Delete connection entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/delConnection/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "connections", "connection", uuid)


def toggle_connection(uuid, enabled=None):
    """
    Toggle connection entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/toggleConnection/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "connections", "connection", uuid, enabled)


def search_local(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search local entries in ipsec/connections.

    Wraps: POST /api/ipsec/connections/searchLocal

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "connections", "local", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_local(uuid=None):
    """
    Get local entry in ipsec/connections.

    Wraps: GET /api/ipsec/connections/getLocal/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "connections", "local", uuid)


def add_local(data):
    """
    Add local entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/addLocal

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "connections", "local", data)


def set_local(uuid, data):
    """
    Set/update local entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/setLocal/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "connections", "local", uuid, data)


def del_local(uuid):
    """
    Delete local entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/delLocal/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "connections", "local", uuid)


def toggle_local(uuid, enabled=None):
    """
    Toggle local entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/toggleLocal/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "connections", "local", uuid, enabled)


def search_remote(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search remote entries in ipsec/connections.

    Wraps: POST /api/ipsec/connections/searchRemote

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "connections", "remote", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_remote(uuid=None):
    """
    Get remote entry in ipsec/connections.

    Wraps: GET /api/ipsec/connections/getRemote/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "connections", "remote", uuid)


def add_remote(data):
    """
    Add remote entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/addRemote

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "connections", "remote", data)


def set_remote(uuid, data):
    """
    Set/update remote entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/setRemote/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "connections", "remote", uuid, data)


def del_remote(uuid):
    """
    Delete remote entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/delRemote/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "connections", "remote", uuid)


def toggle_remote(uuid, enabled=None):
    """
    Toggle remote entry in ipsec/connections.

    Wraps: POST /api/ipsec/connections/toggleRemote/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "connections", "remote", uuid, enabled)


def connections_connection_exists(data=None, uuid=None):
    """
    Execute connectionExists in ipsec/connections.

    Wraps: /api/ipsec/connections/connectionExists

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "connections", "connectionExists", uuid=uuid, data=data)


def connections_is_enabled(data=None, uuid=None):
    """
    Execute isEnabled in ipsec/connections.

    Wraps: /api/ipsec/connections/isEnabled

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "connections", "isEnabled", uuid=uuid, data=data)


def connections_swanctl(data=None, uuid=None):
    """
    Execute swanctl in ipsec/connections.

    Wraps: /api/ipsec/connections/swanctl

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "connections", "swanctl", uuid=uuid, data=data)


# --- keypairs controller ---

def search_keypairs_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in ipsec/keypairs.

    Wraps: POST /api/ipsec/keypairs/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "keypairs", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_keypairs_item(uuid=None):
    """
    Get item entry in ipsec/keypairs.

    Wraps: GET /api/ipsec/keypairs/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "keypairs", "item", uuid)


def add_keypairs_item(data):
    """
    Add item entry in ipsec/keypairs.

    Wraps: POST /api/ipsec/keypairs/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "keypairs", "item", data)


def set_keypairs_item(uuid, data):
    """
    Set/update item entry in ipsec/keypairs.

    Wraps: POST /api/ipsec/keypairs/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "keypairs", "item", uuid, data)


def del_keypairs_item(uuid):
    """
    Delete item entry in ipsec/keypairs.

    Wraps: POST /api/ipsec/keypairs/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "keypairs", "item", uuid)


def keypairs_gen_key_pair(data=None, uuid=None):
    """
    Execute genKeyPair in ipsec/keypairs.

    Wraps: /api/ipsec/keypairs/genKeyPair

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "keypairs", "genKeyPair", uuid=uuid, data=data)


# --- leases controller ---

def search_lease(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search lease entries in ipsec/leases.

    Wraps: POST /api/ipsec/leases/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "leases", "lease", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def leases_pools(data=None, uuid=None):
    """
    Execute pools in ipsec/leases.

    Wraps: /api/ipsec/leases/pools

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "leases", "pools", uuid=uuid, data=data)


# --- legacysubsystem controller ---

def legacysubsystem_apply_config(data=None, uuid=None):
    """
    Execute applyConfig in ipsec/legacysubsystem.

    Wraps: /api/ipsec/legacysubsystem/applyConfig

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "legacysubsystem", "applyConfig", uuid=uuid, data=data)


def legacysubsystem_status(data=None):
    """
    Execute status in ipsec/legacysubsystem.

    Wraps: POST /api/ipsec/legacysubsystem/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "legacysubsystem", "status", data=data, method="POST")


# --- manualspd controller ---

def search_manualspd(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search manualspd entries in ipsec/manualspd.

    Wraps: POST /api/ipsec/manualspd/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "manualspd", "manualspd", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_manualspd(uuid=None):
    """
    Get manualspd entry in ipsec/manualspd.

    Wraps: GET /api/ipsec/manualspd/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "manualspd", "manualspd", uuid)


def add_manualspd(data):
    """
    Add manualspd entry in ipsec/manualspd.

    Wraps: POST /api/ipsec/manualspd/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "manualspd", "manualspd", data)


def set_manualspd(uuid, data):
    """
    Set/update manualspd entry in ipsec/manualspd.

    Wraps: POST /api/ipsec/manualspd/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "manualspd", "manualspd", uuid, data)


def del_manualspd(uuid):
    """
    Delete manualspd entry in ipsec/manualspd.

    Wraps: POST /api/ipsec/manualspd/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "manualspd", "manualspd", uuid)


def toggle_manualspd(uuid, enabled=None):
    """
    Toggle manualspd entry in ipsec/manualspd.

    Wraps: POST /api/ipsec/manualspd/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "manualspd", "manualspd", uuid, enabled)


# --- pools controller ---

def search_pool(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search pool entries in ipsec/pools.

    Wraps: POST /api/ipsec/pools/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "pools", "pool", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_pool(uuid=None):
    """
    Get pool entry in ipsec/pools.

    Wraps: GET /api/ipsec/pools/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "pools", "pool", uuid)


def add_pool(data):
    """
    Add pool entry in ipsec/pools.

    Wraps: POST /api/ipsec/pools/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "pools", "pool", data)


def set_pool(uuid, data):
    """
    Set/update pool entry in ipsec/pools.

    Wraps: POST /api/ipsec/pools/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "pools", "pool", uuid, data)


def del_pool(uuid):
    """
    Delete pool entry in ipsec/pools.

    Wraps: POST /api/ipsec/pools/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "pools", "pool", uuid)


def toggle_pool(uuid, enabled=None):
    """
    Toggle pool entry in ipsec/pools.

    Wraps: POST /api/ipsec/pools/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "pools", "pool", uuid, enabled)


# --- presharedkeys controller ---

def search_presharedkeys_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in ipsec/presharedkeys.

    Wraps: POST /api/ipsec/presharedkeys/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "presharedkeys", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_presharedkeys_item(uuid=None):
    """
    Get item entry in ipsec/presharedkeys.

    Wraps: GET /api/ipsec/presharedkeys/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "presharedkeys", "item", uuid)


def add_presharedkeys_item(data):
    """
    Add item entry in ipsec/presharedkeys.

    Wraps: POST /api/ipsec/presharedkeys/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "presharedkeys", "item", data)


def set_presharedkeys_item(uuid, data):
    """
    Set/update item entry in ipsec/presharedkeys.

    Wraps: POST /api/ipsec/presharedkeys/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "presharedkeys", "item", uuid, data)


def del_presharedkeys_item(uuid):
    """
    Delete item entry in ipsec/presharedkeys.

    Wraps: POST /api/ipsec/presharedkeys/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "presharedkeys", "item", uuid)


# --- sad controller ---

def search_sad(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search sad entries in ipsec/sad.

    Wraps: POST /api/ipsec/sad/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "sad", "sad", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def sad_delete(data=None, uuid=None):
    """
    Execute delete in ipsec/sad.

    Wraps: /api/ipsec/sad/delete

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "sad", "delete", uuid=uuid, data=data)


# --- sessions controller ---

def search_sessions_phase1(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search phase1 entries in ipsec/sessions.

    Wraps: POST /api/ipsec/sessions/searchPhase1

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "sessions", "phase1", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_sessions_phase2(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search phase2 entries in ipsec/sessions.

    Wraps: POST /api/ipsec/sessions/searchPhase2

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "sessions", "phase2", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def sessions_connect(data=None, uuid=None):
    """
    Execute connect in ipsec/sessions.

    Wraps: /api/ipsec/sessions/connect

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "sessions", "connect", uuid=uuid, data=data)


def sessions_disconnect(data=None, uuid=None):
    """
    Execute disconnect in ipsec/sessions.

    Wraps: /api/ipsec/sessions/disconnect

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "sessions", "disconnect", uuid=uuid, data=data)


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in ipsec/settings.

    Wraps: GET /api/ipsec/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("ipsec", "settings")


# --- spd controller ---

def search_spd(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search spd entries in ipsec/spd.

    Wraps: POST /api/ipsec/spd/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "spd", "spd", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def spd_delete(data=None, uuid=None):
    """
    Execute delete in ipsec/spd.

    Wraps: /api/ipsec/spd/delete

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "spd", "delete", uuid=uuid, data=data)


# --- tunnel controller ---

def search_tunnel_phase1(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search phase1 entries in ipsec/tunnel.

    Wraps: POST /api/ipsec/tunnel/searchPhase1

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "tunnel", "phase1", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def del_tunnel_phase1(uuid):
    """
    Delete phase1 entry in ipsec/tunnel.

    Wraps: POST /api/ipsec/tunnel/delPhase1/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "tunnel", "phase1", uuid)


def toggle_tunnel_phase1(uuid, enabled=None):
    """
    Toggle phase1 entry in ipsec/tunnel.

    Wraps: POST /api/ipsec/tunnel/togglePhase1/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "tunnel", "phase1", uuid, enabled)


def search_tunnel_phase2(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search phase2 entries in ipsec/tunnel.

    Wraps: POST /api/ipsec/tunnel/searchPhase2

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "tunnel", "phase2", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def del_tunnel_phase2(uuid):
    """
    Delete phase2 entry in ipsec/tunnel.

    Wraps: POST /api/ipsec/tunnel/delPhase2/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "tunnel", "phase2", uuid)


def toggle_tunnel_phase2(uuid, enabled=None):
    """
    Toggle phase2 entry in ipsec/tunnel.

    Wraps: POST /api/ipsec/tunnel/togglePhase2/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "tunnel", "phase2", uuid, enabled)


def tunnel_toggle(data=None, uuid=None):
    """
    Execute toggle in ipsec/tunnel.

    Wraps: /api/ipsec/tunnel/toggle

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("ipsec", "tunnel", "toggle", uuid=uuid, data=data)


# --- vti controller ---

def search_vti(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search vti entries in ipsec/vti.

    Wraps: POST /api/ipsec/vti/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("ipsec", "vti", "vti", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_vti(uuid=None):
    """
    Get vti entry in ipsec/vti.

    Wraps: GET /api/ipsec/vti/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("ipsec", "vti", "vti", uuid)


def add_vti(data):
    """
    Add vti entry in ipsec/vti.

    Wraps: POST /api/ipsec/vti/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("ipsec", "vti", "vti", data)


def set_vti(uuid, data):
    """
    Set/update vti entry in ipsec/vti.

    Wraps: POST /api/ipsec/vti/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("ipsec", "vti", "vti", uuid, data)


def del_vti(uuid):
    """
    Delete vti entry in ipsec/vti.

    Wraps: POST /api/ipsec/vti/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("ipsec", "vti", "vti", uuid)


def toggle_vti(uuid, enabled=None):
    """
    Toggle vti entry in ipsec/vti.

    Wraps: POST /api/ipsec/vti/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("ipsec", "vti", "vti", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="connections", action="reconfigure", data=None):
    """
    Generic reconfigure for ipsec.

    Wraps: POST /api/ipsec/{controller}/{action}

    :param controller: Controller name, default connections
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("ipsec", controller, action, data)
