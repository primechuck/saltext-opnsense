import json
import logging
import os
import pathlib
from typing import Any

log = logging.getLogger(__name__)

try:
    from saltext.opnsense.utils.common import camel_to_snake
except Exception:

    def camel_to_snake(name: str) -> str:
        import re

        name = name.replace("-", "_")
        s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
        s1 = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s1)
        s1 = s1.lower()
        return re.sub(r"__+", "_", s1).strip("_")


CORE_MODULES = [
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
]

PLUGIN_MODULES = [
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
]

UNBOUND_CONTROLLERS = {
    "settings": [
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
    ],
    "service": ["reconfigure", "restart", "status"],
}

BIND_CONTROLLERS = {
    "domain": [
        "searchPrimaryDomain",
        "getPrimaryDomain",
        "addPrimaryDomain",
        "setPrimaryDomain",
        "delPrimaryDomain",
        "get",
        "set",
        "search_primary_domain",
    ],
    "record": ["searchRecord", "getRecord", "addRecord", "setRecord", "delRecord", "search_record"],
    "service": ["reconfigure", "restart", "status"],
}

FIREWALL_CONTROLLERS = {
    "alias": [
        "searchItem",
        "getItem",
        "addItem",
        "setItem",
        "delItem",
        "toggleItem",
        "search_item",
    ],
    "filter": ["searchRule", "getRule", "addRule", "setRule", "delRule", "search_rule"],
}

INTERFACES_CONTROLLERS = {
    "vlan": ["searchItem", "getItem", "addItem", "setItem", "delItem", "search_item"],
    "vip": ["searchItem", "getItem", "addItem", "setItem", "delItem", "search_item"],
}

KEA_CONTROLLERS = {
    "dhcpv4": [
        "searchSubnet",
        "getSubnet",
        "addSubnet",
        "setSubnet",
        "delSubnet",
        "searchReservation",
        "search_subnet",
        "search_reservation",
    ],
    "service": ["reconfigure", "status"],
}

ACME_CONTROLLERS = {
    "accounts": ["search", "get", "add", "set", "del"],
    "certificates": ["search", "get", "add", "set", "del"],
    "validations": ["search", "get", "add", "set", "del"],
}


_HERE = pathlib.Path(__file__).parent
_CONTROLLERS_JSON = _HERE / "controllers.json"


def _get_allowed_modules_from_env() -> set[str] | None:
    """
    Read allowlist from env var OPNSENSE_ALLOWED_MODULES.

    P2 slim bloat: saltext-opnsense ships 75 modules + 1736 dynamic wrappers, but
    only unbound+bind are used in this fleet. Allow filtering via env var to reduce
    memory and Salt loader time.

    Env var format: comma-separated, e.g. "unbound,bind,firewall"
    Returns None if not set (no filtering), or set of lowercase module names.

    Also respects OPNSENSE_ALLOWED_MODULES_FILE for file-based list (one per line).
    """
    raw = os.environ.get("OPNSENSE_ALLOWED_MODULES", "").strip()
    if not raw:
        # Optional file-based allowlist for containerized deployments
        file_path = os.environ.get("OPNSENSE_ALLOWED_MODULES_FILE", "")
        if file_path:
            try:
                p = pathlib.Path(file_path)
                if p.exists():
                    raw = p.read_text(encoding="utf-8")
            except Exception as exc:
                log.debug("Failed to read allowlist file %s: %s", file_path, exc)
                raw = ""

    if not raw:
        return None

    parts = []
    for token in raw.replace("\n", ",").split(","):
        token = token.strip().lower()
        if token:
            parts.append(token)

    if not parts:
        return None

    allowed = set(parts)
    log.info("OPNSENSE_ALLOWED_MODULES filtering to %s (from env)", sorted(allowed))
    return allowed


