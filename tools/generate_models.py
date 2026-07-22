#!/usr/bin/env python3
"""
Generate OPNsense model field registry from Model XML.

Parses OPNsense Model XML files like:
  src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml
  src/opnsense/mvc/app/models/OPNsense/Bind/Bind.xml
  src/opnsense/mvc/app/models/OPNsense/Kea/KeaDhcpv4.xml

Produces models.json with field metadata for validation / state generation.

Usage:
    python tools/generate_models.py --core /tmp/opnsense-spec/core --plugins /tmp/opnsense-spec/plugins --output tools/models.json
    python tools/generate_models.py --core-ref 25.7 --output tools/models.json
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

def clone_or_update(repo_url, dest, ref=None):
    if dest.exists():
        print(f"Updating {dest}...")
        subprocess.run(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref or "master"], check=False)
        if ref:
            subprocess.run(["git", "-C", str(dest), "checkout", ref], check=False)
    else:
        print(f"Cloning {repo_url} into {dest}...")
        cmd = ["git", "clone", "--depth", "1"]
        if ref:
            cmd += ["--branch", ref]
        cmd += [repo_url, str(dest)]
        subprocess.run(cmd, check=True)

def parse_model_xml(path: pathlib.Path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as e:
        print(f"Failed to parse {path}: {e}", file=sys.stderr)
        return None

    model_name = path.stem
    fields = {}

    # Model XML structure: <model> -> <mount> -> <items> -> field name -> type
    # Example: <host> <type>ArrayField</type> -> nested items
    def walk_items(elem, prefix=""):
        out = {}
        for child in elem:
            field_type_elem = child.find("type")
            field_type = field_type_elem.text if field_type_elem is not None else "StringField"
            help_elem = child.find("help")
            required_elem = child.find("Required")
            default_elem = child.find("Default")
            mask_elem = child.find("Mask")

            is_array = field_type == "ArrayField"
            sub_items = {}
            if is_array:
                # ArrayField has inner model or items
                inner = child.find("*/*")
                # Actually ArrayField typically has its fields as direct children of <host> ? Let's just look for nested <...>
                # Simpler: iterate child elements that are not type/help/...
                for sub in child:
                    if sub.tag in ("type", "help", "Required", "Default", "Mask", "ValidationMessage", "Constraints"):
                        continue
                    # sub is field definition?
                    sub_type_el = sub.find("type")
                    if sub_type_el is not None:
                        sub_items[sub.tag] = {
                            "type": sub_type_el.text,
                            "help": (sub.find("help").text if sub.find("help") is not None else ""),
                            "required": sub.find("Required").text if sub.find("Required") is not None else "0",
                        }

            key = f"{prefix}.{child.tag}" if prefix else child.tag
            out[child.tag] = {
                "type": field_type,
                "help": help_elem.text if help_elem is not None else "",
                "required": required_elem.text if required_elem is not None else "0",
                "default": default_elem.text if default_elem is not None else "",
                "is_array": is_array,
                "sub_fields": sub_items,
            }
        return out

    # Find items root
    mounts = root.findall(".//items")
    if not mounts:
        mounts = [root]

    all_fields = {}
    for mount in mounts:
        # mount may be <items> containing fields
        for child in mount:
            if child.tag in ("type", "help", "Required", "Default"):
                continue
            ft_el = child.find("type")
            if ft_el is None:
                continue
            all_fields.update(walk_items(mount))

            break

    # Alternative: walk all ArrayField types at any depth
    array_fields = {}
    for elem in root.iter():
        type_el = elem.find("type")
        if type_el is not None and type_el.text == "ArrayField":
            # elem.tag is e.g., "host" with uuid keyed items
            model_fields = {}
            for sub in elem:
                if sub.tag in ("type", "help", "Required"):
                    continue
                # sub may be array item template? Actually ArrayField inner fields often defined under same level?
                # Let's try to find fields inside this ArrayField that have type
                for field in sub:
                    if isinstance(field.tag, str) and field.find("type") is not None:
                        ft = field.find("type").text
                        model_fields[field.tag] = {
                            "type": ft,
                            "required": field.find("Required").text if field.find("Required") is not None else "0",
                        }
            # Simpler: direct children that have type are fields
            for field in elem:
                if field.tag in ("type", "help"):
                    continue
                ft_el = field.find("type")
                if ft_el is not None:
                    array_fields[elem.tag] = array_fields.get(elem.tag, {})
                    array_fields[elem.tag][field.tag] = {
                        "type": ft_el.text,
                        "required": field.find("Required").text if field.find("Required") is not None else "0",
                        "help": field.find("help").text if field.find("help") is not None else "",
                    }

    return {
        "model": model_name,
        "path": str(path),
        "array_fields": array_fields,
        "fields": all_fields,
    }

def scan_models(root: pathlib.Path):
    models = {}
    for xml_path in root.rglob("*.xml"):
        if "/models/OPNsense/" not in str(xml_path):
            continue
        m = MODEL_FILE_RE.search(str(xml_path))
        if not m:
            continue
        module = m.group(1).lower()
        model = m.group(2)
        parsed = parse_model_xml(xml_path)
        if parsed and parsed["array_fields"]:
            models.setdefault(module, {})
            models[module][model] = parsed["array_fields"]

    return models

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", help="local path to core repo")
    parser.add_argument("--plugins", help="local path to plugins repo")
    parser.add_argument("--core-ref", default="master", help="core git ref")
    parser.add_argument("--plugins-ref", default="master", help="plugins git ref")
    parser.add_argument("--tmp-dir", default="/tmp/opnsense-spec", help="tmp clone dir")
    parser.add_argument("--output", default="tools/models.json", help="output json")
    args = parser.parse_args()

    tmp = pathlib.Path(args.tmp_dir)
    tmp.mkdir(parents=True, exist_ok=True)

    if args.core:
        core_root = pathlib.Path(args.core)
    else:
        core_dest = tmp / "core"
        clone_or_update("https://github.com/opnsense/core.git", core_dest, args.core_ref if args.core_ref != "master" else None)
        core_root = core_dest

    if args.plugins:
        plugins_root = pathlib.Path(args.plugins)
    else:
        plugins_dest = tmp / "plugins"
        clone_or_update("https://github.com/opnsense/plugins.git", plugins_dest, args.plugins_ref if args.plugins_ref != "master" else None)
        plugins_root = plugins_dest

    print(f"Scanning core models: {core_root}")
    core_models = scan_models(core_root)
    print(f"  Found {len(core_models)} modules with models")

    print(f"Scanning plugins models: {plugins_root}")
    plugin_models = scan_models(plugins_root)
    print(f"  Found {len(plugin_models)} modules with models")

    merged = {}
    for src in [core_models, plugin_models]:
        for mod, models in src.items():
            merged.setdefault(mod, {})
            for model_name, fields in models.items():
                merged[mod][model_name] = fields

    output = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "core_ref": args.core_ref,
            "plugins_ref": args.plugins_ref,
            "total_modules": len(merged),
            "total_models": sum(len(v) for v in merged.values()),
        },
        "models": merged,
    }

    out_path = pathlib.Path(args.output)
    if not out_path.is_absolute():
        out_path = pathlib.Path.cwd() / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True))
    print(f"Wrote {out_path} — modules={len(merged)} models={output['meta']['total_models']}")

if __name__ == "__main__":
    main()
