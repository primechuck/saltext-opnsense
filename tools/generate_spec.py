#!/usr/bin/env python3
"""
Generate controllers.json from opnsense/core and opnsense/plugins repositories.

This implements the templated maintenance strategy: easy to sprint OPNsense releases.

Usage:
    python tools/generate_spec.py [--core-ref 25.1] [--plugins-ref 25.1] [--output tools/controllers.json]
    python tools/generate_spec.py --local-core /path/to/core --local-plugins /path/to/plugins

It parses:
    src/opnsense/mvc/app/controllers/OPNsense/*/Api/*Controller.php
for method names: public function xyzAction

And groups as:
{
  "meta": {"generated_at": ..., "core_ref": "...", "plugins_ref": "..."},
  "modules": {
    "unbound": {
      "settings": ["searchHostOverride", "getHostOverride", ...],
      ...
    }
  }
}

This file is then consumed by saltext.opnsense.utils.api_spec for discovery,
and can be used to generate ergonomic wrappers.
"""

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

CONTROLLER_RE = re.compile(r"src/opnsense/mvc/app/controllers/OPNsense/([^/]+)/Api/([^/]+)Controller\.php")
ACTION_RE = re.compile(r"public\s+function\s+(\w+)Action\s*\(")


def clone_or_update(repo_url, dest, ref=None):
    if dest.exists():
        print(f"Updating {dest}...")
        subprocess.run(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref or "master"], check=False)
        if ref:
            subprocess.run(["git", "-C", str(dest), "checkout", ref], check=False)
        else:
            subprocess.run(["git", "-C", str(dest), "checkout", "master"], check=False)
    else:
        print(f"Cloning {repo_url} into {dest}...")
        cmd = ["git", "clone", "--depth", "1"]
        if ref:
            cmd += ["--branch", ref]
        cmd += [repo_url, str(dest)]
        subprocess.run(cmd, check=True)


def scan_controllers(root: pathlib.Path):
    modules = {}
    for php_file in root.rglob("*Controller.php"):
        if "/Api/" not in str(php_file):
            continue
        rel = php_file.relative_to(root) if root in php_file.parents else php_file
        m = CONTROLLER_RE.search(str(php_file))
        if not m:
            m = CONTROLLER_RE.search(str(rel))
        if not m:
            continue
        module = m.group(1).lower()
        controller = m.group(2).lower()

        content = php_file.read_text(errors="ignore")
        actions = ACTION_RE.findall(content)
        if not actions:
            continue

        modules.setdefault(module, {})
        modules[module].setdefault(controller, [])
        existing = set(modules[module][controller])
        for act in actions:
            if act not in existing:
                modules[module][controller].append(act)
                existing.add(act)

    for mod in modules:
        for ctrl in modules[mod]:
            modules[mod][ctrl] = sorted(set(modules[mod][ctrl]))

    return modules


def merge_specs(core_mods, plugin_mods):
    merged = {}
    for src in [core_mods, plugin_mods]:
        for mod, ctrls in src.items():
            merged.setdefault(mod, {})
            for ctrl, acts in ctrls.items():
                merged[mod].setdefault(ctrl, [])
                s = set(merged[mod][ctrl])
                for a in acts:
                    if a not in s:
                        merged[mod][ctrl].append(a)
                        s.add(a)
                merged[mod][ctrl] = sorted(merged[mod][ctrl])
    return merged


def main():
    parser = argparse.ArgumentParser(description="Generate OPNsense API controllers.json")
    parser.add_argument("--core-ref", default="master", help="git ref for opnsense/core")
    parser.add_argument("--plugins-ref", default="master", help="git ref for opnsense/plugins")
    parser.add_argument("--local-core", help="local path to core repo (skip clone)")
    parser.add_argument("--local-plugins", help="local path to plugins repo (skip clone)")
    parser.add_argument("--output", default="tools/controllers.json", help="output json path")
    parser.add_argument("--tmp-dir", default="/tmp/opnsense-spec", help="temp clone dir")
    args = parser.parse_args()

    tmp = pathlib.Path(args.tmp_dir)
    tmp.mkdir(parents=True, exist_ok=True)

    if args.local_core:
        core_root = pathlib.Path(args.local_core)
    else:
        core_dest = tmp / "core"
        clone_or_update("https://github.com/opnsense/core.git", core_dest, args.core_ref if args.core_ref != "master" else None)
        core_root = core_dest

    if args.local_plugins:
        plugins_root = pathlib.Path(args.local_plugins)
    else:
        plugins_dest = tmp / "plugins"
        clone_or_update("https://github.com/opnsense/plugins.git", plugins_dest, args.plugins_ref if args.plugins_ref != "master" else None)
        plugins_root = plugins_dest

    print(f"Scanning core: {core_root}")
    core_mods = scan_controllers(core_root)
    print(f"  Found {len(core_mods)} modules")

    print(f"Scanning plugins: {plugins_root}")
    plugin_mods = scan_controllers(plugins_root)
    print(f"  Found {len(plugin_mods)} modules")

    merged = merge_specs(core_mods, plugin_mods)

    output = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "core_ref": args.core_ref,
            "plugins_ref": args.plugins_ref,
            "total_modules": len(merged),
            "total_controllers": sum(len(v) for v in merged.values()),
            "total_actions": sum(len(acts) for ctrls in merged.values() for acts in ctrls.values()),
        },
        "modules": merged,
        "core": core_mods,
        "plugins": plugin_mods,
    }

    out_path = pathlib.Path(args.output)
    if not out_path.is_absolute():
        out_path = pathlib.Path.cwd() / out_path

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True))
    print(f"Wrote {out_path} — modules={len(merged)} ctrls={output['meta']['total_controllers']} actions={output['meta']['total_actions']}")

    core_ctrls = sum(len(v) for v in core_mods.values())
    print(f"Core only: modules={len(core_mods)} controllers={core_ctrls}")

    sample_mod = "unbound"
    if sample_mod in merged:
        print(f"\nSample {sample_mod}:")
        print(json.dumps({sample_mod: merged[sample_mod]}, indent=2))


if __name__ == "__main__":
    main()
