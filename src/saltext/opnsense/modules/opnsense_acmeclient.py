# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense acmeclient wrappers.

Generated from controllers.json for module acmeclient.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/acmeclient/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_acmeclient"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- accounts controller ---

def search_account(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search account entries in acmeclient/accounts.

    Wraps: POST /api/acmeclient/accounts/searchAccount

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("acmeclient", "accounts", "account", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_account(uuid=None):
    """
    Get account entry in acmeclient/accounts.

    Wraps: GET /api/acmeclient/accounts/getAccount/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("acmeclient", "accounts", "account", uuid)


def add_account(data):
    """
    Add account entry in acmeclient/accounts.

    Wraps: POST /api/acmeclient/accounts/addAccount

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("acmeclient", "accounts", "account", data)


def set_account(uuid, data):
    """
    Set/update account entry in acmeclient/accounts.

    Wraps: POST /api/acmeclient/accounts/setAccount/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("acmeclient", "accounts", "account", uuid, data)


def del_account(uuid):
    """
    Delete account entry in acmeclient/accounts.

    Wraps: POST /api/acmeclient/accounts/delAccount/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("acmeclient", "accounts", "account", uuid)


def toggle_account(uuid, enabled=None):
    """
    Toggle account entry in acmeclient/accounts.

    Wraps: POST /api/acmeclient/accounts/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("acmeclient", "accounts", "account", uuid, enabled)


def accounts_register(data=None, uuid=None):
    """
    Execute register in acmeclient/accounts.

    Wraps: /api/acmeclient/accounts/register

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "accounts", "register", uuid=uuid, data=data)


def accounts_register_account(data=None, uuid=None):
    """
    Execute registerAccount in acmeclient/accounts.

    Wraps: /api/acmeclient/accounts/registerAccount

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "accounts", "registerAccount", uuid=uuid, data=data)


def accounts_update(data=None, uuid=None):
    """
    Execute update in acmeclient/accounts.

    Wraps: /api/acmeclient/accounts/update

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "accounts", "update", uuid=uuid, data=data)


# --- actions controller ---

def search_action(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search action entries in acmeclient/actions.

    Wraps: POST /api/acmeclient/actions/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("acmeclient", "actions", "action", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_action(uuid=None):
    """
    Get action entry in acmeclient/actions.

    Wraps: GET /api/acmeclient/actions/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("acmeclient", "actions", "action", uuid)


def add_action(data):
    """
    Add action entry in acmeclient/actions.

    Wraps: POST /api/acmeclient/actions/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("acmeclient", "actions", "action", data)


def del_action(uuid):
    """
    Delete action entry in acmeclient/actions.

    Wraps: POST /api/acmeclient/actions/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("acmeclient", "actions", "action", uuid)


def toggle_action(uuid, enabled=None):
    """
    Toggle action entry in acmeclient/actions.

    Wraps: POST /api/acmeclient/actions/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("acmeclient", "actions", "action", uuid, enabled)


def actions_sftp_get_identity(data=None, uuid=None):
    """
    Execute sftpGetIdentity in acmeclient/actions.

    Wraps: /api/acmeclient/actions/sftpGetIdentity

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "actions", "sftpGetIdentity", uuid=uuid, data=data)


def actions_sftp_test_connection(data=None, uuid=None):
    """
    Execute sftpTestConnection in acmeclient/actions.

    Wraps: /api/acmeclient/actions/sftpTestConnection

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "actions", "sftpTestConnection", uuid=uuid, data=data)


def actions_ssh_get_identity(data=None, uuid=None):
    """
    Execute sshGetIdentity in acmeclient/actions.

    Wraps: /api/acmeclient/actions/sshGetIdentity

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "actions", "sshGetIdentity", uuid=uuid, data=data)


def actions_ssh_test_connection(data=None, uuid=None):
    """
    Execute sshTestConnection in acmeclient/actions.

    Wraps: /api/acmeclient/actions/sshTestConnection

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "actions", "sshTestConnection", uuid=uuid, data=data)


def actions_update(data=None, uuid=None):
    """
    Execute update in acmeclient/actions.

    Wraps: /api/acmeclient/actions/update

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "actions", "update", uuid=uuid, data=data)


# --- certificates controller ---

def search_certificate(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search certificate entries in acmeclient/certificates.

    Wraps: POST /api/acmeclient/certificates/searchCertificate

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("acmeclient", "certificates", "certificate", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_certificate(uuid=None):
    """
    Get certificate entry in acmeclient/certificates.

    Wraps: GET /api/acmeclient/certificates/getCertificate/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("acmeclient", "certificates", "certificate", uuid)


def add_certificate(data):
    """
    Add certificate entry in acmeclient/certificates.

    Wraps: POST /api/acmeclient/certificates/addCertificate

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("acmeclient", "certificates", "certificate", data)


def set_certificate(uuid, data):
    """
    Set/update certificate entry in acmeclient/certificates.

    Wraps: POST /api/acmeclient/certificates/setCertificate/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("acmeclient", "certificates", "certificate", uuid, data)


def del_certificate(uuid):
    """
    Delete certificate entry in acmeclient/certificates.

    Wraps: POST /api/acmeclient/certificates/delCertificate/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("acmeclient", "certificates", "certificate", uuid)


def toggle_certificate(uuid, enabled=None):
    """
    Toggle certificate entry in acmeclient/certificates.

    Wraps: POST /api/acmeclient/certificates/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("acmeclient", "certificates", "certificate", uuid, enabled)


