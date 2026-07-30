#!/usr/bin/env python3
"""
Generate ergonomic OPNsense wrappers from controllers.json.

Loads tools/controllers.json + src/saltext/opnsense/utils/controllers.json,
merges, and generates:

- src/saltext/opnsense/modules/opnsense_{module}.py
- src/saltext/opnsense/states/opnsense_{module}.py

Idempotent, with header AUTO-GENERATED.

Usage:
    python tools/generate_wrappers.py
    python tools/generate_wrappers.py --modules unbound,bind,firewall,interfaces,acmeclient,kea
    python tools/generate_wrappers.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import defaultdict
from typing import Dict, List, Set, Tuple

HEADER_TMPL = "# AUTO-GENERATED - DO NOT EDIT MANUALLY (Built against OPNsense {core_ref}) - run tools/generate_wrappers.py\n"
HEADER = HEADER_TMPL.format(core_ref="25.7")


# Manually curated fallback for acmeclient if missing
MANUAL_ACMECLIENT = {
    "accounts": [
        "searchAccount",
        "getAccount",
        "addAccount",
        "setAccount",
        "delAccount",
        "registerAccount",
    ],
    "validations": [
        "searchValidation",
        "getValidation",
        "addValidation",
        "setValidation",
        "delValidation",
    ],
    "certificates": [
        "searchCertificate",
        "getCertificate",
        "addCertificate",
        "setCertificate",
        "delCertificate",
        "signCertificate",
        "revokeCertificate",
    ],
    "settings": ["get", "set"],
    "service": ["reconfigure", "restart", "status"],
}

CRUD_VERBS = ["search", "get", "add", "set", "del", "toggle"]
CRUD_VERBS_SET = set(CRUD_VERBS)


def camel_to_snake(name: str) -> str:
    if not name:
        return ""
    # Replace - with _
    name = name.replace("-", "_")
    # Handle already snake
    # Insert _ before capital that follows lower/number
    s1 = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    # Handle acronym boundary: e.g., XMLParser -> XML_Parser
    s1 = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s1)
    # Lower and replace multiple __
    s1 = s1.lower()
    s1 = re.sub(r"__+", "_", s1)
    s1 = s1.strip("_")
    # Convert any remaining camel parts that still have uppercase lost? already lower
    # Also handle spaces
    s1 = re.sub(r"[^0-9a-z_]+", "_", s1)
    return s1


def singularize(name: str) -> str:
    n = name.lower()
    if n.endswith("ies") and len(n) > 3:
        return n[:-3] + "y"
    if n.endswith("ses") and len(n) > 3:
        # statuses -> status handling: remove es
        if n.endswith("ses"):
            # naive: remove last 2 (es) -> statu? better check
            # For our controllers: aliases is not, but keep simple
            pass
    if n.endswith("s") and len(n) > 1 and not n.endswith("ss") and not n.endswith("us"):
        return n[:-1]
    return n


def parse_verb_suffix(action: str) -> Tuple[str | None, str]:
    """
    Returns (verb, suffix) where verb in CRUD_VERBS and suffix is remaining part.
    Handles both camelCase and snake_case: searchHostAlias -> (search, HostAlias)
    search_host_alias -> (search, host_alias)
    If no verb matches, return (None, action)
    If verb matches and no suffix, suffix == "" (singleton)
    """
    low = action.lower()
    for verb in sorted(CRUD_VERBS, key=len, reverse=True):
        if low.startswith(verb):
            rest = action[len(verb) :]
            if rest == "":
                return verb, ""
            # rest may start with _ or capital
            if rest.startswith("_"):
                suffix = rest[1:]
            else:
                suffix = rest
            # Ensure suffix is not starting with lowercase that would be weird? e.g., searchQueries -> Queries is ok
            # For snake, suffix is snake already
            if suffix:
                return verb, suffix
    return None, action


def find_spec_files() -> List[pathlib.Path]:
    base = pathlib.Path(__file__).resolve().parent
    candidates = [
        base / "controllers.json",
        base.parent / "src/saltext/opnsense/utils/controllers.json",
        base / ".." / "src/saltext/opnsense/utils/controllers.json",
        pathlib.Path.cwd() / "tools/controllers.json",
        pathlib.Path.cwd() / "src/saltext/opnsense/utils/controllers.json",
    ]
    found = []
    for p in candidates:
        try:
            pp = p.resolve()
        except Exception:
            pp = p
        if pp.exists() and pp not in found:
            found.append(pp)
    return found


def load_merged_spec() -> dict:
    files = find_spec_files()
    merged_modules: Dict[str, Dict[str, List[str]]] = {}
    meta = {}
    for f in files:
        try:
            data = json.loads(f.read_text())
        except Exception as e:
            print(f"warn: failed to load {f}: {e}", file=sys.stderr)
            continue
        mods = data.get("modules") or {}
        # data may also have "core" and "plugins" keys with same structure (older generator)
        # Merge them too if they look like modules
        for k in ["core", "plugins"]:
            if k in data and isinstance(data[k], dict):
                # these are also module->controller->actions
                for mod, ctrls in data[k].items():
                    if isinstance(ctrls, dict):
                        merged_modules.setdefault(mod, {})
                        for ctrl, acts in ctrls.items():
                            merged_modules[mod].setdefault(ctrl, [])
                            # acts may be list
                            if isinstance(acts, list):
                                existing = set(merged_modules[mod][ctrl])
                                for a in acts:
                                    if a not in existing:
                                        merged_modules[mod][ctrl].append(a)
                                        existing.add(a)
        for mod, ctrls in mods.items():
            if not isinstance(ctrls, dict):
                continue
            merged_modules.setdefault(mod, {})
            for ctrl, acts in ctrls.items():
                if not isinstance(acts, list):
                    continue
                merged_modules[mod].setdefault(ctrl, [])
                existing = set(merged_modules[mod][ctrl])
                for a in acts:
                    if a not in existing:
                        merged_modules[mod][ctrl].append(a)
                        existing.add(a)
        # keep last meta
        if "meta" in data:
            meta.update(data["meta"])

    # Inject manual acmeclient if missing or incomplete
    if "acmeclient" not in merged_modules:
        merged_modules["acmeclient"] = MANUAL_ACMECLIENT
    else:
        # Ensure acmeclient has at least accounts, validations, certificates, settings, service
        for ctrl, acts in MANUAL_ACMECLIENT.items():
            if ctrl not in merged_modules["acmeclient"]:
                merged_modules["acmeclient"][ctrl] = acts
            else:
                # merge missing actions
                existing = set(merged_modules["acmeclient"][ctrl])
                for a in acts:
                    if a not in existing:
                        merged_modules["acmeclient"][ctrl].append(a)
                        existing.add(a)

    return {"meta": meta, "modules": merged_modules}


def analyze_controller(controller: str, actions: List[str]) -> dict:
    """
    Returns dict with:
      crud_types: dict normalized_snake -> {orig_suffix_camel, snake, verbs:set, verb_to_orig_action:dict, verb_to_suffix:dict}
      generic_map: dict normalized_snake_action -> orig_action (camel preferred)
      singleton: set of singleton verbs present (get,set)
      raw_actions: list
    """
    # Deduplicate actions preserving order
    seen = set()
    uniq_actions = []
    for a in actions:
        if a not in seen:
            seen.add(a)
            uniq_actions.append(a)

    temp_type_map: Dict[
        str, dict
    ] = {}  # normalized_snake -> {orig_suffixes:set, verbs:set, verb_to_orig_action:dict, verb_to_suffix:dict}
    generic_raw: List[str] = []
    singleton: Set[str] = set()

    for act in uniq_actions:
        low = act.lower()
        if low in ("get", "set"):
            singleton.add(low)
            continue
        verb, suffix = parse_verb_suffix(act)
        if verb is None:
            generic_raw.append(act)
            continue
        if suffix == "":
            # singleton exact verb but already handled get/set; others like search alone?
            if verb in ("get", "set"):
                singleton.add(verb)
            else:
                # e.g., "search" alone (acmeclient case) -> treat as generic search for pseudo type later
                generic_raw.append(act)
            continue
        # verb present with suffix
        norm_snake = camel_to_snake(suffix)
        if not norm_snake:
            generic_raw.append(act)
            continue
        entry = temp_type_map.setdefault(
            norm_snake,
            {
                "orig_suffixes": set(),
                "verbs": set(),
                "verb_to_orig_action": {},
                "verb_to_suffix": {},
                "representative_suffix": suffix,  # will choose best later
            },
        )
        entry["orig_suffixes"].add(suffix)
        entry["verbs"].add(verb)
        # store mapping verb->orig_action, prefer keeping first camelCase variant
        if verb not in entry["verb_to_orig_action"]:
            entry["verb_to_orig_action"][verb] = act
            entry["verb_to_suffix"][verb] = suffix
        else:
            # If existing is snake and new is CamelCase, replace to prefer CamelCase for docs
            existing = entry["verb_to_orig_action"][verb]
            # prefer CamelCase if it has uppercase and existing is all lower with _
            if "_" not in act and "_" in existing:
                entry["verb_to_orig_action"][verb] = act
                entry["verb_to_suffix"][verb] = suffix
                entry["representative_suffix"] = suffix

    # Determine which temp types are valid CRUD vs should be moved to generic
    crud_types: Dict[str, dict] = {}
    for norm_snake, info in temp_type_map.items():
        verbs = info["verbs"]
        # Valid if search in verbs or at least 2 verbs or (add+set) etc
        if "search" in verbs or len(verbs) >= 2 or ("add" in verbs and "set" in verbs):
            # choose best representative suffix: prefer CamelCase (contains uppercase and not underscore)
            best = None
            for s in info["orig_suffixes"]:
                if "_" not in s and any(c.isupper() for c in s):
                    best = s
                    break
            if not best:
                # pick one with uppercase first letter
                for s in info["orig_suffixes"]:
                    if s and s[0].isupper():
                        best = s
                        break
            if not best:
                best = next(iter(info["orig_suffixes"]))
            info["representative_suffix"] = best
            crud_types[norm_snake] = info
        else:
            # Move each verb action to generic
            for verb, orig_act in info["verb_to_orig_action"].items():
                generic_raw.append(orig_act)

    # Now generic deduplication by normalized snake action
    generic_map: Dict[str, str] = {}  # snake_action -> orig_action preferred camel
    for g in generic_raw:
        # For actions that are like "search" alone, keep as is
        snake = camel_to_snake(g)
        if not snake:
            snake = g.lower()
        if snake not in generic_map:
            generic_map[snake] = g
        else:
            existing = generic_map[snake]
            # Prefer CamelCase variant for docs if possible
            if "_" not in g and "_" in existing:
                generic_map[snake] = g

    # Merge simple CRUD verbs into existing crud type when controller singular matches a crud type
    # Handles acmeclient where both simple add/search and typed addAccount/searchAccount coexist
    if crud_types:
        sing_snake = camel_to_snake(singularize(controller))
        target_key = None
        if sing_snake in crud_types:
            target_key = sing_snake
        elif len(crud_types) == 1:
            target_key = next(iter(crud_types.keys()))
        if target_key:
            target_info = crud_types[target_key]
            # Move simple CRUD verbs from generic_map into target
            for g_snake, orig in list(generic_map.items()):
                low = orig.lower()
                if low in CRUD_VERBS_SET:
                    if low not in target_info["verbs"]:
                        target_info["verbs"].add(low)
                        target_info["verb_to_orig_action"][low] = orig
                        target_info["verb_to_suffix"][low] = target_info.get(
                            "representative_suffix", target_key
                        )
                    del generic_map[g_snake]
            # Also merge singleton get/set if they belong to same target (when target is singular controller)
            for sverb in list(singleton):
                if sverb in CRUD_VERBS_SET:
                    if sverb not in target_info["verbs"]:
                        target_info["verbs"].add(sverb)
                        target_info["verb_to_orig_action"][sverb] = sverb
                        target_info["verb_to_suffix"][sverb] = target_info.get(
                            "representative_suffix", target_key
                        )
            # Remove merged singleton verbs
            singleton = set([v for v in singleton if v not in target_info["verbs"]])

    # Also handle pseudo type fallback for simple CRUD controllers like acmeclient where actions are just search/get/add/set/del/toggle without suffix
    # If no crud_types and generic_map contains search/get etc as simple verbs
    if not crud_types:
        # Check if controller has simple CRUD verbs as generic actions (without suffix)
        simple_verbs = set()
        for g_snake, orig in generic_map.items():
            low = orig.lower()
            if low in CRUD_VERBS_SET:
                simple_verbs.add(low)
            # Also check for verb without suffix but in generic_raw? Actually generic_map keys are snake of original, e.g., "search" -> "search"
        # For acmeclient style, if we have search and at least add/set or get etc, we have simple CRUD
        if (
            "search" in generic_map
            or "search" in simple_verbs
            or ("search" in [a.lower() for a in uniq_actions])
        ):
            raw_low = [a.lower() for a in uniq_actions]
            if "search" in raw_low:
                # create pseudo type from controller name singular
                pseudo_snake = camel_to_snake(singularize(controller))
                # verbs are those simple CRUD present
                verbs = set()
                verb_to_orig = {}
                verb_to_suffix = {}
                for act in uniq_actions:
                    low_act = act.lower()
                    if low_act in CRUD_VERBS_SET:
                        verbs.add(low_act)
                        verb_to_orig[low_act] = act
                        verb_to_suffix[low_act] = (
                            pseudo_snake  # not really original suffix, but use controller name
                        )
                if verbs:
                    # Remove those simple verbs from generic_map
                    for v in list(verbs):
                        # need to find key in generic_map that corresponds to this verb simple
                        for k, orig in list(generic_map.items()):
                            if orig.lower() == v:
                                del generic_map[k]
                                break
                        # also if key == v
                        if v in generic_map and generic_map[v].lower() == v:
                            del generic_map[v]
                    crud_types[pseudo_snake] = {
                        "orig_suffixes": {controller},
                        "verbs": verbs,
                        "verb_to_orig_action": verb_to_orig,
                        "verb_to_suffix": verb_to_suffix,
                        "representative_suffix": controller,  # original controller name as suffix for docs (capitalized)
                    }
                    # singleton handling: get/set may have been in singleton set, but now we moved them to crud, so clear singleton if they were part of pseudo
                    # If we used get/set as part of pseudo, remove from singleton
                    singleton = singleton - verbs

    return {
        "crud_types": crud_types,
        "generic_map": generic_map,
        "singleton": singleton,
        "raw_actions": uniq_actions,
    }


def build_module_analysis(modules_dict: Dict[str, Dict[str, List[str]]]) -> Dict[str, dict]:
    """
    Returns per module analysis:
      controllers: dict controller_name -> analysis dict from analyze_controller
      type_collisions: dict snake -> list of controllers where it appears
    """
    result = {}
    for mod, ctrls in modules_dict.items():
        ctrl_analysis = {}
        type_to_ctrls = defaultdict(list)
        for ctrl_name, actions in ctrls.items():
            analysis = analyze_controller(ctrl_name, actions)
            ctrl_analysis[ctrl_name] = analysis
            for type_snake in analysis["crud_types"].keys():
                type_to_ctrls[type_snake].append(ctrl_name)
        result[mod] = {
            "controllers": ctrl_analysis,
            "type_collisions": dict(type_to_ctrls),
            "raw_controllers": ctrls,
        }
    return result


def generate_exec_module_code(module: str, mod_data: dict) -> str:
    controllers = mod_data["controllers"]
    collisions = mod_data["type_collisions"]
    # Gather reconfigure info
    controller_has_reconf = {}
    for ctrl, analysis in controllers.items():
        has_reconf = False
        # check generic_map for reconfigure
        for snake, orig in analysis["generic_map"].items():
            if snake == "reconfigure" or orig.lower() == "reconfigure":
                has_reconf = True
                break
        # also check raw actions case-insensitive reconfigure
        if not has_reconf:
            for act in analysis["raw_actions"]:
                if act.lower() == "reconfigure":
                    has_reconf = True
                    break
        controller_has_reconf[ctrl] = has_reconf

    has_service_reconf = controller_has_reconf.get("service", False)

    lines = []
    lines.append(HEADER)
    lines.append('"""')
    lines.append(f"Auto-generated OPNsense {module} wrappers.")
    lines.append("")
    lines.append(f"Generated from controllers.json for module {module}.")
    lines.append("Do not edit manually; run tools/generate_wrappers.py to regenerate.")
    lines.append("")
    lines.append(f"API pattern: /api/{module}/{{controller}}/{{action}}[/{{uuid}}]")
    lines.append("")
    lines.append("This module wraps generic opnsense.* calls, working in both")
    lines.append("proxy and direct modes via __salt__['opnsense.*']")
    lines.append('"""')
    lines.append("")
    lines.append("import logging")
    lines.append("")
    lines.append("log = logging.getLogger(__name__)")
    lines.append("")
    lines.append(f'__virtualname__ = "opnsense_{module}"')
    lines.append("")
    lines.append("")
    lines.append("def __virtual__():")
    lines.append('    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:')
    lines.append("        return __virtualname__")
    lines.append('    return (False, "opnsense execution module not loaded")')
    lines.append("")
    lines.append("")

    generated_names = set()

    # For each controller, generate functions
    # Sort controllers for determinism
    for ctrl in sorted(controllers.keys()):
        analysis = controllers[ctrl]
        crud = analysis["crud_types"]
        generic_map = analysis["generic_map"]
        singleton = analysis["singleton"]
        crud_snakes = set(crud.keys())
        sing_ctrl = camel_to_snake(singularize(ctrl))

        lines.append(f"# --- {ctrl} controller ---")
        lines.append("")

        # Singleton get/set => get_{controller}, set_{controller} but avoid dup if CRUD already has same name
        if "get" in singleton:
            fn = f"get_{ctrl}"
            # skip if collides with CRUD type same as controller
            if (
                ctrl not in crud_snakes
                and sing_ctrl not in crud_snakes
                and fn not in generated_names
            ):
                lines.append(f"def {fn}():")
                lines.append('    """')
                lines.append(f"    Get {ctrl} singleton config in {module}/{ctrl}.")
                lines.append("")
                lines.append(f"    Wraps: GET /api/{module}/{ctrl}/get")
                lines.append("")
                lines.append("    :return: API response dict")
                lines.append('    """')
                lines.append(f'    return __salt__["opnsense.get"]("{module}", "{ctrl}")')
                lines.append("")
                lines.append("")
                generated_names.add(fn)

        if "set" in singleton:
            fn = f"set_{ctrl}"
            if (
                ctrl not in crud_snakes
                and sing_ctrl not in crud_snakes
                and fn not in generated_names
            ):
                lines.append(f"def {fn}(data):")
                lines.append('    """')
                lines.append(f"    Set {ctrl} singleton config in {module}/{ctrl}.")
                lines.append("")
                lines.append(f"    Wraps: POST /api/{module}/{ctrl}/set")
                lines.append("")
                lines.append("    :param data: Config dict")
                lines.append("    :return: API response dict")
                lines.append('    """')
                lines.append(
                    f'    return __salt__["opnsense.call"]("{module}", "{ctrl}", "set", data=data, method="POST")'
                )
                lines.append("")
                lines.append("")
                generated_names.add(fn)

        # CRUD types
        for type_snake in sorted(crud.keys()):
            info = crud[type_snake]
            verbs = info["verbs"]
            collided = len(collisions.get(type_snake, [])) > 1
            rep_suffix = info.get("representative_suffix") or type_snake
            if collided:
                func_suffix = f"{ctrl}_{type_snake}"
            else:
                func_suffix = type_snake

            # search
            if "search" in verbs:
                fn = f"search_{func_suffix}"
                if fn not in generated_names:
                    orig_action = info["verb_to_orig_action"].get("search", f"search{rep_suffix}")
                    lines.append(
                        f'def {fn}(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):'
                    )
                    lines.append('    """')
                    lines.append(f"    Search {type_snake} entries in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}")
                    lines.append("")
                    lines.append("    :param search_phrase: Optional search phrase")
                    lines.append("    :param row_count: Rows per page, -1 for all")
                    lines.append("    :param current: Current page")
                    lines.append("    :param sort: Sort dict")
                    lines.append("    :param kwargs: Additional filters")
                    lines.append("    :return: API response with rows")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.search"]("{module}", "{ctrl}", "{type_snake}", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)'
                    )
                    lines.append("")
                    lines.append("")
                    generated_names.add(fn)

            if "get" in verbs:
                fn = f"get_{func_suffix}"
                if fn not in generated_names:
                    orig_action = info["verb_to_orig_action"].get("get", f"get{rep_suffix}")
                    lines.append(f"def {fn}(uuid=None):")
                    lines.append('    """')
                    lines.append(f"    Get {type_snake} entry in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: GET /api/{module}/{ctrl}/{orig_action}/{{uuid}}")
                    lines.append("")
                    lines.append("    :param uuid: Optional UUID")
                    lines.append("    :return: API response")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.get"]("{module}", "{ctrl}", "{type_snake}", uuid)'
                    )
                    lines.append("")
                    lines.append("")
                    generated_names.add(fn)

            if "add" in verbs:
                fn = f"add_{func_suffix}"
                if fn not in generated_names:
                    orig_action = info["verb_to_orig_action"].get("add", f"add{rep_suffix}")
                    lines.append(f"def {fn}(data):")
                    lines.append('    """')
                    lines.append(f"    Add {type_snake} entry in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}")
                    lines.append("")
                    lines.append("    :param data: Dict with entry data")
                    lines.append("    :return: API response with uuid")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.add"]("{module}", "{ctrl}", "{type_snake}", data)'
                    )
                    lines.append("")
                    lines.append("")
                    generated_names.add(fn)

            if "set" in verbs:
                fn = f"set_{func_suffix}"
                if fn not in generated_names:
                    orig_action = info["verb_to_orig_action"].get("set", f"set{rep_suffix}")
                    lines.append(f"def {fn}(uuid, data):")
                    lines.append('    """')
                    lines.append(f"    Set/update {type_snake} entry in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}/{{uuid}}")
                    lines.append("")
                    lines.append("    :param uuid: UUID of existing entry")
                    lines.append("    :param data: Updated data")
                    lines.append("    :return: API response")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.set_item"]("{module}", "{ctrl}", "{type_snake}", uuid, data)'
                    )
                    lines.append("")
                    lines.append("")
                    generated_names.add(fn)

            if "del" in verbs:
                fn = f"del_{func_suffix}"
                if fn not in generated_names:
                    orig_action = info["verb_to_orig_action"].get("del", f"del{rep_suffix}")
                    lines.append(f"def {fn}(uuid):")
                    lines.append('    """')
                    lines.append(f"    Delete {type_snake} entry in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}/{{uuid}}")
                    lines.append("")
                    lines.append("    :param uuid: UUID to delete")
                    lines.append("    :return: API response")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.delete"]("{module}", "{ctrl}", "{type_snake}", uuid)'
                    )
                    lines.append("")
                    lines.append("")
                    generated_names.add(fn)

            if "toggle" in verbs:
                fn = f"toggle_{func_suffix}"
                if fn not in generated_names:
                    orig_action = info["verb_to_orig_action"].get("toggle", f"toggle{rep_suffix}")
                    lines.append(f"def {fn}(uuid, enabled=None):")
                    lines.append('    """')
                    lines.append(f"    Toggle {type_snake} entry in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(
                        f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}/{{uuid}}[/{{enabled}}]"
                    )
                    lines.append("")
                    lines.append("    :param uuid: UUID")
                    lines.append("    :param enabled: Optional 0/1 to force state")
                    lines.append("    :return: API response")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.toggle"]("{module}", "{ctrl}", "{type_snake}", uuid, enabled)'
                    )
                    lines.append("")
                    lines.append("")
                    generated_names.add(fn)

        # Generic actions
        for gen_snake in sorted(generic_map.keys()):
            orig_action = generic_map[gen_snake]
            if gen_snake in ("get", "set"):
                continue
            func_name = f"{ctrl}_{gen_snake}"
            func_name = re.sub(r"[^0-9a-z_]", "_", func_name.lower())
            func_name = re.sub(r"__+", "_", func_name)
            if func_name in generated_names:
                continue

            is_reconf_like = gen_snake in (
                "reconfigure",
                "reconfigure_general",
                "restart",
                "start",
                "stop",
                "status",
                "apply",
                "savepoint",
                "cancel_rollback",
            )
            if is_reconf_like or gen_snake == "reconfigure":
                if gen_snake.startswith("reconfigure"):
                    lines.append(f'def {func_name}(action="{orig_action}", data=None):')
                    lines.append('    """')
                    lines.append(f"    {orig_action} action in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}")
                    lines.append("")
                    lines.append(f"    :param action: Action override, default {orig_action}")
                    lines.append("    :param data: Optional data")
                    lines.append("    :return: API response")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.reconfigure"]("{module}", "{ctrl}", action, data)'
                    )
                    lines.append("")
                    lines.append("")
                else:
                    lines.append(f"def {func_name}(data=None):")
                    lines.append('    """')
                    lines.append(f"    Execute {orig_action} in {module}/{ctrl}.")
                    lines.append("")
                    lines.append(f"    Wraps: POST /api/{module}/{ctrl}/{orig_action}")
                    lines.append("")
                    lines.append("    :param data: Optional data dict")
                    lines.append("    :return: API response")
                    lines.append('    """')
                    lines.append(
                        f'    return __salt__["opnsense.call"]("{module}", "{ctrl}", "{orig_action}", data=data, method="POST")'
                    )
                    lines.append("")
                    lines.append("")
            else:
                lines.append(f"def {func_name}(data=None, uuid=None):")
                lines.append('    """')
                lines.append(f"    Execute {orig_action} in {module}/{ctrl}.")
                lines.append("")
                lines.append(f"    Wraps: /api/{module}/{ctrl}/{orig_action}")
                lines.append("")
                lines.append("    :param data: Optional data")
                lines.append("    :param uuid: Optional UUID")
                lines.append("    :return: API response")
                lines.append('    """')
                lines.append(
                    f'    return __salt__["opnsense.call"]("{module}", "{ctrl}", "{orig_action}", uuid=uuid, data=data)'
                )
                lines.append("")
                lines.append("")
            generated_names.add(func_name)

        # Explicit per-controller reconfigure helper if controller has reconfigure
        if controller_has_reconf.get(ctrl):
            fn = f"{ctrl}_reconfigure"
            if fn not in generated_names:
                lines.append(f'def {fn}(action="reconfigure", data=None):')
                lines.append('    """')
                lines.append(f"    Reconfigure {module}/{ctrl}.")
                lines.append("")
                lines.append(f"    Wraps: POST /api/{module}/{ctrl}/reconfigure")
                lines.append("")
                lines.append("    :param action: Action, default reconfigure")
                lines.append("    :param data: Optional data")
                lines.append("    :return: API response")
                lines.append('    """')
                lines.append(
                    f'    return __salt__["opnsense.reconfigure"]("{module}", "{ctrl}", action, data)'
                )
                lines.append("")
                lines.append("")
                generated_names.add(fn)

    # Module-level generic reconfigure
    lines.append("")
    lines.append("# Generic module-level helpers")
    lines.append("")
    default_ctrl = (
        "service"
        if has_service_reconf
        else (sorted(controllers.keys())[0] if controllers else "service")
    )
    if "reconfigure" not in generated_names:
        lines.append(
            f'def reconfigure(controller="{default_ctrl}", action="reconfigure", data=None):'
        )
        lines.append('    """')
        lines.append(f"    Generic reconfigure for {module}.")
        lines.append("")
        lines.append(f"    Wraps: POST /api/{module}/{{controller}}/{{action}}")
        lines.append("")
        lines.append(f"    :param controller: Controller name, default {default_ctrl}")
        lines.append("    :param action: Action name, default reconfigure")
        lines.append("    :param data: Optional data")
        lines.append("    :return: API response")
        lines.append('    """')
        lines.append(
            f'    return __salt__["opnsense.reconfigure"]("{module}", controller, action, data)'
        )
        lines.append("")

    return "\n".join(lines)


