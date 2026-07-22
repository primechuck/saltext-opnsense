# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense core wrappers.

Generated from controllers.json for module core.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/core/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_core"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- backup controller ---

def backup_backups(data=None, uuid=None):
    """
    Execute backups in core/backup.

    Wraps: /api/core/backup/backups

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "backup", "backups", uuid=uuid, data=data)


def backup_delete_backup(data=None, uuid=None):
    """
    Execute deleteBackup in core/backup.

    Wraps: /api/core/backup/deleteBackup

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "backup", "deleteBackup", uuid=uuid, data=data)


def backup_diff(data=None, uuid=None):
    """
    Execute diff in core/backup.

    Wraps: /api/core/backup/diff

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "backup", "diff", uuid=uuid, data=data)


def backup_download(data=None, uuid=None):
    """
    Execute download in core/backup.

    Wraps: /api/core/backup/download

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "backup", "download", uuid=uuid, data=data)


def backup_providers(data=None, uuid=None):
    """
    Execute providers in core/backup.

    Wraps: /api/core/backup/providers

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "backup", "providers", uuid=uuid, data=data)


def backup_revert_backup(data=None, uuid=None):
    """
    Execute revertBackup in core/backup.

    Wraps: /api/core/backup/revertBackup

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "backup", "revertBackup", uuid=uuid, data=data)


# --- dashboard controller ---

def dashboard_get_dashboard(data=None, uuid=None):
    """
    Execute getDashboard in core/dashboard.

    Wraps: /api/core/dashboard/getDashboard

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "dashboard", "getDashboard", uuid=uuid, data=data)


def dashboard_picture(data=None, uuid=None):
    """
    Execute picture in core/dashboard.

    Wraps: /api/core/dashboard/picture

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "dashboard", "picture", uuid=uuid, data=data)


def dashboard_product_info_feed(data=None, uuid=None):
    """
    Execute productInfoFeed in core/dashboard.

    Wraps: /api/core/dashboard/productInfoFeed

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "dashboard", "productInfoFeed", uuid=uuid, data=data)


def dashboard_restore_defaults(data=None, uuid=None):
    """
    Execute restoreDefaults in core/dashboard.

    Wraps: /api/core/dashboard/restoreDefaults

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "dashboard", "restoreDefaults", uuid=uuid, data=data)


def dashboard_save_widgets(data=None, uuid=None):
    """
    Execute saveWidgets in core/dashboard.

    Wraps: /api/core/dashboard/saveWidgets

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "dashboard", "saveWidgets", uuid=uuid, data=data)


# --- defaults controller ---

def get_defaults():
    """
    Get defaults singleton config in core/defaults.

    Wraps: GET /api/core/defaults/get

    :return: API response dict
    """
    return __salt__["opnsense.get"]("core", "defaults")


def defaults_factory_defaults(data=None, uuid=None):
    """
    Execute factoryDefaults in core/defaults.

    Wraps: /api/core/defaults/factoryDefaults

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "defaults", "factoryDefaults", uuid=uuid, data=data)


def defaults_get_installed_sections(data=None, uuid=None):
    """
    Execute getInstalledSections in core/defaults.

    Wraps: /api/core/defaults/getInstalledSections

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "defaults", "getInstalledSections", uuid=uuid, data=data)


def defaults_reset(data=None, uuid=None):
    """
    Execute reset in core/defaults.

    Wraps: /api/core/defaults/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "defaults", "reset", uuid=uuid, data=data)


# --- firmware controller ---

def set_firmware(data):
    """
    Set firmware singleton config in core/firmware.

    Wraps: POST /api/core/firmware/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("core", "firmware", "set", data=data, method="POST")


def firmware_audit(data=None, uuid=None):
    """
    Execute audit in core/firmware.

    Wraps: /api/core/firmware/audit

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "audit", uuid=uuid, data=data)


def firmware_changelog(data=None, uuid=None):
    """
    Execute changelog in core/firmware.

    Wraps: /api/core/firmware/changelog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "changelog", uuid=uuid, data=data)


def firmware_check(data=None, uuid=None):
    """
    Execute check in core/firmware.

    Wraps: /api/core/firmware/check

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "check", uuid=uuid, data=data)


def firmware_cleanup(data=None, uuid=None):
    """
    Execute cleanup in core/firmware.

    Wraps: /api/core/firmware/cleanup

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "cleanup", uuid=uuid, data=data)


def firmware_connection(data=None, uuid=None):
    """
    Execute connection in core/firmware.

    Wraps: /api/core/firmware/connection

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "connection", uuid=uuid, data=data)


def firmware_details(data=None, uuid=None):
    """
    Execute details in core/firmware.

    Wraps: /api/core/firmware/details

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "details", uuid=uuid, data=data)


def firmware_get_options(data=None, uuid=None):
    """
    Execute getOptions in core/firmware.

    Wraps: /api/core/firmware/getOptions

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "getOptions", uuid=uuid, data=data)


