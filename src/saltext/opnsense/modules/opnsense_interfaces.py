# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense interfaces wrappers.

Generated from controllers.json for module interfaces.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/interfaces/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_interfaces"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- assignment controller ---

def search_assignment_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/assignment.

    Wraps: POST /api/interfaces/assignment/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "assignment", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_assignment_item(uuid=None):
    """
    Get item entry in interfaces/assignment.

    Wraps: GET /api/interfaces/assignment/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "assignment", "item", uuid)


def add_assignment_item(data):
    """
    Add item entry in interfaces/assignment.

    Wraps: POST /api/interfaces/assignment/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "assignment", "item", data)


def set_assignment_item(uuid, data):
    """
    Set/update item entry in interfaces/assignment.

    Wraps: POST /api/interfaces/assignment/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "assignment", "item", uuid, data)


def del_assignment_item(uuid):
    """
    Delete item entry in interfaces/assignment.

    Wraps: POST /api/interfaces/assignment/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "assignment", "item", uuid)


def assignment_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/assignment.

    Wraps: POST /api/interfaces/assignment/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "assignment", action, data)


# --- bridgesettings controller ---

def search_bridgesettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/bridgesettings.

    Wraps: POST /api/interfaces/bridgesettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "bridgesettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_bridgesettings_item(uuid=None):
    """
    Get item entry in interfaces/bridgesettings.

    Wraps: GET /api/interfaces/bridgesettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "bridgesettings", "item", uuid)


def add_bridgesettings_item(data):
    """
    Add item entry in interfaces/bridgesettings.

    Wraps: POST /api/interfaces/bridgesettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "bridgesettings", "item", data)


def set_bridgesettings_item(uuid, data):
    """
    Set/update item entry in interfaces/bridgesettings.

    Wraps: POST /api/interfaces/bridgesettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "bridgesettings", "item", uuid, data)


def del_bridgesettings_item(uuid):
    """
    Delete item entry in interfaces/bridgesettings.

    Wraps: POST /api/interfaces/bridgesettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "bridgesettings", "item", uuid)


def bridgesettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/bridgesettings.

    Wraps: POST /api/interfaces/bridgesettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "bridgesettings", action, data)


# --- gifsettings controller ---

def search_gifsettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/gifsettings.

    Wraps: POST /api/interfaces/gifsettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "gifsettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_gifsettings_item(uuid=None):
    """
    Get item entry in interfaces/gifsettings.

    Wraps: GET /api/interfaces/gifsettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "gifsettings", "item", uuid)


def add_gifsettings_item(data):
    """
    Add item entry in interfaces/gifsettings.

    Wraps: POST /api/interfaces/gifsettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "gifsettings", "item", data)


def set_gifsettings_item(uuid, data):
    """
    Set/update item entry in interfaces/gifsettings.

    Wraps: POST /api/interfaces/gifsettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "gifsettings", "item", uuid, data)


def del_gifsettings_item(uuid):
    """
    Delete item entry in interfaces/gifsettings.

    Wraps: POST /api/interfaces/gifsettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "gifsettings", "item", uuid)


def gifsettings_get_if_options(data=None, uuid=None):
    """
    Execute getIfOptions in interfaces/gifsettings.

    Wraps: /api/interfaces/gifsettings/getIfOptions

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "gifsettings", "getIfOptions", uuid=uuid, data=data)


def gifsettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/gifsettings.

    Wraps: POST /api/interfaces/gifsettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "gifsettings", action, data)


# --- gresettings controller ---

def search_gresettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/gresettings.

    Wraps: POST /api/interfaces/gresettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "gresettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_gresettings_item(uuid=None):
    """
    Get item entry in interfaces/gresettings.

    Wraps: GET /api/interfaces/gresettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "gresettings", "item", uuid)


def add_gresettings_item(data):
    """
    Add item entry in interfaces/gresettings.

    Wraps: POST /api/interfaces/gresettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "gresettings", "item", data)


def set_gresettings_item(uuid, data):
    """
    Set/update item entry in interfaces/gresettings.

    Wraps: POST /api/interfaces/gresettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "gresettings", "item", uuid, data)


