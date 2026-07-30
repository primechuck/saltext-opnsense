import json
import pathlib
from typing import Any

# Primary source: models.json co-located with this file (declared as
# package-data in pyproject.toml so it is always present after install).
SPEC_FILE = pathlib.Path(__file__).with_name("models.json")

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
    "dec_hw",
    "dhcp",
    "dnscryptproxy",
    "dyndns",
    "freeradius",
    "haproxy",
    "nginx",
    "postfix",
    "quagga",
    "tor",
    "wireguard",
    "kea",
]


def load_spec() -> dict[str, Any]:
    # Try the canonical package JSON first, then a fallback location for
    # unusual in-tree installations.
    for path in [
        SPEC_FILE,
        pathlib.Path.cwd() / "src" / "saltext" / "opnsense" / "utils" / "models.json",
    ]:
        if path.exists():
            try:
                data = json.loads(path.read_text())
                mods = data.get("models") or {}
                if mods:
                    return data
            except Exception:
                continue

    return {
        "generated": False,
        "models": {},
        "meta": {},
    }


def list_modules() -> list[str]:
    spec = load_spec()
    return sorted((spec.get("models") or {}).keys())


def list_models(module: str) -> list[str]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module in mods:
        return sorted(mods[module].keys())
    return []


def list_arrays(module: str, model: str) -> list[str]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module in mods and model in mods[module]:
        return sorted(mods[module][model].keys())
    return []


def get_fields(module: str, model: str, array: str) -> dict[str, Any]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module in mods and model in mods[module] and array in mods[module][model]:
        return mods[module][model][array]
    return {}


def get_model_arrays(module: str, model: str) -> dict[str, Any]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module in mods and model in mods[module]:
        return mods[module][model]
    return {}


def list_module_models(module: str) -> dict[str, list[str]]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module not in mods:
        return {}
    out: dict[str, list[str]] = {}
    for model_name, arrays in mods[module].items():
        out[model_name] = sorted(arrays.keys())
    return out


def _is_relation_type(field_type: str) -> bool:
    if not isinstance(field_type, str):
        return False
    ft = field_type
    return "ModelRelationField" in ft or "RelationField" in ft or ft.endswith("RelationField")


def is_relation_field(field_meta: dict[str, Any]) -> bool:
    if not isinstance(field_meta, dict):
        return False
    t = field_meta.get("type", "")
    if _is_relation_type(t):
        return True
    if "relation" in field_meta or "relation_targets" in field_meta:
        return True
    return False


def get_relation_fields(module: str, model: str, array: str) -> dict[str, Any]:
    fields = get_fields(module, model, array)
    if not fields:
        return {}
    out: dict[str, Any] = {}
    for fname, fmeta in fields.items():
        if is_relation_field(fmeta):
            out[fname] = fmeta
    return out


def get_relation_fields_for_array(module: str, array: str) -> dict[str, Any]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module not in mods:
        return {}
    for model_name, arrays in mods[module].items():
        if array in arrays:
            rel = get_relation_fields(module, model_name, array)
            if rel:
                return rel
    for model_name, arrays in mods[module].items():
        for arr_name, fields in arrays.items():
            if arr_name == array or array in arr_name or arr_name in array:
                rel = get_relation_fields(module, model_name, arr_name)
                if rel:
                    return rel
    return {}


def get_relation_targets(field_meta: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(field_meta, dict):
        return []
    if "relation_targets" in field_meta and isinstance(field_meta["relation_targets"], list):
        return field_meta["relation_targets"]
    if "relation" in field_meta:
        rel = field_meta["relation"]
        if isinstance(rel, dict):
            return [rel]
        if isinstance(rel, list):
            return rel
    return []


def parse_relation_source(source: str) -> tuple[str, str]:
    if not source:
        return "", ""
    parts = source.split(".")
    if len(parts) >= 3 and parts[0] == "OPNsense":
        mod = parts[1].lower()
        model = parts[2]
        return mod, model
    if len(parts) >= 2:
        return parts[-2].lower(), parts[-1]
    return source.lower(), ""


def parse_relation_items(items: str) -> tuple[str, str]:
    if not items:
        return "", ""
    if "." in items:
        container, arr = items.rsplit(".", 1)
        return container, arr
    return "", items


def find_model_for_array(module: str, type_name: str) -> tuple[str, str, dict]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module not in mods:
        return "", "", {}
    cands = []
    tn = type_name.lower()
    for model_name, arrays in mods[module].items():
        for arr_name, fields in arrays.items():
            arr_low = arr_name.lower()
            score = 0
            if tn == arr_low:
                score = 100
            elif tn.endswith("_" + arr_low) or tn.endswith(arr_low):
                score = 90
            elif arr_low in tn:
                score = 80
            elif tn in arr_low:
                score = 70
            elif "_" in tn and arr_low == tn.split("_")[-1]:
                score = 85
            elif "_" in tn and arr_low == tn.split("_")[0]:
                score = 75
            if score:
                cands.append((score, model_name, arr_name, fields))
    if not cands:
        return "", "", {}
    cands.sort(key=lambda x: (-x[0], x[1], x[2]))
    _, m, a, f = cands[0]
    return m, a, f


def find_model_containing_field(module: str, field_name: str) -> list[tuple[str, str, dict]]:
    spec = load_spec()
    mods = spec.get("models") or {}
    if module not in mods:
        return []
    out = []
    for model_name, arrays in mods[module].items():
        for arr_name, fields in arrays.items():
            if field_name in fields and is_relation_field(fields[field_name]):
                out.append((model_name, arr_name, fields[field_name]))
    return out


def all_relation_fields(module: str | None = None) -> dict[str, list[dict[str, Any]]]:
    spec = load_spec()
    mods = spec.get("models") or {}
    result: dict[str, list[dict]] = {}
    target_modules = [module] if module else list(mods.keys())
    for mod in target_modules:
        if mod not in mods:
            continue
        for model_name, arrays in mods[mod].items():
            for arr_name, fields in arrays.items():
                for fname, fmeta in fields.items():
                    if is_relation_field(fmeta):
                        key = f"{mod}.{model_name}.{arr_name}.{fname}"
                        result.setdefault(mod, []).append(
                            {
                                "key": key,
                                "model": model_name,
                                "array": arr_name,
                                "field": fname,
                                "meta": fmeta,
                            }
                        )
    return result
