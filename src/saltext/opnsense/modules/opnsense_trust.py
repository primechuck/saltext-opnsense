# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense trust wrappers.

Generated from controllers.json for module trust.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/trust/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_trust"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- ca controller ---

def search_ca(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ca entries in trust/ca.

    Wraps: POST /api/trust/ca/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("trust", "ca", "ca", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ca(uuid=None):
    """
    Get ca entry in trust/ca.

    Wraps: GET /api/trust/ca/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("trust", "ca", "ca", uuid)


def add_ca(data):
    """
    Add ca entry in trust/ca.

    Wraps: POST /api/trust/ca/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("trust", "ca", "ca", data)


def set_ca(uuid, data):
    """
    Set/update ca entry in trust/ca.

    Wraps: POST /api/trust/ca/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("trust", "ca", "ca", uuid, data)


def del_ca(uuid):
    """
    Delete ca entry in trust/ca.

    Wraps: POST /api/trust/ca/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("trust", "ca", "ca", uuid)


def ca_ca_info(data=None, uuid=None):
    """
    Execute caInfo in trust/ca.

    Wraps: /api/trust/ca/caInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "ca", "caInfo", uuid=uuid, data=data)


def ca_ca_list(data=None, uuid=None):
    """
    Execute caList in trust/ca.

    Wraps: /api/trust/ca/caList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "ca", "caList", uuid=uuid, data=data)


def ca_generate_file(data=None, uuid=None):
    """
    Execute generateFile in trust/ca.

    Wraps: /api/trust/ca/generateFile

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "ca", "generateFile", uuid=uuid, data=data)


def ca_raw_dump(data=None, uuid=None):
    """
    Execute rawDump in trust/ca.

    Wraps: /api/trust/ca/rawDump

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "ca", "rawDump", uuid=uuid, data=data)


# --- cert controller ---

def search_cert(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search cert entries in trust/cert.

    Wraps: POST /api/trust/cert/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("trust", "cert", "cert", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_cert(uuid=None):
    """
    Get cert entry in trust/cert.

    Wraps: GET /api/trust/cert/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("trust", "cert", "cert", uuid)


def add_cert(data):
    """
    Add cert entry in trust/cert.

    Wraps: POST /api/trust/cert/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("trust", "cert", "cert", data)


def set_cert(uuid, data):
    """
    Set/update cert entry in trust/cert.

    Wraps: POST /api/trust/cert/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("trust", "cert", "cert", uuid, data)


def del_cert(uuid):
    """
    Delete cert entry in trust/cert.

    Wraps: POST /api/trust/cert/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("trust", "cert", "cert", uuid)


def cert_ca_info(data=None, uuid=None):
    """
    Execute caInfo in trust/cert.

    Wraps: /api/trust/cert/caInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "cert", "caInfo", uuid=uuid, data=data)


def cert_ca_list(data=None, uuid=None):
    """
    Execute caList in trust/cert.

    Wraps: /api/trust/cert/caList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "cert", "caList", uuid=uuid, data=data)


def cert_generate_file(data=None, uuid=None):
    """
    Execute generateFile in trust/cert.

    Wraps: /api/trust/cert/generateFile

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "cert", "generateFile", uuid=uuid, data=data)


def cert_raw_dump(data=None, uuid=None):
    """
    Execute rawDump in trust/cert.

    Wraps: /api/trust/cert/rawDump

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "cert", "rawDump", uuid=uuid, data=data)


def cert_user_list(data=None, uuid=None):
    """
    Execute userList in trust/cert.

    Wraps: /api/trust/cert/userList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "cert", "userList", uuid=uuid, data=data)


# --- crl controller ---

def search_crl(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search crl entries in trust/crl.

    Wraps: POST /api/trust/crl/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("trust", "crl", "crl", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_crl(uuid=None):
    """
    Get crl entry in trust/crl.

    Wraps: GET /api/trust/crl/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("trust", "crl", "crl", uuid)


def set_crl(uuid, data):
    """
    Set/update crl entry in trust/crl.

    Wraps: POST /api/trust/crl/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("trust", "crl", "crl", uuid, data)


def del_crl(uuid):
    """
    Delete crl entry in trust/crl.

    Wraps: POST /api/trust/crl/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("trust", "crl", "crl", uuid)


def crl_raw_dump(data=None, uuid=None):
    """
    Execute rawDump in trust/crl.

    Wraps: /api/trust/crl/rawDump

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("trust", "crl", "rawDump", uuid=uuid, data=data)


# --- settings controller ---

def settings_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in trust/settings.

    Wraps: POST /api/trust/settings/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("trust", "settings", action, data)



# Generic module-level helpers

def reconfigure(controller="ca", action="reconfigure", data=None):
    """
    Generic reconfigure for trust.

    Wraps: POST /api/trust/{controller}/{action}

    :param controller: Controller name, default ca
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("trust", controller, action, data)
