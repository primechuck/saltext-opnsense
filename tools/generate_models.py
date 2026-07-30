#!/usr/bin/env python3
"""
Generate OPNsense model field registry from Model XML.

Parses OPNsense Model XML files like:
  src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml
  src/opnsense/mvc/app/models/OPNsense/Bind/Domain.xml
  src/opnsense/mvc/app/models/OPNsense/Kea/KeaDhcpv4.xml
  plugins/.../models/OPNsense/AcmeClient/AcmeClient.xml

Produces models.json with field metadata for validation / state generation.

Usage:
    python tools/generate_models.py --core /tmp/opnsense-spec/core --plugins /tmp/opnsense-spec/plugins --output src/saltext/opnsense/utils/models.json
    python tools/generate_models.py --core-ref 25.7
"""

import argparse
import json
import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

MODEL_FILE_RE = re.compile(r"src/opnsense/mvc/app/models/OPNsense/([^/]+)/([^/]+)\.xml")

SKIP_TAGS = {
    "type",
    "help",
    "Help",
    "Required",
    "Default",
    "Mask",
    "Model",
    "BlankDesc",
    "Multiple",
    "AsList",
    "ChangeCase",
    "Validation",
    "ConfigdPopulateAct",
    "Sorted",
    "filters",
    "VolumeSize",
    "WildcardEnabled",
    "NetMaskRequired",
    "NetMaskAllowed",
    "AddressFamily",
    "Strict",
    "IpAllowed",
    "HostWildcardAllowed",
    "FqdnWildcardAllowed",
    "IsDNSName",
    "NetMaskAllowed",
    "MaskPerItem",
}