def del_gresettings_item(uuid):
    """
    Delete item entry in interfaces/gresettings.

    Wraps: POST /api/interfaces/gresettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "gresettings", "item", uuid)


def gresettings_get_if_options(data=None, uuid=None):
    """
    Execute getIfOptions in interfaces/gresettings.

    Wraps: /api/interfaces/gresettings/getIfOptions

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "gresettings", "getIfOptions", uuid=uuid, data=data)


def gresettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/gresettings.

    Wraps: POST /api/interfaces/gresettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "gresettings", action, data)


# --- laggsettings controller ---

def search_laggsettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/laggsettings.

    Wraps: POST /api/interfaces/laggsettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "laggsettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_laggsettings_item(uuid=None):
    """
    Get item entry in interfaces/laggsettings.

    Wraps: GET /api/interfaces/laggsettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "laggsettings", "item", uuid)


def add_laggsettings_item(data):
    """
    Add item entry in interfaces/laggsettings.

    Wraps: POST /api/interfaces/laggsettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "laggsettings", "item", data)


def set_laggsettings_item(uuid, data):
    """
    Set/update item entry in interfaces/laggsettings.

    Wraps: POST /api/interfaces/laggsettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "laggsettings", "item", uuid, data)


def del_laggsettings_item(uuid):
    """
    Delete item entry in interfaces/laggsettings.

    Wraps: POST /api/interfaces/laggsettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "laggsettings", "item", uuid)


def laggsettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/laggsettings.

    Wraps: POST /api/interfaces/laggsettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "laggsettings", action, data)


# --- loopbacksettings controller ---

def search_loopbacksettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/loopbacksettings.

    Wraps: POST /api/interfaces/loopbacksettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "loopbacksettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_loopbacksettings_item(uuid=None):
    """
    Get item entry in interfaces/loopbacksettings.

    Wraps: GET /api/interfaces/loopbacksettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "loopbacksettings", "item", uuid)


def add_loopbacksettings_item(data):
    """
    Add item entry in interfaces/loopbacksettings.

    Wraps: POST /api/interfaces/loopbacksettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "loopbacksettings", "item", data)


def set_loopbacksettings_item(uuid, data):
    """
    Set/update item entry in interfaces/loopbacksettings.

    Wraps: POST /api/interfaces/loopbacksettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "loopbacksettings", "item", uuid, data)


def del_loopbacksettings_item(uuid):
    """
    Delete item entry in interfaces/loopbacksettings.

    Wraps: POST /api/interfaces/loopbacksettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "loopbacksettings", "item", uuid)


def loopbacksettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/loopbacksettings.

    Wraps: POST /api/interfaces/loopbacksettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "loopbacksettings", action, data)


# --- neighborsettings controller ---

def search_neighborsettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/neighborsettings.

    Wraps: POST /api/interfaces/neighborsettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "neighborsettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_neighborsettings_item(uuid=None):
    """
    Get item entry in interfaces/neighborsettings.

    Wraps: GET /api/interfaces/neighborsettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "neighborsettings", "item", uuid)


def add_neighborsettings_item(data):
    """
    Add item entry in interfaces/neighborsettings.

    Wraps: POST /api/interfaces/neighborsettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "neighborsettings", "item", data)


def set_neighborsettings_item(uuid, data):
    """
    Set/update item entry in interfaces/neighborsettings.

    Wraps: POST /api/interfaces/neighborsettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "neighborsettings", "item", uuid, data)


def del_neighborsettings_item(uuid):
    """
    Delete item entry in interfaces/neighborsettings.

    Wraps: POST /api/interfaces/neighborsettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "neighborsettings", "item", uuid)


def neighborsettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/neighborsettings.

    Wraps: POST /api/interfaces/neighborsettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "neighborsettings", action, data)


# --- overview controller ---

def overview_export(data=None, uuid=None):
    """
    Execute export in interfaces/overview.

    Wraps: /api/interfaces/overview/export

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "overview", "export", uuid=uuid, data=data)


def overview_get_interface(data=None, uuid=None):
    """
    Execute getInterface in interfaces/overview.

    Wraps: /api/interfaces/overview/getInterface

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "overview", "getInterface", uuid=uuid, data=data)


