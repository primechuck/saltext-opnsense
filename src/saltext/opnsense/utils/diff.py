from __future__ import annotations

from typing import Any, Final

from saltext.opnsense.utils.common import is_uuid

BOOL_TRUE: Final[frozenset[str]] = frozenset({"1", "true", "yes", "enabled", "on"})
BOOL_FALSE: Final[frozenset[str]] = frozenset({"0", "false", "no", "disabled", "off", ""})


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
        return tuple(sorted(items, key=str))
    if isinstance(val, str) and "," in val:
        return tuple(sorted([s.strip() for s in val.split(",") if s.strip()], key=str))
    return None


def _norm_str(val: Any) -> str:
    if not isinstance(val, str):
        return ""
    s = val.strip()
    if s.endswith(".") and len(s) > 1 and not s.endswith(".."):
        s = s.rstrip(".")
    return s


def normalize_field_value(
    key: str, val: Any, parent_human: Any | None = None, field_meta: dict[str, Any] | None = None
) -> Any:
    # 1. None handling
    if val is None:
        k = str(key).lower()
        if k in ("enabled", "disabled") or k.endswith("_enabled") or k.startswith("is_"):
            return False
        return ""

    # 2. bool
    bn = _normalize_bool(val)
    if bn is not None:
        return bn

    # 3. list/csv
    ln = _normalize_list(val)
    if ln is not None:
        return ln

    # 4. parent_human relation equivalence: UUID vs human FQDN should be equal
    ph_str = None
    if parent_human:
        if isinstance(parent_human, dict):
            if parent_human.get("hostname") and parent_human.get("domain"):
                ph_str = f"{parent_human['hostname']}.{parent_human['domain']}"
            elif parent_human.get("uuid"):
                ph_str = str(parent_human.get("uuid")).strip()
            elif parent_human.get("name"):
                ph_str = str(parent_human.get("name")).strip()
            else:
                ph_str = str(parent_human).strip()
        else:
            ph_str = str(parent_human).strip()

    # dict with uuid -> return ph_str if parent_human present and uuid-like
    if isinstance(val, dict):
        if val.get("uuid") and is_uuid(str(val["uuid"])):
            uuid_v = str(val["uuid"]).strip()
            if ph_str and (ph_str == uuid_v or is_uuid(ph_str) or ph_str):
                # For relation fields, uuid and human are equivalent -> return parent_human
                # Check if key looks like relation or parent_human supplied
                if parent_human:
                    return ph_str
            return uuid_v
        if val.get("hostname") and val.get("domain"):
            fqdn = f"{val['hostname']}.{val['domain']}".strip()
            if ph_str and ph_str == fqdn:
                return ph_str
            return fqdn
        if val.get("name"):
            return _norm_str(val.get("name"))

    # handle relation equivalence for string values
    if isinstance(val, str):
        vs = _norm_str(val)
        if ph_str:
            # if val is uuid and parent_human is fqdn, or vice versa, treat as equal by returning ph_str
            if is_uuid(vs) or is_uuid(ph_str):
                return ph_str
            if vs == ph_str:
                return ph_str
        # number
        try:
            if vs and vs not in (ph_str or ""):
                # don't parse IPs as numbers – only pure digits
                if vs.isdigit() or (vs.lstrip("-").isdigit()):
                    return int(vs)
                # float check only if not containing dots beyond maybe one? keep simple
                fv = float(vs)
                if "." not in vs or vs.replace(".", "", 1).replace("-", "", 1).isdigit():
                    return int(fv) if fv.is_integer() else fv
        except ValueError:
            pass
        # track number parsing for pure numeric strings
        # more robust int parsing
        s = vs
        try:
            if (
                s
                and s[0] not in (".",)
                and s.replace("-", "", 1).replace(".", "", 1).isdigit() is False
            ):
                pass
            else:
                # attempt int
                if s.lstrip("-").isdigit():
                    return int(s)
                fv = float(s)
                return int(fv) if fv.is_integer() else fv
        except ValueError:
            pass
        return s

    if isinstance(val, (int, float)) and not isinstance(val, bool):
        if isinstance(val, float) and val.is_integer():
            return int(val)
        return val
    return val


def diff_models(
    existing: dict[str, Any] | None,
    desired: dict[str, Any] | None,
    field_specs: dict[str, dict[str, Any]] | None = None,
    parent_human: str | None = None,
) -> dict[str, dict[str, Any]]:
    existing = existing or {}
    desired = desired or {}
    field_specs = field_specs or {}
    diff: dict[str, dict[str, Any]] = {}
    for k, dv in desired.items():
        if k == "uuid":
            continue
        ev = existing.get(k)
        fm = field_specs.get(k)
        if normalize_field_value(
            k, ev, parent_human=parent_human, field_meta=fm
        ) != normalize_field_value(k, dv, parent_human=parent_human, field_meta=fm):
            diff[k] = {"old": ev, "new": dv}
    return diff
