# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense freeradius wrappers.

Generated from controllers.json for module freeradius.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/freeradius/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_freeradius"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- avpair controller ---

def search_avpair(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search avpair entries in freeradius/avpair.

    Wraps: POST /api/freeradius/avpair/searchAvpair

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "avpair", "avpair", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_avpair(uuid=None):
    """
    Get avpair entry in freeradius/avpair.

    Wraps: GET /api/freeradius/avpair/getAvpair/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "avpair", "avpair", uuid)


def add_avpair(data):
    """
    Add avpair entry in freeradius/avpair.

    Wraps: POST /api/freeradius/avpair/addAvpair

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "avpair", "avpair", data)


def set_avpair(uuid, data):
    """
    Set/update avpair entry in freeradius/avpair.

    Wraps: POST /api/freeradius/avpair/setAvpair/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "avpair", "avpair", uuid, data)


def del_avpair(uuid):
    """
    Delete avpair entry in freeradius/avpair.

    Wraps: POST /api/freeradius/avpair/delAvpair/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "avpair", "avpair", uuid)


def toggle_avpair(uuid, enabled=None):
    """
    Toggle avpair entry in freeradius/avpair.

    Wraps: POST /api/freeradius/avpair/toggleAvpair/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "avpair", "avpair", uuid, enabled)


# --- client controller ---

def search_client(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search client entries in freeradius/client.

    Wraps: POST /api/freeradius/client/searchClient

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "client", "client", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_client(uuid=None):
    """
    Get client entry in freeradius/client.

    Wraps: GET /api/freeradius/client/getClient/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "client", "client", uuid)


def add_client(data):
    """
    Add client entry in freeradius/client.

    Wraps: POST /api/freeradius/client/addClient

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "client", "client", data)


def set_client(uuid, data):
    """
    Set/update client entry in freeradius/client.

    Wraps: POST /api/freeradius/client/setClient/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "client", "client", uuid, data)


def del_client(uuid):
    """
    Delete client entry in freeradius/client.

    Wraps: POST /api/freeradius/client/delClient/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "client", "client", uuid)


def toggle_client(uuid, enabled=None):
    """
    Toggle client entry in freeradius/client.

    Wraps: POST /api/freeradius/client/toggleClient/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "client", "client", uuid, enabled)


# --- dhcp controller ---

def search_dhcp(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search dhcp entries in freeradius/dhcp.

    Wraps: POST /api/freeradius/dhcp/searchDhcp

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "dhcp", "dhcp", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcp(uuid=None):
    """
    Get dhcp entry in freeradius/dhcp.

    Wraps: GET /api/freeradius/dhcp/getDhcp/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "dhcp", "dhcp", uuid)


def add_dhcp(data):
    """
    Add dhcp entry in freeradius/dhcp.

    Wraps: POST /api/freeradius/dhcp/addDhcp

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "dhcp", "dhcp", data)


def set_dhcp(uuid, data):
    """
    Set/update dhcp entry in freeradius/dhcp.

    Wraps: POST /api/freeradius/dhcp/setDhcp/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "dhcp", "dhcp", uuid, data)


def del_dhcp(uuid):
    """
    Delete dhcp entry in freeradius/dhcp.

    Wraps: POST /api/freeradius/dhcp/delDhcp/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "dhcp", "dhcp", uuid)


def toggle_dhcp(uuid, enabled=None):
    """
    Toggle dhcp entry in freeradius/dhcp.

    Wraps: POST /api/freeradius/dhcp/toggleDhcp/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "dhcp", "dhcp", uuid, enabled)


# --- eap controller ---

def get_eap():
    """
    Get eap singleton config in freeradius/eap.

    Wraps: GET /api/freeradius/eap/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("freeradius", "eap")


def set_eap(data):
    """
    Set eap singleton config in freeradius/eap.

    Wraps: POST /api/freeradius/eap/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("freeradius", "eap", "set", data=data, method="POST")


# --- general controller ---

def get_general():
    """
    Get general singleton config in freeradius/general.

    Wraps: GET /api/freeradius/general/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("freeradius", "general")


def set_general(data):
    """
    Set general singleton config in freeradius/general.

    Wraps: POST /api/freeradius/general/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("freeradius", "general", "set", data=data, method="POST")


# --- ldapgroup controller ---

def search_ldapgroup(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ldapgroup entries in freeradius/ldapgroup.

    Wraps: POST /api/freeradius/ldapgroup/searchLdapgroup

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "ldapgroup", "ldapgroup", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ldapgroup(uuid=None):
    """
    Get ldapgroup entry in freeradius/ldapgroup.

    Wraps: GET /api/freeradius/ldapgroup/getLdapgroup/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "ldapgroup", "ldapgroup", uuid)


def add_ldapgroup(data):
    """
    Add ldapgroup entry in freeradius/ldapgroup.

    Wraps: POST /api/freeradius/ldapgroup/addLdapgroup

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "ldapgroup", "ldapgroup", data)


def set_ldapgroup(uuid, data):
    """
    Set/update ldapgroup entry in freeradius/ldapgroup.

    Wraps: POST /api/freeradius/ldapgroup/setLdapgroup/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "ldapgroup", "ldapgroup", uuid, data)


def del_ldapgroup(uuid):
    """
    Delete ldapgroup entry in freeradius/ldapgroup.

    Wraps: POST /api/freeradius/ldapgroup/delLdapgroup/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "ldapgroup", "ldapgroup", uuid)


def toggle_ldapgroup(uuid, enabled=None):
    """
    Toggle ldapgroup entry in freeradius/ldapgroup.

    Wraps: POST /api/freeradius/ldapgroup/toggleLdapgroup/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "ldapgroup", "ldapgroup", uuid, enabled)