def firmware_health(data=None, uuid=None):
    """
    Execute health in core/firmware.

    Wraps: /api/core/firmware/health

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "health", uuid=uuid, data=data)


def firmware_info(data=None, uuid=None):
    """
    Execute info in core/firmware.

    Wraps: /api/core/firmware/info

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "info", uuid=uuid, data=data)


def firmware_install(data=None, uuid=None):
    """
    Execute install in core/firmware.

    Wraps: /api/core/firmware/install

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "install", uuid=uuid, data=data)


def firmware_license(data=None, uuid=None):
    """
    Execute license in core/firmware.

    Wraps: /api/core/firmware/license

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "license", uuid=uuid, data=data)


def firmware_lock(data=None, uuid=None):
    """
    Execute lock in core/firmware.

    Wraps: /api/core/firmware/lock

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "lock", uuid=uuid, data=data)


def firmware_log(data=None, uuid=None):
    """
    Execute log in core/firmware.

    Wraps: /api/core/firmware/log

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "log", uuid=uuid, data=data)


def firmware_poweroff(data=None, uuid=None):
    """
    Execute poweroff in core/firmware.

    Wraps: /api/core/firmware/poweroff

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "poweroff", uuid=uuid, data=data)


def firmware_reboot(data=None, uuid=None):
    """
    Execute reboot in core/firmware.

    Wraps: /api/core/firmware/reboot

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "reboot", uuid=uuid, data=data)


def firmware_reinstall(data=None, uuid=None):
    """
    Execute reinstall in core/firmware.

    Wraps: /api/core/firmware/reinstall

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "reinstall", uuid=uuid, data=data)


def firmware_remove(data=None, uuid=None):
    """
    Execute remove in core/firmware.

    Wraps: /api/core/firmware/remove

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "remove", uuid=uuid, data=data)


def firmware_resync_plugins(data=None, uuid=None):
    """
    Execute resyncPlugins in core/firmware.

    Wraps: /api/core/firmware/resyncPlugins

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "resyncPlugins", uuid=uuid, data=data)


def firmware_running(data=None, uuid=None):
    """
    Execute running in core/firmware.

    Wraps: /api/core/firmware/running

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "running", uuid=uuid, data=data)


def firmware_status(data=None):
    """
    Execute status in core/firmware.

    Wraps: POST /api/core/firmware/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "status", data=data, method="POST")


def firmware_sync_plugins(data=None, uuid=None):
    """
    Execute syncPlugins in core/firmware.

    Wraps: /api/core/firmware/syncPlugins

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "syncPlugins", uuid=uuid, data=data)


def firmware_unlock(data=None, uuid=None):
    """
    Execute unlock in core/firmware.

    Wraps: /api/core/firmware/unlock

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "unlock", uuid=uuid, data=data)


def firmware_update(data=None, uuid=None):
    """
    Execute update in core/firmware.

    Wraps: /api/core/firmware/update

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "update", uuid=uuid, data=data)


def firmware_upgrade(data=None, uuid=None):
    """
    Execute upgrade in core/firmware.

    Wraps: /api/core/firmware/upgrade

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "upgrade", uuid=uuid, data=data)


def firmware_upgradestatus(data=None, uuid=None):
    """
    Execute upgradestatus in core/firmware.

    Wraps: /api/core/firmware/upgradestatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "firmware", "upgradestatus", uuid=uuid, data=data)


# --- hasync controller ---

def hasync_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in core/hasync.

    Wraps: POST /api/core/hasync/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("core", "hasync", action, data)


# --- hasyncstatus controller ---

def hasyncstatus_restart(data=None):
    """
    Execute restart in core/hasyncstatus.

    Wraps: POST /api/core/hasyncstatus/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "hasyncstatus", "restart", data=data, method="POST")


def hasyncstatus_restart_all(data=None, uuid=None):
    """
    Execute restartAll in core/hasyncstatus.

    Wraps: /api/core/hasyncstatus/restartAll

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "hasyncstatus", "restartAll", uuid=uuid, data=data)


def hasyncstatus_services(data=None, uuid=None):
    """
    Execute services in core/hasyncstatus.

    Wraps: /api/core/hasyncstatus/services

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "hasyncstatus", "services", uuid=uuid, data=data)


def hasyncstatus_start(data=None):
    """
    Execute start in core/hasyncstatus.

    Wraps: POST /api/core/hasyncstatus/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "hasyncstatus", "start", data=data, method="POST")


def hasyncstatus_stop(data=None):
    """
    Execute stop in core/hasyncstatus.

    Wraps: POST /api/core/hasyncstatus/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "hasyncstatus", "stop", data=data, method="POST")


def hasyncstatus_version(data=None, uuid=None):
    """
    Execute version in core/hasyncstatus.

    Wraps: /api/core/hasyncstatus/version

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "hasyncstatus", "version", uuid=uuid, data=data)


