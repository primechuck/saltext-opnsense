# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense diagnostics wrappers.

Generated from controllers.json for module diagnostics.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/diagnostics/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_diagnostics"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- activity controller ---

def activity_get_activity(data=None, uuid=None):
    """
    Execute getActivity in diagnostics/activity.

    Wraps: /api/diagnostics/activity/getActivity

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "activity", "getActivity", uuid=uuid, data=data)


# --- cpuusage controller ---

def cpuusage_get_cpu_type(data=None, uuid=None):
    """
    Execute getCPUType in diagnostics/cpuusage.

    Wraps: /api/diagnostics/cpuusage/getCPUType

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "cpuusage", "getCPUType", uuid=uuid, data=data)


def cpuusage_stream(data=None, uuid=None):
    """
    Execute stream in diagnostics/cpuusage.

    Wraps: /api/diagnostics/cpuusage/stream

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "cpuusage", "stream", uuid=uuid, data=data)


# --- dns controller ---

def dns_reverse_lookup(data=None, uuid=None):
    """
    Execute reverseLookup in diagnostics/dns.

    Wraps: /api/diagnostics/dns/reverseLookup

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "dns", "reverseLookup", uuid=uuid, data=data)


# --- dnsdiagnostics controller ---

def set_dnsdiagnostics(data):
    """
    Set dnsdiagnostics singleton config in diagnostics/dnsdiagnostics.

    Wraps: POST /api/diagnostics/dnsdiagnostics/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("diagnostics", "dnsdiagnostics", "set", data=data, method="POST")


# --- firewall controller ---

def firewall_del_state(data=None, uuid=None):
    """
    Execute delState in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/delState

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "delState", uuid=uuid, data=data)


def firewall_flush_sources(data=None, uuid=None):
    """
    Execute flushSources in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/flushSources

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "flushSources", uuid=uuid, data=data)


def firewall_flush_states(data=None, uuid=None):
    """
    Execute flushStates in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/flushStates

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "flushStates", uuid=uuid, data=data)


def firewall_kill_states(data=None, uuid=None):
    """
    Execute killStates in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/killStates

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "killStates", uuid=uuid, data=data)


def firewall_list_rule_ids(data=None, uuid=None):
    """
    Execute listRuleIds in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/listRuleIds

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "listRuleIds", uuid=uuid, data=data)


def firewall_log(data=None, uuid=None):
    """
    Execute log in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/log

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "log", uuid=uuid, data=data)


def firewall_log_filters(data=None, uuid=None):
    """
    Execute logFilters in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/logFilters

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "logFilters", uuid=uuid, data=data)


def firewall_pf_states(data=None, uuid=None):
    """
    Execute pfStates in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/pfStates

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "pfStates", uuid=uuid, data=data)


def firewall_pf_statistics(data=None, uuid=None):
    """
    Execute pfStatistics in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/pfStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "pfStatistics", uuid=uuid, data=data)


def firewall_query_pf_top(data=None, uuid=None):
    """
    Execute queryPfTop in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/queryPfTop

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "queryPfTop", uuid=uuid, data=data)


def firewall_query_states(data=None, uuid=None):
    """
    Execute queryStates in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/queryStates

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "queryStates", uuid=uuid, data=data)


def firewall_stats(data=None, uuid=None):
    """
    Execute stats in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/stats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "stats", uuid=uuid, data=data)


def firewall_stream_log(data=None, uuid=None):
    """
    Execute streamLog in diagnostics/firewall.

    Wraps: /api/diagnostics/firewall/streamLog

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "firewall", "streamLog", uuid=uuid, data=data)


# --- interface controller ---

