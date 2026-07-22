import logging
from typing import Any

log = logging.getLogger(__name__)

__virtualname__ = "opnsense"


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


def item_present(name, module, controller, type, data, match=None, reconfigure=None, search_field=None):
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

    payload = data
    if isinstance(data, dict) and type not in data and not any(
        k in data for k in ["alias", "host", "record", "domain", "item", "rule", "network", "client", "server"]
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

    if found is None:
        if __opts__.get("test"):
            ret["result"] = None
            ret["comment"] = f"{type} {name} would be created"
            ret["changes"] = {"added": match}
            return ret
        try:
            res = __salt__["opnsense.add"](module, controller, type, payload)
            ret["changes"] = {"added": res}
            ret["result"] = True
            ret["comment"] = f"{type} {name} created"
            rcfg = _parse_reconfigure(reconfigure)
            if rcfg:
                if __opts__.get("test"):
                    ret["comment"] += f" (would reconfigure {reconfigure})"
                else:
                    __salt__["opnsense.reconfigure"](rcfg["module"], rcfg["controller"], rcfg["action"])
                    ret["comment"] += f" and reconfigured {reconfigure}"
            return ret
        except Exception as exc:
            ret["comment"] = f"add failed: {exc}"
            return ret

    diff = {}
    flat_data = payload
    if isinstance(payload, dict) and len(payload) == 1:
        inner = list(payload.values())[0]
        if isinstance(inner, dict):
            flat_data = inner

    for k, v in flat_data.items():
        if k == "uuid":
            continue
        existing_val = found.get(k)
        if str(existing_val or "") != str(v or ""):
            diff[k] = {"old": existing_val, "new": v}

    if not diff:
        ret["result"] = True
        ret["comment"] = f"{type} {name} already present"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"{type} {name} would be updated"
        ret["changes"] = diff
        return ret

    try:
        uuid = found.get("uuid")
        res = __salt__["opnsense.set_item"](module, controller, type, uuid, payload)
        ret["changes"] = diff
        ret["result"] = True
        ret["comment"] = f"{type} {name} updated"
        rcfg = _parse_reconfigure(reconfigure)
        if rcfg:
            __salt__["opnsense.reconfigure"](rcfg["module"], rcfg["controller"], rcfg["action"])
            ret["comment"] += f" and reconfigured {reconfigure}"
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

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"{type} {name} would be deleted"
        ret["changes"] = {"deleted": found.get("uuid")}
        return ret

    try:
        uuid = found.get("uuid")
        __salt__["opnsense.delete"](module, controller, type, uuid)
        ret["changes"] = {"deleted": uuid}
        ret["result"] = True
        ret["comment"] = f"{type} {name} deleted"
        rcfg = _parse_reconfigure(reconfigure)
        if rcfg:
            __salt__["opnsense.reconfigure"](rcfg["module"], rcfg["controller"], rcfg["action"])
            ret["comment"] += f" and reconfigured {reconfigure}"
        return ret
    except Exception as exc:
        ret["comment"] = f"delete failed: {exc}"
        return ret


def reconfigured(name, module, controller, action="reconfigure"):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"would reconfigure {module}/{controller}/{action}"
        ret["changes"] = {"reconfigure": f"{module}/{controller}/{action}"}
        return ret

    try:
        __salt__["opnsense.reconfigure"](module, controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured {module}/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"{module}/{controller}/{action}"}
        return ret
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
        return ret


def items_present(name, module, controller, type, items, reconfigure=None, search_field=None):
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    if not isinstance(items, list):
        ret["comment"] = "items must be a list of dicts with name/data/match"
        return ret

    if __opts__.get("test"):
        ret["result"] = None
        ret["comment"] = f"would ensure {len(items)} {type} items present"
        ret["changes"] = {f"would_present_{i}": it.get("name", str(i)) for i, it in enumerate(items)}
        return ret

    total_changes = {}
    errors = []
    for item in items:
        item_name = item.get("name", "unnamed")
        data = item.get("data", {})
        match = item.get("match")
        sf = item.get("search_field", search_field)
        try:
            single_ret = item_present(item_name, module, controller, type, data, match=match, reconfigure=False, search_field=sf)
            if single_ret.get("changes"):
                total_changes[item_name] = single_ret["changes"]
            if not single_ret.get("result") and single_ret.get("result") is not False:
                pass
            if single_ret.get("result") is False and "failed" in single_ret.get("comment", "").lower():
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
        rcfg = _parse_reconfigure(reconfigure)
        if rcfg:
            try:
                __salt__["opnsense.reconfigure"](rcfg["module"], rcfg["controller"], rcfg["action"])
                ret["comment"] = f"ensured {len(items)} {type} items ({len(total_changes)} changed) and reconfigured {reconfigure}"
            except Exception as exc:
                ret["comment"] = f"items present but reconfigure failed: {exc}"
                ret["result"] = False
                return ret
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
            single_ret = item_absent(item_name, module, controller, type, match=match, reconfigure=False, search_field=sf)
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
        rcfg = _parse_reconfigure(reconfigure)
        if rcfg:
            try:
                __salt__["opnsense.reconfigure"](rcfg["module"], rcfg["controller"], rcfg["action"])
                ret["comment"] = f"removed {len(total_changes)} {type} items and reconfigured {reconfigure}"
            except Exception as exc:
                ret["comment"] = f"items absent but reconfigure failed: {exc}"
                ret["result"] = False
                return ret
        else:
            ret["comment"] = f"removed {len(total_changes)} {type} items"
        ret["result"] = True
    else:
        ret["comment"] = f"{len(items)} {type} items already absent"
        ret["result"] = True

    return ret


def _camel_to_snake(name: str):
    import re

    name = name.replace("-", "_")
    s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    s1 = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s1)
    s1 = s1.lower()
    s1 = re.sub(r"__+", "_", s1)
    s1 = re.sub(r"[^0-9a-z_]+", "_", s1)
    return s1.strip("_")


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
            mod_snake = _camel_to_snake(mod_name)
            for ctrl_name, actions in controllers.items():
                if not isinstance(actions, list):
                    if isinstance(actions, dict):
                        actions = list(actions.keys())
                    else:
                        continue
                ctrl_snake = _camel_to_snake(ctrl_name)

                crud_types = {}
                for action in actions:
                    verb = None
                    low = action.lower()
                    for v in ["search", "get", "add", "set", "del", "toggle"]:
                        if low.startswith(v):
                            rest = action[len(v) :]
                            if rest.startswith("_"):
                                rest = rest[1:]
                            suffix = rest
                            if not suffix:
                                continue
                            suffix_snake = _camel_to_snake(suffix)
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

                    reconfigure_guess = None
                    if "service" in controllers:
                        reconfigure_guess = f"{mod_name}/service/reconfigure"
                    else:
                        reconfigure_guess = f"{mod_name}/{ctrl_name}/reconfigure"

                    def _make_present(m=mod_name, c=ctrl_name, t=type_snake, rc=reconfigure_guess):
                        def _present(name, data=None, match=None, reconfigure=rc, search_field=None):
                            return item_present(name, m, c, t, data, match=match, reconfigure=reconfigure, search_field=search_field)

                        _present.__name__ = present_name
                        _present.__doc__ = f"Auto-generated: ensure {t} present in {m}/{c}. Wraps item_present. Reconfigure default {rc}."
                        return _present

                    def _make_absent(m=mod_name, c=ctrl_name, t=type_snake, rc=reconfigure_guess):
                        def _absent(name, match=None, reconfigure=rc, search_field=None):
                            return item_absent(name, m, c, t, match=match, reconfigure=reconfigure, search_field=search_field)

                        _absent.__name__ = absent_name
                        _absent.__doc__ = f"Auto-generated: ensure {t} absent in {m}/{c}. Wraps item_absent."
                        return _absent

                    globals()[present_name] = _make_present()
                    globals()[absent_name] = _make_absent()
                    existing.add(present_name)
                    existing.add(absent_name)

    except Exception as exc:
        log.debug("Dynamic state wrapper injection failed: %s", exc)


_inject_dynamic_state_wrappers()
