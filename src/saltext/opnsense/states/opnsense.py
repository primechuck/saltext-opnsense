import logging
import socket

log = logging.getLogger(__name__)

from saltext.opnsense.utils.common import (
    camel_to_snake as _camel_to_snake_generic,
)
from saltext.opnsense.utils.common import (
    is_uuid as _is_uuid,
)
from saltext.opnsense.utils.diff import diff_models

__virtualname__ = "opnsense"

_RESOLVE_MAP = {
    "host": {
        "module": "unbound",
        "controller": "settings",
        "type": "host_override",
        "search_field": "hostname",
        "match_keys": ["hostname", "domain"],
    },
    "subnet": {
        "module": "kea",
        "controller": "dhcpv4",
        "type": "subnet",
        "search_field": "subnet",
    },
    "domain": {
        "module": "bind",
        "controller": "domain",
        "type": "primary_domain",
        "search_field": "domainname",
    },
    "primary_domain": {
        "module": "bind",
        "controller": "domain",
        "type": "primary_domain",
        "search_field": "domainname",
    },
    "account": {
        "module": "acmeclient",
        "controller": "accounts",
        "type": "account",
        "search_field": "name",
    },
    "validationMethod": {
        "module": "acmeclient",
        "controller": "validations",
        "type": "validation",
        "search_field": "name",
    },
    "validation": {
        "module": "acmeclient",
        "controller": "validations",
        "type": "validation",
        "search_field": "name",
    },
    "restartActions": {
        "module": "acmeclient",
        "controller": "actions",
        "type": "action",
        "search_field": "name",
    },
    "action": {
        "module": "acmeclient",
        "controller": "actions",
        "type": "action",
        "search_field": "name",
    },
    "actions": {
        "module": "acmeclient",
        "controller": "actions",
        "type": "action",
        "search_field": "name",
    },
}

_RECONFIGURE_MODULE_DEFAULTS = {
    "unbound": "unbound/service/reconfigure",
    "bind": "bind/service/reconfigure",
    "kea": "kea/service/reconfigure",
    "acmeclient": "acmeclient/service/reconfigure",
}

_RECONFIGURE_OVERRIDES = {
    ("unbound", "settings"): "unbound/service/reconfigure",
    ("unbound", "settings", "host_alias"): "unbound/service/reconfigure",
    ("unbound", "settings", "host_override"): "unbound/service/reconfigure",
    ("bind", "domain"): "bind/service/reconfigure",
    ("bind", "record"): "bind/service/reconfigure",
    ("bind", "general"): "bind/service/reconfigure",
    ("kea", "dhcpv4"): "kea/service/reconfigure",
    ("kea", "dhcpv6"): "kea/service/reconfigure",
    ("acmeclient", "accounts"): "acmeclient/service/reconfigure",
    ("acmeclient", "validations"): "acmeclient/service/reconfigure",
    ("acmeclient", "certificates"): "acmeclient/service/reconfigure",
    ("firewall", "alias"): "firewall/alias/reconfigure",
    ("firewall", "alias", "item"): "firewall/alias/reconfigure",
    ("firewall", "filter"): "firewall/filter_base/apply",
    ("firewall", "filter", "rule"): "firewall/filter_base/apply",
    ("firewall", "filter_base"): "firewall/filter_base/apply",
}


def _singularize(name: str) -> str:
    n = name.lower()
    if n.endswith("ies") and len(n) > 3:
        return n[:-3] + "y"
    if n.endswith("s") and len(n) > 1 and not n.endswith("ss") and not n.endswith("us"):
        return n[:-1]
    return n


def _safe_search_fn():
    try:
        fn = __salt__["opnsense.search"]  # type: ignore[name-defined]
        return fn
    except Exception:
        try:
            glb = globals().get("__salt__")
            if glb and "opnsense.search" in glb:
                return glb["opnsense.search"]
        except Exception:
            pass
    return None


def _safe_call_fn():
    try:
        fn = __salt__["opnsense.call"]  # type: ignore[name-defined]
        return fn
    except Exception:
        try:
            glb = globals().get("__salt__")
            if glb and "opnsense.call" in glb:
                return glb["opnsense.call"]
        except Exception:
            pass
    return None


def _safe_list_controllers_fn():
    try:
        fn = __salt__["opnsense.list_api_controllers"]  # type: ignore[name-defined]
        return fn
    except Exception:
        return None


def _safe_list_actions_fn():
    try:
        fn = __salt__["opnsense.list_api_actions"]  # type: ignore[name-defined]
        return fn
    except Exception:
        return None


def _safe_list_controllers(module: str):
    try:
        fn = _safe_list_controllers_fn()
        if fn:
            res = fn(module)
            if isinstance(res, list):
                return res
    except Exception:
        pass
    try:
        from saltext.opnsense.utils.api_spec import list_controllers

        return list_controllers(module)
    except Exception:
        return []


def _safe_list_actions(module: str, controller: str):
    try:
        fn = _safe_list_actions_fn()
        if fn:
            res = fn(module, controller)
            if isinstance(res, list):
                return res
    except Exception:
        pass
    try:
        from saltext.opnsense.utils.api_spec import list_actions

        return list_actions(module, controller)
    except Exception:
        return []


def _do_search(module: str, controller: str, typ: str, search_phrase: str = ""):
    fn = _safe_search_fn()
    if fn is None:
        return []
    try:
        res = fn(module, controller, typ, search_phrase=search_phrase, row_count=-1)
        return res.get("rows", []) if isinstance(res, dict) else []
    except TypeError:
        try:
            res = fn(module, controller, typ, row_count=-1)
            return res.get("rows", []) if isinstance(res, dict) else []
        except Exception as exc:
            log.debug("search %s/%s/%s failed: %s", module, controller, typ, exc)
            return []
    except Exception as exc:
        log.debug("search %s/%s/%s failed: %s", module, controller, typ, exc)
        return []


_MODELS_UTILS = None
_MODELS_DATA = None


def _load_models_utils():
    global _MODELS_UTILS
    if _MODELS_UTILS is not None:
        return _MODELS_UTILS
    for cand in ("saltext.opnsense.utils.models",):
        try:
            import importlib

            m = importlib.import_module(cand)
            if hasattr(m, "get_relation_fields"):
                _MODELS_UTILS = m
                return m
        except Exception:
            continue
    try:
        import importlib

        m = importlib.import_module("saltext.opnsense.utils.models")
        _MODELS_UTILS = m
        return m
    except Exception as exc:
        log.debug("load models utils failed: %s", exc)
    return None


def _load_models_data_dict():
    global _MODELS_DATA
    if _MODELS_DATA is not None:
        return _MODELS_DATA
    try:
        mu = _load_models_utils()
        if mu and hasattr(mu, "load_spec"):
            spec = mu.load_spec()
            models = spec.get("models") or {}
            if models:
                _MODELS_DATA = models
                return models
    except Exception as exc:
        log.debug("load models dict via utils failed: %s", exc)
    _MODELS_DATA = {}
    return {}


def _find_model_for_type(module: str, type_name: str):
    mu = _load_models_utils()
    if mu and hasattr(mu, "find_model_for_array"):
        try:
            mname, aname, fields = mu.find_model_for_array(module, type_name)
            if mname:
                return mname, aname, fields
        except Exception as exc:
            log.debug("find_model_for_array failed: %s", exc)
    models = _load_models_data_dict()
    if module not in models:
        return "", "", {}
    tn = (type_name or "").lower()
    cands = []
    for model_name, arrays in models[module].items():
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
    _, mn, an, f = cands[0]
    return mn, an, f


