# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense kea wrappers.

Generated from controllers.json for module kea.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/kea/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_kea"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- ctrlagent controller ---

def get_ctrlagent():
    """
    Get ctrlagent singleton config in kea/ctrlagent.

    Wraps: GET /api/kea/ctrlagent/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("kea", "ctrlagent")


# --- ddns controller ---

def get_ddns():
    """
    Get ddns singleton config in kea/ddns.

    Wraps: GET /api/kea/ddns/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("kea", "ddns")


# --- dhcpv4 controller ---

def get_dhcpv4():
    """
    Get dhcpv4 singleton config in kea/dhcpv4.

    Wraps: GET /api/kea/dhcpv4/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("kea", "dhcpv4")


def search_dhcpv4_option(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search option entries in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/searchOption

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv4", "option", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv4_option(uuid=None):
    """
    Get option entry in kea/dhcpv4.

    Wraps: GET /api/kea/dhcpv4/getOption/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv4", "option", uuid)


def add_dhcpv4_option(data):
    """
    Add option entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/addOption

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv4", "option", data)


def set_dhcpv4_option(uuid, data):
    """
    Set/update option entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/setOption/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv4", "option", uuid, data)


def del_dhcpv4_option(uuid):
    """
    Delete option entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/delOption/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv4", "option", uuid)


def search_dhcpv4_peer(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search peer entries in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/searchPeer

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv4", "peer", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv4_peer(uuid=None):
    """
    Get peer entry in kea/dhcpv4.

    Wraps: GET /api/kea/dhcpv4/getPeer/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv4", "peer", uuid)


def add_dhcpv4_peer(data):
    """
    Add peer entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/addPeer

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv4", "peer", data)


def set_dhcpv4_peer(uuid, data):
    """
    Set/update peer entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/setPeer/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv4", "peer", uuid, data)


def del_dhcpv4_peer(uuid):
    """
    Delete peer entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/delPeer/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv4", "peer", uuid)


def search_dhcpv4_reservation(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search reservation entries in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/searchReservation

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv4", "reservation", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv4_reservation(uuid=None):
    """
    Get reservation entry in kea/dhcpv4.

    Wraps: GET /api/kea/dhcpv4/getReservation/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv4", "reservation", uuid)


def add_dhcpv4_reservation(data):
    """
    Add reservation entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/addReservation

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv4", "reservation", data)


def set_dhcpv4_reservation(uuid, data):
    """
    Set/update reservation entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/setReservation/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv4", "reservation", uuid, data)


def del_dhcpv4_reservation(uuid):
    """
    Delete reservation entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/delReservation/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv4", "reservation", uuid)


def search_dhcpv4_subnet(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search subnet entries in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/searchSubnet

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv4", "subnet", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv4_subnet(uuid=None):
    """
    Get subnet entry in kea/dhcpv4.

    Wraps: GET /api/kea/dhcpv4/getSubnet/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv4", "subnet", uuid)


def add_dhcpv4_subnet(data):
    """
    Add subnet entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/addSubnet

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv4", "subnet", data)


def set_dhcpv4_subnet(uuid, data):
    """
    Set/update subnet entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/setSubnet/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv4", "subnet", uuid, data)


def del_dhcpv4_subnet(uuid):
    """
    Delete subnet entry in kea/dhcpv4.

    Wraps: POST /api/kea/dhcpv4/delSubnet/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv4", "subnet", uuid)


def dhcpv4_download_reservations(data=None, uuid=None):
    """
    Execute downloadReservations in kea/dhcpv4.

    Wraps: /api/kea/dhcpv4/downloadReservations

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("kea", "dhcpv4", "downloadReservations", uuid=uuid, data=data)


def dhcpv4_upload_reservations(data=None, uuid=None):
    """
    Execute uploadReservations in kea/dhcpv4.

    Wraps: /api/kea/dhcpv4/uploadReservations

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("kea", "dhcpv4", "uploadReservations", uuid=uuid, data=data)


# --- dhcpv6 controller ---

def get_dhcpv6():
    """
    Get dhcpv6 singleton config in kea/dhcpv6.

    Wraps: GET /api/kea/dhcpv6/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("kea", "dhcpv6")