def overview_interfaces_info(data=None, uuid=None):
    """
    Execute interfacesInfo in interfaces/overview.

    Wraps: /api/interfaces/overview/interfacesInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "overview", "interfacesInfo", uuid=uuid, data=data)


def overview_reload_interface(data=None, uuid=None):
    """
    Execute reloadInterface in interfaces/overview.

    Wraps: /api/interfaces/overview/reloadInterface

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "overview", "reloadInterface", uuid=uuid, data=data)


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in interfaces/settings.

    Wraps: GET /api/interfaces/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("interfaces", "settings")


def settings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/settings.

    Wraps: POST /api/interfaces/settings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "settings", action, data)


# --- vipsettings controller ---

def search_vipsettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/vipsettings.

    Wraps: POST /api/interfaces/vipsettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "vipsettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_vipsettings_item(uuid=None):
    """
    Get item entry in interfaces/vipsettings.

    Wraps: GET /api/interfaces/vipsettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "vipsettings", "item", uuid)


def add_vipsettings_item(data):
    """
    Add item entry in interfaces/vipsettings.

    Wraps: POST /api/interfaces/vipsettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "vipsettings", "item", data)


def set_vipsettings_item(uuid, data):
    """
    Set/update item entry in interfaces/vipsettings.

    Wraps: POST /api/interfaces/vipsettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "vipsettings", "item", uuid, data)


def del_vipsettings_item(uuid):
    """
    Delete item entry in interfaces/vipsettings.

    Wraps: POST /api/interfaces/vipsettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "vipsettings", "item", uuid)


def vipsettings_get_unused_vhid(data=None, uuid=None):
    """
    Execute getUnusedVhid in interfaces/vipsettings.

    Wraps: /api/interfaces/vipsettings/getUnusedVhid

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("interfaces", "vipsettings", "getUnusedVhid", uuid=uuid, data=data)


def vipsettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/vipsettings.

    Wraps: POST /api/interfaces/vipsettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "vipsettings", action, data)


# --- vlansettings controller ---

def search_vlansettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/vlansettings.

    Wraps: POST /api/interfaces/vlansettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "vlansettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_vlansettings_item(uuid=None):
    """
    Get item entry in interfaces/vlansettings.

    Wraps: GET /api/interfaces/vlansettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "vlansettings", "item", uuid)


def add_vlansettings_item(data):
    """
    Add item entry in interfaces/vlansettings.

    Wraps: POST /api/interfaces/vlansettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "vlansettings", "item", data)


def set_vlansettings_item(uuid, data):
    """
    Set/update item entry in interfaces/vlansettings.

    Wraps: POST /api/interfaces/vlansettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "vlansettings", "item", uuid, data)


def del_vlansettings_item(uuid):
    """
    Delete item entry in interfaces/vlansettings.

    Wraps: POST /api/interfaces/vlansettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "vlansettings", "item", uuid)


def vlansettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/vlansettings.

    Wraps: POST /api/interfaces/vlansettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "vlansettings", action, data)


# --- vxlansettings controller ---

def search_vxlansettings_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in interfaces/vxlansettings.

    Wraps: POST /api/interfaces/vxlansettings/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("interfaces", "vxlansettings", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_vxlansettings_item(uuid=None):
    """
    Get item entry in interfaces/vxlansettings.

    Wraps: GET /api/interfaces/vxlansettings/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("interfaces", "vxlansettings", "item", uuid)


def add_vxlansettings_item(data):
    """
    Add item entry in interfaces/vxlansettings.

    Wraps: POST /api/interfaces/vxlansettings/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("interfaces", "vxlansettings", "item", data)


def set_vxlansettings_item(uuid, data):
    """
    Set/update item entry in interfaces/vxlansettings.

    Wraps: POST /api/interfaces/vxlansettings/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("interfaces", "vxlansettings", "item", uuid, data)


def del_vxlansettings_item(uuid):
    """
    Delete item entry in interfaces/vxlansettings.

    Wraps: POST /api/interfaces/vxlansettings/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("interfaces", "vxlansettings", "item", uuid)


def vxlansettings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in interfaces/vxlansettings.

    Wraps: POST /api/interfaces/vxlansettings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", "vxlansettings", action, data)



# Generic module-level helpers

def reconfigure(controller="assignment", action="reconfigure", data=None):
    """
    Generic reconfigure for interfaces.

    Wraps: POST /api/interfaces/{controller}/{action}

    :param controller: Controller name, default assignment
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("interfaces", controller, action, data)