def _get_relation_fields_for_parent(module: str, type_name: str):
    mu = _load_models_utils()
    mname, aname, fields = _find_model_for_type(module, type_name)
    if not mname:
        return {}, "", ""
    if mu and hasattr(mu, "get_relation_fields"):
        try:
            rel = mu.get_relation_fields(module, mname, aname)
            return rel, mname, aname
        except Exception as exc:
            log.debug("get_relation_fields failed: %s", exc)
    out = {}
    for fname, fmeta in (fields or {}).items():
        if not isinstance(fmeta, dict):
            continue
        t = fmeta.get("type", "")
        if "Relation" in t or "relation" in fmeta:
            out[fname] = fmeta
    return out, mname, aname


def _parse_relation_source(source: str):
    if not source:
        return "", ""
    parts = source.split(".")
    if len(parts) >= 3 and parts[0] == "OPNsense":
        return parts[1].lower(), parts[2]
    if len(parts) >= 2:
        return parts[-2].lower(), parts[-1]
    return source.lower(), ""


def _parse_relation_items(items: str):
    if not items:
        return "", ""
    if "." in items:
        container, arr = items.rsplit(".", 1)
        return container, arr
    return "", items


def _get_candidate_locations(target_module: str, target_array: str):
    modules_dict = {}
    try:
        from saltext.opnsense.utils.api_spec import load_spec as ctrl_load

        spec = ctrl_load()
        modules_dict = spec.get("modules") or {}
    except Exception:
        pass
    if target_module not in modules_dict:
        if target_array:
            return [
                ("settings", target_array),
                ("domain", target_array),
                ("record", target_array),
                ("dhcpv4", target_array),
            ]
        return []
    ctrls = modules_dict[target_module]
    candidates = []
    ta = (target_array or "").lower()
    for ctrl_name, actions in ctrls.items():
        if not isinstance(actions, list):
            if isinstance(actions, dict):
                actions = list(actions.keys())
            else:
                continue
        for act in actions:
            if not isinstance(act, str):
                continue
            low = act.lower()
            if not low.startswith("search"):
                continue
            suffix = act[len("search") :]
            if suffix.startswith("_"):
                suffix = suffix[1:]
            if not suffix:
                pseudo = _singularize(ctrl_name)
                typ = _camel_to_snake_generic(pseudo)
                if typ:
                    candidates.append((ctrl_name, typ, 50, act))
                continue
            typ = _camel_to_snake_generic(suffix)
            if not typ:
                continue
            score = 0
            if ta and typ == ta:
                score = 100
            elif ta and typ.endswith("_" + ta):
                score = 90
            elif ta and ta in typ:
                score = 80
            elif ta and typ in ta:
                score = 60
            else:
                score = 10
            candidates.append((ctrl_name, typ, score, act))
    candidates.sort(key=lambda x: (-x[2], x[0], x[1]))
    seen = set()
    uniq = []
    for ctrl, typ, score, act in candidates:
        key = (ctrl, typ)
        if key in seen:
            continue
        seen.add(key)
        if ta and score < 10:
            continue
        if ta == "" or score >= 10:
            uniq.append((ctrl, typ))
    if not uniq and ta:
        for ctrl_name in ctrls.keys():
            uniq.append((ctrl_name, ta))
    return uniq


def _match_rows_to_value(value, rows, display_fields, target_array=""):
    if not rows:
        return None
    if isinstance(value, dict):
        hostname = value.get("hostname")
        domain = value.get("domain")
        if hostname and domain:
            for row in rows:
                if row.get("hostname") == hostname and row.get("domain") == domain:
                    if row.get("uuid"):
                        return row["uuid"]
        for row in rows:
            ok = True
            for k, v in value.items():
                if k == "uuid":
                    continue
                if v is None:
                    continue
                if str(row.get(k, "")) != str(v):
                    ok = False
                    break
            if ok and row.get("uuid"):
                return row["uuid"]
        return None
    if not isinstance(value, str):
        return None
    v = value.strip()
    if not v:
        return None
    if _is_uuid(v):
        return v
    for row in rows:
        if not isinstance(row, dict):
            continue
        uuid = row.get("uuid")
        if not uuid:
            continue
        for df in display_fields:
            if df in row and str(row.get(df, "")) == v:
                return uuid
        if target_array and target_array in row and str(row.get(target_array, "")) == v:
            return uuid
        combined = None
        if len(display_fields) > 1:
            parts = []
            for df in display_fields:
                if row.get(df):
                    parts.append(str(row.get(df)))
            if len(parts) == 2 and set(display_fields) >= {"hostname", "domain"}:
                combined = f"{parts[0]}.{parts[1]}" if len(parts) == 2 else ".".join(parts)
            elif parts:
                combined = ".".join(parts)
            if combined and combined == v:
                return uuid
        if row.get("domainname") == v:
            return uuid
        if row.get("name") == v:
            return uuid
        if row.get("description") == v:
            return uuid
        if row.get("subnet") == v:
            return uuid
        if row.get("hostname") == v and len(display_fields) == 1:
            return uuid
    if "." in v and any(df in ("hostname", "domain") for df in display_fields):
        parts = v.split(".", 1)
        if len(parts) == 2:
            hn, dom = parts[0], parts[1]
            for row in rows:
                if row.get("hostname") == hn and row.get("domain") == dom and row.get("uuid"):
                    return row["uuid"]
    for row in rows:
        if not isinstance(row, dict):
            continue
        uuid = row.get("uuid")
        if not uuid:
            continue
        for df in display_fields:
            rv = str(row.get(df, "")).lower()
            if rv and (v.lower() == rv or v.lower() in rv):
                if len(rows) == 1:
                    return uuid
        for key in ("name", "description", "domainname", "subnet", "hostname"):
            rv = str(row.get(key, "")).lower()
            if rv and v.lower() in rv and len(rows) == 1:
                return uuid
    return None


def _resolve_via_relation(value, relation_meta):
    mu = _load_models_utils()
    targets = []
    if mu and hasattr(mu, "get_relation_targets"):
        try:
            targets = mu.get_relation_targets(relation_meta)
        except Exception:
            targets = []
    if not targets:
        rel = relation_meta.get("relation")
        if isinstance(rel, dict):
            targets = [rel]
        elif isinstance(rel, list):
            targets = rel
        elif "relation_targets" in relation_meta:
            targets = relation_meta.get("relation_targets") or []
    if not targets:
        return None
    if isinstance(targets, dict):
        targets = [targets]
    for target in targets:
        if not isinstance(target, dict):
            continue
        source = target.get("source", "")
        items = target.get("items", "")
        display = target.get("display", "")
        tmod, _ = _parse_relation_source(source)
        if not tmod:
            continue
        _, tarray = _parse_relation_items(items)
        display_fields = (
            [d.strip() for d in (display or "").split(",") if d.strip()] if display else []
        )
        cand_locs = _get_candidate_locations(tmod, tarray or "")
        if not cand_locs:
            if tmod == "unbound" and (tarray == "host" or "host" in str(display).lower()):
                cand_locs = [("settings", "host_override")]
            elif tmod == "bind" and tarray == "domain":
                cand_locs = [("domain", "primary_domain"), ("domain", "domain")]
            elif tmod == "kea" and tarray in ("subnet", "subnet4", "subnet6"):
                cand_locs = [("dhcpv4", "subnet"), ("dhcpv6", "subnet")]
            else:
                cand_locs = [(None, tarray)] if tarray else []
        for ctrl, typ in cand_locs:
            if ctrl is None:
                continue
            phrases = []
            if isinstance(value, str):
                if value:
                    phrases.append(value)
                    if "." in value:
                        phrases.append(value.split(".", 1)[0])
                phrases.append("")
            else:
                phrases.append("")
            for phrase in phrases:
                rows = _do_search(tmod, ctrl, typ, search_phrase=phrase)
                if not rows and phrase != "":
                    continue
                if not rows:
                    continue
                matched = _match_rows_to_value(value, rows, display_fields, tarray)
                if matched:
                    return matched
                if isinstance(value, str) and len(rows) == 1 and rows[0].get("uuid"):
                    r = rows[0]
                    comb_fields = display_fields or [tarray]
                    for df in comb_fields:
                        if r.get(df) and value.lower() in str(r.get(df)).lower():
                            return r["uuid"]
                    if (
                        value.lower() in str(r.get("name", "")).lower()
                        or value.lower() in str(r.get("description", "")).lower()
                    ):
                        return r["uuid"]
    return None


