import re
from typing import Any

_UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)

RECONFIGURE_DEFAULTS = {
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


def strip_salt_internal_kwargs(kwargs: dict) -> dict:
    return {k: v for k, v in kwargs.items() if not k.startswith("__")}


def is_uuid(v: Any) -> bool:
    if not isinstance(v, str):
        return False
    return bool(_UUID_RE.match(v.strip()))


def get_reconfigure(reconfigure, module: str):
    if reconfigure is False:
        return None
    if reconfigure is True or reconfigure is None:
        return RECONFIGURE_DEFAULTS.get(module)
    if isinstance(reconfigure, str):
        if reconfigure.strip() == "":
            return RECONFIGURE_DEFAULTS.get(module)
        return reconfigure.strip()
    if isinstance(reconfigure, dict):
        return reconfigure
    return RECONFIGURE_DEFAULTS.get(module)


def parse_reconfigure_path(path):
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


def fqdn_to_parts(fqdn: str):
    if not isinstance(fqdn, str) or "." not in fqdn:
        return None, None
    parts = fqdn.split(".", 1)
    return parts[0], parts[1]


def build_fqdn(hostname: str, domain: str) -> str:
    hostname = (hostname or "").strip().strip(".")
    domain = (domain or "").strip().strip(".")
    if not hostname:
        return domain
    if not domain:
        return hostname
    return f"{hostname}.{domain}"


def normalize_enabled(v):
    if isinstance(v, bool):
        return "1" if v else "0"
    if isinstance(v, (int, float)):
        return "1" if v else "0"
    s = str(v).lower()
    if s in ("1", "true", "yes", "enabled", "on"):
        return "1"
    if s in ("0", "false", "no", "disabled", "off"):
        return "0"
    return "1" if v else "0"
