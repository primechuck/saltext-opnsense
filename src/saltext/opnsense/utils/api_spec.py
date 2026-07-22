import json
import pathlib
from typing import Any

SPEC_FILE = pathlib.Path(__file__).parent.parent / ".." / ".." / ".." / "tools" / "controllers.json"
SPEC_FILE_FALLBACK = pathlib.Path(__file__).with_name("controllers.json")

CORE_MODULES = [
    "auth", "captiveportal", "core", "cron", "dhcrelay", "diagnostics", "dnsmasq",
    "firewall", "firmware", "hostdiscovery", "ids", "interfaces", "ipsec",
    "kea", "monit", "ntpd", "openvpn", "radvd", "routes", "routing",
    "syslog", "trafficshaper", "trust", "unbound", "wireguard"
]

PLUGIN_MODULES = [
    "acmeclient", "apcupsd", "bind", "caddy", "chrony", "clamav", "collectd",
    "crowdsec", "dec_hw", "dhcp", "dnscryptproxy", "dyndns", "etpro-telemetry",
    "freeradius", "ftpproxy", "haproxy", "igmpproxy", "lldpd", "mdnsrepeater",
    "monit", "munin", "net-snmp", "netdata", "nginx", "nrpe", "ntp", "nut",
    "openconnect", "os-c-icap", "postfix", "proxy", "quagga", "radvd",
    "relayd", "reroute", "routing", "stunnel", "tayga", "tinc", "tor",
    "udpbroadcastrelay", "upnp", "wireguard", "zerotier", "qemu-guest-agent",
    "telegraf", "zabbix-agent", "zabbix-proxy", "cron", "smart", "wol",
]

COMMON_ACTIONS = {
    "crud": ["search_{type}", "get_{type}", "add_{type}", "set_{type}", "del_{type}", "toggle_{type}"],
    "service": ["reconfigure", "restart", "start", "stop", "status"],
    "singleton": ["get", "set"],
}

UNBOUND_CONTROLLERS = {
    "settings": [
        "searchHostOverride", "getHostOverride", "addHostOverride", "setHostOverride", "delHostOverride", "toggleHostOverride",
        "searchHostAlias", "getHostAlias", "addHostAlias", "setHostAlias", "delHostAlias", "toggleHostAlias",
        "searchDot", "getDot", "addDot", "setDot", "delDot",
        "searchForward", "getForward", "addForward", "setForward", "delForward", "toggleForward",
        "searchAcl", "getAcl", "addAcl", "setAcl", "delAcl", "toggleAcl",
        "searchDnsbl", "getDnsbl", "addDnsbl", "setDnsbl", "delDnsbl", "toggleDnsbl",
        "getNameservers", "updateBlocklist",
        "get", "set",
        "search_host_override", "get_host_override", "add_host_override", "set_host_override", "del_host_override", "toggle_host_override",
        "search_host_alias", "get_host_alias", "add_host_alias", "set_host_alias", "del_host_alias", "toggle_host_alias",
        "search_dot", "get_dot", "add_dot", "set_dot", "del_dot",
        "search_forward", "get_forward", "add_forward", "set_forward", "del_forward", "toggle_forward",
        "search_acl", "get_acl", "add_acl", "set_acl", "del_acl", "toggle_acl",
        "search_dnsbl", "get_dnsbl", "add_dnsbl", "set_dnsbl", "del_dnsbl", "toggle_dnsbl",
        "get_nameservers", "update_blocklist",
    ],
    "service": ["reconfigure", "reconfigure_general", "reconfigureGeneral", "restart", "start", "status", "stop", "dnsbl"],
    "diagnostics": ["stats", "listLocalZones", "listLocalData", "listInsecure", "dumpCache", "dumpInfra", "testBlocklist",
                    "list_local_zones", "list_local_data", "list_insecure", "dump_cache", "dump_infra", "test_blocklist"],
    "overview": ["isEnabled", "isBlockListEnabled", "getPolicies", "searchQueries", "totals", "_rolling",
                 "is_enabled", "is_block_list_enabled", "get_policies", "search_queries"],
}

