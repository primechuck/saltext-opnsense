#!/usr/bin/env python3
"""
Debug helper: dump full API reference from controllers.json to stdout or file.

This is NOT part of the committed docs — docs/API.md is hand-written live discovery.
Use this only for offline grepping / debugging when you need a full table:

  python tools/generate_api_docs.py --output /tmp/API_REFERENCE.md
  python tools/generate_api_docs.py | head -100

Do NOT commit output to docs/. SOT is src/saltext/opnsense/utils/controllers.json meta.
"""

import argparse
import json
import pathlib
import sys

DEFAULT_SRC = (
    pathlib.Path(__file__).parent.parent
    / "src"
    / "saltext"
    / "opnsense"
    / "utils"
    / "controllers.json"
)


def main() -> None:
    ap = argparse.ArgumentParser(description="Dump API reference (debug only, not committed)")
    ap.add_argument("--src", default=str(DEFAULT_SRC), help="controllers.json path")
    ap.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output file (default stdout). Use /tmp/ for debug, do not commit to docs/",
    )
    args = ap.parse_args()

    src = pathlib.Path(args.src)
    data = json.loads(src.read_text())
    modules = data.get("modules", {})
    meta = data.get("meta", {})

    out_lines: list[str] = []
    out_lines.append(
        f"# API Reference (DEBUG dump) — {len(modules)} modules, {meta.get('total_actions', '?')} endpoints\n"
    )
    out_lines.append(
        f"> OPNsense {meta.get('core_ref', '')} / plugins {meta.get('plugins_ref', '')} — generated {meta.get('generated_at', '')} — DEBUG ONLY, not committed\n"
    )
    out_lines.append(
        "All endpoints via generic `opnsense.call` and dynamic `opnsense.{module}_{controller}_{action}`.\n"
    )
    out_lines.append("```bash")
    out_lines.append("salt -C 'T@opnsense:fw-01' opnsense.list_api_modules")
    out_lines.append("salt -C 'T@opnsense:fw-01' opnsense.list_api_controllers unbound")
    out_lines.append("salt -C 'T@opnsense:fw-01' opnsense.list_api_actions unbound settings")
    out_lines.append("```\n")
    out_lines.append("## Quick lookup\n")
    out_lines.append("| Module | Controllers | Actions | Example |")
    out_lines.append("|---|---|---|---|")
    for mod in sorted(modules.keys()):
        ctrls = modules[mod]
        total = sum(
            len(v) if isinstance(v, list) else len(v.keys()) if isinstance(v, dict) else 0
            for v in ctrls.values()
        )
        ex_ctrl = next(iter(ctrls.keys())) if ctrls else ""
        ex_act = ""
        if ex_ctrl:
            acts = ctrls[ex_ctrl]
            if isinstance(acts, list) and acts:
                ex_act = acts[0]
            elif isinstance(acts, dict) and acts:
                ex_act = next(iter(acts.keys()))
        out_lines.append(
            f"| {mod} | {len(ctrls)} | {total} | `opnsense.call {mod} {ex_ctrl} {ex_act}` |"
        )
    out_lines.append("\n## Full listing\n")
    for mod in sorted(modules.keys()):
        out_lines.append(f"### {mod}\n")
        ctrls = modules[mod]
        for ctrl in sorted(ctrls.keys()):
            acts = ctrls[ctrl]
            if isinstance(acts, dict):
                acts = sorted(acts.keys())
            else:
                acts = sorted(acts)
            out_lines.append(
                f"- **{ctrl}** ({len(acts)}): `{', '.join(acts[:20])}`"
                + (f" +{len(acts) - 20} more" if len(acts) > 20 else "")
            )
        out_lines.append("")

    content = "\n".join(out_lines)

    if args.output:
        p = pathlib.Path(args.output)
        p.write_text(content)
        print(f"Wrote {p} ({p.stat().st_size} bytes)", file=sys.stderr)
    else:
        sys.stdout.write(content)


if __name__ == "__main__":
    main()
