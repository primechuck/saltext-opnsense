# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense bind wrappers.

Generated from controllers.json for module bind.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/bind/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_bind"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- acl controller ---

def search_acl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search acl entries in bind/acl.

    Wraps: POST /api/bind/acl/searchAcl

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "acl", "acl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_acl(uuid=None):
    """
    Get acl entry in bind/acl.

    Wraps: GET /api/bind/acl/getAcl/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("bind", "acl", "acl", uuid)


def add_acl(data):
    """
    Add acl entry in bind/acl.

    Wraps: POST /api/bind/acl/addAcl

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("bind", "acl", "acl", data)


def set_acl(uuid, data):
    """
    Set/update acl entry in bind/acl.

    Wraps: POST /api/bind/acl/setAcl/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("bind", "acl", "acl", uuid, data)


def del_acl(uuid):
    """
    Delete acl entry in bind/acl.

    Wraps: POST /api/bind/acl/delAcl/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("bind", "acl", "acl", uuid)


def toggle_acl(uuid, enabled=None):
    """
    Toggle acl entry in bind/acl.

    Wraps: POST /api/bind/acl/toggleAcl/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("bind", "acl", "acl", uuid, enabled)


# --- domain controller ---

def get_domain(uuid=None):
    """
    Get domain entry in bind/domain.

    Wraps: GET /api/bind/domain/getDomain/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("bind", "domain", "domain", uuid)


def set_domain(uuid, data):
    """
    Set/update domain entry in bind/domain.

    Wraps: POST /api/bind/domain/setDomain/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("bind", "domain", "domain", uuid, data)


def del_domain(uuid):
    """
    Delete domain entry in bind/domain.

    Wraps: POST /api/bind/domain/delDomain/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("bind", "domain", "domain", uuid)


def toggle_domain(uuid, enabled=None):
    """
    Toggle domain entry in bind/domain.

    Wraps: POST /api/bind/domain/toggleDomain/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("bind", "domain", "domain", uuid, enabled)


def search_forward_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search forward_domain entries in bind/domain.

    Wraps: POST /api/bind/domain/searchForwardDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "domain", "forward_domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def add_forward_domain(data):
    """
    Add forward_domain entry in bind/domain.

    Wraps: POST /api/bind/domain/addForwardDomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("bind", "domain", "forward_domain", data)


def search_master_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search master_domain entries in bind/domain.

    Wraps: POST /api/bind/domain/searchMasterDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "domain", "master_domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def search_primary_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search primary_domain entries in bind/domain.

    Wraps: POST /api/bind/domain/searchPrimaryDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "domain", "primary_domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def add_primary_domain(data):
    """
    Add primary_domain entry in bind/domain.

    Wraps: POST /api/bind/domain/addPrimaryDomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("bind", "domain", "primary_domain", data)


def search_secondary_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search secondary_domain entries in bind/domain.

    Wraps: POST /api/bind/domain/searchSecondaryDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "domain", "secondary_domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def add_secondary_domain(data):
    """
    Add secondary_domain entry in bind/domain.

    Wraps: POST /api/bind/domain/addSecondaryDomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("bind", "domain", "secondary_domain", data)


def search_slave_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search slave_domain entries in bind/domain.

    Wraps: POST /api/bind/domain/searchSlaveDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "domain", "slave_domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- general controller ---

def general_zoneshow(data=None, uuid=None):
    """
    Execute zoneshow in bind/general.

    Wraps: /api/bind/general/zoneshow

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("bind", "general", "zoneshow", uuid=uuid, data=data)


def general_zonetest(data=None, uuid=None):
    """
    Execute zonetest in bind/general.

    Wraps: /api/bind/general/zonetest

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("bind", "general", "zonetest", uuid=uuid, data=data)


# --- record controller ---

def search_record(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search record entries in bind/record.

    Wraps: POST /api/bind/record/searchRecord

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("bind", "record", "record", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_record(uuid=None):
    """
    Get record entry in bind/record.

    Wraps: GET /api/bind/record/getRecord/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("bind", "record", "record", uuid)


def add_record(data):
    """
    Add record entry in bind/record.

    Wraps: POST /api/bind/record/addRecord

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("bind", "record", "record", data)


def set_record(uuid, data):
    """
    Set/update record entry in bind/record.

    Wraps: POST /api/bind/record/setRecord/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("bind", "record", "record", uuid, data)


def del_record(uuid):
    """
    Delete record entry in bind/record.

    Wraps: POST /api/bind/record/delRecord/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("bind", "record", "record", uuid)


def toggle_record(uuid, enabled=None):
    """
    Toggle record entry in bind/record.

    Wraps: POST /api/bind/record/toggleRecord/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("bind", "record", "record", uuid, enabled)


# --- service controller ---

def service_dnsbl(data=None, uuid=None):
    """
    Execute dnsbl in bind/service.

    Wraps: /api/bind/service/dnsbl

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("bind", "service", "dnsbl", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="acl", action="reconfigure", data=None):
    """
    Generic reconfigure for bind.

    Wraps: POST /api/bind/{controller}/{action}

    :param controller: Controller name, default acl
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("bind", controller, action, data)
