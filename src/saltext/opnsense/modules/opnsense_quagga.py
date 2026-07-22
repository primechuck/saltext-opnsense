# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense quagga wrappers.

Generated from controllers.json for module quagga.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/quagga/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_quagga"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- bfd controller ---

def search_bfd_neighbor(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search neighbor entries in quagga/bfd.

    Wraps: POST /api/quagga/bfd/searchNeighbor

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bfd", "neighbor", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_bfd_neighbor(uuid=None):
    """
    Get neighbor entry in quagga/bfd.

    Wraps: GET /api/quagga/bfd/getNeighbor/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bfd", "neighbor", uuid)


def add_bfd_neighbor(data):
    """
    Add neighbor entry in quagga/bfd.

    Wraps: POST /api/quagga/bfd/addNeighbor

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bfd", "neighbor", data)


def set_bfd_neighbor(uuid, data):
    """
    Set/update neighbor entry in quagga/bfd.

    Wraps: POST /api/quagga/bfd/setNeighbor/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bfd", "neighbor", uuid, data)


def del_bfd_neighbor(uuid):
    """
    Delete neighbor entry in quagga/bfd.

    Wraps: POST /api/quagga/bfd/delNeighbor/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bfd", "neighbor", uuid)


def toggle_bfd_neighbor(uuid, enabled=None):
    """
    Toggle neighbor entry in quagga/bfd.

    Wraps: POST /api/quagga/bfd/toggleNeighbor/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bfd", "neighbor", uuid, enabled)


# --- bgp controller ---

def search_aspath(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search aspath entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchAspath

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "aspath", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_aspath(uuid=None):
    """
    Get aspath entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getAspath/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "aspath", uuid)


def add_aspath(data):
    """
    Add aspath entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addAspath

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "aspath", data)


def set_aspath(uuid, data):
    """
    Set/update aspath entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setAspath/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "aspath", uuid, data)


def del_aspath(uuid):
    """
    Delete aspath entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delAspath/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "aspath", uuid)


def toggle_aspath(uuid, enabled=None):
    """
    Toggle aspath entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/toggleAspath/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "aspath", uuid, enabled)


def search_communitylist(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search communitylist entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchCommunitylist

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "communitylist", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_communitylist(uuid=None):
    """
    Get communitylist entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getCommunitylist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "communitylist", uuid)


def add_communitylist(data):
    """
    Add communitylist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addCommunitylist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "communitylist", data)


def set_communitylist(uuid, data):
    """
    Set/update communitylist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setCommunitylist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "communitylist", uuid, data)


def del_communitylist(uuid):
    """
    Delete communitylist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delCommunitylist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "communitylist", uuid)


def toggle_communitylist(uuid, enabled=None):
    """
    Toggle communitylist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/toggleCommunitylist/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "communitylist", uuid, enabled)


def search_bgp_neighbor(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search neighbor entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchNeighbor

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "neighbor", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_bgp_neighbor(uuid=None):
    """
    Get neighbor entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getNeighbor/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "neighbor", uuid)


def add_bgp_neighbor(data):
    """
    Add neighbor entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addNeighbor

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "neighbor", data)


def set_bgp_neighbor(uuid, data):
    """
    Set/update neighbor entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setNeighbor/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "neighbor", uuid, data)


def del_bgp_neighbor(uuid):
    """
    Delete neighbor entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delNeighbor/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "neighbor", uuid)


def toggle_bgp_neighbor(uuid, enabled=None):
    """
    Toggle neighbor entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/toggleNeighbor/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "neighbor", uuid, enabled)


def search_peergroup(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search peergroup entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchPeergroup

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "peergroup", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_peergroup(uuid=None):
    """
    Get peergroup entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getPeergroup/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "peergroup", uuid)


def add_peergroup(data):
    """
    Add peergroup entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addPeergroup

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "peergroup", data)


def set_peergroup(uuid, data):
    """
    Set/update peergroup entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setPeergroup/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "peergroup", uuid, data)


def del_peergroup(uuid):
    """
    Delete peergroup entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delPeergroup/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "peergroup", uuid)