def search_dhcpv6_option(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search option entries in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/searchOption

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv6", "option", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv6_option(uuid=None):
    """
    Get option entry in kea/dhcpv6.

    Wraps: GET /api/kea/dhcpv6/getOption/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv6", "option", uuid)


def add_dhcpv6_option(data):
    """
    Add option entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/addOption

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv6", "option", data)


def set_dhcpv6_option(uuid, data):
    """
    Set/update option entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/setOption/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv6", "option", uuid, data)


def del_dhcpv6_option(uuid):
    """
    Delete option entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/delOption/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv6", "option", uuid)


def search_pd_pool(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search pd_pool entries in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/searchPdPool

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv6", "pd_pool", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_pd_pool(uuid=None):
    """
    Get pd_pool entry in kea/dhcpv6.

    Wraps: GET /api/kea/dhcpv6/getPdPool/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv6", "pd_pool", uuid)


def add_pd_pool(data):
    """
    Add pd_pool entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/addPdPool

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv6", "pd_pool", data)


def set_pd_pool(uuid, data):
    """
    Set/update pd_pool entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/setPdPool/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv6", "pd_pool", uuid, data)


def del_pd_pool(uuid):
    """
    Delete pd_pool entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/delPdPool/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv6", "pd_pool", uuid)


def search_dhcpv6_peer(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search peer entries in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/searchPeer

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv6", "peer", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv6_peer(uuid=None):
    """
    Get peer entry in kea/dhcpv6.

    Wraps: GET /api/kea/dhcpv6/getPeer/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv6", "peer", uuid)


def add_dhcpv6_peer(data):
    """
    Add peer entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/addPeer

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv6", "peer", data)


def set_dhcpv6_peer(uuid, data):
    """
    Set/update peer entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/setPeer/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv6", "peer", uuid, data)


def del_dhcpv6_peer(uuid):
    """
    Delete peer entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/delPeer/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv6", "peer", uuid)


def search_dhcpv6_reservation(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search reservation entries in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/searchReservation

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv6", "reservation", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv6_reservation(uuid=None):
    """
    Get reservation entry in kea/dhcpv6.

    Wraps: GET /api/kea/dhcpv6/getReservation/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv6", "reservation", uuid)


def add_dhcpv6_reservation(data):
    """
    Add reservation entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/addReservation

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv6", "reservation", data)


def set_dhcpv6_reservation(uuid, data):
    """
    Set/update reservation entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/setReservation/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv6", "reservation", uuid, data)


def del_dhcpv6_reservation(uuid):
    """
    Delete reservation entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/delReservation/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv6", "reservation", uuid)


def search_dhcpv6_subnet(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search subnet entries in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/searchSubnet

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "dhcpv6", "subnet", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_dhcpv6_subnet(uuid=None):
    """
    Get subnet entry in kea/dhcpv6.

    Wraps: GET /api/kea/dhcpv6/getSubnet/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("kea", "dhcpv6", "subnet", uuid)


def add_dhcpv6_subnet(data):
    """
    Add subnet entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/addSubnet

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("kea", "dhcpv6", "subnet", data)


def set_dhcpv6_subnet(uuid, data):
    """
    Set/update subnet entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/setSubnet/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("kea", "dhcpv6", "subnet", uuid, data)


def del_dhcpv6_subnet(uuid):
    """
    Delete subnet entry in kea/dhcpv6.

    Wraps: POST /api/kea/dhcpv6/delSubnet/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("kea", "dhcpv6", "subnet", uuid)


def dhcpv6_download_reservations(data=None, uuid=None):
    """
    Execute downloadReservations in kea/dhcpv6.

    Wraps: /api/kea/dhcpv6/downloadReservations

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("kea", "dhcpv6", "downloadReservations", uuid=uuid, data=data)


def dhcpv6_upload_reservations(data=None, uuid=None):
    """
    Execute uploadReservations in kea/dhcpv6.

    Wraps: /api/kea/dhcpv6/uploadReservations

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("kea", "dhcpv6", "uploadReservations", uuid=uuid, data=data)


# --- leases controller ---

def search_lease(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search lease entries in kea/leases.

    Wraps: POST /api/kea/leases/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("kea", "leases", "lease", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def leases_del_lease(data=None, uuid=None):
    """
    Execute delLease in kea/leases.

    Wraps: /api/kea/leases/delLease

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("kea", "leases", "delLease", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="ctrlagent", action="reconfigure", data=None):
    """
    Generic reconfigure for kea.

    Wraps: POST /api/kea/{controller}/{action}

    :param controller: Controller name, default ctrlagent
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("kea", controller, action, data)