def _get_relation_meta(parent_module: str, parent_type: str, field: str):
    rel_fields, _, _ = _get_relation_fields_for_parent(parent_module, parent_type)
    base = field[:-5] if field.endswith("_uuid") else field
    if field in rel_fields:
        return rel_fields[field]
    if base in rel_fields:
        return rel_fields[base]
    models = _load_models_data_dict()
    if parent_module in models:
        for model_name, arrays in models[parent_module].items():
            for arr_name, fields in arrays.items():
                if field in fields:
                    fm = fields[field]
                    if isinstance(fm, dict) and (
                        "Relation" in str(fm.get("type", "")) or "relation" in fm
                    ):
                        return fm
                if base in fields:
                    fm = fields[base]
                    if isinstance(fm, dict) and (
                        "Relation" in str(fm.get("type", "")) or "relation" in fm
                    ):
                        return fm
    return None


def _resolve_host_single(value):
    cfg = _RESOLVE_MAP["host"]
    if isinstance(value, dict):
        hostname = value.get("hostname")
        domain = value.get("domain")
        if not hostname or not domain:
            return value
        for phrase in (hostname, "", f"{hostname}.{domain}"):
            rows = _do_search(cfg["module"], cfg["controller"], cfg["type"], search_phrase=phrase)
            for row in rows:
                if row.get("hostname") == hostname and row.get("domain") == domain:
                    if row.get("uuid"):
                        return row["uuid"]
        return value
    if isinstance(value, str):
        if _is_uuid(value):
            return value
        if "." in value:
            parts = value.split(".", 1)
            hostname = parts[0]
            domain = parts[1]
            for phrase in (hostname, "", value):
                rows = _do_search(
                    cfg["module"], cfg["controller"], cfg["type"], search_phrase=phrase
                )
                for row in rows:
                    if row.get("hostname") == hostname and row.get("domain") == domain:
                        if row.get("uuid"):
                            return row["uuid"]
        return value
    return value


def _resolve_subnet_single(value):
    if not isinstance(value, str):
        return value
    if _is_uuid(value):
        return value
    if "/" not in value:
        return value
    cfg = _RESOLVE_MAP["subnet"]
    for phrase in (value, ""):
        rows = _do_search(cfg["module"], cfg["controller"], cfg["type"], search_phrase=phrase)
        for row in rows:
            if row.get("subnet") == value and row.get("uuid"):
                return row["uuid"]
        if rows and phrase == value:
            for row in rows:
                if row.get("uuid") and row.get("subnet") and value in str(row.get("subnet")):
                    return row["uuid"]
            if len(rows) == 1 and rows[0].get("uuid"):
                return rows[0]["uuid"]
    return value


def _resolve_generic_single(value, cfg):
    if not isinstance(value, str):
        return value
    if _is_uuid(value):
        return value
    if not value:
        return value
    search_field = cfg.get("search_field", "name")
    for phrase in (value, ""):
        rows = _do_search(cfg["module"], cfg["controller"], cfg["type"], search_phrase=phrase)
        for row in rows:
            if str(row.get(search_field, "")) == value or str(row.get("name", "")) == value:
                if row.get("uuid"):
                    return row["uuid"]
        if phrase == value and rows:
            if len(rows) == 1 and rows[0].get("uuid"):
                if (
                    value.lower() in str(rows[0].get(search_field, "")).lower()
                    or value.lower() in str(rows[0].get("name", "")).lower()
                ):
                    return rows[0]["uuid"]
    return value


def _should_resolve_field(
    field: str, parent_module: str, parent_controller: str, parent_type: str
) -> bool:
    if _get_relation_meta(parent_module, parent_type, field):
        return True
    if field == "domain":
        return parent_module == "bind"
    if field in (
        "account",
        "validationMethod",
        "validation",
        "restartActions",
        "action",
        "actions",
    ):
        return parent_module == "acmeclient"
    if field == "host":
        return parent_module == "unbound"
    if field == "subnet":
        return parent_module == "kea"
    base = field[:-5] if field.endswith("_uuid") else field
    if base in _RESOLVE_MAP:
        cfg = _RESOLVE_MAP.get(field) or _RESOLVE_MAP.get(base)
        if cfg:
            if base == "domain" and parent_module != "bind":
                return False
            return True
    return field in _RESOLVE_MAP or base in _RESOLVE_MAP


def _resolve_single_field(
    field: str, value, parent_module: str = "", parent_controller: str = "", parent_type: str = ""
):
    if value is None:
        return value
    if isinstance(value, str) and _is_uuid(value):
        return value
    rel_meta = _get_relation_meta(parent_module, parent_type, field)
    if rel_meta:
        resolved = _resolve_via_relation(value, rel_meta)
        if resolved and resolved != value:
            return resolved
    if not _should_resolve_field(field, parent_module, parent_controller, parent_type):
        return value
    base = field
    if field.endswith("_uuid"):
        base = field[: -len("_uuid")]
        if not base:
            base = field
    cfg = _RESOLVE_MAP.get(field) or _RESOLVE_MAP.get(base)
    if cfg is None:
        return value
    if cfg["type"] == "host_override":
        return _resolve_host_single(value)
    if cfg["type"] == "subnet":
        return _resolve_subnet_single(value)
    return _resolve_generic_single(value, cfg)


def _resolve_reference(
    field: str, value, parent_module: str = "", parent_controller: str = "", parent_type: str = ""
):
    if value is None:
        return value
    if isinstance(value, dict):
        rel_meta = _get_relation_meta(parent_module, parent_type, field)
        if rel_meta or field == "host" or field.endswith("host"):
            return _resolve_single_field(
                field, value, parent_module, parent_controller, parent_type
            )
        return value
    if isinstance(value, str):
        if _is_uuid(value):
            return value
        if "," in value and "/" not in value:
            parts = [p.strip() for p in value.split(",") if p.strip()]
            if len(parts) > 1:
                resolved = []
                changed = False
                for p in parts:
                    if _is_uuid(p):
                        resolved.append(p)
                    else:
                        r = _resolve_single_field(
                            field, p, parent_module, parent_controller, parent_type
                        )
                        resolved.append(r)
                        if r != p:
                            changed = True
                if changed:
                    return ",".join(resolved)
        return _resolve_single_field(field, value, parent_module, parent_controller, parent_type)
    return value


