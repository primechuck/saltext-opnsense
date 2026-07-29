"""
Centralized diff engine and value normalization for OPNsense state modules.
"""

from typing import Any

from saltext.opnsense.utils.common import is_uuid

BOOL_TRUE = {"1", "true", "yes", "enabled", "on"}
BOOL_FALSE = {"0", "false", "no", "disabled", "off", ""}

RELATION_KEYS = {
    "host",
    "domain",
    "subnet",
    "account",
    "validationmethod",
    "action",
    "server",
    "alias",
    "rule",
    "item",
}


def _is_bool_context(key: Any, val: Any, field_meta: dict | None = None) -> bool:
    if isinstance(val, bool):
        return True
    if isinstance(key, str):
        k_low = key.lower()
        if (
            k_low in ("enabled", "disabled")
            or k_low.endswith("_enabled")
            or k_low.startswith("is_")
        ):
            return True
    if field_meta and isinstance(field_meta, dict):
        ftype = str(field_meta.get("type", ""))
        if ftype in ("BooleanField", "OptionField") or "bool" in ftype.lower():
            return True
    if isinstance(val, str) and val.strip().lower() in (
        "true",
        "false",
        "yes",
        "no",
        "enabled",
        "disabled",
    ):
        return True
    return False


def _is_relation_key(key: Any, field_meta: dict | None = None) -> bool:
    if not isinstance(key, str):
        return False
    k_low = key.lower()
    if k_low in RELATION_KEYS or k_low.endswith("_uuid") or k_low.endswith("_ref"):
        return True
    if field_meta and isinstance(field_meta, dict):
        ftype = str(field_meta.get("type", ""))
        if (
            "relation" in ftype.lower()
            or "relation" in field_meta
            or "relation_targets" in field_meta
        ):
            return True
    return False


def normalize_field_value(
    key: str,
    val: Any,
    parent_human: Any = None,
    field_meta: dict | None = None,
) -> Any:
    """
    Normalize a single field value for order-agnostic and type-safe comparison.

    Rules:
    - Booleans: "1", 1, True, "true", "yes", "enabled" -> True
                "0", 0, False, "false", "no", "disabled", "" -> False
    - Relation / Foreign Key Fields:
                UUID string and human reference (parent_human) are treated as equivalent
                if val matches parent_human or if val is UUID and parent_human is provided.
                Dicts with FQDN / UUID are reduced to FQDN or UUID.
    - Lists / CSV Strings:
                Lists ["lan", "wan"] and CSV strings "lan,wan" -> sorted tuples for order-agnostic comparison.
    - Numbers:  Numeric strings "80" vs 80 -> int or float.
    - Strings:  Stripped surrounding whitespace.
    """
    if val is None:
        return False if _is_bool_context(key, val, field_meta) else ""

    # 1. Booleans
    if isinstance(val, bool):
        return val

    if isinstance(val, (int, str)):
        s = str(val).strip().lower()
        if s in BOOL_TRUE:
            return True
        if s in BOOL_FALSE:
            return False

    # 2. Lists / Tuples / Sets / CSV Strings
    if isinstance(val, (list, tuple, set)):
        items = []
        for x in val:
            if isinstance(x, str) and "," in x:
                items.extend(s.strip() for s in x.split(",") if s.strip())
            elif isinstance(x, str):
                s = x.strip()
                if s:
                    items.append(s)
            elif x is not None:
                items.append(x)
        return tuple(sorted(items, key=lambda i: str(i)))

    if isinstance(val, str) and "," in val:
        items = [s.strip() for s in val.split(",") if s.strip()]
        return tuple(sorted(items, key=lambda i: str(i)))

    # 3. Relation / Foreign Key Fields & Dicts
    ph_str = None
    if parent_human is not None:
        if isinstance(parent_human, dict):
            if parent_human.get("hostname") and parent_human.get("domain"):
                ph_str = f"{parent_human['hostname']}.{parent_human['domain']}".strip()
            elif parent_human.get("uuid"):
                ph_str = str(parent_human["uuid"]).strip()
            elif parent_human.get("name"):
                ph_str = str(parent_human["name"]).strip()
            else:
                ph_str = str(parent_human).strip()
        else:
            ph_str = str(parent_human).strip()

    if isinstance(val, dict):
        if val.get("uuid") and is_uuid(str(val["uuid"])):
            val_str = str(val["uuid"]).strip()
        elif val.get("hostname") and val.get("domain"):
            val_str = f"{val['hostname']}.{val['domain']}".strip()
        elif val.get("name"):
            val_str = str(val["name"]).strip()
        else:
            val_str = str(val).strip()
    elif isinstance(val, str):
        val_str = val.strip()
    else:
        val_str = str(val)

    if _is_relation_key(key, field_meta) or (
        ph_str and (val_str == ph_str or is_uuid(val_str) or isinstance(val, dict))
    ):
        if ph_str:
            if val_str == ph_str:
                return ph_str
            if is_uuid(val_str) or is_uuid(ph_str):
                return ph_str
        return val_str

    # 4. Numbers
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        if isinstance(val, float) and val.is_integer():
            return int(val)
        return val

    if isinstance(val, str) and val_str:
        try:
            val_int = int(val_str)
            return val_int
        except ValueError:
            pass
        try:
            val_float = float(val_str)
            if val_float.is_integer():
                return int(val_float)
            return val_float
        except ValueError:
            pass

    # 5. Strings
    if isinstance(val, str):
        s = val.strip()
        if s.endswith(".") and len(s) > 1 and not s.endswith(".."):
            s = s.rstrip(".")
        return s

    return val


def diff_models(
    existing: dict | None,
    desired: dict | None,
    field_specs: dict | None = None,
    parent_human: str | None = None,
) -> dict:
    """
    Compare existing vs desired dictionary keys using normalize_field_value.
    Ignore 'uuid' key.
    Return {field: {"old": existing_val, "new": desired_val}} ONLY when normalized values genuinely differ.
    """
    existing = existing or {}
    desired = desired or {}
    field_specs = field_specs or {}
    diff = {}

    for k, desired_val in desired.items():
        if k == "uuid":
            continue

        existing_val = existing.get(k)
        field_meta = field_specs.get(k)

        norm_existing = normalize_field_value(
            k, existing_val, parent_human=parent_human, field_meta=field_meta
        )
        norm_desired = normalize_field_value(
            k, desired_val, parent_human=parent_human, field_meta=field_meta
        )

        if norm_existing != norm_desired:
            diff[k] = {"old": existing_val, "new": desired_val}

    return diff