def generate_state_module_code(module: str, mod_data: dict) -> str:
    controllers = mod_data["controllers"]
    collisions = mod_data["type_collisions"]

    # Reconfigure detection same as exec
    controller_has_reconf = {}
    for ctrl, analysis in controllers.items():
        has = False
        for snake, orig in analysis["generic_map"].items():
            if snake == "reconfigure" or orig.lower() == "reconfigure":
                has = True
                break
        if not has:
            for act in analysis["raw_actions"]:
                if act.lower() == "reconfigure":
                    has = True
                    break
        controller_has_reconf[ctrl] = has

    has_service = "service" in controllers and controller_has_reconf.get("service", False)
    # Pick default reconfigure path overall
    default_reconf_overall = None
    if has_service:
        default_reconf_overall = f"{module}/service/reconfigure"
    else:
        for ctrl in sorted(controllers.keys()):
            if controller_has_reconf.get(ctrl):
                default_reconf_overall = f"{module}/{ctrl}/reconfigure"
                break

    lines = []
    lines.append(HEADER)
    lines.append('"""')
    lines.append(f"Auto-generated OPNsense {module} state wrappers.")
    lines.append("")
    lines.append(f"Generated from controllers.json for module {module}.")
    lines.append("Do not edit manually; run tools/generate_wrappers.py.")
    lines.append("")
    lines.append("Uses opnsense.item_present/absent which work in proxy and direct modes.")
    lines.append('"""')
    lines.append("")
    lines.append("import logging")
    lines.append("")
    lines.append("log = logging.getLogger(__name__)")
    lines.append("")
    lines.append(f'__virtualname__ = "opnsense_{module}"')
    lines.append("")
    lines.append("")
    lines.append("def __virtual__():")
    lines.append('    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:')
    lines.append("        return __virtualname__")
    lines.append(
        '    return (False, "opnsense state module not loaded: opnsense execution module missing")'
    )
    lines.append("")
    lines.append("")

    for ctrl in sorted(controllers.keys()):
        analysis = controllers[ctrl]
        crud = analysis["crud_types"]
        if not crud:
            continue
        lines.append(f"# --- {ctrl} controller ---")
        lines.append("")
        # Determine default reconfigure for this controller
        if controller_has_reconf.get(ctrl):
            default_reconf = f"{module}/{ctrl}/reconfigure"
        elif has_service:
            default_reconf = f"{module}/service/reconfigure"
        else:
            default_reconf = default_reconf_overall

        default_reconf_str = f'"{default_reconf}"' if default_reconf else "None"

        for type_snake in sorted(crud.keys()):
            collided = len(collisions.get(type_snake, [])) > 1
            if collided:
                base_name = f"{ctrl}_{type_snake}"
            else:
                base_name = type_snake

            info = crud[type_snake]
            rep_suffix = info.get("representative_suffix") or type_snake
            orig_search = info["verb_to_orig_action"].get("search", f"search{rep_suffix}")

            # present
            lines.append(
                f"def {base_name}_present(name, data=None, match=None, reconfigure={default_reconf_str}, search_field=None):"
            )
            lines.append('    """')
            lines.append(f"    Ensure {type_snake} {ctrl} present in {module}.")
            lines.append("")
            lines.append(f"    Wraps opnsense.item_present for /api/{module}/{ctrl}/{orig_search}")
            lines.append("")
            lines.append(
                "    :param name: Identifier for state, used for matching if match not given"
            )
            lines.append("    :param data: Dict of fields to set")
            lines.append(
                '    :param match: Dict to identify existing entry, e.g. {"hostname": "www"}'
            )
            lines.append(
                f"    :param reconfigure: Reconfigure path, default {default_reconf or 'None'}"
            )
            lines.append(
                "    :param search_field: Optional field to use as match if match not supplied"
            )
            lines.append("    :return: State result dict")
            lines.append('    """')
            lines.append(
                f'    return __salt__["opnsense.item_present"](name, "{module}", "{ctrl}", "{type_snake}", data, match=match, reconfigure=reconfigure, search_field=search_field)'
            )
            lines.append("")
            lines.append("")

            # absent
            lines.append(
                f"def {base_name}_absent(name, match=None, reconfigure={default_reconf_str}, search_field=None):"
            )
            lines.append('    """')
            lines.append(f"    Ensure {type_snake} {ctrl} absent in {module}.")
            lines.append("")
            lines.append(f"    Wraps opnsense.item_absent for /api/{module}/{ctrl}/{orig_search}")
            lines.append("")
            lines.append("    :param name: Identifier")
            lines.append("    :param match: Dict to identify entry to delete")
            lines.append("    :param reconfigure: Reconfigure path")
            lines.append("    :param search_field: Optional search field")
            lines.append("    :return: State result")
            lines.append('    """')
            lines.append(
                f'    return __salt__["opnsense.item_absent"](name, "{module}", "{ctrl}", "{type_snake}", match=match, reconfigure=reconfigure, search_field=search_field)'
            )
            lines.append("")
            lines.append("")

    # Generic reconfigured state helper for module
    lines.append("")
    lines.append(
        f'def reconfigured(name, controller="{"service" if has_service else sorted(controllers.keys())[0] if controllers else "service"}", action="reconfigure"):'
    )
    lines.append('    """')
    lines.append(f"    Trigger reconfigure for {module}.")
    lines.append("")
    lines.append("    Wraps opnsense.reconfigured state.")
    lines.append("")
    lines.append("    :param name: State name")
    lines.append("    :param controller: Controller to reconfigure")
    lines.append("    :param action: Action, default reconfigure")
    lines.append('    """')
    lines.append(
        f'    return __salt__["opnsense.reconfigured"](name, "{module}", controller, action) if "opnsense.reconfigured" in __salt__ else __salt__["opnsense.item_present"](name, "{module}", controller, "reconfigure", {{}}, reconfigure=None)  # fallback'
    )
    # Actually call opnsense.reconfigured via state? The state module has reconfigured function. We have __salt__ mapping for state? No, states call execution module directly. Simpler: we call execution reconfigure via module state?
    # We'll implement direct call to execution's reconfigure via __salt__['opnsense.reconfigure'] and return result style
    # Rewrite: use opnsense.reconfigured state if available, else fallback
    # For simplicity, we will call the generic state opnsense.reconfigured if it exists as state, but __salt__ is execution. So we need to implement inline similar to states/opnsense.py reconfigured
    # We'll instead directly implement
    lines.pop()  # remove last line workaround
    lines.append('    ret = {"name": name, "result": False, "changes": {}, "comment": ""}')
    lines.append("    try:")
    lines.append(f'        __salt__["opnsense.reconfigure"]("{module}", controller, action)')
    lines.append('        ret["result"] = True')
    lines.append(f'        ret["comment"] = f"reconfigured {module}/{{controller}}/{{action}}"')
    lines.append(
        f'        ret["changes"] = {{"reconfigured": f"{module}/{{controller}}/{{action}}"}}'
    )
    lines.append("    except Exception as exc:")
    lines.append('        ret["comment"] = f"reconfigure failed: {exc}"')
    lines.append("    return ret")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate OPNsense wrapper modules")
    parser.add_argument(
        "--modules", help="comma-separated list of modules to generate, default all"
    )
    parser.add_argument("--dry-run", action="store_true", help="print what would be generated")
    parser.add_argument("--spec", help="path to controllers.json override")
    args = parser.parse_args()

    if args.spec:
        spec_path = pathlib.Path(args.spec)
        if not spec_path.exists():
            print(f"spec file not found: {spec_path}", file=sys.stderr)
            sys.exit(1)
        data = json.loads(spec_path.read_text())
        modules_dict = data.get("modules", {})
    else:
        merged = load_merged_spec()
        modules_dict = merged.get("modules", {})
        meta = merged.get("meta", {})
        print(
            f"Loaded spec from {len(find_spec_files())} file(s), modules={len(modules_dict)}, meta={meta}"
        )

    # Filter modules
    if args.modules:
        wanted = [m.strip() for m in args.modules.split(",") if m.strip()]
        filtered = {k: v for k, v in modules_dict.items() if k in wanted}
        # For manual acmeclient if wanted includes acmeclient but not in spec, inject
        if "acmeclient" in wanted and "acmeclient" not in filtered:
            filtered["acmeclient"] = MANUAL_ACMECLIENT
        modules_dict = filtered

    analysis = build_module_analysis(modules_dict)

    # Determine output dirs
    # Try to locate src/.../modules and states relative to this file
    base = pathlib.Path(__file__).resolve().parent
    src_modules_dir = base.parent / "src/saltext/opnsense/modules"
    src_states_dir = base.parent / "src/saltext/opnsense/states"

    # Fallback to cwd
    alt_modules = pathlib.Path.cwd() / "src/saltext/opnsense/modules"
    alt_states = pathlib.Path.cwd() / "src/saltext/opnsense/states"
    if not src_modules_dir.exists() and alt_modules.exists():
        src_modules_dir = alt_modules
        src_states_dir = alt_states

    # Ensure dirs exist
    src_modules_dir.mkdir(parents=True, exist_ok=True)
    src_states_dir.mkdir(parents=True, exist_ok=True)

    generated_files = []

    for mod_name, mod_data in sorted(analysis.items()):
        # Skip if no controllers?
        if not mod_data["controllers"]:
            continue

        exec_code = generate_exec_module_code(mod_name, mod_data)
        state_code = generate_state_module_code(mod_name, mod_data)

        exec_path = src_modules_dir / f"opnsense_{mod_name}.py"
        state_path = src_states_dir / f"opnsense_{mod_name}.py"

        if args.dry_run:
            print(f"Would write {exec_path} ({len(exec_code)} bytes)")
            print(f"Would write {state_path} ({len(state_code)} bytes)")
            continue

        exec_path.write_text(exec_code)
        state_path.write_text(state_code)
        generated_files.append(str(exec_path))
        generated_files.append(str(state_path))
        print(f"Generated {exec_path} and {state_path}")

    print(f"\nGenerated {len(generated_files)} files for {len(analysis)} modules")
    for f in generated_files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