def _auto_resolve_dict(
    flat_data: dict, parent_module: str = "", parent_controller: str = "", parent_type: str = ""
):
    if not isinstance(flat_data, dict):
        return flat_data
    for k in list(flat_data.keys()):
        if k == "uuid":
            continue
        v = flat_data[k]
        if isinstance(v, list):
            new_list = []
            changed = False
            for item in v:
                if isinstance(item, (str, dict)):
                    rv = _resolve_reference(k, item, parent_module, parent_controller, parent_type)
                    if rv != item:
                        changed = True
                    new_list.append(rv)
                else:
                    new_list.append(item)
            if changed:
                flat_data[k] = new_list
        elif isinstance(v, (str, dict)):
            rv = _resolve_reference(k, v, parent_module, parent_controller, parent_type)
            if rv != v:
                log.debug(
                    "Auto-resolved field %s: %r -> %r in %s/%s/%s",
                    k,
                    v,
                    rv,
                    parent_module,
                    parent_controller,
                    parent_type,
                )
                flat_data[k] = rv
    return flat_data


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


def _parse_reconfigure(reconfigure):
    if not reconfigure:
        return None
    if isinstance(reconfigure, bool):
        return None
    if isinstance(reconfigure, str):
        parts = reconfigure.split("/")
        if len(parts) == 3:
            return {"module": parts[0], "controller": parts[1], "action": parts[2]}
        if len(parts) == 2:
            return {"module": parts[0], "controller": parts[1], "action": "reconfigure"}
    if isinstance(reconfigure, dict):
        return reconfigure
    return None


def _infer_reconfigure(module: str, controller: str, type_name: str | None = None):
    try:
        check_keys = [
            (module, controller, type_name),
            (module, controller, None),
            (module, controller),
            (module, None, None),
            (module, None, type_name),
        ]
        for key in check_keys:
            if key is None:
                continue
            if key in _RECONFIGURE_OVERRIDES:
                parsed = _parse_reconfigure(_RECONFIGURE_OVERRIDES[key])
                if parsed:
                    return parsed
            if isinstance(key, tuple) and len(key) == 3:
                two = (key[0], key[1])
                if two in _RECONFIGURE_OVERRIDES:
                    parsed = _parse_reconfigure(_RECONFIGURE_OVERRIDES[two])
                    if parsed:
                        return parsed

        if module in _RECONFIGURE_MODULE_DEFAULTS:
            if not (
                module == "firewall" and controller in ("alias", "filter", "filter_base", "group")
            ):
                parsed = _parse_reconfigure(_RECONFIGURE_MODULE_DEFAULTS[module])
                if parsed:
                    return parsed

        controllers = _safe_list_controllers(module)

        if module == "firewall":
            if controller == "alias":
                return _parse_reconfigure("firewall/alias/reconfigure")
            if controller in ("filter", "filter_base", "filterbase"):
                if controllers and ("filter_base" in controllers or "filterbase" in controllers):
                    return _parse_reconfigure("firewall/filter_base/apply")
                acts = _safe_list_actions(module, controller)
                if acts and "apply" in [a.lower() for a in acts]:
                    return _parse_reconfigure(f"{module}/{controller}/apply")
                return _parse_reconfigure("firewall/filter_base/apply")
            if controller == "group":
                return _parse_reconfigure("firewall/group/reconfigure")

        if controllers:
            if "service" in controllers:
                svc_actions = _safe_list_actions(module, "service")
                if not svc_actions:
                    return _parse_reconfigure(f"{module}/service/reconfigure")
                low = [a.lower() for a in svc_actions]
                if "reconfigure" in low:
                    idx = low.index("reconfigure")
                    return _parse_reconfigure(f"{module}/service/{svc_actions[idx]}")
                return _parse_reconfigure(f"{module}/service/reconfigure")

        if controller:
            acts = _safe_list_actions(module, controller)
            if acts:
                low = [a.lower() for a in acts]
                if "reconfigure" in low:
                    idx = low.index("reconfigure")
                    return _parse_reconfigure(f"{module}/{controller}/{acts[idx]}")
                if "apply" in low:
                    idx = low.index("apply")
                    return _parse_reconfigure(f"{module}/{controller}/{acts[idx]}")

        if controller:
            return _parse_reconfigure(f"{module}/{controller}/reconfigure")
        return _parse_reconfigure(f"{module}/service/reconfigure")
    except Exception as exc:
        log.debug("_infer_reconfigure %s/%s/%s failed: %s", module, controller, type_name, exc)
        if controller:
            return _parse_reconfigure(f"{module}/{controller}/reconfigure")
        return _parse_reconfigure(f"{module}/service/reconfigure")


def _get_reconfigure(module: str, controller: str, type_name: str | None, reconfigure_arg):
    if reconfigure_arg is False:
        return None
    if reconfigure_arg is None or reconfigure_arg is True:
        return _infer_reconfigure(module, controller, type_name)
    if isinstance(reconfigure_arg, str):
        stripped = reconfigure_arg.strip()
        low = stripped.lower()
        if low in ("auto", "infer", "true", "yes", ""):
            return _infer_reconfigure(module, controller, type_name)
        parsed = _parse_reconfigure(stripped)
        if parsed:
            return parsed
        return _infer_reconfigure(module, controller, type_name)
    if isinstance(reconfigure_arg, dict):
        if "module" in reconfigure_arg and "controller" in reconfigure_arg:
            return reconfigure_arg
        return _parse_reconfigure(reconfigure_arg) or _infer_reconfigure(
            module, controller, type_name
        )
    return _infer_reconfigure(module, controller, type_name)

def _verify_reconfigure_call(module: str, controller: str, action: str = "reconfigure"):
    try:
        res = __salt__["opnsense.reconfigure"](module, controller, action)
        if isinstance(res, dict):
            status = str(res.get("status", "")).lower()
            result = str(res.get("result", "")).lower()
            if status in ("failed", "error") or result in ("failed", "error"):
                msg = res.get("message") or res.get("error") or res.get("validations") or res
                return False, str(msg)
        elif isinstance(res, str):
            if res.lower() in ("failed", "error"):
                return False, res
        return True, ""
    except Exception as exc:
        return False, str(exc)


