# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense tor wrappers.

Generated from controllers.json for module tor.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/tor/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_tor"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- exitacl controller ---

def search_exitacl_acl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search acl entries in tor/exitacl.

    Wraps: POST /api/tor/exitacl/searchacl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tor", "exitacl", "acl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_exitacl_acl(uuid=None):
    """
    Get acl entry in tor/exitacl.

    Wraps: GET /api/tor/exitacl/getacl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tor", "exitacl", "acl", uuid)


def add_exitacl_acl(data):
    """
    Add acl entry in tor/exitacl.

    Wraps: POST /api/tor/exitacl/addacl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tor", "exitacl", "acl", data)


def set_exitacl_acl(uuid, data):
    """
    Set/update acl entry in tor/exitacl.

    Wraps: POST /api/tor/exitacl/setacl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tor", "exitacl", "acl", uuid, data)


def del_exitacl_acl(uuid):
    """
    Delete acl entry in tor/exitacl.

    Wraps: POST /api/tor/exitacl/delacl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tor", "exitacl", "acl", uuid)


def toggle_exitacl_acl(uuid, enabled=None):
    """
    Toggle acl entry in tor/exitacl.

    Wraps: POST /api/tor/exitacl/toggleacl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tor", "exitacl", "acl", uuid, enabled)


# --- general controller ---

def search_hidservauth(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search hidservauth entries in tor/general.

    Wraps: POST /api/tor/general/searchhidservauth

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tor", "general", "hidservauth", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_hidservauth(uuid=None):
    """
    Get hidservauth entry in tor/general.

    Wraps: GET /api/tor/general/gethidservauth/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tor", "general", "hidservauth", uuid)


def add_hidservauth(data):
    """
    Add hidservauth entry in tor/general.

    Wraps: POST /api/tor/general/addhidservauth

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tor", "general", "hidservauth", data)


def set_hidservauth(uuid, data):
    """
    Set/update hidservauth entry in tor/general.

    Wraps: POST /api/tor/general/sethidservauth/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tor", "general", "hidservauth", uuid, data)


def del_hidservauth(uuid):
    """
    Delete hidservauth entry in tor/general.

    Wraps: POST /api/tor/general/delhidservauth/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tor", "general", "hidservauth", uuid)


def toggle_hidservauth(uuid, enabled=None):
    """
    Toggle hidservauth entry in tor/general.

    Wraps: POST /api/tor/general/togglehidservauth/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tor", "general", "hidservauth", uuid, enabled)


# --- hiddenservice controller ---

def search_service(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search service entries in tor/hiddenservice.

    Wraps: POST /api/tor/hiddenservice/searchservice

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tor", "hiddenservice", "service", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_service(uuid=None):
    """
    Get service entry in tor/hiddenservice.

    Wraps: GET /api/tor/hiddenservice/getservice/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tor", "hiddenservice", "service", uuid)


def add_service(data):
    """
    Add service entry in tor/hiddenservice.

    Wraps: POST /api/tor/hiddenservice/addservice

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tor", "hiddenservice", "service", data)


def set_service(uuid, data):
    """
    Set/update service entry in tor/hiddenservice.

    Wraps: POST /api/tor/hiddenservice/setservice/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tor", "hiddenservice", "service", uuid, data)


def del_service(uuid):
    """
    Delete service entry in tor/hiddenservice.

    Wraps: POST /api/tor/hiddenservice/delservice/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tor", "hiddenservice", "service", uuid)


def toggle_service(uuid, enabled=None):
    """
    Toggle service entry in tor/hiddenservice.

    Wraps: POST /api/tor/hiddenservice/toggleservice/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tor", "hiddenservice", "service", uuid, enabled)


# --- hiddenserviceacl controller ---

def search_hiddenserviceacl_acl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search acl entries in tor/hiddenserviceacl.

    Wraps: POST /api/tor/hiddenserviceacl/searchacl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tor", "hiddenserviceacl", "acl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_hiddenserviceacl_acl(uuid=None):
    """
    Get acl entry in tor/hiddenserviceacl.

    Wraps: GET /api/tor/hiddenserviceacl/getacl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tor", "hiddenserviceacl", "acl", uuid)


def add_hiddenserviceacl_acl(data):
    """
    Add acl entry in tor/hiddenserviceacl.

    Wraps: POST /api/tor/hiddenserviceacl/addacl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tor", "hiddenserviceacl", "acl", data)


def set_hiddenserviceacl_acl(uuid, data):
    """
    Set/update acl entry in tor/hiddenserviceacl.

    Wraps: POST /api/tor/hiddenserviceacl/setacl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tor", "hiddenserviceacl", "acl", uuid, data)


def del_hiddenserviceacl_acl(uuid):
    """
    Delete acl entry in tor/hiddenserviceacl.

    Wraps: POST /api/tor/hiddenserviceacl/delacl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tor", "hiddenserviceacl", "acl", uuid)


def toggle_hiddenserviceacl_acl(uuid, enabled=None):
    """
    Toggle acl entry in tor/hiddenserviceacl.

    Wraps: POST /api/tor/hiddenserviceacl/toggleacl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tor", "hiddenserviceacl", "acl", uuid, enabled)


# --- service controller ---

def service_circuits(data=None, uuid=None):
    """
    Execute circuits in tor/service.

    Wraps: /api/tor/service/circuits

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "circuits", uuid=uuid, data=data)


def service_get_hidden_services(data=None, uuid=None):
    """
    Execute getHiddenServices in tor/service.

    Wraps: /api/tor/service/getHiddenServices

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "getHiddenServices", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in tor/service.

    Wraps: POST /api/tor/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("tor", "service", action, data)


def service_restart(data=None):
    """
    Execute restart in tor/service.

    Wraps: POST /api/tor/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in tor/service.

    Wraps: POST /api/tor/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in tor/service.

    Wraps: POST /api/tor/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in tor/service.

    Wraps: POST /api/tor/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "stop", data=data, method="POST")


def service_streams(data=None, uuid=None):
    """
    Execute streams in tor/service.

    Wraps: /api/tor/service/streams

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("tor", "service", "streams", uuid=uuid, data=data)


# --- socksacl controller ---

def search_socksacl_acl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search acl entries in tor/socksacl.

    Wraps: POST /api/tor/socksacl/searchacl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("tor", "socksacl", "acl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_socksacl_acl(uuid=None):
    """
    Get acl entry in tor/socksacl.

    Wraps: GET /api/tor/socksacl/getacl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("tor", "socksacl", "acl", uuid)


def add_socksacl_acl(data):
    """
    Add acl entry in tor/socksacl.

    Wraps: POST /api/tor/socksacl/addacl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("tor", "socksacl", "acl", data)


def set_socksacl_acl(uuid, data):
    """
    Set/update acl entry in tor/socksacl.

    Wraps: POST /api/tor/socksacl/setacl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("tor", "socksacl", "acl", uuid, data)


def del_socksacl_acl(uuid):
    """
    Delete acl entry in tor/socksacl.

    Wraps: POST /api/tor/socksacl/delacl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("tor", "socksacl", "acl", uuid)


def toggle_socksacl_acl(uuid, enabled=None):
    """
    Toggle acl entry in tor/socksacl.

    Wraps: POST /api/tor/socksacl/toggleacl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("tor", "socksacl", "acl", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for tor.

    Wraps: POST /api/tor/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("tor", controller, action, data)