BIND_CONTROLLERS = {
    "domain": [
        "searchPrimaryDomain", "getPrimaryDomain", "addPrimaryDomain", "setPrimaryDomain", "delPrimaryDomain",
        "searchSecondaryDomain", "getSecondaryDomain", "addSecondaryDomain", "setSecondaryDomain", "delSecondaryDomain",
        "searchForwardDomain", "searchMasterDomain", "searchSlaveDomain",
        "getDomain", "addDomain", "setDomain", "delDomain", "toggleDomain",
        "search_primary_domain", "get_primary_domain", "add_primary_domain", "set_primary_domain", "del_primary_domain",
        "search_secondary_domain", "get_secondary_domain", "add_secondary_domain", "set_secondary_domain", "del_secondary_domain",
        "search_forward_domain", "search_master_domain", "search_slave_domain",
        "get_domain", "add_domain", "set_domain", "del_domain", "toggle_domain",
        "get", "set"
    ],
    "record": [
        "searchRecord", "getRecord", "addRecord", "setRecord", "delRecord", "toggleRecord",
        "search_record", "get_record", "add_record", "set_record", "del_record", "toggle_record",
        "get", "set"
    ],
    "acl": [
        "searchAcl", "getAcl", "addAcl", "setAcl", "delAcl", "toggleAcl",
        "search_acl", "get_acl", "add_acl", "set_acl", "del_acl", "toggle_acl",
        "get", "set"
    ],
    "general": ["get", "set", "zoneshow", "zonetest", "zoneShow", "zoneTest", "zone_show", "zone_test"],
    "service": ["reconfigure", "restart", "start", "status", "stop", "dnsbl"],
    "dnsbl": ["get", "set"],
}

FIREWALL_CONTROLLERS = {
    "alias": ["searchItem", "getItem", "addItem", "setItem", "delItem", "toggleItem", "listCountries", "reconfigure", "util",
              "search_item", "get_item", "add_item", "set_item", "del_item", "toggle_item", "list_countries"],
    "filter": ["searchRule", "getRule", "addRule", "setRule", "delRule", "toggleRule", "apply", "savepoint", "cancelRollback",
               "search_rule", "get_rule", "add_rule", "set_rule", "del_rule", "toggle_rule", "cancel_rollback"],
    "category": ["searchItem", "getItem", "addItem", "setItem", "delItem", "search_item", "get_item", "add_item", "set_item", "del_item"],
    "group": ["searchItem", "getItem", "addItem", "setItem", "delItem", "search_item", "get_item", "add_item", "set_item", "del_item"],
}

INTERFACES_CONTROLLERS = {
    "overview": ["export", "interfaces", "getArp", "get_arp"],
    "vlan": ["searchItem", "getItem", "addItem", "setItem", "delItem", "reconfigure",
             "search_item", "get_item", "add_item", "set_item", "del_item"],
    "vip": ["searchItem", "getItem", "addItem", "setItem", "delItem", "reconfigure",
            "search_item", "get_item", "add_item", "set_item", "del_item"],
}