def _human_diff(type_name, match, diff, data, found=None, module=None, controller=None, name=None):
    try:

        def _fqdn_from_dict(d, fallback):
            if not isinstance(d, dict):
                d = {}
            h = d.get("hostname") or (match.get("hostname") if isinstance(match, dict) else None)
            dom = d.get("domain") or (match.get("domain") if isinstance(match, dict) else None)
            if h and dom:
                return f"{h}.{dom}"
            if isinstance(fallback, str) and "." in fallback:
                return fallback
            return h or dom or fallback or ""

        alias_fqdn = _fqdn_from_dict(data if isinstance(data, dict) else {}, name) or (
            f"{match.get('hostname')}.{match.get('domain')}"
            if isinstance(match, dict) and match.get("hostname") and match.get("domain")
            else name or ""
        )

        if found is None:
            if type_name in ("host_alias", "alias") or (
                module == "unbound" and controller == "settings"
            ):
                if isinstance(data, dict):
                    inner = data
                    if len(data) == 1 and isinstance(list(data.values())[0], dict):
                        inner = list(data.values())[0]
                    host = inner.get("host")
                    if host:
                        return f"{alias_fqdn} -> {host}"
                    return f"create {type_name} {alias_fqdn}"
            if type_name == "record" or (module == "bind" and controller == "record"):
                d = data if isinstance(data, dict) else {}
                if isinstance(d, dict) and len(d) == 1 and isinstance(list(d.values())[0], dict):
                    d = list(d.values())[0]
                rn = d.get("name") or alias_fqdn or name or ""
                rt = d.get("type") or ""
                rv = d.get("value") or ""
                if rn or rt or rv:
                    return f"{rn} {rt} {rv}".strip()
            if module == "firewall" and controller == "alias":
                d = data if isinstance(data, dict) else {}
                if isinstance(d, dict) and len(d) == 1 and isinstance(list(d.values())[0], dict):
                    d = list(d.values())[0]
                an = d.get("name") or name or "alias"
                content = d.get("content") or d.get("address") or ""
                if content:
                    return f"alias {an} -> {content}"
                return f"create firewall alias {an}"

        if type_name in ("host_alias", "alias") and (
            module == "unbound" or type_name == "host_alias"
        ):
            if "host" in diff:
                old = diff["host"]["old"]
                new = diff["host"]["new"]
                return f"{alias_fqdn} -> {new} (was {old})"
            if "hostname" in diff or "domain" in diff:
                old_h = (
                    found.get("hostname")
                    if found
                    else (match.get("hostname") if isinstance(match, dict) else "")
                )
                old_d = (
                    found.get("domain")
                    if found
                    else (match.get("domain") if isinstance(match, dict) else "")
                )
                old_fqdn = f"{old_h}.{old_d}" if old_h and old_d else alias_fqdn
                new_h = (
                    diff.get("hostname", {}).get("new")
                    if "hostname" in diff
                    else (data.get("hostname") if isinstance(data, dict) else old_h)
                )
                new_d = (
                    diff.get("domain", {}).get("new")
                    if "domain" in diff
                    else (data.get("domain") if isinstance(data, dict) else old_d)
                )
                new_fqdn = f"{new_h}.{new_d}" if new_h and new_d else alias_fqdn
                return f"{old_fqdn} -> {new_fqdn}"
            if "enabled" in diff and len(diff) == 1:
                old = diff["enabled"]["old"]
                new = diff["enabled"]["new"]
                s_old = "enabled" if str(old) in ("1", "true", "True") else "disabled"
                s_new = "enabled" if str(new) in ("1", "true", "True") else "disabled"
                return f"{alias_fqdn} {s_old} -> {s_new}"

        if type_name == "host_override":
            fqdn = _fqdn_from_dict(data if isinstance(data, dict) else {}, name)
            for k in ("server", "ip", "address"):
                if k in diff:
                    old = diff[k]["old"]
                    new = diff[k]["new"]
                    return f"{fqdn} {old} -> {new}"

        if type_name == "record" or (module == "bind" and controller == "record"):
            rec_name = (
                (match.get("name") if isinstance(match, dict) else None)
                or (data.get("name") if isinstance(data, dict) else None)
                or name
                or ""
            )
            rec_type = (
                (match.get("type") if isinstance(match, dict) else None)
                or (data.get("type") if isinstance(data, dict) else None)
                or ""
            )
            if "value" in diff:
                old = diff["value"]["old"]
                new = diff["value"]["new"]
                return f"{rec_name} {rec_type} {old} -> {new}".strip()
            if diff:
                parts = []
                for kk in ("name", "type", "value"):
                    if kk in diff:
                        parts.append(f"{kk} {diff[kk]['old']} -> {diff[kk]['new']}")
                if parts:
                    return f"record {rec_name}: " + ", ".join(parts)

        if module == "firewall" and controller == "alias":
            alias_name = (
                (match.get("name") if isinstance(match, dict) else None)
                or (data.get("name") if isinstance(data, dict) else None)
                or name
                or "alias"
            )
            if "content" in diff:
                old = diff["content"]["old"]
                new = diff["content"]["new"]
                old_s = (str(old)[:60] + "...") if len(str(old)) > 60 else str(old)
                new_s = (str(new)[:60] + "...") if len(str(new)) > 60 else str(new)
                return f"alias {alias_name}: {old_s} -> {new_s}"
            if "address" in diff or "network" in diff:
                k = (
                    "address"
                    if "address" in diff
                    else "network"
                    if "network" in diff
                    else list(diff.keys())[0]
                )
                old = diff[k]["old"]
                new = diff[k]["new"]
                return f"alias {alias_name} {k}: {old} -> {new}"

        if diff:
            bits = []
            for k, v in list(diff.items())[:3]:
                bits.append(f"{k}: {v.get('old')} -> {v.get('new')}")
            if len(diff) > 3:
                bits.append(f"... +{len(diff) - 3} more")
            return "; ".join(bits)
    except Exception as exc:
        log.debug("human_diff failed: %s", exc)
    return None


def _check_host_override_exists(host_val):
    if not host_val:
        return False
    try:
        if isinstance(host_val, dict):
            hostname = host_val.get("hostname")
            domain = host_val.get("domain")
            if hostname and domain:
                rows = _do_search("unbound", "settings", "host_override", search_phrase=hostname)
                for r in rows:
                    if r.get("hostname") == hostname and r.get("domain") == domain:
                        return True
            return False
        if isinstance(host_val, str):
            if _is_uuid(host_val):
                rows = _do_search("unbound", "settings", "host_override", search_phrase="")
                for r in rows:
                    if r.get("uuid") == host_val:
                        return True
                return False
            if "." in host_val:
                parts = host_val.split(".", 1)
                hostname, domain = parts[0], parts[1]
                rows = _do_search("unbound", "settings", "host_override", search_phrase=hostname)
                for r in rows:
                    if r.get("hostname") == hostname and r.get("domain") == domain:
                        return True
                return False
    except Exception:
        return False
    return False


def _check_bind_domain_exists(domain_val):
    if not domain_val:
        return False
    try:
        if isinstance(domain_val, str):
            if _is_uuid(domain_val):
                rows = _do_search("bind", "domain", "primary_domain", search_phrase="")
                for r in rows:
                    if r.get("uuid") == domain_val:
                        return True
                return False
            else:
                rows = _do_search("bind", "domain", "primary_domain", search_phrase=domain_val)
                for r in rows:
                    if r.get("domainname") == domain_val:
                        return True
                return False
        if isinstance(domain_val, dict):
            dn = domain_val.get("domainname") or domain_val.get("name")
            if dn:
                return _check_bind_domain_exists(dn)
    except Exception:
        return False
    return False


def _run_zonetest():
    fn = _safe_call_fn()
    if not fn:
        return True, ""
    try:
        for action in ("zonetest", "zoneTest", "zone_test"):
            try:
                res = fn("bind", "general", action)
                if isinstance(res, dict):
                    if res.get("result") == "failed" or res.get("status") == "failed":
                        return False, f"bind {action} failed: {res}"
                    if "validations" in res and res["validations"]:
                        return False, f"bind {action} validations: {res['validations']}"
                return True, ""
            except Exception as e:
                msg = str(e).lower()
                if "404" in msg or "not found" in msg or "endpoint" in msg:
                    continue
                log.debug("zonetest %s error: %s", action, e)
                continue
        return True, ""
    except Exception as exc:
        log.debug("zonetest overall error: %s", exc)
        return True, ""


