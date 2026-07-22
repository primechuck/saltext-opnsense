# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense proxysso wrappers.

Generated from controllers.json for module proxysso.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/proxysso/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_proxysso"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_createkeytab(data=None, uuid=None):
    """
    Execute createkeytab in proxysso/service.

    Wraps: /api/proxysso/service/createkeytab

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxysso", "service", "createkeytab", uuid=uuid, data=data)


def service_deletekeytab(data=None, uuid=None):
    """
    Execute deletekeytab in proxysso/service.

    Wraps: /api/proxysso/service/deletekeytab

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxysso", "service", "deletekeytab", uuid=uuid, data=data)


def service_get_check_list(data=None, uuid=None):
    """
    Execute getCheckList in proxysso/service.

    Wraps: /api/proxysso/service/getCheckList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxysso", "service", "getCheckList", uuid=uuid, data=data)


def service_showkeytab(data=None, uuid=None):
    """
    Execute showkeytab in proxysso/service.

    Wraps: /api/proxysso/service/showkeytab

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxysso", "service", "showkeytab", uuid=uuid, data=data)


def service_testkerblogin(data=None, uuid=None):
    """
    Execute testkerblogin in proxysso/service.

    Wraps: /api/proxysso/service/testkerblogin

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxysso", "service", "testkerblogin", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for proxysso.

    Wraps: POST /api/proxysso/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("proxysso", controller, action, data)