def toggle_peergroup(uuid, enabled=None):
    """
    Toggle peergroup entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/togglePeergroup/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "peergroup", uuid, enabled)


def search_bgp_prefixlist(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search prefixlist entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchPrefixlist

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "prefixlist", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_bgp_prefixlist(uuid=None):
    """
    Get prefixlist entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getPrefixlist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "prefixlist", uuid)


def add_bgp_prefixlist(data):
    """
    Add prefixlist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addPrefixlist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "prefixlist", data)


def set_bgp_prefixlist(uuid, data):
    """
    Set/update prefixlist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setPrefixlist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "prefixlist", uuid, data)


def del_bgp_prefixlist(uuid):
    """
    Delete prefixlist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delPrefixlist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "prefixlist", uuid)


def toggle_bgp_prefixlist(uuid, enabled=None):
    """
    Toggle prefixlist entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/togglePrefixlist/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "prefixlist", uuid, enabled)


def search_bgp_redistribution(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search redistribution entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchRedistribution

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "redistribution", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_bgp_redistribution(uuid=None):
    """
    Get redistribution entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getRedistribution/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "redistribution", uuid)


def add_bgp_redistribution(data):
    """
    Add redistribution entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addRedistribution

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "redistribution", data)


def set_bgp_redistribution(uuid, data):
    """
    Set/update redistribution entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setRedistribution/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "redistribution", uuid, data)


def del_bgp_redistribution(uuid):
    """
    Delete redistribution entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delRedistribution/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "redistribution", uuid)


def toggle_bgp_redistribution(uuid, enabled=None):
    """
    Toggle redistribution entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/toggleRedistribution/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "redistribution", uuid, enabled)


def search_bgp_routemap(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search routemap entries in quagga/bgp.

    Wraps: POST /api/quagga/bgp/searchRoutemap

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "bgp", "routemap", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_bgp_routemap(uuid=None):
    """
    Get routemap entry in quagga/bgp.

    Wraps: GET /api/quagga/bgp/getRoutemap/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "bgp", "routemap", uuid)


def add_bgp_routemap(data):
    """
    Add routemap entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/addRoutemap

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "bgp", "routemap", data)


def set_bgp_routemap(uuid, data):
    """
    Set/update routemap entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/setRoutemap/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "bgp", "routemap", uuid, data)


def del_bgp_routemap(uuid):
    """
    Delete routemap entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/delRoutemap/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "bgp", "routemap", uuid)


def toggle_bgp_routemap(uuid, enabled=None):
    """
    Toggle routemap entry in quagga/bgp.

    Wraps: POST /api/quagga/bgp/toggleRoutemap/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "bgp", "routemap", uuid, enabled)


# --- diagnostics controller ---

