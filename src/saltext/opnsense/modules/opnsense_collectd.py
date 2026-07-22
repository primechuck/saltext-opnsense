# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense collectd wrappers.

Generated from controllers.json for module collectd.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/collectd/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_collectd"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- general controller ---

def get_general():
    """
    Get general singleton config in collectd/general.

    Wraps: GET /api/collectd/general/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("collectd", "general")


def set_general(data):
    """
    Set general singleton config in collectd/general.

    Wraps: POST /api/collectd/general/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("collectd", "general", "set", data=data, method="POST")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in collectd/service.

    Wraps: POST /api/collectd/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("collectd", "service", action, data)


def service_restart(data=None):
    """
    Execute restart in collectd/service.

    Wraps: POST /api/collectd/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("collectd", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in collectd/service.

    Wraps: POST /api/collectd/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("collectd", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in collectd/service.

    Wraps: POST /api/collectd/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("collectd", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in collectd/service.

    Wraps: POST /api/collectd/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("collectd", "service", "stop", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for collectd.

    Wraps: POST /api/collectd/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("collectd", controller, action, data)