# --- lease controller ---

def search_lease(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search lease entries in freeradius/lease.

    Wraps: POST /api/freeradius/lease/searchLease

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "lease", "lease", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_lease(uuid=None):
    """
    Get lease entry in freeradius/lease.

    Wraps: GET /api/freeradius/lease/getLease/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "lease", "lease", uuid)


def add_lease(data):
    """
    Add lease entry in freeradius/lease.

    Wraps: POST /api/freeradius/lease/addLease

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "lease", "lease", data)


def set_lease(uuid, data):
    """
    Set/update lease entry in freeradius/lease.

    Wraps: POST /api/freeradius/lease/setLease/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "lease", "lease", uuid, data)


def del_lease(uuid):
    """
    Delete lease entry in freeradius/lease.

    Wraps: POST /api/freeradius/lease/delLease/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "lease", "lease", uuid)


def toggle_lease(uuid, enabled=None):
    """
    Toggle lease entry in freeradius/lease.

    Wraps: POST /api/freeradius/lease/toggleLease/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "lease", "lease", uuid, enabled)


# --- proxy controller ---

def get_proxy():
    """
    Get proxy singleton config in freeradius/proxy.

    Wraps: GET /api/freeradius/proxy/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("freeradius", "proxy")


def set_proxy(data):
    """
    Set proxy singleton config in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("freeradius", "proxy", "set", data=data, method="POST")


def search_homeserver(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search homeserver entries in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/searchHomeserver

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "proxy", "homeserver", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_homeserver(uuid=None):
    """
    Get homeserver entry in freeradius/proxy.

    Wraps: GET /api/freeradius/proxy/getHomeserver/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "proxy", "homeserver", uuid)


def add_homeserver(data):
    """
    Add homeserver entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/addHomeserver

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "proxy", "homeserver", data)


def set_homeserver(uuid, data):
    """
    Set/update homeserver entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/setHomeserver/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "proxy", "homeserver", uuid, data)


def del_homeserver(uuid):
    """
    Delete homeserver entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/delHomeserver/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "proxy", "homeserver", uuid)


def toggle_homeserver(uuid, enabled=None):
    """
    Toggle homeserver entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/toggleHomeserver/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "proxy", "homeserver", uuid, enabled)


def search_homeserverpool(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search homeserverpool entries in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/searchHomeserverpool

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "proxy", "homeserverpool", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_homeserverpool(uuid=None):
    """
    Get homeserverpool entry in freeradius/proxy.

    Wraps: GET /api/freeradius/proxy/getHomeserverpool/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "proxy", "homeserverpool", uuid)


def add_homeserverpool(data):
    """
    Add homeserverpool entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/addHomeserverpool

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "proxy", "homeserverpool", data)


def set_homeserverpool(uuid, data):
    """
    Set/update homeserverpool entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/setHomeserverpool/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "proxy", "homeserverpool", uuid, data)


def del_homeserverpool(uuid):
    """
    Delete homeserverpool entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/delHomeserverpool/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "proxy", "homeserverpool", uuid)


def toggle_homeserverpool(uuid, enabled=None):
    """
    Toggle homeserverpool entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/toggleHomeserverpool/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "proxy", "homeserverpool", uuid, enabled)


def search_realm(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search realm entries in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/searchRealm

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "proxy", "realm", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_realm(uuid=None):
    """
    Get realm entry in freeradius/proxy.

    Wraps: GET /api/freeradius/proxy/getRealm/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "proxy", "realm", uuid)


def add_realm(data):
    """
    Add realm entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/addRealm

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "proxy", "realm", data)


def set_realm(uuid, data):
    """
    Set/update realm entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/setRealm/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "proxy", "realm", uuid, data)


def del_realm(uuid):
    """
    Delete realm entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/delRealm/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "proxy", "realm", uuid)


def toggle_realm(uuid, enabled=None):
    """
    Toggle realm entry in freeradius/proxy.

    Wraps: POST /api/freeradius/proxy/toggleRealm/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "proxy", "realm", uuid, enabled)


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in freeradius/service.

    Wraps: POST /api/freeradius/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("freeradius", "service", action, data)


def service_restart(data=None):
    """
    Execute restart in freeradius/service.

    Wraps: POST /api/freeradius/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("freeradius", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in freeradius/service.

    Wraps: POST /api/freeradius/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("freeradius", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in freeradius/service.

    Wraps: POST /api/freeradius/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("freeradius", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in freeradius/service.

    Wraps: POST /api/freeradius/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("freeradius", "service", "stop", data=data, method="POST")


# --- user controller ---

def search_user(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search user entries in freeradius/user.

    Wraps: POST /api/freeradius/user/searchUser

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("freeradius", "user", "user", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_user(uuid=None):
    """
    Get user entry in freeradius/user.

    Wraps: GET /api/freeradius/user/getUser/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("freeradius", "user", "user", uuid)


def add_user(data):
    """
    Add user entry in freeradius/user.

    Wraps: POST /api/freeradius/user/addUser

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("freeradius", "user", "user", data)


def set_user(uuid, data):
    """
    Set/update user entry in freeradius/user.

    Wraps: POST /api/freeradius/user/setUser/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("freeradius", "user", "user", uuid, data)


def del_user(uuid):
    """
    Delete user entry in freeradius/user.

    Wraps: POST /api/freeradius/user/delUser/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("freeradius", "user", "user", uuid)


def toggle_user(uuid, enabled=None):
    """
    Toggle user entry in freeradius/user.

    Wraps: POST /api/freeradius/user/toggleUser/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("freeradius", "user", "user", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for freeradius.

    Wraps: POST /api/freeradius/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("freeradius", controller, action, data)
