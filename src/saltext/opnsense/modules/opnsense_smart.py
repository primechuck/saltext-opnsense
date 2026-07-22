# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense smart wrappers.

Generated from controllers.json for module smart.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/smart/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_smart"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_abort(data=None, uuid=None):
    """
    Execute abort in smart/service.

    Wraps: /api/smart/service/abort

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("smart", "service", "abort", uuid=uuid, data=data)


def service_info(data=None, uuid=None):
    """
    Execute info in smart/service.

    Wraps: /api/smart/service/info

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("smart", "service", "info", uuid=uuid, data=data)


def service_list(data=None, uuid=None):
    """
    Execute list in smart/service.

    Wraps: /api/smart/service/list

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("smart", "service", "list", uuid=uuid, data=data)


def service_logs(data=None, uuid=None):
    """
    Execute logs in smart/service.

    Wraps: /api/smart/service/logs

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("smart", "service", "logs", uuid=uuid, data=data)


def service_test(data=None, uuid=None):
    """
    Execute test in smart/service.

    Wraps: /api/smart/service/test

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("smart", "service", "test", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for smart.

    Wraps: POST /api/smart/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("smart", controller, action, data)
