from __future__ import annotations

import json
import logging
import pathlib
from functools import lru_cache
from typing import Any, Final

log = logging.getLogger(__name__)

try:
    from saltext.opnsense.utils.common import camel_to_snake
except (ImportError, ModuleNotFoundError):

    def camel_to_snake(name: str) -> str:
        import re

        name = name.replace("-", "_")
        s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
        s1 = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s1)
        s1 = s1.lower()
        return re.sub(r"__+", "_", s1).strip("_")


CORE_MODULES: Final[tuple[str, ...]] = (
    "auth",
    "captiveportal",
    "core",
    "cron",
    "dhcrelay",
    "diagnostics",
    "dnsmasq",
    "firewall",
    "firmware",
    "hostdiscovery",
    "ids",
    "interfaces",
    "ipsec",
    "kea",
    "monit",
    "ntpd",
    "openvpn",
    "radvd",
    "routes",
    "routing",
    "syslog",
    "trafficshaper",
    "trust",
    "unbound",
    "wireguard",
)

PLUGIN_MODULES: Final[tuple[str, ...]] = (
    "acmeclient",
    "apcupsd",
    "bind",
    "caddy",
    "chrony",
    "clamav",
    "collectd",
    "crowdsec",
    "dhcp",
    "dnscryptproxy",
    "dyndns",
    "freeradius",
    "haproxy",
    "nginx",
    "postfix",
    "proxy",
    "telegraf",
    "wireguard",
    "zerotier",
)

UNBOUND_CONTROLLERS: Final[dict[str, tuple[str, ...]]] = {
    "settings": (
        "searchHostOverride",
        "getHostOverride",
        "addHostOverride",
        "setHostOverride",
        "delHostOverride",
        "toggleHostOverride",
        "searchHostAlias",
        "getHostAlias",
        "addHostAlias",
        "setHostAlias",
        "delHostAlias",
        "toggleHostAlias",
        "get",
        "set",
        "search_host_override",
        "search_host_alias",
    ),
    "service": ("reconfigure", "restart", "status"),
}

BIND_CONTROLLERS: Final[dict[str, tuple[str, ...]]] = {
    "domain": (
        "searchPrimaryDomain",
        "getPrimaryDomain",
        "addPrimaryDomain",
        "setPrimaryDomain",
        "delPrimaryDomain",
        "get",
        "set",
        "search_primary_domain",
    ),
    "record": (
        "searchRecord",
        "getRecord",
        "addRecord",
        "setRecord",
        "delRecord",
        "search_record",
    ),
    "service": ("reconfigure", "restart", "status"),
}

FIREWALL_CONTROLLERS: Final[dict[str, tuple[str, ...]]] = {
    "alias": (
        "searchItem",
        "getItem",
        "addItem",
        "setItem",
        "delItem",
        "toggleItem",
        "search_item",
    ),
    "filter": (
        "searchRule",
        "getRule",
        "addRule",
        "setRule",
        "delRule",
        "search_rule",
    ),
}

INTERFACES_CONTROLLERS: Final[dict[str, tuple[str, ...]]] = {
    "vlan": (
        "searchItem",
        "getItem",
        "addItem",
        "setItem",
        "delItem",
        "search_item",
    ),
    "vip": (
        "searchItem",
        "getItem",
        "addItem",
        "setItem",
        "delItem",
        "search_item",
    ),
}

KEA_CONTROLLERS: Final[dict[str, tuple[str, ...]]] = {
    "dhcpv4": (
        "searchSubnet",
        "getSubnet",
        "addSubnet",
        "setSubnet",
        "delSubnet",
        "searchReservation",
        "search_subnet",
        "search_reservation",
    ),
    "service": ("reconfigure", "status"),
}

ACME_CONTROLLERS: Final[dict[str, tuple[str, ...]]] = {
    "accounts": ("search", "get", "add", "set", "del"),
    "certificates": ("search", "get", "add", "set", "del"),
    "validations": ("search", "get", "add", "set", "del"),
}


_HERE: Final[pathlib.Path] = pathlib.Path(__file__).parent
_CONTROLLERS_JSON: Final[pathlib.Path] = _HERE / "controllers.json"


def _load_via_filesystem() -> dict[str, Any] | None:
    try:
        from importlib.resources import files as res_files

        for pkg in ("saltext.opnsense.utils", "saltext.opnsense"):
            try:
                pkg_files = res_files(pkg)
                for name in ("controllers.json", "utils/controllers.json"):
                    candidate = pkg_files.joinpath(name)
                    if candidate.is_file():
                        text = candidate.read_text(encoding="utf-8")
                        data = json.loads(text)
                        if data.get("modules"):
                            return data
            except (FileNotFoundError, OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
                log.debug("Failed to load %s/%s via resources: %s", pkg, name, exc)
                continue
            except (ModuleNotFoundError, AttributeError, TypeError) as exc:
                log.debug("importlib.resources failure for %s: %s", pkg, exc)
                continue
    except (ImportError, ModuleNotFoundError, AttributeError) as exc:
        log.debug("importlib.resources not available: %s", exc)

    try:
        if _CONTROLLERS_JSON.exists():
            text = _CONTROLLERS_JSON.read_text(encoding="utf-8")
            data = json.loads(text)
            if data.get("modules"):
                log.debug("Loaded spec from %s", _CONTROLLERS_JSON)
                return data
    except (FileNotFoundError, OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        log.debug("Failed to load %s: %s", _CONTROLLERS_JSON, exc)

    return None


@lru_cache(maxsize=1)
def load_spec() -> dict[str, Any]:
    try:
        data = _load_via_filesystem()
        if data and data.get("modules"):
            return data
    except (OSError, json.JSONDecodeError) as exc:
        log.debug("_load_via_filesystem failed: %s", exc)

    log.debug("Falling back to curated 6-module spec")
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
    return sorted(spec.get("modules", {}).keys()) or sorted(set(CORE_MODULES + PLUGIN_MODULES))


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
        if isinstance(val, tuple):
            return sorted(val)
    return []
