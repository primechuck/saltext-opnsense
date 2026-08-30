from __future__ import annotations

import re
from types import MappingProxyType
from typing import Any, Final

_UUID_RE: Final[re.Pattern[str]] = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)

_RECONFIGURE_DEFAULTS_RAW: Final[dict[str, str]] = {
    "unbound": "unbound/service/reconfigure",
    "bind": "bind/service/reconfigure",
    "kea": "kea/service/reconfigure",
    "acmeclient": "acmeclient/service/reconfigure",
    "dns": "unbound/service/reconfigure",
    "acme": "acmeclient/service/reconfigure",
    "dhcp": "kea/service/reconfigure",
    "firewall": "firewall/alias/reconfigure",
    "interfaces": "interfaces/vlan/reconfigure",
}
RECONFIGURE_DEFAULTS: Final[MappingProxyType[str, str]] = MappingProxyType(
    _RECONFIGURE_DEFAULTS_RAW
)

_ENABLED_TRUE: Final[frozenset[str]] = frozenset({"1", "true", "yes", "enabled", "on"})
_ENABLED_FALSE: Final[frozenset[str]] = frozenset({"0", "false", "no", "disabled", "off"})


def camel_to_snake(name: str) -> str:
    name = name.replace("-", "_")
    s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    s1 = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s1)
    s1 = s1.lower()
    s1 = re.sub(r"__+", "_", s1)
    s1 = re.sub(r"[^0-9a-z_]+", "_", s1)
    return s1.strip("_")


def snake_to_pascal(snake: str) -> str:
    return "".join(p.capitalize() for p in snake.split("_") if p)


def strip_salt_internal_kwargs(kwargs: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in kwargs.items() if not k.startswith("__")}


def is_uuid(v: Any) -> bool:
    if not isinstance(v, str):
        return False
    return bool(_UUID_RE.match(v.strip()))


def get_reconfigure(
    reconfigure: str | bool | None | dict[str, str] | Any,
    module: str,
) -> str | dict[str, str] | None:
    if reconfigure is False:
        return None
    if reconfigure is True or reconfigure is None:
        return RECONFIGURE_DEFAULTS.get(module)
    if isinstance(reconfigure, str):
        stripped = reconfigure.strip()
        if stripped == "":
            return RECONFIGURE_DEFAULTS.get(module)
        return stripped
    if isinstance(reconfigure, dict):
        return reconfigure
    return RECONFIGURE_DEFAULTS.get(module)


def parse_reconfigure_path(
    path: str | dict[str, str] | None,
) -> dict[str, str] | None:
    if not path:
        return None
    if isinstance(path, dict):
        return path
    if not isinstance(path, str):
        return None
    parts = path.split("/")
    if len(parts) == 3:
        return {"module": parts[0], "controller": parts[1], "action": parts[2]}
    if len(parts) == 2:
        return {"module": parts[0], "controller": parts[1], "action": "reconfigure"}
    return None


def fqdn_to_parts(fqdn: str) -> tuple[str | None, str | None]:
    if not isinstance(fqdn, str) or "." not in fqdn:
        return None, None
    head, tail = fqdn.split(".", 1)
    return head, tail


def build_fqdn(hostname: str, domain: str) -> str:
    hostname = (hostname or "").strip().strip(".")
    domain = (domain or "").strip().strip(".")
    if not hostname:
        return domain
    if not domain:
        return hostname
    return f"{hostname}.{domain}"


def normalize_enabled(v: Any) -> str:
    if isinstance(v, bool):
        return "1" if v else "0"
    if isinstance(v, (int, float)):
        return "1" if v else "0"
    s = str(v).lower()
    if s in _ENABLED_TRUE:
        return "1"
    if s in _ENABLED_FALSE:
        return "0"
    return "1" if v else "0"