def search_arp(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search arp entries in diagnostics/interface.

    Wraps: POST /api/diagnostics/interface/searchArp

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("diagnostics", "interface", "arp", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_arp(uuid=None):
    """
    Get arp entry in diagnostics/interface.

    Wraps: GET /api/diagnostics/interface/getArp/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("diagnostics", "interface", "arp", uuid)


def search_ndp(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search ndp entries in diagnostics/interface.

    Wraps: POST /api/diagnostics/interface/searchNdp

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("diagnostics", "interface", "ndp", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_ndp(uuid=None):
    """
    Get ndp entry in diagnostics/interface.

    Wraps: GET /api/diagnostics/interface/getNdp/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("diagnostics", "interface", "ndp", uuid)


def interface_carp_status(data=None, uuid=None):
    """
    Execute carpStatus in diagnostics/interface.

    Wraps: /api/diagnostics/interface/carpStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "carpStatus", uuid=uuid, data=data)


def interface_del_route(data=None, uuid=None):
    """
    Execute delRoute in diagnostics/interface.

    Wraps: /api/diagnostics/interface/delRoute

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "delRoute", uuid=uuid, data=data)


def interface_flush_arp(data=None, uuid=None):
    """
    Execute flushArp in diagnostics/interface.

    Wraps: /api/diagnostics/interface/flushArp

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "flushArp", uuid=uuid, data=data)


def interface_get_bpf_statistics(data=None, uuid=None):
    """
    Execute getBpfStatistics in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getBpfStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getBpfStatistics", uuid=uuid, data=data)


def interface_get_interface_config(data=None, uuid=None):
    """
    Execute getInterfaceConfig in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getInterfaceConfig

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getInterfaceConfig", uuid=uuid, data=data)


def interface_get_interface_names(data=None, uuid=None):
    """
    Execute getInterfaceNames in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getInterfaceNames

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getInterfaceNames", uuid=uuid, data=data)


def interface_get_interface_statistics(data=None, uuid=None):
    """
    Execute getInterfaceStatistics in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getInterfaceStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getInterfaceStatistics", uuid=uuid, data=data)


def interface_get_memory_statistics(data=None, uuid=None):
    """
    Execute getMemoryStatistics in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getMemoryStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getMemoryStatistics", uuid=uuid, data=data)


def interface_get_netisr_statistics(data=None, uuid=None):
    """
    Execute getNetisrStatistics in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getNetisrStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getNetisrStatistics", uuid=uuid, data=data)


def interface_get_pfsync_nodes(data=None, uuid=None):
    """
    Execute getPfsyncNodes in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getPfsyncNodes

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getPfsyncNodes", uuid=uuid, data=data)


def interface_get_protocol_statistics(data=None, uuid=None):
    """
    Execute getProtocolStatistics in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getProtocolStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getProtocolStatistics", uuid=uuid, data=data)


def interface_get_routes(data=None, uuid=None):
    """
    Execute getRoutes in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getRoutes

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getRoutes", uuid=uuid, data=data)


def interface_get_socket_statistics(data=None, uuid=None):
    """
    Execute getSocketStatistics in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getSocketStatistics

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getSocketStatistics", uuid=uuid, data=data)


def interface_get_vip_status(data=None, uuid=None):
    """
    Execute getVipStatus in diagnostics/interface.

    Wraps: /api/diagnostics/interface/getVipStatus

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "interface", "getVipStatus", uuid=uuid, data=data)


# --- lvtemplate controller ---

def search_item(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search item entries in diagnostics/lvtemplate.

    Wraps: POST /api/diagnostics/lvtemplate/searchItem

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("diagnostics", "lvtemplate", "item", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_item(uuid=None):
    """
    Get item entry in diagnostics/lvtemplate.

    Wraps: GET /api/diagnostics/lvtemplate/getItem/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("diagnostics", "lvtemplate", "item", uuid)


def add_item(data):
    """
    Add item entry in diagnostics/lvtemplate.

    Wraps: POST /api/diagnostics/lvtemplate/addItem

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("diagnostics", "lvtemplate", "item", data)


def set_item(uuid, data):
    """
    Set/update item entry in diagnostics/lvtemplate.

    Wraps: POST /api/diagnostics/lvtemplate/setItem/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("diagnostics", "lvtemplate", "item", uuid, data)


def del_item(uuid):
    """
    Delete item entry in diagnostics/lvtemplate.

    Wraps: POST /api/diagnostics/lvtemplate/delItem/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("diagnostics", "lvtemplate", "item", uuid)


# --- netflow controller ---

def get_config(uuid=None):
    """
    Get config entry in diagnostics/netflow.

    Wraps: GET /api/diagnostics/netflow/getconfig/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("diagnostics", "netflow", "config", uuid)


def set_config(uuid, data):
    """
    Set/update config entry in diagnostics/netflow.

    Wraps: POST /api/diagnostics/netflow/setconfig/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("diagnostics", "netflow", "config", uuid, data)


def netflow_cache_stats(data=None, uuid=None):
    """
    Execute cacheStats in diagnostics/netflow.

    Wraps: /api/diagnostics/netflow/cacheStats

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "netflow", "cacheStats", uuid=uuid, data=data)


def netflow_is_enabled(data=None, uuid=None):
    """
    Execute isEnabled in diagnostics/netflow.

    Wraps: /api/diagnostics/netflow/isEnabled

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "netflow", "isEnabled", uuid=uuid, data=data)


def netflow_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in diagnostics/netflow.

    Wraps: POST /api/diagnostics/netflow/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("diagnostics", "netflow", action, data)


def netflow_reset(data=None, uuid=None):
    """
    Execute reset in diagnostics/netflow.

    Wraps: /api/diagnostics/netflow/reset

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "netflow", "reset", uuid=uuid, data=data)


def netflow_status(data=None):
    """
    Execute status in diagnostics/netflow.

    Wraps: POST /api/diagnostics/netflow/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "netflow", "status", data=data, method="POST")


