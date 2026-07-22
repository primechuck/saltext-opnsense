# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense vnstat wrappers.

Generated from controllers.json for module vnstat.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/vnstat/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_vnstat"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- service controller ---

def service_daily(data=None, uuid=None):
    """
    Execute daily in vnstat/service.

    Wraps: /api/vnstat/service/daily

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "daily", uuid=uuid, data=data)


def service_get_json_data(data=None, uuid=None):
    """
    Execute getJsonData in vnstat/service.

    Wraps: /api/vnstat/service/getJsonData

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "getJsonData", uuid=uuid, data=data)


def service_hourly(data=None, uuid=None):
    """
    Execute hourly in vnstat/service.

    Wraps: /api/vnstat/service/hourly

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "hourly", uuid=uuid, data=data)


def service_interface_list(data=None, uuid=None):
    """
    Execute interfaceList in vnstat/service.

    Wraps: /api/vnstat/service/interfaceList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "interfaceList", uuid=uuid, data=data)


def service_monthly(data=None, uuid=None):
    """
    Execute monthly in vnstat/service.

    Wraps: /api/vnstat/service/monthly

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "monthly", uuid=uuid, data=data)


def service_resetdb(data=None, uuid=None):
    """
    Execute resetdb in vnstat/service.

    Wraps: /api/vnstat/service/resetdb

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "resetdb", uuid=uuid, data=data)


def service_yearly(data=None, uuid=None):
    """
    Execute yearly in vnstat/service.

    Wraps: /api/vnstat/service/yearly

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("vnstat", "service", "yearly", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for vnstat.

    Wraps: POST /api/vnstat/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("vnstat", controller, action, data)