def certificates_automation(data=None, uuid=None):
    """
    Execute automation in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/automation

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "automation", uuid=uuid, data=data)


def certificates_import(data=None, uuid=None):
    """
    Execute import in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/import

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "import", uuid=uuid, data=data)


def certificates_removekey(data=None, uuid=None):
    """
    Execute removekey in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/removekey

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "removekey", uuid=uuid, data=data)


def certificates_revoke(data=None, uuid=None):
    """
    Execute revoke in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/revoke

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "revoke", uuid=uuid, data=data)


def certificates_revoke_certificate(data=None, uuid=None):
    """
    Execute revokeCertificate in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/revokeCertificate

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "revokeCertificate", uuid=uuid, data=data)


def certificates_sign(data=None, uuid=None):
    """
    Execute sign in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/sign

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "sign", uuid=uuid, data=data)


def certificates_sign_certificate(data=None, uuid=None):
    """
    Execute signCertificate in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/signCertificate

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "signCertificate", uuid=uuid, data=data)


def certificates_update(data=None, uuid=None):
    """
    Execute update in acmeclient/certificates.

    Wraps: /api/acmeclient/certificates/update

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "certificates", "update", uuid=uuid, data=data)


# --- service controller ---

def service_configtest(data=None, uuid=None):
    """
    Execute configtest in acmeclient/service.

    Wraps: /api/acmeclient/service/configtest

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "configtest", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in acmeclient/service.

    Wraps: POST /api/acmeclient/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("acmeclient", "service", action, data)


def service_reset(data=None, uuid=None):
    """
    Execute reset in acmeclient/service.

    Wraps: /api/acmeclient/service/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "reset", uuid=uuid, data=data)


def service_restart(data=None):
    """
    Execute restart in acmeclient/service.

    Wraps: POST /api/acmeclient/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "restart", data=data, method="POST")


def service_signallcerts(data=None, uuid=None):
    """
    Execute signallcerts in acmeclient/service.

    Wraps: /api/acmeclient/service/signallcerts

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "signallcerts", uuid=uuid, data=data)


def service_start(data=None):
    """
    Execute start in acmeclient/service.

    Wraps: POST /api/acmeclient/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "start", data=data, method="POST")


def service_status(data=None):
    """
    Execute status in acmeclient/service.

    Wraps: POST /api/acmeclient/service/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "status", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in acmeclient/service.

    Wraps: POST /api/acmeclient/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "service", "stop", data=data, method="POST")


# --- settings controller ---

def get_settings():
    """
    Get settings singleton config in acmeclient/settings.

    Wraps: GET /api/acmeclient/settings/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("acmeclient", "settings")


def set_settings(data):
    """
    Set settings singleton config in acmeclient/settings.

    Wraps: POST /api/acmeclient/settings/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("acmeclient", "settings", "set", data=data, method="POST")


def settings_fetch_cron_integration(data=None, uuid=None):
    """
    Execute fetchCronIntegration in acmeclient/settings.

    Wraps: /api/acmeclient/settings/fetchCronIntegration

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "settings", "fetchCronIntegration", uuid=uuid, data=data)


def settings_fetch_ha_proxy_integration(data=None, uuid=None):
    """
    Execute fetchHAProxyIntegration in acmeclient/settings.

    Wraps: /api/acmeclient/settings/fetchHAProxyIntegration

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "settings", "fetchHAProxyIntegration", uuid=uuid, data=data)


def settings_get_bind_plugin_status(data=None, uuid=None):
    """
    Execute getBindPluginStatus in acmeclient/settings.

    Wraps: /api/acmeclient/settings/getBindPluginStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "settings", "getBindPluginStatus", uuid=uuid, data=data)


def settings_get_gcloud_plugin_status(data=None, uuid=None):
    """
    Execute getGcloudPluginStatus in acmeclient/settings.

    Wraps: /api/acmeclient/settings/getGcloudPluginStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "settings", "getGcloudPluginStatus", uuid=uuid, data=data)


# --- validations controller ---

def search_validation(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search validation entries in acmeclient/validations.

    Wraps: POST /api/acmeclient/validations/searchValidation

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("acmeclient", "validations", "validation", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_validation(uuid=None):
    """
    Get validation entry in acmeclient/validations.

    Wraps: GET /api/acmeclient/validations/getValidation/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("acmeclient", "validations", "validation", uuid)


def add_validation(data):
    """
    Add validation entry in acmeclient/validations.

    Wraps: POST /api/acmeclient/validations/addValidation

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("acmeclient", "validations", "validation", data)


def set_validation(uuid, data):
    """
    Set/update validation entry in acmeclient/validations.

    Wraps: POST /api/acmeclient/validations/setValidation/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("acmeclient", "validations", "validation", uuid, data)


def del_validation(uuid):
    """
    Delete validation entry in acmeclient/validations.

    Wraps: POST /api/acmeclient/validations/delValidation/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("acmeclient", "validations", "validation", uuid)


def toggle_validation(uuid, enabled=None):
    """
    Toggle validation entry in acmeclient/validations.

    Wraps: POST /api/acmeclient/validations/toggle/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("acmeclient", "validations", "validation", uuid, enabled)


def validations_update(data=None, uuid=None):
    """
    Execute update in acmeclient/validations.

    Wraps: /api/acmeclient/validations/update

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("acmeclient", "validations", "update", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for acmeclient.

    Wraps: POST /api/acmeclient/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("acmeclient", controller, action, data)