# --- networkinsight controller ---

def networkinsight_export(data=None, uuid=None):
    """
    Execute export in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/export

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "export", uuid=uuid, data=data)


def networkinsight_get_interfaces(data=None, uuid=None):
    """
    Execute getInterfaces in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/getInterfaces

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "getInterfaces", uuid=uuid, data=data)


def networkinsight_get_metadata(data=None, uuid=None):
    """
    Execute getMetadata in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/getMetadata

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "getMetadata", uuid=uuid, data=data)


def networkinsight_get_protocols(data=None, uuid=None):
    """
    Execute getProtocols in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/getProtocols

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "getProtocols", uuid=uuid, data=data)


def networkinsight_get_services(data=None, uuid=None):
    """
    Execute getServices in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/getServices

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "getServices", uuid=uuid, data=data)


def networkinsight_timeserie(data=None, uuid=None):
    """
    Execute timeserie in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/timeserie

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "timeserie", uuid=uuid, data=data)


def networkinsight_top(data=None, uuid=None):
    """
    Execute top in diagnostics/networkinsight.

    Wraps: /api/diagnostics/networkinsight/top

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "networkinsight", "top", uuid=uuid, data=data)


# --- packetcapture controller ---

def search_packetcapture_jobs(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search jobs entries in diagnostics/packetcapture.

    Wraps: POST /api/diagnostics/packetcapture/searchJobs

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("diagnostics", "packetcapture", "jobs", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def set_packetcapture_jobs(uuid, data):
    """
    Set/update jobs entry in diagnostics/packetcapture.

    Wraps: POST /api/diagnostics/packetcapture/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("diagnostics", "packetcapture", "jobs", uuid, data)


def packetcapture_download(data=None, uuid=None):
    """
    Execute download in diagnostics/packetcapture.

    Wraps: /api/diagnostics/packetcapture/download

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "packetcapture", "download", uuid=uuid, data=data)


def packetcapture_mac_info(data=None, uuid=None):
    """
    Execute macInfo in diagnostics/packetcapture.

    Wraps: /api/diagnostics/packetcapture/macInfo

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "packetcapture", "macInfo", uuid=uuid, data=data)


def packetcapture_remove(data=None, uuid=None):
    """
    Execute remove in diagnostics/packetcapture.

    Wraps: /api/diagnostics/packetcapture/remove

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "packetcapture", "remove", uuid=uuid, data=data)


def packetcapture_start(data=None):
    """
    Execute start in diagnostics/packetcapture.

    Wraps: POST /api/diagnostics/packetcapture/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "packetcapture", "start", data=data, method="POST")


def packetcapture_stop(data=None):
    """
    Execute stop in diagnostics/packetcapture.

    Wraps: POST /api/diagnostics/packetcapture/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "packetcapture", "stop", data=data, method="POST")


def packetcapture_view(data=None, uuid=None):
    """
    Execute view in diagnostics/packetcapture.

    Wraps: /api/diagnostics/packetcapture/view

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "packetcapture", "view", uuid=uuid, data=data)


# --- ping controller ---

def search_ping_jobs(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search jobs entries in diagnostics/ping.

    Wraps: POST /api/diagnostics/ping/searchJobs

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("diagnostics", "ping", "jobs", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def set_ping_jobs(uuid, data):
    """
    Set/update jobs entry in diagnostics/ping.

    Wraps: POST /api/diagnostics/ping/set/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("diagnostics", "ping", "jobs", uuid, data)


def ping_remove(data=None, uuid=None):
    """
    Execute remove in diagnostics/ping.

    Wraps: /api/diagnostics/ping/remove

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "ping", "remove", uuid=uuid, data=data)


def ping_start(data=None):
    """
    Execute start in diagnostics/ping.

    Wraps: POST /api/diagnostics/ping/start

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "ping", "start", data=data, method="POST")


def ping_stop(data=None):
    """
    Execute stop in diagnostics/ping.

    Wraps: POST /api/diagnostics/ping/stop

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "ping", "stop", data=data, method="POST")


# --- portprobe controller ---

def set_portprobe(data):
    """
    Set portprobe singleton config in diagnostics/portprobe.

    Wraps: POST /api/diagnostics/portprobe/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("diagnostics", "portprobe", "set", data=data, method="POST")


# --- proofpointet controller ---

def proofpointet_status(data=None):
    """
    Execute status in diagnostics/proofpointet.

    Wraps: POST /api/diagnostics/proofpointet/status

    :param data: Optional data dict
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "proofpointet", "status", data=data, method="POST")


