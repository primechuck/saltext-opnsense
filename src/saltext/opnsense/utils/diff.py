"""
Centralized diff engine and value normalization for OPNsense state modules.
"""

from __future__ import annotations

from typing import Any, Final

from saltext.opnsense.utils.common import is_uuid

BOOL_TRUE: Final[frozenset[str]] = frozenset({"1", "true", "yes", "enabled", "on"})
BOOL_FALSE: Final[frozenset[str]] = frozenset({"0", "false", "no", "disabled", "off", ""})

RELATION_KEYS: Final[frozenset[str]] = frozenset(
    {
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
)


def _is_bool_context(key: Any, val: Any, field_meta: dict[str, Any] | None = None) -> bool:
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


def _is_relation_key(key: Any, field_meta: dict[str, Any] | None = None) -> bool:
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


def _str_key(value: Any) -> str:
    return str(value)


def _normalize_bool(val: Any) -> bool | None:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, str)):
        s = str(val).strip().lower()
        if s in BOOL_TRUE:
            return True
        if s in BOOL_FALSE:
            return False
    return None


def _normalize_list(val: Any) -> tuple[Any, ...] | None:
    if isinstance(val, (list, tuple, set)):
        items: list[Any] = []
        for x in val:
            if isinstance(x, str) and "," in x:
                items.extend(s.strip() for s in x.split(",") if s.strip())
            elif isinstance(x, str):
                s = x.strip()
                if s:
                    items.append(s)
            elif x is not None:
                items.append(x)
        return tuple(sorted(items, key=_str_key))
    if isinstance(val, str) and "," in val:
        items = [s.strip() for s in val.split(",") if s.strip()]
        return tuple(sorted(items, key=_str_key))
    return None


def _get_parent_human_str(parent_human: Any) -> str | None:
    if parent_human is None:
        return None
    if isinstance(parent_human, dict):
        if parent_human.get("hostname") and parent_human.get("domain"):
            return f"{parent_human['hostname']}.{parent_human['domain']}".strip()
        if parent_human.get("uuid"):
            return str(parent_human["uuid"]).strip()
        if parent_human.get("name"):
            return str(parent_human["name"]).strip()
        return str(parent_human).strip()
    return str(parent_human).strip()


def _get_value_str(val: Any) -> str:
    if isinstance(val, dict):
        if val.get("uuid") and is_uuid(str(val["uuid"])):
            return str(val["uuid"]).strip()
        if val.get("hostname") and val.get("domain"):
            return f"{val['hostname']}.{val['domain']}".strip()
        if val.get("name"):
            return str(val["name"]).strip()
        return str(val).strip()
    if isinstance(val, str):
        return val.strip()
    return str(val)


def _normalize_relation(
    key: str,
    val: Any,
    parent_human: Any,
    field_meta: dict[str, Any] | None,
    val_str: str,
    ph_str: str | None,
) -> str | None:
    is_rel = _is_relation_key(key, field_meta) or (
        ph_str is not None and (val_str == ph_str or is_uuid(val_str) or isinstance(val, dict))
    )
    if not is_rel:
        return None
    if ph_str:
        if val_str == ph_str:
            return ph_str
        if is_uuid(val_str) or is_uuid(ph_str):
            return ph_str
    return val_str


def _normalize_number(val: Any, val_str: str) -> int | float | None:
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        if isinstance(val, float) and val.is_integer():
            return int(val)
        return val
    if isinstance(val, str) and val_str:
        try:
            return int(val_str)
        except ValueError:
            pass
        try:
            fv = float(val_str)
            return int(fv) if fv.is_integer() else fv
        except ValueError:
            pass
    return None


def normalize_field_value(
    key: str,
    val: Any,
    parent_human: Any | None = None,
    field_meta: dict[str, Any] | None = None,
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

    bool_norm = _normalize_bool(val)
    if bool_norm is not None:
        return bool_norm

    list_norm = _normalize_list(val)
    if list_norm is not None:
        return list_norm

    ph_str = _get_parent_human_str(parent_human)
    val_str = _get_value_str(val)

    rel_norm = _normalize_relation(key, val, parent_human, field_meta, val_str, ph_str)
    if rel_norm is not None:
        return rel_norm

    num_norm = _normalize_number(val, val_str)
    if num_norm is not None:
        return num_norm

    if isinstance(val, str):
        s = val.strip()
        if s.endswith(".") and len(s) > 1 and not s.endswith(".."):
            s = s.rstrip(".")
        return s

    return val


def diff_models(
    existing: dict[str, Any] | None,
    desired: dict[str, Any] | None,
    field_specs: dict[str, dict[str, Any]] | None = None,
    parent_human: str | None = None,
) -> dict[str, dict[str, Any]]:
    """
    Compare existing vs desired dictionary keys using normalize_field_value.
    Ignore 'uuid' key.
    Return {field: {"old": existing_val, "new": desired_val}} ONLY when normalized values genuinely differ.
    """
    existing = existing or {}
    desired = desired or {}
    field_specs = field_specs or {}
    diff: dict[str, dict[str, Any]] = {}

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