KEA_CONTROLLERS = {
    "dhcpv4": [
        "get", "set",
        "searchSubnet", "getSubnet", "addSubnet", "setSubnet", "delSubnet",
        "searchReservation", "getReservation", "addReservation", "setReservation", "delReservation",
        "searchOption", "getOption", "addOption", "setOption", "delOption",
        "searchPeer", "getPeer", "addPeer", "setPeer", "delPeer",
        "downloadReservations", "uploadReservations",
        "search_subnet", "get_subnet", "add_subnet", "set_subnet", "del_subnet",
        "search_reservation", "get_reservation", "add_reservation", "set_reservation", "del_reservation",
        "search_option", "get_option", "add_option", "set_option", "del_option",
        "search_peer", "get_peer", "add_peer", "set_peer", "del_peer",
        "download_reservations", "upload_reservations",
    ],
    "dhcpv6": [
        "get", "set",
        "searchSubnet", "getSubnet", "addSubnet", "setSubnet", "delSubnet",
        "searchReservation", "getReservation", "addReservation", "setReservation", "delReservation",
        "searchOption", "getOption", "addOption", "setOption", "delOption",
        "searchPeer", "getPeer", "addPeer", "setPeer", "delPeer",
        "searchPdPool", "getPdPool", "addPdPool", "setPdPool", "delPdPool",
        "downloadReservations", "uploadReservations",
        "search_subnet", "get_subnet", "add_subnet", "set_subnet", "del_subnet",
        "search_reservation", "get_reservation", "add_reservation", "set_reservation", "del_reservation",
        "search_option", "get_option", "add_option", "set_option", "del_option",
        "search_peer", "get_peer", "add_peer", "set_peer", "del_peer",
        "search_pd_pool", "get_pd_pool", "add_pd_pool", "set_pd_pool", "del_pd_pool",
        "download_reservations", "upload_reservations",
    ],
    "leases": ["search", "delLease", "del_lease", "searchLease4", "searchLease6", "search_lease4", "search_lease6"],
    "ctrl_agent": ["get", "set"],
    "ddns": ["get", "set"],
    "service": ["reconfigure", "restart", "start", "status", "stop"],
}

ACME_CONTROLLERS = {
    "accounts": ["search", "get", "add", "set", "del", "toggle", "update", "register"],
    "actions": ["search", "get", "add", "set", "del", "toggle", "update",
                "sftp_get_identity", "sftp_test_connection", "ssh_get_identity", "ssh_test_connection",
                "sftpGetIdentity", "sftpTestConnection", "sshGetIdentity", "sshTestConnection"],
    "certificates": ["search", "get", "add", "set", "del", "toggle", "update",
                     "automation", "import", "removekey", "remove_key", "removeKey", "revoke", "sign"],
    "service": ["configtest", "config_test", "configTest", "reconfigure", "reset", "restart",
                "signallcerts", "sign_all_certs", "signAllCerts", "start", "status", "stop"],
    "settings": ["get", "set",
                 "fetch_cron_integration", "fetch_h_a_proxy_integration",
                 "fetchCronIntegration", "fetchHAProxyIntegration",
                 "get_bind_plugin_status", "get_gcloud_plugin_status",
                 "getBindPluginStatus", "getGcloudPluginStatus"],
    "validations": ["search", "get", "add", "set", "del", "toggle", "update"],
}


def load_spec() -> dict[str, Any]:
    for path in [SPEC_FILE, SPEC_FILE_FALLBACK, pathlib.Path.cwd() / "tools" / "controllers.json"]:
        if path.exists():
            try:
                return json.loads(path.read_text())
            except Exception:
                continue
    return {
        "generated": False,
        "modules": {
            "unbound": UNBOUND_CONTROLLERS,
            "bind": BIND_CONTROLLERS,
            "firewall": FIREWALL_CONTROLLERS,
            "interfaces": INTERFACES_CONTROLLERS,
            "kea": KEA_CONTROLLERS,
            "acmeclient": ACME_CONTROLLERS,
        },
        "core_modules": CORE_MODULES,
        "plugin_modules": PLUGIN_MODULES,
    }


def list_modules() -> list[str]:
    spec = load_spec()
    if "modules" in spec:
        return sorted(spec["modules"].keys())
    return sorted(set(CORE_MODULES + PLUGIN_MODULES))


def list_controllers(module: str) -> list[str]:
    spec = load_spec()
    mods = spec.get("modules", {})
    if module in mods:
        return sorted(mods[module].keys())
    return []


def list_actions(module: str, controller: str) -> list[str]:
    spec = load_spec()
    mods = spec.get("modules", {})
    if module in mods and controller in mods[module]:
        val = mods[module][controller]
        if isinstance(val, dict):
            return sorted(val.keys())
        if isinstance(val, list):
            return sorted(val)
    return []
