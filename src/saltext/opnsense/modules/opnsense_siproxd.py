# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense siproxd wrappers.

Generated from controllers.json for module siproxd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/siproxd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_siproxd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- domain controller ---

def search_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search domain entries in siproxd/domain.

    Wraps: POST /api/siproxd/domain/searchDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("siproxd", "domain", "domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_domain(uuid=None):
    """
    Get domain entry in siproxd/domain.

    Wraps: GET /api/siproxd/domain/getDomain/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("siproxd", "domain", "domain", uuid)


def add_domain(data):
    """
    Add domain entry in siproxd/domain.

    Wraps: POST /api/siproxd/domain/addDomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("siproxd", "domain", "domain", data)


def set_domain(uuid, data):
    """
    Set/update domain entry in siproxd/domain.

    Wraps: POST /api/siproxd/domain/setDomain/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("siproxd", "domain", "domain", uuid, data)


def del_domain(uuid):
    """
    Delete domain entry in siproxd/domain.

    Wraps: POST /api/siproxd/domain/delDomain/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("siproxd", "domain", "domain", uuid)


def toggle_domain(uuid, enabled=None):
    """
    Toggle domain entry in siproxd/domain.

    Wraps: POST /api/siproxd/domain/toggleDomain/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("siproxd", "domain", "domain", uuid, enabled)


# --- general controller ---

def get_general():
    """
    Get general singleton config in siproxd/general.

    Wraps: GET /api/siproxd/general/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("siproxd", "general")


def set_general(data):
    """
    Set general singleton config in siproxd/general.

    Wraps: POST /api/siproxd/general/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("siproxd", "general", "set", data=data, method="POST")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in siproxd/service.

    Wraps: POST /api/siproxd/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("siproxd", "service", action, data)


def service_restart(data=None):
    """
    Execute restart in siproxd/service.

    Wraps: POST /api/siproxd/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("siproxd", "service", "restart", data=data, method="POST")


def service_showregistrations(data=None, uuid=None):
    """
    Execute showregistrations in siproxd/service.

    Wraps: /api/siproxd/service/showregistrations

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("siproxd", "service", "showregistrations", uuid=uuid, data=data)


def service_start(data=None):
    """
    Execute start in siproxd/service.

    Wraps: POST /api/siproxd/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("siproxd", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in siproxd/service.

    Wraps: POST /api/siproxd/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("siproxd", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in siproxd/service.

    Wraps: POST /api/siproxd/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("siproxd", "service", "stop", data=data, method="POST")


# --- user controller ---

def search_user(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search user entries in siproxd/user.

    Wraps: POST /api/siproxd/user/searchUser

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("siproxd", "user", "user", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_user(uuid=None):
    """
    Get user entry in siproxd/user.

    Wraps: GET /api/siproxd/user/getUser/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("siproxd", "user", "user", uuid)


def add_user(data):
    """
    Add user entry in siproxd/user.

    Wraps: POST /api/siproxd/user/addUser

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("siproxd", "user", "user", data)


def set_user(uuid, data):
    """
    Set/update user entry in siproxd/user.

    Wraps: POST /api/siproxd/user/setUser/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("siproxd", "user", "user", uuid, data)


def del_user(uuid):
    """
    Delete user entry in siproxd/user.

    Wraps: POST /api/siproxd/user/delUser/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("siproxd", "user", "user", uuid)


def toggle_user(uuid, enabled=None):
    """
    Toggle user entry in siproxd/user.

    Wraps: POST /api/siproxd/user/toggleUser/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("siproxd", "user", "user", uuid, enabled)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for siproxd.

    Wraps: POST /api/siproxd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("siproxd", controller, action, data)