# --- system controller ---

def system_memory(data=None, uuid=None):
    """
    Execute memory in diagnostics/system.

    Wraps: /api/diagnostics/system/memory

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "memory", uuid=uuid, data=data)


def system_system_disk(data=None, uuid=None):
    """
    Execute systemDisk in diagnostics/system.

    Wraps: /api/diagnostics/system/systemDisk

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemDisk", uuid=uuid, data=data)


def system_system_information(data=None, uuid=None):
    """
    Execute systemInformation in diagnostics/system.

    Wraps: /api/diagnostics/system/systemInformation

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemInformation", uuid=uuid, data=data)


def system_system_mbuf(data=None, uuid=None):
    """
    Execute systemMbuf in diagnostics/system.

    Wraps: /api/diagnostics/system/systemMbuf

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemMbuf", uuid=uuid, data=data)


def system_system_resources(data=None, uuid=None):
    """
    Execute systemResources in diagnostics/system.

    Wraps: /api/diagnostics/system/systemResources

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemResources", uuid=uuid, data=data)


def system_system_swap(data=None, uuid=None):
    """
    Execute systemSwap in diagnostics/system.

    Wraps: /api/diagnostics/system/systemSwap

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemSwap", uuid=uuid, data=data)


def system_system_temperature(data=None, uuid=None):
    """
    Execute systemTemperature in diagnostics/system.

    Wraps: /api/diagnostics/system/systemTemperature

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemTemperature", uuid=uuid, data=data)


def system_system_time(data=None, uuid=None):
    """
    Execute systemTime in diagnostics/system.

    Wraps: /api/diagnostics/system/systemTime

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "system", "systemTime", uuid=uuid, data=data)


# --- systemhealth controller ---

def systemhealth_del_rrd(data=None, uuid=None):
    """
    Execute delRRD in diagnostics/systemhealth.

    Wraps: /api/diagnostics/systemhealth/delRRD

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "systemhealth", "delRRD", uuid=uuid, data=data)


def systemhealth_export_as_csv(data=None, uuid=None):
    """
    Execute exportAsCSV in diagnostics/systemhealth.

    Wraps: /api/diagnostics/systemhealth/exportAsCSV

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "systemhealth", "exportAsCSV", uuid=uuid, data=data)


def systemhealth_get_interfaces(data=None, uuid=None):
    """
    Execute getInterfaces in diagnostics/systemhealth.

    Wraps: /api/diagnostics/systemhealth/getInterfaces

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "systemhealth", "getInterfaces", uuid=uuid, data=data)


def systemhealth_get_rrd_list(data=None, uuid=None):
    """
    Execute getRrdList in diagnostics/systemhealth.

    Wraps: /api/diagnostics/systemhealth/getRrdList

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "systemhealth", "getRrdList", uuid=uuid, data=data)


def systemhealth_get_system_health(data=None, uuid=None):
    """
    Execute getSystemHealth in diagnostics/systemhealth.

    Wraps: /api/diagnostics/systemhealth/getSystemHealth

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "systemhealth", "getSystemHealth", uuid=uuid, data=data)


def systemhealth_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in diagnostics/systemhealth.

    Wraps: POST /api/diagnostics/systemhealth/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("diagnostics", "systemhealth", action, data)


# --- traceroute controller ---

def set_traceroute(data):
    """
    Set traceroute singleton config in diagnostics/traceroute.

    Wraps: POST /api/diagnostics/traceroute/set

    :param data: Config dict
    :return: API response dict
    """
    return __salt__["opnsense.call"]("diagnostics", "traceroute", "set", data=data, method="POST")


# --- traffic controller ---

def traffic_interface(data=None, uuid=None):
    """
    Execute Interface in diagnostics/traffic.

    Wraps: /api/diagnostics/traffic/Interface

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "traffic", "Interface", uuid=uuid, data=data)


def traffic_stream(data=None, uuid=None):
    """
    Execute stream in diagnostics/traffic.

    Wraps: /api/diagnostics/traffic/stream

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "traffic", "stream", uuid=uuid, data=data)


def traffic_top(data=None, uuid=None):
    """
    Execute Top in diagnostics/traffic.

    Wraps: /api/diagnostics/traffic/Top

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("diagnostics", "traffic", "Top", uuid=uuid, data=data)



# Generic module-level helpers

def reconfigure(controller="activity", action="reconfigure", data=None):
    """
    Generic reconfigure for diagnostics.

    Wraps: POST /api/diagnostics/{controller}/{action}

    :param controller: Controller name, default activity
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("diagnostics", controller, action, data)