def _preflight_check(module, controller, type_name, flat_data, match, found, is_create):
    if not isinstance(flat_data, dict):
        return True, ""
    if module == "unbound" and type_name in ("host_alias", "alias"):
        host_val = flat_data.get("host")
        if host_val:
            if isinstance(host_val, str) and _is_uuid(host_val):
                if not _check_host_override_exists(host_val):
                    return (
                        False,
                        f"pre-flight: parent host_override {host_val} not found – create parent first",
                    )
            elif isinstance(host_val, dict):
                if not _check_host_override_exists(host_val):
                    return False, f"pre-flight: parent host {host_val} not found"
    if module == "bind" and controller == "record" and type_name == "record":
        domain_val = flat_data.get("domain")
        if domain_val:
            if not _check_bind_domain_exists(domain_val):
                return (
                    False,
                    f"pre-flight: parent bind domain {domain_val} not found – create zone first",
                )
        ok, msg = _run_zonetest()
        if not ok:
            return False, f"pre-flight: {msg}"
    return True, ""


def _extract_data_payload(type_name, data):
    if not data:
        return {}
    if len(data) == 1 and list(data.keys())[0] == type_name:
        return data
    singular = type_name
    for suffix in ["s"]:
        if singular.endswith(suffix):
            singular = singular[:-1]
    wrapped_keys = [type_name, singular, "alias", "host", "record", "domain", "item", "rule"]
    for wk in wrapped_keys:
        if wk in data and isinstance(data[wk], dict):
            return data
    return {type_name: data} if type_name not in data else data


def item_present(
    name, module, controller, type, data, match=None, reconfigure=None, search_field=None
):
    """
    Ensure a single item exists in the OPNsense API.

    Foreign key relations (like assigning a host to a subnet) are automatically
    resolved by name if defined in the upstream models. For complex examples,
    see the tutorials in the extension documentation.

    State Example (Raw Syntax):
        create_alias:
          opnsense.item_present:
            - module: unbound
            - controller: settings
            - type: host_alias
            - search_field: hostname
            - data:
                hostname: www
                server: 10.0.0.1
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    if match is None and search_field is not None:
        match = {search_field: name}
    if match is None:
        match = {"description": name}

    try:
        existing_res = __salt__["opnsense.search"](module, controller, type, row_count=-1)
        rows = existing_res.get("rows", [])
    except Exception as exc:
        ret["comment"] = f"search failed: {exc}"
        return ret

    found = None
    for row in rows:
        ok = True
        for k, v in match.items():
            if str(row.get(k, "")) != str(v):
                ok = False
                break
        if ok:
            found = row
            break

    if found and found.get("uuid"):
        try:
            full_item = __salt__["opnsense.get"](module, controller, type, uuid=found.get("uuid"))
            if isinstance(full_item, dict):
                if type in full_item and isinstance(full_item[type], dict):
                    found = full_item[type]
                elif len(full_item) == 1 and isinstance(list(full_item.values())[0], dict):
                    found = list(full_item.values())[0]
                else:
                    found = full_item
        except Exception as exc:
            log.debug("get full item failed: %s", exc)

    payload = data
    if (
        isinstance(data, dict)
        and type not in data
        and not any(
            k in data
            for k in [
                "alias",
                "host",
                "record",
                "domain",
                "item",
                "rule",
                "network",
                "client",
                "server",
            ]
        )
    ):
        if isinstance(data, dict) and len(data) > 0:
            if type not in ["host_override", "host_alias", "record", "domain", "item", "rule"]:
                payload = {type: data}
            else:
                inner_key = {
                    "host_override": "host",
                    "host_alias": "alias",
                    "record": "record",
                    "domain": "domain",
                    "item": "alias",
                    "rule": "rule",
                    "alias": "alias",
                }.get(type, type)
                if inner_key not in data:
                    payload = {inner_key: data}
                else:
                    payload = data
    else:
        payload = data

    try:
        flat_tmp = payload
        if isinstance(payload, dict) and len(payload) == 1:
            inner_tmp = list(payload.values())[0]
            if isinstance(inner_tmp, dict):
                flat_tmp = inner_tmp
        if isinstance(flat_tmp, dict):
            _auto_resolve_dict(
                flat_tmp, parent_module=module, parent_controller=controller, parent_type=type
            )
    except Exception as exc:
        log.debug("auto-resolve failed: %s", exc)

    flat_data = payload
    if isinstance(payload, dict) and len(payload) == 1:
        inner = list(payload.values())[0]
        if isinstance(inner, dict):
            flat_data = inner

    if found is None:
        ok, msg = _preflight_check(
            module,
            controller,
            type,
            flat_data if isinstance(flat_data, dict) else {},
            match,
            found,
            is_create=True,
        )
        if not ok:
            ret["result"] = False
            ret["comment"] = msg
            return ret

        human = _human_diff(
            type,
            match,
            {},
            flat_data if isinstance(flat_data, dict) else data,
            found=None,
            module=module,
            controller=controller,
            name=name,
        )

        if __opts__.get("test"):
            ret["result"] = None
            ret["comment"] = f"{type} {name} would be created"
            if human:
                ret["comment"] += f" – {human}"
            ret["changes"] = {"added": match}
            if human:
                ret["changes"]["human"] = human
            rcfg = _get_reconfigure(module, controller, type, reconfigure)
            if rcfg:
                ret["comment"] += (
                    f" (would reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']})"
                )
            return ret
        try:
            res = __salt__["opnsense.add"](module, controller, type, payload)
            ret["changes"] = {"added": res}
            if human:
                ret["changes"]["human"] = human
            ret["result"] = True
            ret["comment"] = f"{type} {name} created"
            if human:
                ret["comment"] += f" – {human}"
            rcfg = _get_reconfigure(module, controller, type, reconfigure)
            if rcfg:
                ok, err = _verify_reconfigure_call(rcfg["module"], rcfg["controller"], rcfg["action"])
                if not ok:
                    ret["result"] = False
                    ret["comment"] += (
                        f" but reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']} failed: {err}"
                    )
                    return ret
                ret["comment"] += (
                    f" and reconfigured {rcfg['module']}/{rcfg['controller']}/{rcfg['action']}"
                )
            return ret
        except Exception as exc:
            ret["comment"] = f"add failed: {exc}"
            return ret

    diff = diff_models(found, flat_data if isinstance(flat_data, dict) else {})

    if not diff:
        ret["result"] = True
        ret["comment"] = f"{type} {name} already present"
        return ret

    ok, msg = _preflight_check(
        module,
        controller,
        type,
        flat_data if isinstance(flat_data, dict) else {},
        match,
        found,
        is_create=False,
    )
    if not ok:
        ret["result"] = False
        ret["comment"] = msg
        return ret

    human = _human_diff(
        type,
        match,
        diff,
        flat_data if isinstance(flat_data, dict) else data,
        found=found,
        module=module,
        controller=controller,
        name=name,
    )

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"{type} {name} would be updated"
        if human:
            ret["comment"] += f" – {human}"
        ret["changes"] = diff
        if human:
            ret["changes"]["human"] = human
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ret["comment"] += (
                f" (would reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']})"
            )
        return ret

    try:
        uuid = found.get("uuid")
        res = __salt__["opnsense.set_item"](module, controller, type, uuid, payload)
        ret["changes"] = diff
        if human:
            ret["changes"]["human"] = human
        ret["result"] = True
        ret["comment"] = f"{type} {name} updated"
        if human:
            ret["comment"] += f" – {human}"
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ok, err = _verify_reconfigure_call(rcfg["module"], rcfg["controller"], rcfg["action"])
            if not ok:
                ret["result"] = False
                ret["comment"] += (
                    f" but reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']} failed: {err}"
                )
                return ret
            ret["comment"] += (
                f" and reconfigured {rcfg['module']}/{rcfg['controller']}/{rcfg['action']}"
            )
        return ret
    except Exception as exc:
        ret["comment"] = f"set failed: {exc}"
        return ret


def item_absent(name, module, controller, type, match=None, reconfigure=None, search_field=None):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    if match is None and search_field is not None:
        match = {search_field: name}
    if match is None:
        match = {"description": name}

    try:
        existing_res = __salt__["opnsense.search"](module, controller, type, row_count=-1)
        rows = existing_res.get("rows", [])
    except Exception as exc:
        ret["comment"] = f"search failed: {exc}"
        return ret

    found = None
    for row in rows:
        ok = True
        for k, v in match.items():
            if str(row.get(k, "")) != str(v):
                ok = False
                break
        if ok:
            found = row
            break

    if found is None:
        ret["result"] = True
        ret["comment"] = f"{type} {name} already absent"
        return ret

    human = None
    try:
        human = _human_diff(
            type, match, {}, found, found=found, module=module, controller=controller, name=name
        )
    except Exception:
        pass

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"{type} {name} would be deleted"
        if human:
            ret["comment"] += f" – {human}"
        ret["changes"] = {"deleted": found.get("uuid")}
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ret["comment"] += (
                f" (would reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']})"
            )
        return ret

    try:
        uuid = found.get("uuid")
        __salt__["opnsense.delete"](module, controller, type, uuid)
        ret["changes"] = {"deleted": uuid}
        if human:
            ret["changes"]["human"] = human
        ret["result"] = True
        ret["comment"] = f"{type} {name} deleted"
        if human:
            ret["comment"] += f" – {human}"
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ok, err = _verify_reconfigure_call(rcfg["module"], rcfg["controller"], rcfg["action"])
            if not ok:
                ret["result"] = False
                ret["comment"] += (
                    f" but reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']} failed: {err}"
                )
                return ret
            ret["comment"] += (
                f" and reconfigured {rcfg['module']}/{rcfg['controller']}/{rcfg['action']}"
            )
        return ret
    except Exception as exc:
        ret["comment"] = f"delete failed: {exc}"
        return ret


def reconfigured(name, module, controller, action="reconfigure"):
    """
    Trigger a service reconfiguration (apply) in OPNsense.

    State Example:
        apply_unbound:
          opnsense.reconfigured:
            - module: unbound
            - controller: service
            - onchanges:
              - opnsense: create_aliases
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"would reconfigure {module}/{controller}/{action}"
        ret["changes"] = {"reconfigure": f"{module}/{controller}/{action}"}
        return ret

    ok, err = _verify_reconfigure_call(module, controller, action)
    if ok:
        ret["result"] = True
        ret["comment"] = f"reconfigured {module}/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"{module}/{controller}/{action}"}
    else:
        ret["result"] = False
        ret["comment"] = f"reconfigure failed: {err}"
    return ret