# --- initialsetup controller ---

def initialsetup_abort(data=None, uuid=None):
    """
    Execute abort in core/initialsetup.

    Wraps: /api/core/initialsetup/abort

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "initialsetup", "abort", uuid=uuid, data=data)


def initialsetup_configure(data=None, uuid=None):
    """
    Execute configure in core/initialsetup.

    Wraps: /api/core/initialsetup/configure

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "initialsetup", "configure", uuid=uuid, data=data)


# --- menu controller ---

def search_menu(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search menu entries in core/menu.

    Wraps: POST /api/core/menu/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("core", "menu", "menu", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def menu_tree(data=None, uuid=None):
    """
    Execute tree in core/menu.

    Wraps: /api/core/menu/tree

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "menu", "tree", uuid=uuid, data=data)


# --- service controller ---

def search_service(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search service entries in core/service.

    Wraps: POST /api/core/service/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("core", "service", "service", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def service_restart(data=None):
    """
    Execute restart in core/service.

    Wraps: POST /api/core/service/restart

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "service", "restart", data=data, method="POST")


def service_start(data=None):
    """
    Execute start in core/service.

    Wraps: POST /api/core/service/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "service", "start", data=data, method="POST")


def service_stop(data=None):
    """
    Execute stop in core/service.

    Wraps: POST /api/core/service/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "service", "stop", data=data, method="POST")


# --- snapshots controller ---

def search_snapshot(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search snapshot entries in core/snapshots.

    Wraps: POST /api/core/snapshots/search

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("core", "snapshots", "snapshot", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_snapshot(uuid=None):
    """
    Get snapshot entry in core/snapshots.

    Wraps: GET /api/core/snapshots/get/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("core", "snapshots", "snapshot", uuid)


def add_snapshot(data):
    """
    Add snapshot entry in core/snapshots.

    Wraps: POST /api/core/snapshots/add

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("core", "snapshots", "snapshot", data)


def set_snapshot(uuid, data):
    """
    Set/update snapshot entry in core/snapshots.

    Wraps: POST /api/core/snapshots/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("core", "snapshots", "snapshot", uuid, data)


def del_snapshot(uuid):
    """
    Delete snapshot entry in core/snapshots.

    Wraps: POST /api/core/snapshots/del/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("core", "snapshots", "snapshot", uuid)


def snapshots_activate(data=None, uuid=None):
    """
    Execute activate in core/snapshots.

    Wraps: /api/core/snapshots/activate

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "snapshots", "activate", uuid=uuid, data=data)


def snapshots_is_supported(data=None, uuid=None):
    """
    Execute isSupported in core/snapshots.

    Wraps: /api/core/snapshots/isSupported

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "snapshots", "isSupported", uuid=uuid, data=data)


# --- system controller ---

def system_dismiss_status(data=None, uuid=None):
    """
    Execute dismissStatus in core/system.

    Wraps: /api/core/system/dismissStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "system", "dismissStatus", uuid=uuid, data=data)


def system_halt(data=None, uuid=None):
    """
    Execute halt in core/system.

    Wraps: /api/core/system/halt

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "system", "halt", uuid=uuid, data=data)


def system_reboot(data=None, uuid=None):
    """
    Execute reboot in core/system.

    Wraps: /api/core/system/reboot

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "system", "reboot", uuid=uuid, data=data)


def system_status(data=None):
    """
    Execute status in core/system.

    Wraps: POST /api/core/system/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "system", "status", data=data, method="POST")


# --- tunables controller ---

def search_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in core/tunables.

    Wraps: POST /api/core/tunables/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("core", "tunables", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_item(uuid=None):
    """
    Get item entry in core/tunables.

    Wraps: GET /api/core/tunables/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("core", "tunables", "item", uuid)


def add_item(data):
    """
    Add item entry in core/tunables.

    Wraps: POST /api/core/tunables/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("core", "tunables", "item", data)


def set_item(uuid, data):
    """
    Set/update item entry in core/tunables.

    Wraps: POST /api/core/tunables/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("core", "tunables", "item", uuid, data)


def del_item(uuid):
    """
    Delete item entry in core/tunables.

    Wraps: POST /api/core/tunables/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("core", "tunables", "item", uuid)


def tunables_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in core/tunables.

    Wraps: POST /api/core/tunables/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("core", "tunables", action, data)


def tunables_reset(data=None, uuid=None):
    """
    Execute reset in core/tunables.

    Wraps: /api/core/tunables/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("core", "tunables", "reset", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="backup", action="reconfigure", data=None):
    """
    Generic reconfigure for core.

    Wraps: POST /api/core/{controller}/{action}

    :param controller: Controller name, default backup
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("core", controller, action, data)