def search_bgproute4(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search bgproute4 entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchBgproute4

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "bgproute4", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_bgproute6(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search bgproute6 entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchBgproute6

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "bgproute6", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_generalroute4(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search generalroute4 entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchGeneralroute4

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "generalroute4", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_generalroute6(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search generalroute6 entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchGeneralroute6

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "generalroute6", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_ospfneighbor(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ospfneighbor entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchOspfneighbor

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "ospfneighbor", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_ospfroute(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ospfroute entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchOspfroute

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "ospfroute", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_ospfv3database(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ospfv3database entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchOspfv3database

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "ospfv3database", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_ospfv3route(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ospfv3route entries in quagga/diagnostics.

    Wraps: POST /api/quagga/diagnostics/searchOspfv3route

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "diagnostics", "ospfv3route", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def diagnostics_bfdcounters(data=None, uuid=None):
    """
    Execute bfdcounters in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/bfdcounters

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "bfdcounters", uuid=uuid, data=data)


def diagnostics_bfdneighbors(data=None, uuid=None):
    """
    Execute bfdneighbors in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/bfdneighbors

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "bfdneighbors", uuid=uuid, data=data)


def diagnostics_bfdstaticroute(data=None, uuid=None):
    """
    Execute bfdstaticroute in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/bfdstaticroute

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "bfdstaticroute", uuid=uuid, data=data)


def diagnostics_bfdsummary(data=None, uuid=None):
    """
    Execute bfdsummary in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/bfdsummary

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "bfdsummary", uuid=uuid, data=data)


def diagnostics_bgpneighbors(data=None, uuid=None):
    """
    Execute bgpneighbors in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/bgpneighbors

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "bgpneighbors", uuid=uuid, data=data)


def diagnostics_bgpsummary(data=None, uuid=None):
    """
    Execute bgpsummary in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/bgpsummary

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "bgpsummary", uuid=uuid, data=data)


def diagnostics_generalrunningconfig(data=None, uuid=None):
    """
    Execute generalrunningconfig in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/generalrunningconfig

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "generalrunningconfig", uuid=uuid, data=data)


def diagnostics_ospfdatabase(data=None, uuid=None):
    """
    Execute ospfdatabase in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/ospfdatabase

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "ospfdatabase", uuid=uuid, data=data)


def diagnostics_ospfinterface(data=None, uuid=None):
    """
    Execute ospfinterface in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/ospfinterface

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "ospfinterface", uuid=uuid, data=data)


def diagnostics_ospfoverview(data=None, uuid=None):
    """
    Execute ospfoverview in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/ospfoverview

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "ospfoverview", uuid=uuid, data=data)


def diagnostics_ospfv3interface(data=None, uuid=None):
    """
    Execute ospfv3interface in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/ospfv3interface

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "ospfv3interface", uuid=uuid, data=data)


def diagnostics_ospfv3overview(data=None, uuid=None):
    """
    Execute ospfv3overview in quagga/diagnostics.

    Wraps: /api/quagga/diagnostics/ospfv3overview

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("quagga", "diagnostics", "ospfv3overview", uuid=uuid, data=data)


# --- ospf6settings controller ---

def search_ospf6settings_interface(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search interface entries in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/searchInterface

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospf6settings", "interface", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospf6settings_interface(uuid=None):
    """
    Get interface entry in quagga/ospf6settings.

    Wraps: GET /api/quagga/ospf6settings/getInterface/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospf6settings", "interface", uuid)


def add_ospf6settings_interface(data):
    """
    Add interface entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/addInterface

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospf6settings", "interface", data)


def set_ospf6settings_interface(uuid, data):
    """
    Set/update interface entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/setInterface/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospf6settings", "interface", uuid, data)


def del_ospf6settings_interface(uuid):
    """
    Delete interface entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/delInterface/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospf6settings", "interface", uuid)


def toggle_ospf6settings_interface(uuid, enabled=None):
    """
    Toggle interface entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/toggleInterface/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospf6settings", "interface", uuid, enabled)


def search_ospf6settings_network(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search network entries in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/searchNetwork

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospf6settings", "network", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospf6settings_network(uuid=None):
    """
    Get network entry in quagga/ospf6settings.

    Wraps: GET /api/quagga/ospf6settings/getNetwork/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospf6settings", "network", uuid)


def add_ospf6settings_network(data):
    """
    Add network entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/addNetwork

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospf6settings", "network", data)


def set_ospf6settings_network(uuid, data):
    """
    Set/update network entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/setNetwork/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospf6settings", "network", uuid, data)


def del_ospf6settings_network(uuid):
    """
    Delete network entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/delNetwork/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospf6settings", "network", uuid)


def toggle_ospf6settings_network(uuid, enabled=None):
    """
    Toggle network entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/toggleNetwork/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospf6settings", "network", uuid, enabled)


def search_ospf6settings_prefixlist(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search prefixlist entries in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/searchPrefixlist

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospf6settings", "prefixlist", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospf6settings_prefixlist(uuid=None):
    """
    Get prefixlist entry in quagga/ospf6settings.

    Wraps: GET /api/quagga/ospf6settings/getPrefixlist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospf6settings", "prefixlist", uuid)


def add_ospf6settings_prefixlist(data):
    """
    Add prefixlist entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/addPrefixlist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospf6settings", "prefixlist", data)


def set_ospf6settings_prefixlist(uuid, data):
    """
    Set/update prefixlist entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/setPrefixlist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospf6settings", "prefixlist", uuid, data)


def del_ospf6settings_prefixlist(uuid):
    """
    Delete prefixlist entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/delPrefixlist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospf6settings", "prefixlist", uuid)


def toggle_ospf6settings_prefixlist(uuid, enabled=None):
    """
    Toggle prefixlist entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/togglePrefixlist/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospf6settings", "prefixlist", uuid, enabled)


def search_ospf6settings_redistribution(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search redistribution entries in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/searchRedistribution

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospf6settings", "redistribution", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospf6settings_redistribution(uuid=None):
    """
    Get redistribution entry in quagga/ospf6settings.

    Wraps: GET /api/quagga/ospf6settings/getRedistribution/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospf6settings", "redistribution", uuid)


def add_ospf6settings_redistribution(data):
    """
    Add redistribution entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/addRedistribution

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospf6settings", "redistribution", data)


def set_ospf6settings_redistribution(uuid, data):
    """
    Set/update redistribution entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/setRedistribution/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospf6settings", "redistribution", uuid, data)


def del_ospf6settings_redistribution(uuid):
    """
    Delete redistribution entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/delRedistribution/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospf6settings", "redistribution", uuid)


def toggle_ospf6settings_redistribution(uuid, enabled=None):
    """
    Toggle redistribution entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/toggleRedistribution/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospf6settings", "redistribution", uuid, enabled)


def search_ospf6settings_routemap(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search routemap entries in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/searchRoutemap

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospf6settings", "routemap", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospf6settings_routemap(uuid=None):
    """
    Get routemap entry in quagga/ospf6settings.

    Wraps: GET /api/quagga/ospf6settings/getRoutemap/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospf6settings", "routemap", uuid)


def add_ospf6settings_routemap(data):
    """
    Add routemap entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/addRoutemap

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospf6settings", "routemap", data)


def set_ospf6settings_routemap(uuid, data):
    """
    Set/update routemap entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/setRoutemap/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospf6settings", "routemap", uuid, data)


def del_ospf6settings_routemap(uuid):
    """
    Delete routemap entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/delRoutemap/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospf6settings", "routemap", uuid)


def toggle_ospf6settings_routemap(uuid, enabled=None):
    """
    Toggle routemap entry in quagga/ospf6settings.

    Wraps: POST /api/quagga/ospf6settings/toggleRoutemap/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospf6settings", "routemap", uuid, enabled)


# --- ospfsettings controller ---

def search_area(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search area entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchArea

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "area", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_area(uuid=None):
    """
    Get area entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getArea/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "area", uuid)


def add_area(data):
    """
    Add area entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addArea

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "area", data)


def set_area(uuid, data):
    """
    Set/update area entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setArea/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "area", uuid, data)


def del_area(uuid):
    """
    Delete area entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delArea/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "area", uuid)


def toggle_area(uuid, enabled=None):
    """
    Toggle area entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/toggleArea/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "area", uuid, enabled)


def search_ospfsettings_interface(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search interface entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchInterface

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "interface", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospfsettings_interface(uuid=None):
    """
    Get interface entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getInterface/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "interface", uuid)


def add_ospfsettings_interface(data):
    """
    Add interface entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addInterface

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "interface", data)


def set_ospfsettings_interface(uuid, data):
    """
    Set/update interface entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setInterface/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "interface", uuid, data)


def del_ospfsettings_interface(uuid):
    """
    Delete interface entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delInterface/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "interface", uuid)


def toggle_ospfsettings_interface(uuid, enabled=None):
    """
    Toggle interface entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/toggleInterface/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "interface", uuid, enabled)


def search_ospfsettings_neighbor(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search neighbor entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchNeighbor

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "neighbor", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospfsettings_neighbor(uuid=None):
    """
    Get neighbor entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getNeighbor/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "neighbor", uuid)


def add_ospfsettings_neighbor(data):
    """
    Add neighbor entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addNeighbor

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "neighbor", data)


def set_ospfsettings_neighbor(uuid, data):
    """
    Set/update neighbor entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setNeighbor/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "neighbor", uuid, data)


