# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense routes wrappers.

Generated from controllers.json for module routes.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/routes/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_routes"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- gateway controller ---

def gateway_status(data=None):
    """
    Execute status in routes/gateway.

    Wraps: POST /api/routes/gateway/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("routes", "gateway", "status", data=data, method="POST")


# --- routes controller ---

def search_route(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search route entries in routes/routes.

    Wraps: POST /api/routes/routes/searchroute

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("routes", "routes", "route", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_route(uuid=None):
    """
    Get route entry in routes/routes.

    Wraps: GET /api/routes/routes/getroute/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("routes", "routes", "route", uuid)


def add_route(data):
    """
    Add route entry in routes/routes.

    Wraps: POST /api/routes/routes/addroute

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("routes", "routes", "route", data)


def set_route(uuid, data):
    """
    Set/update route entry in routes/routes.

    Wraps: POST /api/routes/routes/setroute/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("routes", "routes", "route", uuid, data)


def del_route(uuid):
    """
    Delete route entry in routes/routes.

    Wraps: POST /api/routes/routes/delroute/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("routes", "routes", "route", uuid)


def toggle_route(uuid, enabled=None):
    """
    Toggle route entry in routes/routes.

    Wraps: POST /api/routes/routes/toggleroute/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("routes", "routes", "route", uuid, enabled)


def routes_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in routes/routes.

    Wraps: POST /api/routes/routes/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("routes", "routes", action, data)



# Generic module-level helpers

def reconfigure(controller="gateway", action="reconfigure", data=None):
    """
    Generic reconfigure for routes.

    Wraps: POST /api/routes/{controller}/{action}

    :param controller: Controller name, default gateway
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("routes", controller, action, data)