def items_present(name, module, controller, type, items, reconfigure=None, search_field=None):
    """
    Ensure multiple items exist in the OPNsense API, processed as a batch.

    This defers the `reconfigure` command until all items are evaluated, making it
    significantly faster than `item_present` for bulk records. This is best paired
    with Pillar data.

    State Example (Pillar-Driven):
        # Pillar:
        # opnsense:
        #   aliases:
        #     - hostname: www
        #       server: 10.0.0.1

        create_aliases:
          opnsense.items_present:
            - module: unbound
            - controller: settings
            - type: host_alias
            - search_field: hostname
            - items: {{ salt['pillar.get']('opnsense:aliases', []) | tojson }}
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    if not isinstance(items, list):
        ret["comment"] = "items must be a list of dicts with name/data/match"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"would ensure {len(items)} {type} items present"
        ret["changes"] = {
            f"would_present_{i}": it.get("name", str(i)) for i, it in enumerate(items)
        }
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ret["comment"] += (
                f" (would reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']})"
            )
        return ret

    total_changes = {}
    errors = []
    for item in items:
        item_name = item.get("name", "unnamed")
        data = item.get("data", {})
        match = item.get("match")
        sf = item.get("search_field", search_field)
        try:
            single_ret = item_present(
                item_name,
                module,
                controller,
                type,
                data,
                match=match,
                reconfigure=False,
                search_field=sf,
            )
            if single_ret.get("changes"):
                total_changes[item_name] = single_ret["changes"]
            if (
                single_ret.get("result") is False
                and "failed" in single_ret.get("comment", "").lower()
            ):
                errors.append(f"{item_name}: {single_ret['comment']}")
        except Exception as exc:
            errors.append(f"{item_name}: {exc}")

    if errors:
        ret["comment"] = "; ".join(errors)
        ret["result"] = False
        ret["changes"] = total_changes
        return ret

    if total_changes:
        ret["changes"] = total_changes
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ok, err = _verify_reconfigure_call(rcfg["module"], rcfg["controller"], rcfg["action"])
            if not ok:
                ret["comment"] = f"items present but reconfigure failed: {err}"
                ret["result"] = False
                return ret
            ret["comment"] = (
                f"ensured {len(items)} {type} items ({len(total_changes)} changed) and reconfigured {rcfg['module']}/{rcfg['controller']}/{rcfg['action']}"
            )
        else:
            ret["comment"] = f"ensured {len(items)} {type} items ({len(total_changes)} changed)"
        ret["result"] = True
    else:
        ret["comment"] = f"{len(items)} {type} items already present"
        ret["result"] = True

    return ret


def items_absent(name, module, controller, type, items, reconfigure=None, search_field=None):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    if not isinstance(items, list):
        ret["comment"] = "items must be a list"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"would ensure {len(items)} {type} items absent"
        ret["changes"] = {f"would_absent_{i}": it.get("name", str(i)) for i, it in enumerate(items)}
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ret["comment"] += (
                f" (would reconfigure {rcfg['module']}/{rcfg['controller']}/{rcfg['action']})"
            )
        return ret

    total_changes = {}
    errors = []
    for item in items:
        item_name = item.get("name", "unnamed")
        match = item.get("match")
        if match is None and item.get("search_field"):
            match = {item["search_field"]: item_name}
        if match is None and search_field:
            match = {search_field: item_name}
        sf = item.get("search_field", search_field)
        try:
            single_ret = item_absent(
                item_name, module, controller, type, match=match, reconfigure=False, search_field=sf
            )
            if single_ret.get("changes"):
                total_changes[item_name] = single_ret["changes"]
        except Exception as exc:
            errors.append(f"{item_name}: {exc}")

    if errors:
        ret["comment"] = "; ".join(errors)
        ret["result"] = False
        ret["changes"] = total_changes
        return ret

    if total_changes:
        ret["changes"] = total_changes
        rcfg = _get_reconfigure(module, controller, type, reconfigure)
        if rcfg:
            ok, err = _verify_reconfigure_call(rcfg["module"], rcfg["controller"], rcfg["action"])
            if not ok:
                ret["comment"] = f"items absent but reconfigure failed: {err}"
                ret["result"] = False
                return ret
            ret["comment"] = (
                f"removed {len(total_changes)} {type} items and reconfigured {rcfg['module']}/{rcfg['controller']}/{rcfg['action']}"
            )
        else:
            ret["comment"] = f"removed {len(total_changes)} {type} items"
        ret["result"] = True
    else:
        ret["comment"] = f"{len(items)} {type} items already absent"
        ret["result"] = True

    return ret


def assert_resolves(name, hostname, expected_ip, server=None, timeout=10, ttl=60):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"would verify {hostname} resolves to {expected_ip}"
        ret["changes"] = {"would_check": f"{hostname} -> {expected_ip}"}
        return ret

    try:
        fn_call = _safe_call_fn()
        if fn_call:
            try:
                ld = fn_call("unbound", "diagnostics", "listLocalData")
                txt = str(ld)
                if hostname in txt and expected_ip in txt:
                    ret["result"] = True
                    ret["comment"] = f"{hostname} found in unbound localData with {expected_ip}"
                    ret["changes"] = {
                        "verified": f"{hostname} -> {expected_ip} via unbound localData"
                    }
                    return ret
            except Exception as exc:
                log.debug("assert_resolves listLocalData failed: %s", exc)
            try:
                if expected_ip and "." in expected_ip:
                    rev = fn_call(
                        "diagnostics", "dns", "reverseLookup", data={"hostname": expected_ip}
                    )
                    if hostname in str(rev):
                        ret["result"] = True
                        ret["comment"] = (
                            f"{expected_ip} reverse resolves to {hostname} via diagnostics/dns"
                        )
                        ret["changes"] = {
                            "verified": f"{hostname} -> {expected_ip} via reverseLookup"
                        }
                        return ret
            except Exception as exc:
                log.debug("assert_resolves reverseLookup failed: %s", exc)
    except Exception as exc:
        log.debug("assert_resolves api path failed: %s", exc)

    try:
        if "network.dig" in __salt__:
            dig_res = __salt__["network.dig"](hostname)
            if expected_ip in str(dig_res):
                ret["result"] = True
                ret["comment"] = f"{hostname} resolves to {expected_ip} via dig"
                ret["changes"] = {"verified": f"{hostname} -> {expected_ip} via dig"}
                return ret
            else:
                if dig_res:
                    ret["comment"] = (
                        f"{hostname} dig result {dig_res} does not contain {expected_ip}"
                    )
                else:
                    ret["comment"] = f"{hostname} dig returned empty, expected {expected_ip}"
                ret["result"] = False
                return ret
    except Exception as exc:
        log.debug("assert_resolves dig failed: %s", exc)

    try:
        resolved = socket.gethostbyname(hostname)
        if resolved == expected_ip:
            ret["result"] = True
            ret["comment"] = f"{hostname} resolves to {expected_ip} (socket)"
            ret["changes"] = {"verified": f"{hostname} -> {expected_ip}"}
            return ret
        else:
            ret["result"] = False
            ret["comment"] = f"{hostname} resolves to {resolved}, expected {expected_ip}"
            return ret
    except Exception as exc:
        ret["result"] = False
        ret["comment"] = f"failed to resolve {hostname}: {exc}"
        return ret


def _inject_dynamic_state_wrappers():
    try:
        import importlib

        try:
            from saltext.opnsense.utils.api_spec import load_spec
        except Exception:
            try:
                mod = importlib.import_module("saltext.opnsense.utils.api_spec")
                load_spec = getattr(mod, "load_spec")
            except Exception:
                return

        spec_data = load_spec() or {}
        modules_dict = spec_data.get("modules") or {}
        if not modules_dict:
            return

        existing = set(globals().keys())

        for mod_name, controllers in modules_dict.items():
            if not isinstance(controllers, dict):
                continue
            mod_snake = _camel_to_snake_generic(mod_name)
            for ctrl_name, actions in controllers.items():
                if not isinstance(actions, list):
                    if isinstance(actions, dict):
                        actions = list(actions.keys())
                    else:
                        continue
                ctrl_snake = _camel_to_snake_generic(ctrl_name)

                crud_types = {}
                for action in actions:
                    low = action.lower()
                    for v in ["search", "get", "add", "set", "del", "toggle"]:
                        if low.startswith(v):
                            rest = action[len(v) :]
                            if rest.startswith("_"):
                                rest = rest[1:]
                            suffix = rest
                            if not suffix:
                                continue
                            suffix_snake = _camel_to_snake_generic(suffix)
                            if not suffix_snake:
                                continue
                            crud_types.setdefault(suffix_snake, {})
                            crud_types[suffix_snake][v] = action
                            break

                for type_snake in crud_types.keys():
                    present_name = f"{mod_snake}_{ctrl_snake}_{type_snake}_present"
                    absent_name = f"{mod_snake}_{ctrl_snake}_{type_snake}_absent"
                    if present_name in existing or absent_name in existing:
                        continue

                    def _make_present(m=mod_name, c=ctrl_name, t=type_snake):
                        def _present(
                            name, data=None, match=None, reconfigure=True, search_field=None
                        ):
                            return item_present(
                                name,
                                m,
                                c,
                                t,
                                data,
                                match=match,
                                reconfigure=reconfigure,
                                search_field=search_field,
                            )

                        _present.__name__ = present_name
                        type_human = t.replace("_", " ")
                        _present.__doc__ = f"""Ensure {type_human} present in {m} {c} .