def del_ospfsettings_neighbor(uuid):
    """
    Delete neighbor entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delNeighbor/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "neighbor", uuid)


def toggle_ospfsettings_neighbor(uuid, enabled=None):
    """
    Toggle neighbor entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/toggleNeighbor/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "neighbor", uuid, enabled)


def search_ospfsettings_network(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search network entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchNetwork

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "network", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospfsettings_network(uuid=None):
    """
    Get network entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getNetwork/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "network", uuid)


def add_ospfsettings_network(data):
    """
    Add network entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addNetwork

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "network", data)


def set_ospfsettings_network(uuid, data):
    """
    Set/update network entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setNetwork/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "network", uuid, data)


def del_ospfsettings_network(uuid):
    """
    Delete network entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delNetwork/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "network", uuid)


def toggle_ospfsettings_network(uuid, enabled=None):
    """
    Toggle network entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/toggleNetwork/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "network", uuid, enabled)


def search_ospfsettings_prefixlist(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search prefixlist entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchPrefixlist

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "prefixlist", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospfsettings_prefixlist(uuid=None):
    """
    Get prefixlist entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getPrefixlist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "prefixlist", uuid)


def add_ospfsettings_prefixlist(data):
    """
    Add prefixlist entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addPrefixlist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "prefixlist", data)


def set_ospfsettings_prefixlist(uuid, data):
    """
    Set/update prefixlist entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setPrefixlist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "prefixlist", uuid, data)


