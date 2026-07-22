# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense captiveportal wrappers.

Generated from controllers.json for module captiveportal.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/captiveportal/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_captiveportal"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- access controller ---

def access_api(data=None, uuid=None):
    """
    Execute api in captiveportal/access.

    Wraps: /api/captiveportal/access/api

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "access", "api", uuid=uuid, data=data)


def access_logoff(data=None, uuid=None):
    """
    Execute logoff in captiveportal/access.

    Wraps: /api/captiveportal/access/logoff

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "access", "logoff", uuid=uuid, data=data)


def access_logon(data=None, uuid=None):
    """
    Execute logon in captiveportal/access.

    Wraps: /api/captiveportal/access/logon

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "access", "logon", uuid=uuid, data=data)


def access_status(data=None):
    """
    Execute status in captiveportal/access.

    Wraps: POST /api/captiveportal/access/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "access", "status", data=data, method="POST")


# --- service controller ---

def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in captiveportal/service.

    Wraps: POST /api/captiveportal/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("captiveportal", "service", action, data)


# --- session controller ---

def search_session(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search session entries in captiveportal/session.

    Wraps: POST /api/captiveportal/session/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("captiveportal", "session", "session", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def session_connect(data=None, uuid=None):
    """
    Execute connect in captiveportal/session.

    Wraps: /api/captiveportal/session/connect

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "session", "connect", uuid=uuid, data=data)


def session_disconnect(data=None, uuid=None):
    """
    Execute disconnect in captiveportal/session.

    Wraps: /api/captiveportal/session/disconnect

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "session", "disconnect", uuid=uuid, data=data)


def session_list(data=None, uuid=None):
    """
    Execute list in captiveportal/session.

    Wraps: /api/captiveportal/session/list

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "session", "list", uuid=uuid, data=data)


def session_zones(data=None, uuid=None):
    """
    Execute zones in captiveportal/session.

    Wraps: /api/captiveportal/session/zones

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "session", "zones", uuid=uuid, data=data)


# --- settings controller ---

def get_zone(uuid=None):
    """
    Get zone entry in captiveportal/settings.

    Wraps: GET /api/captiveportal/settings/getZone/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("captiveportal", "settings", "zone", uuid)


def add_zone(data):
    """
    Add zone entry in captiveportal/settings.

    Wraps: POST /api/captiveportal/settings/addZone

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("captiveportal", "settings", "zone", data)


def set_zone(uuid, data):
    """
    Set/update zone entry in captiveportal/settings.

    Wraps: POST /api/captiveportal/settings/setZone/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("captiveportal", "settings", "zone", uuid, data)


def del_zone(uuid):
    """
    Delete zone entry in captiveportal/settings.

    Wraps: POST /api/captiveportal/settings/delZone/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("captiveportal", "settings", "zone", uuid)


def toggle_zone(uuid, enabled=None):
    """
    Toggle zone entry in captiveportal/settings.

    Wraps: POST /api/captiveportal/settings/toggleZone/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("captiveportal", "settings", "zone", uuid, enabled)


def search_zones(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search zones entries in captiveportal/settings.

    Wraps: POST /api/captiveportal/settings/searchZones

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("captiveportal", "settings", "zones", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- template controller ---

def get_template(uuid=None):
    """
    Get template entry in captiveportal/template.

    Wraps: GET /api/captiveportal/template/getTemplate/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("captiveportal", "template", "template", uuid)


def del_template(uuid):
    """
    Delete template entry in captiveportal/template.

    Wraps: POST /api/captiveportal/template/delTemplate/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("captiveportal", "template", "template", uuid)


def search_templates(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search templates entries in captiveportal/template.

    Wraps: POST /api/captiveportal/template/searchTemplates

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("captiveportal", "template", "templates", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def template_save_template(data=None, uuid=None):
    """
    Execute saveTemplate in captiveportal/template.

    Wraps: /api/captiveportal/template/saveTemplate

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "template", "saveTemplate", uuid=uuid, data=data)


# --- voucher controller ---

def voucher_drop_expired_vouchers(data=None, uuid=None):
    """
    Execute dropExpiredVouchers in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/dropExpiredVouchers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "dropExpiredVouchers", uuid=uuid, data=data)


def voucher_drop_voucher_group(data=None, uuid=None):
    """
    Execute dropVoucherGroup in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/dropVoucherGroup

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "dropVoucherGroup", uuid=uuid, data=data)


def voucher_expire_voucher(data=None, uuid=None):
    """
    Execute expireVoucher in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/expireVoucher

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "expireVoucher", uuid=uuid, data=data)


def voucher_generate_vouchers(data=None, uuid=None):
    """
    Execute generateVouchers in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/generateVouchers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "generateVouchers", uuid=uuid, data=data)


def voucher_list_providers(data=None, uuid=None):
    """
    Execute listProviders in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/listProviders

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "listProviders", uuid=uuid, data=data)


def voucher_list_voucher_groups(data=None, uuid=None):
    """
    Execute listVoucherGroups in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/listVoucherGroups

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "listVoucherGroups", uuid=uuid, data=data)


def voucher_list_vouchers(data=None, uuid=None):
    """
    Execute listVouchers in captiveportal/voucher.

    Wraps: /api/captiveportal/voucher/listVouchers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("captiveportal", "voucher", "listVouchers", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for captiveportal.

    Wraps: POST /api/captiveportal/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("captiveportal", controller, action, data)
