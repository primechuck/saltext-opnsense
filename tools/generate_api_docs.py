#!/usr/bin/env python3
"""
Generate docs/API.md from controllers.json
Lists all 75 modules with controllers and actions.
"""

import json
import pathlib

SRC = (
    pathlib.Path(__file__).parent.parent
    / "src"
    / "saltext"
    / "opnsense"
    / "utils"
    / "controllers.json"
)
OUT = pathlib.Path(__file__).parent.parent / "docs" / "API.md"

data = json.loads(SRC.read_text())
modules = data.get("modules", {})
meta = data.get("meta", {})

with OUT.open("w") as f:
    f.write(
        f"# API Reference — {len(modules)} modules, {meta.get('total_actions', '?')} endpoints\n\n"
    )
    f.write(
        f"> OPNsense {meta.get('core_ref', '')} / plugins {meta.get('plugins_ref', '')} — generated {meta.get('generated_at', '')}\n\n"
    )
    f.write(
        "All endpoints are accessible via generic `opnsense.call` and dynamic wrappers `opnsense.{module}_{controller}_{action}`.\n\n"
    )
    f.write("```bash\n")
    f.write("salt opnsense-router opnsense.list_api_modules\n")
    f.write("salt opnsense-router opnsense.list_api_controllers unbound\n")
    f.write("salt opnsense-router opnsense.list_api_actions unbound settings\n")
    f.write("salt opnsense-router opnsense.search unbound settings host_alias row_count=1\n")
    f.write("```\n\n")
    f.write("## Quick lookup\n\n")
    f.write("| Module | Controllers | Actions | Example |\n")
    f.write("|---|---|---|---|\n")
    for mod in sorted(modules.keys()):
        ctrls = modules[mod]
        total_actions = sum(
            len(v) if isinstance(v, list) else len(v.keys()) if isinstance(v, dict) else 0
            for v in ctrls.values()
        )
        example_ctrl = next(iter(ctrls.keys())) if ctrls else ""
        example_act = ""
        if example_ctrl:
            acts = ctrls[example_ctrl]
            if isinstance(acts, list) and acts:
                example_act = acts[0]
            elif isinstance(acts, dict) and acts:
                example_act = next(iter(acts.keys()))
        f.write(
            f"| {mod} | {len(ctrls)} | {total_actions} | `opnsense.call {mod} {example_ctrl} {example_act}` |\n"
        )
    f.write("\n## Full listing\n\n")
    for mod in sorted(modules.keys()):
        f.write(f"### {mod}\n\n")
        ctrls = modules[mod]
        for ctrl in sorted(ctrls.keys()):
            acts = ctrls[ctrl]
            if isinstance(acts, dict):
                acts = sorted(acts.keys())
            else:
                acts = sorted(acts)
            f.write(f"- **{ctrl}** ({len(acts)}): `{', '.join(acts[:15])}`")
            if len(acts) > 15:
                f.write(f" +{len(acts) - 15} more")
            f.write("\n")
        f.write("\n")

print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