def del_ospfsettings_prefixlist(uuid):
    """
    Delete prefixlist entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delPrefixlist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "prefixlist", uuid)


def toggle_ospfsettings_prefixlist(uuid, enabled=None):
    """
    Toggle prefixlist entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/togglePrefixlist/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "prefixlist", uuid, enabled)


def search_ospfsettings_redistribution(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search redistribution entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchRedistribution

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "redistribution", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospfsettings_redistribution(uuid=None):
    """
    Get redistribution entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getRedistribution/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "redistribution", uuid)


def add_ospfsettings_redistribution(data):
    """
    Add redistribution entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addRedistribution

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "redistribution", data)


def set_ospfsettings_redistribution(uuid, data):
    """
    Set/update redistribution entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setRedistribution/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "redistribution", uuid, data)


def del_ospfsettings_redistribution(uuid):
    """
    Delete redistribution entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delRedistribution/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "redistribution", uuid)


def toggle_ospfsettings_redistribution(uuid, enabled=None):
    """
    Toggle redistribution entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/toggleRedistribution/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "redistribution", uuid, enabled)


def search_ospfsettings_routemap(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search routemap entries in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/searchRoutemap

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "ospfsettings", "routemap", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ospfsettings_routemap(uuid=None):
    """
    Get routemap entry in quagga/ospfsettings.

    Wraps: GET /api/quagga/ospfsettings/getRoutemap/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "ospfsettings", "routemap", uuid)


def add_ospfsettings_routemap(data):
    """
    Add routemap entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/addRoutemap

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "ospfsettings", "routemap", data)


def set_ospfsettings_routemap(uuid, data):
    """
    Set/update routemap entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/setRoutemap/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "ospfsettings", "routemap", uuid, data)


def del_ospfsettings_routemap(uuid):
    """
    Delete routemap entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/delRoutemap/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "ospfsettings", "routemap", uuid)


def toggle_ospfsettings_routemap(uuid, enabled=None):
    """
    Toggle routemap entry in quagga/ospfsettings.

    Wraps: POST /api/quagga/ospfsettings/toggleRoutemap/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "ospfsettings", "routemap", uuid, enabled)


# --- static controller ---

def search_route(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search route entries in quagga/static.

    Wraps: POST /api/quagga/static/searchRoute

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("quagga", "static", "route", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_route(uuid=None):
    """
    Get route entry in quagga/static.

    Wraps: GET /api/quagga/static/getRoute/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("quagga", "static", "route", uuid)


def add_route(data):
    """
    Add route entry in quagga/static.

    Wraps: POST /api/quagga/static/addRoute

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("quagga", "static", "route", data)


def set_route(uuid, data):
    """
    Set/update route entry in quagga/static.

    Wraps: POST /api/quagga/static/setRoute/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("quagga", "static", "route", uuid, data)


def del_route(uuid):
    """
    Delete route entry in quagga/static.

    Wraps: POST /api/quagga/static/delRoute/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("quagga", "static", "route", uuid)


def toggle_route(uuid, enabled=None):
    """
    Toggle route entry in quagga/static.

    Wraps: POST /api/quagga/static/toggleRoute/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("quagga", "static", "route", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="bfd", action="reconfigure", data=None):
    """
    Generic reconfigure for quagga.

    Wraps: POST /api/quagga/{controller}/{action}

    :param controller: Controller name, default bfd
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("quagga", controller, action, data)
