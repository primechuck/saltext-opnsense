# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense proxy wrappers.

Generated from controllers.json for module proxy.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/proxy/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_proxy"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- acl controller ---

def search_custom_policy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search custom_policy entries in proxy/acl.

    Wraps: POST /api/proxy/acl/searchCustomPolicy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("proxy", "acl", "custom_policy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_custom_policy(uuid=None):
    """
    Get custom_policy entry in proxy/acl.

    Wraps: GET /api/proxy/acl/getCustomPolicy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("proxy", "acl", "custom_policy", uuid)


def add_custom_policy(data):
    """
    Add custom_policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/addCustomPolicy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("proxy", "acl", "custom_policy", data)


def set_custom_policy(uuid, data):
    """
    Set/update custom_policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/setCustomPolicy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("proxy", "acl", "custom_policy", uuid, data)


def del_custom_policy(uuid):
    """
    Delete custom_policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/delCustomPolicy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("proxy", "acl", "custom_policy", uuid)


def toggle_custom_policy(uuid, enabled=None):
    """
    Toggle custom_policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/toggleCustomPolicy/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("proxy", "acl", "custom_policy", uuid, enabled)


def search_policy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search policy entries in proxy/acl.

    Wraps: POST /api/proxy/acl/searchPolicy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("proxy", "acl", "policy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_policy(uuid=None):
    """
    Get policy entry in proxy/acl.

    Wraps: GET /api/proxy/acl/getPolicy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("proxy", "acl", "policy", uuid)


def add_policy(data):
    """
    Add policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/addPolicy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("proxy", "acl", "policy", data)


def set_policy(uuid, data):
    """
    Set/update policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/setPolicy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("proxy", "acl", "policy", uuid, data)


def del_policy(uuid):
    """
    Delete policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/delPolicy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("proxy", "acl", "policy", uuid)


def toggle_policy(uuid, enabled=None):
    """
    Toggle policy entry in proxy/acl.

    Wraps: POST /api/proxy/acl/togglePolicy/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("proxy", "acl", "policy", uuid, enabled)


def acl_apply(data=None):
    """
    Execute apply in proxy/acl.

    Wraps: POST /api/proxy/acl/apply

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "acl", "apply", data=data, method="POST")


def acl_test(data=None, uuid=None):
    """
    Execute test in proxy/acl.

    Wraps: /api/proxy/acl/test

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "acl", "test", uuid=uuid, data=data)


# --- service controller ---

def service_downloadacls(data=None, uuid=None):
    """
    Execute downloadacls in proxy/service.

    Wraps: /api/proxy/service/downloadacls

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "service", "downloadacls", uuid=uuid, data=data)


def service_fetchacls(data=None, uuid=None):
    """
    Execute fetchacls in proxy/service.

    Wraps: /api/proxy/service/fetchacls

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "service", "fetchacls", uuid=uuid, data=data)


def service_refresh_template(data=None, uuid=None):
    """
    Execute refreshTemplate in proxy/service.

    Wraps: /api/proxy/service/refreshTemplate

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "service", "refreshTemplate", uuid=uuid, data=data)


def service_reset(data=None, uuid=None):
    """
    Execute reset in proxy/service.

    Wraps: /api/proxy/service/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "service", "reset", uuid=uuid, data=data)


def service_restart(data=None):
    """
    Execute restart in proxy/service.

    Wraps: POST /api/proxy/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in proxy/service.

    Wraps: POST /api/proxy/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "service", "start", data=data, method="POST")


# --- settings controller ---

def search_pac_match(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search pac_match entries in proxy/settings.

    Wraps: POST /api/proxy/settings/searchPacMatch

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("proxy", "settings", "pac_match", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_pac_match(uuid=None):
    """
    Get pac_match entry in proxy/settings.

    Wraps: GET /api/proxy/settings/getPacMatch/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("proxy", "settings", "pac_match", uuid)


def add_pac_match(data):
    """
    Add pac_match entry in proxy/settings.

    Wraps: POST /api/proxy/settings/addPacMatch

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("proxy", "settings", "pac_match", data)


def set_pac_match(uuid, data):
    """
    Set/update pac_match entry in proxy/settings.

    Wraps: POST /api/proxy/settings/setPacMatch/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("proxy", "settings", "pac_match", uuid, data)


