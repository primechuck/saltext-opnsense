# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense iperf wrappers.

Generated from controllers.json for module iperf.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/iperf/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_iperf"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- instance controller ---

def set_instance(data):
    """
    Set instance singleton config in iperf/instance.

    Wraps: POST /api/iperf/instance/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("iperf", "instance", "set", data=data, method="POST")


def instance_query(data=None, uuid=None):
    """
    Execute query in iperf/instance.

    Wraps: /api/iperf/instance/query

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("iperf", "instance", "query", uuid=uuid, data=data)


# --- service controller ---

def service_restart(data=None):
    """
    Execute restart in iperf/service.

    Wraps: POST /api/iperf/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("iperf", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in iperf/service.

    Wraps: POST /api/iperf/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("iperf", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in iperf/service.

    Wraps: POST /api/iperf/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("iperf", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in iperf/service.

    Wraps: POST /api/iperf/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("iperf", "service", "stop", data=data, method="POST")



# Generic module-level helpers

def reconfigure(controller="instance", action="reconfigure", data=None):
    """
    Generic reconfigure for iperf.

    Wraps: POST /api/iperf/{controller}/{action}

    :param controller: Controller name, default instance
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("iperf", controller, action, data)