Uses generic item_present with auto-inferred reconfigure ({m}/service/reconfigure if service exists else {m}/{c}/reconfigure).
Match dict finds UUID without knowing it. Supports test=True dry-run with human diff.

Example (human parent, no UUID):
    {type_human.replace(" ", "_")}_example:
      opnsense.{present_name}:
        - name: my{t.replace("_", "")}
        - data:
            enabled: '1'
            description: salt managed
        - match: {{'name': 'my{t.replace("_", "")}'}}
        - reconfigure: auto   # auto-inferred, single reload

Batch better:
    dns_batch:
      opnsense.items_present:
        - module: {m}
        - controller: {c}
        - type: {t}
        - items: [{{'name': 'www', 'data': {{'enabled':'1'}}}}]
        - reconfigure: {m}/service/reconfigure

Docs: https://docs.opnsense.org/development/api/core/{m}.html
"""
                        return _present

                    def _make_absent(m=mod_name, c=ctrl_name, t=type_snake):
                        def _absent(name, match=None, reconfigure=True, search_field=None):
                            return item_absent(
                                name,
                                m,
                                c,
                                t,
                                match=match,
                                reconfigure=reconfigure,
                                search_field=search_field,
                            )

                        _absent.__name__ = absent_name
                        type_human = t.replace("_", " ")
                        _absent.__doc__ = f"""Ensure {type_human} absent in {m} {c}.

Auto-removes via del_{t}/{{uuid}} after search match. Auto reconfigure.

Example:
    purge_{t}:
      opnsense.{absent_name}:
        - name: old{t}
        - match: {{'description': 'old'}}
        - reconfigure: auto
"""
                        return _absent

                    globals()[present_name] = _make_present()
                    globals()[absent_name] = _make_absent()
                    existing.add(present_name)
                    existing.add(absent_name)

    except Exception as exc:
        log.debug("Dynamic state wrapper injection failed: %s", exc)


_inject_dynamic_state_wrappers()