def del_pac_match(uuid):
    """
    Delete pac_match entry in proxy/settings.

    Wraps: POST /api/proxy/settings/delPacMatch/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("proxy", "settings", "pac_match", uuid)


def search_pac_proxy(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search pac_proxy entries in proxy/settings.

    Wraps: POST /api/proxy/settings/searchPacProxy

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("proxy", "settings", "pac_proxy", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_pac_proxy(uuid=None):
    """
    Get pac_proxy entry in proxy/settings.

    Wraps: GET /api/proxy/settings/getPacProxy/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("proxy", "settings", "pac_proxy", uuid)


def add_pac_proxy(data):
    """
    Add pac_proxy entry in proxy/settings.

    Wraps: POST /api/proxy/settings/addPacProxy

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("proxy", "settings", "pac_proxy", data)


def set_pac_proxy(uuid, data):
    """
    Set/update pac_proxy entry in proxy/settings.

    Wraps: POST /api/proxy/settings/setPacProxy/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("proxy", "settings", "pac_proxy", uuid, data)


def del_pac_proxy(uuid):
    """
    Delete pac_proxy entry in proxy/settings.

    Wraps: POST /api/proxy/settings/delPacProxy/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("proxy", "settings", "pac_proxy", uuid)


def search_pac_rule(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search pac_rule entries in proxy/settings.

    Wraps: POST /api/proxy/settings/searchPacRule

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("proxy", "settings", "pac_rule", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_pac_rule(uuid=None):
    """
    Get pac_rule entry in proxy/settings.

    Wraps: GET /api/proxy/settings/getPacRule/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("proxy", "settings", "pac_rule", uuid)


def add_pac_rule(data):
    """
    Add pac_rule entry in proxy/settings.

    Wraps: POST /api/proxy/settings/addPACRule

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("proxy", "settings", "pac_rule", data)


def set_pac_rule(uuid, data):
    """
    Set/update pac_rule entry in proxy/settings.

    Wraps: POST /api/proxy/settings/setPacRule/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("proxy", "settings", "pac_rule", uuid, data)


def del_pac_rule(uuid):
    """
    Delete pac_rule entry in proxy/settings.

    Wraps: POST /api/proxy/settings/delPacRule/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("proxy", "settings", "pac_rule", uuid)


def toggle_pac_rule(uuid, enabled=None):
    """
    Toggle pac_rule entry in proxy/settings.

    Wraps: POST /api/proxy/settings/togglePacRule/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("proxy", "settings", "pac_rule", uuid, enabled)


def get_remote_blacklist(uuid=None):
    """
    Get remote_blacklist entry in proxy/settings.

    Wraps: GET /api/proxy/settings/getRemoteBlacklist/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("proxy", "settings", "remote_blacklist", uuid)


def add_remote_blacklist(data):
    """
    Add remote_blacklist entry in proxy/settings.

    Wraps: POST /api/proxy/settings/addRemoteBlacklist

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("proxy", "settings", "remote_blacklist", data)


def set_remote_blacklist(uuid, data):
    """
    Set/update remote_blacklist entry in proxy/settings.

    Wraps: POST /api/proxy/settings/setRemoteBlacklist/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("proxy", "settings", "remote_blacklist", uuid, data)


def del_remote_blacklist(uuid):
    """
    Delete remote_blacklist entry in proxy/settings.

    Wraps: POST /api/proxy/settings/delRemoteBlacklist/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("proxy", "settings", "remote_blacklist", uuid)


def toggle_remote_blacklist(uuid, enabled=None):
    """
    Toggle remote_blacklist entry in proxy/settings.

    Wraps: POST /api/proxy/settings/toggleRemoteBlacklist/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("proxy", "settings", "remote_blacklist", uuid, enabled)


def search_remote_blacklists(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search remote_blacklists entries in proxy/settings.

    Wraps: POST /api/proxy/settings/searchRemoteBlacklists

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("proxy", "settings", "remote_blacklists", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def settings_fetch_rb_cron(data=None, uuid=None):
    """
    Execute fetchRbCron in proxy/settings.

    Wraps: /api/proxy/settings/fetchRbCron

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "settings", "fetchRbCron", uuid=uuid, data=data)


# --- template controller ---

def get_template():
    """
    Get template singleton config in proxy/template.

    Wraps: GET /api/proxy/template/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("proxy", "template")


def set_template(data):
    """
    Set template singleton config in proxy/template.

    Wraps: POST /api/proxy/template/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("proxy", "template", "set", data=data, method="POST")


def template_reset(data=None, uuid=None):
    """
    Execute reset in proxy/template.

    Wraps: /api/proxy/template/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("proxy", "template", "reset", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="acl", action="reconfigure", data=None):
    """
    Generic reconfigure for proxy.

    Wraps: POST /api/proxy/{controller}/{action}

    :param controller: Controller name, default acl
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("proxy", controller, action, data)