def clone_or_update(repo_url, dest, ref=None):
    if dest.exists():
        print(f"Updating {dest}...")
        subprocess.run(
            ["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref or "master"],
            check=False,
        )
        if ref:
            subprocess.run(["git", "-C", str(dest), "checkout", ref], check=False)
    else:
        print(f"Cloning {repo_url} into {dest}...")
        cmd = ["git", "clone", "--depth", "1"]
        if ref:
            cmd += ["--branch", ref]
        cmd += [repo_url, str(dest)]
        subprocess.run(cmd, check=True)


def _get_type_from_elem(elem: ET.Element) -> str:
    t = elem.attrib.get("type")
    if t:
        return t.strip()
    child = elem.find("type")
    if child is not None and child.text:
        return child.text.strip()
    return ""


def _get_child_text(elem: ET.Element, tag_name: str) -> str:
    child = elem.find(tag_name)
    if child is not None and child.text:
        return child.text.strip()
    # case-insensitive fallback for some tags
    tag_lower = tag_name.lower()
    for sub in elem:
        if sub.tag.lower() == tag_lower and sub.text:
            return sub.text.strip()
    return ""


def _extract_relation_targets(field_elem: ET.Element) -> list[dict]:
    targets: list[dict] = []
    model_elem = field_elem.find("Model")
    if model_elem is None:
        for child in field_elem:
            if child.tag.lower() == "model":
                model_elem = child
                break
    if model_elem is None:
        return targets
    for rel in model_elem:
        if not isinstance(rel.tag, str):
            continue
        source = _get_child_text(rel, "source") or _get_child_text(rel, "Source")
        if not source and rel.text:
            source = (rel.text or "").strip()
        if not source:
            for sub in rel:
                if sub.tag.lower() == "source" and sub.text:
                    source = sub.text.strip()
                    break
        if not source:
            continue
        items = _get_child_text(rel, "items") or _get_child_text(rel, "Items")
        display = _get_child_text(rel, "display") or _get_child_text(rel, "Display")
        t: dict = {"key": rel.tag, "source": source}
        if items:
            t["items"] = items
        if display:
            t["display"] = display
        for fn in ("filters", "Filters"):
            fe = rel.find(fn)
            if fe is not None:
                filt = {}
                for fchild in fe:
                    if isinstance(fchild.tag, str) and fchild.text:
                        filt[fchild.tag] = fchild.text.strip()
                if filt:
                    t["filters"] = filt
                break
        targets.append(t)
    return targets


def extract_field_meta(field_elem: ET.Element) -> dict:
    ftype = _get_type_from_elem(field_elem)
    required = _get_child_text(field_elem, "Required")
    default = _get_child_text(field_elem, "Default")
    help_text = _get_child_text(field_elem, "help")
    if not help_text:
        help_text = _get_child_text(field_elem, "Help")
    meta = {
        "type": ftype,
        "required": required or "0",
        "help": help_text,
        "default": default,
    }

    # Extract additional constraints for client-side validation
    for tag in ("ValidationMessage", "MaximumValue", "MinimumValue"):
        val = _get_child_text(field_elem, tag)
        if val:
            meta[tag] = val

    # Extract OptionValues (Enum choices)
    ov_elem = field_elem.find("OptionValues")
    if ov_elem is not None:
        options = {}
        for child in ov_elem:
            if isinstance(child.tag, str):
                options[child.tag] = (child.text or "").strip()
        if options:
            meta["OptionValues"] = options

    # Extract generic Constraints if available
    constraints_elem = field_elem.find("Constraints")
    if constraints_elem is not None:
        constraints = {}
        for child in constraints_elem:
            if isinstance(child.tag, str):
                constraints[child.tag] = (child.text or "").strip()
        if constraints:
            meta["Constraints"] = constraints

    if "ModelRelationField" in ftype or "RelationField" in ftype:
        rels = _extract_relation_targets(field_elem)
        if rels:
            meta["relation"] = rels if len(rels) > 1 else rels[0]
            if len(rels) == 1:
                meta["relation_targets"] = rels
            else:
                meta["relation_targets"] = rels
        multiple = _get_child_text(field_elem, "Multiple")
        if multiple:
            meta["multiple"] = multiple
    return meta


def parse_model_xml(path: pathlib.Path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as e:
        print(f"Failed to parse {path}: {e}", file=sys.stderr)
        return None

    array_fields: dict[str, dict] = {}

    for elem in root.iter():
        if not isinstance(elem.tag, str):
            continue
        elem_type = _get_type_from_elem(elem)
        if elem_type != "ArrayField":
            continue

        array_name = elem.tag
        if not array_name:
            continue

        fields: dict[str, dict] = {}

        for child in elem:
            if not isinstance(child.tag, str):
                continue
            if child.tag in SKIP_TAGS:
                continue

            child_type = _get_type_from_elem(child)
            if child_type:
                # direct field
                if child.tag not in fields:
                    fields[child.tag] = extract_field_meta(child)
            else:
                # container without type (e.g., option_data) – look one level deeper
                for sub in child:
                    if not isinstance(sub.tag, str):
                        continue
                    if sub.tag in SKIP_TAGS:
                        continue
                    sub_type = _get_type_from_elem(sub)
                    if sub_type and sub.tag not in fields:
                        fields[sub.tag] = extract_field_meta(sub)
                    elif not sub_type:
                        # third level fallback for deeply nested structures
                        for sub2 in sub:
                            if not isinstance(sub2.tag, str):
                                continue
                            if sub2.tag in SKIP_TAGS:
                                continue
                            sub2_type = _get_type_from_elem(sub2)
                            if sub2_type and sub2.tag not in fields:
                                fields[sub2.tag] = extract_field_meta(sub2)

        if fields:
            array_fields[array_name] = fields

    if not array_fields:
        return None

    return {
        "model": path.stem,
        "path": str(path),
        "array_fields": array_fields,
    }


def extract_module_model(xml_path: pathlib.Path):
    s = str(xml_path)
    if "/models/OPNsense/" not in s:
        return None, None
    # split after OPNsense/
    try:
        after = s.split("/models/OPNsense/")[1]
    except IndexError:
        return None, None
    parts = after.split("/")
    if not parts:
        return None, None
    module = parts[0]
    model = xml_path.stem
    # sanity: model file should be xml; skip if module contains "."
    if not module:
        return None, None
    return module.lower(), model


def scan_models(root: pathlib.Path):
    models: dict = {}
    for xml_path in root.rglob("*.xml"):
        if "/models/OPNsense/" not in str(xml_path):
            continue
        # quick skip for ACL/Menu etc – still parse but they often have no ArrayField
        # Use improved extraction
        module, model = extract_module_model(xml_path)
        if not module or not model:
            # fallback to regex
            m = MODEL_FILE_RE.search(str(xml_path))
            if not m:
                continue
            module = m.group(1).lower()
            model = m.group(2)
        parsed = parse_model_xml(xml_path)
        if not parsed:
            continue
        if not parsed["array_fields"]:
            continue
        models.setdefault(module, {})
        models[module].setdefault(model, {})
        # merge arrays for same model (if multiple xml define same model? but we use array granularity)
        for arr_name, fields in parsed["array_fields"].items():
            if arr_name not in models[module][model]:
                models[module][model][arr_name] = fields
            else:
                # merge fields
                for f_name, f_meta in fields.items():
                    models[module][model][arr_name].setdefault(f_name, f_meta)

    return models


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", help="local path to core repo")
    parser.add_argument("--plugins", help="local path to plugins repo")
    parser.add_argument("--core-ref", default="master", help="core git ref")
    parser.add_argument("--plugins-ref", default="master", help="plugins git ref")
    parser.add_argument("--tmp-dir", default="/tmp/opnsense-spec", help="tmp clone dir")
    parser.add_argument(
        "--output", default="src/saltext/opnsense/utils/models.json", help="output json"
    )
    args = parser.parse_args()

    tmp = pathlib.Path(args.tmp_dir)
    tmp.mkdir(parents=True, exist_ok=True)

    if args.core:
        core_root = pathlib.Path(args.core)
    else:
        core_dest = tmp / "core"
        clone_or_update(
            "https://github.com/opnsense/core.git",
            core_dest,
            args.core_ref if args.core_ref != "master" else None,
        )
        core_root = core_dest

    if args.plugins:
        plugins_root = pathlib.Path(args.plugins)
    else:
        plugins_dest = tmp / "plugins"
        clone_or_update(
            "https://github.com/opnsense/plugins.git",
            plugins_dest,
            args.plugins_ref if args.plugins_ref != "master" else None,
        )
        plugins_root = plugins_dest

    print(f"Scanning core models: {core_root}")
    core_models = scan_models(core_root)
    print(f"  Found {len(core_models)} modules with models")
    for mod, mmodels in sorted(core_models.items())[:20]:
        print(f"    core {mod}: {list(mmodels.keys())[:5]} ({len(mmodels)} models)")

    print(f"Scanning plugins models: {plugins_root}")
    plugin_models = scan_models(plugins_root)
    print(f"  Found {len(plugin_models)} modules with models")
    for mod, mmodels in sorted(plugin_models.items())[:20]:
        print(f"    plug {mod}: {list(mmodels.keys())[:5]} ({len(mmodels)} models)")

    merged = {}
    for src in [core_models, plugin_models]:
        for mod, models in src.items():
            merged.setdefault(mod, {})
            for model_name, arrays in models.items():
                merged[mod].setdefault(model_name, {})
                for arr_name, fields in arrays.items():
                    if arr_name not in merged[mod][model_name]:
                        merged[mod][model_name][arr_name] = fields
                    else:
                        merged[mod][model_name][arr_name].update(fields)

    output = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "core_ref": args.core_ref,
            "plugins_ref": args.plugins_ref,
            "total_modules": len(merged),
            "total_models": sum(len(v) for v in merged.values()),
            "total_arrays": sum(len(arrs) for mods in merged.values() for arrs in mods.values()),
        },
        "models": merged,
    }

    out_path = pathlib.Path(args.output)
    if not out_path.is_absolute():
        out_path = pathlib.Path.cwd() / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True))
    print(
        f"Wrote {out_path} — modules={len(merged)} models={output['meta']['total_models']} arrays={output['meta']['total_arrays']}"
    )

    # highlight required modules
    for need in ["unbound", "bind", "kea", "acmeclient"]:
        if need in merged:
            print(f"  OK {need}: models={list(merged[need].keys())}")
        else:
            print(f"  MISSING {need}", file=sys.stderr)


if __name__ == "__main__":
    main()