def _filter_spec_by_allowlist(spec: dict[str, Any], allowed: set[str] | None) -> dict[str, Any]:
    if not allowed:
        return spec

    modules = spec.get("modules", {})
    if not modules:
        return spec

    filtered_modules = {k: v for k, v in modules.items() if k.lower() in allowed}
    # If allowlist contains modules not in spec, log warning but don't fail
    missing = allowed - {k.lower() for k in modules.keys()}
    if missing:
        log.warning("Allowlist contains unknown modules not in spec: %s", sorted(missing))

    # Always keep core fallback modules if they were requested? No, strict filter per P2.
    spec_filtered = dict(spec)
    spec_filtered["modules"] = filtered_modules
    spec_filtered["_filtered_by_allowlist"] = sorted(allowed)
    spec_filtered["_original_module_count"] = len(modules)
    spec_filtered["_filtered_module_count"] = len(filtered_modules)
    log.info(
        "Filtered spec from %d to %d modules via allowlist %s",
        len(modules),
        len(filtered_modules),
        sorted(allowed),
    )
    return spec_filtered


def _load_via_filesystem() -> dict[str, Any] | None:
    candidates = [
        _CONTROLLERS_JSON,
        pathlib.Path.cwd() / "src" / "saltext" / "opnsense" / "utils" / "controllers.json",
    ]

    try:
        from importlib.resources import files as res_files

        for pkg in ["saltext.opnsense.utils", "saltext.opnsense"]:
            try:
                pkg_files = res_files(pkg)
                for name in ["controllers.json", "utils/controllers.json"]:
                    candidate = pkg_files.joinpath(name)
                    if candidate.is_file():
                        data = json.loads(candidate.read_text())
                        if data.get("modules"):
                            return data
            except Exception:
                continue
    except Exception as exc:
        log.debug("importlib.resources load failed: %s", exc)

    for path in candidates:
        try:
            if path.exists():
                data = json.loads(path.read_text())
                if data.get("modules"):
                    log.debug("Loaded spec from %s", path)
                    return data
        except Exception as exc:
            log.debug("Failed to load %s: %s", path, exc)
            continue
    return None


def load_spec(allowlist: list[str] | set[str] | None = None) -> dict[str, Any]:
    """
    Load OPNsense API spec, with optional allowlist filtering.

    P2 slim: supports filtering via:
    - explicit allowlist param (list/set of module names)
    - env var OPNSENSE_ALLOWED_MODULES (comma-separated)
    - env var OPNSENSE_ALLOWED_MODULES_FILE (file path, one per line)

    Example:
        load_spec(allowlist=["unbound", "bind"])
        # or
        OPNSENSE_ALLOWED_MODULES=unbound,bind python -m ...

    Returns spec dict with 'modules' filtered if allowlist present.
    """
    try:
        data = _load_via_filesystem()
        if data and data.get("modules"):
            spec = data
        else:
            raise ValueError("No filesystem spec")
    except Exception as exc:
        log.debug("_load_via_filesystem failed: %s, falling back to curated", exc)
        spec = {
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

    # Resolve allowlist: explicit param takes precedence over env
    allowed: set[str] | None = None
    if allowlist is not None:
        allowed = {str(m).strip().lower() for m in allowlist if str(m).strip()}
    else:
        allowed = _get_allowed_modules_from_env()

    if allowed:
        spec = _filter_spec_by_allowlist(spec, allowed)

    return spec


def list_modules(allowlist: list[str] | set[str] | None = None) -> list[str]:
    # allowlist param for direct call, else env var via load_spec
    if allowlist is not None:
        spec = load_spec(allowlist=allowlist)
    else:
        spec = load_spec()
    return sorted(spec.get("modules", {}).keys()) or sorted(set(CORE_MODULES + PLUGIN_MODULES))


def list_controllers(module: str, allowlist: list[str] | set[str] | None = None) -> list[str]:
    if allowlist is not None:
        spec = load_spec(allowlist=allowlist)
    else:
        spec = load_spec()
    mods = spec.get("modules", {})
    if module in mods:
        return sorted(mods[module].keys())
    return []


def list_actions(module: str, controller: str, allowlist: list[str] | set[str] | None = None) -> list[str]:
    if allowlist is not None:
        spec = load_spec(allowlist=allowlist)
    else:
        spec = load_spec()
    mods = spec.get("modules", {})
    if module in mods and controller in mods[module]:
        val = mods[module][controller]
        if isinstance(val, dict):
            return sorted(val.keys())
        if isinstance(val, list):
            return sorted(val)
    return []
