#!/usr/bin/env python3
"""
generate_all.py — single entrypoint to regenerate entire saltext-opnsense codegen pipeline.

Orchestrates:
  1. generate_spec.py --core-ref $REF --plugins-ref $REF
     -> writes directly to src/saltext/opnsense/utils/controllers.json
  2. generate_models.py --core /tmp/opnsense-spec/core --plugins /tmp/opnsense-spec/plugins
     -> writes directly to src/saltext/opnsense/utils/models.json
  3. generate_wrappers.py (all 76 modules)
  4. sync_extmods.py --copy (if target extmods directory found)
  5. verify_import.py
  6. pytest tests/unit -q

Usage:
  python tools/generate_all.py [--core-ref 25.7] [--plugins-ref 25.7] [--skip-sync] [--skip-live]
  python tools/generate_all.py --only spec|models|wrappers|sync|verify|test
  CORE_REF=25.7 PLUGINS_REF=25.7 make gen-all

Maintainers: run `make gen-all` or `nox -s gen_all` for full refresh.
Renovate post-upgrade calls this via vendor_charts.py + gen-all.
"""

from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS_DIR = PROJECT_ROOT / "tools"
SRC_UTILS = PROJECT_ROOT / "src" / "saltext" / "opnsense" / "utils"
TMP_DIR = pathlib.Path("/tmp/opnsense-spec")

# Single source of truth: JSON files live in the package, not in tools/
CTRL_JSON_SRC = SRC_UTILS / "controllers.json"
MODELS_JSON_SRC = SRC_UTILS / "models.json"


def run_cmd(cmd: list[str], cwd: pathlib.Path = PROJECT_ROOT, desc: str = "") -> int:
    label = desc or " ".join(cmd[:6])
    print(f"\n=== {label} ===")
    print(f"$ {' '.join(cmd)} (cwd={cwd})")
    result = subprocess.run(cmd, cwd=str(cwd))
    if result.returncode != 0:
        print(f"!! FAILED ({result.returncode}): {label}", file=sys.stderr)
    else:
        print(f"OK: {label}")
    return result.returncode


def run_cmd_output(cmd: list[str], cwd: pathlib.Path = PROJECT_ROOT) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def find_repo_root() -> pathlib.Path | None:
    candidates = [
        PROJECT_ROOT.parent.parent,
        PROJECT_ROOT.parent,
        PROJECT_ROOT,
        pathlib.Path.cwd(),
        pathlib.Path.cwd().parent.parent,
    ]
    seen = set()
    for cand in candidates:
        try:
            cand = cand.resolve()
        except Exception:
            continue
        if cand in seen:
            continue
        seen.add(cand)
        if (cand / "infra" / "salt" / "states").exists() and (
            cand / "projects" / "saltext-opnsense"
        ).exists():
            return cand
    p = PROJECT_ROOT.resolve()
    for _ in range(10):
        p = p.parent
        if (p / "infra" / "salt" / "states").exists():
            return p
    return None


def step_spec(core_ref: str, plugins_ref: str) -> int:
    SRC_UTILS.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        str(TOOLS_DIR / "generate_spec.py"),
        "--core-ref",
        core_ref,
        "--plugins-ref",
        plugins_ref,
        "--output",
        str(CTRL_JSON_SRC),
        "--tmp-dir",
        str(TMP_DIR),
    ]
    rc = run_cmd(cmd, desc=f"generate_spec core={core_ref} plugins={plugins_ref}")
    if rc != 0:
        return rc
    if not CTRL_JSON_SRC.exists():
        print(f"ERROR: {CTRL_JSON_SRC} not created", file=sys.stderr)
        return 1
    return 0


def step_models(core_ref: str, plugins_ref: str) -> int:
    SRC_UTILS.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(TOOLS_DIR / "generate_models.py")]
    core_path = TMP_DIR / "core"
    plugins_path = TMP_DIR / "plugins"
    if core_path.exists() and plugins_path.exists():
        cmd += ["--core", str(core_path), "--plugins", str(plugins_path)]
    else:
        cmd += ["--core-ref", core_ref, "--plugins-ref", plugins_ref, "--tmp-dir", str(TMP_DIR)]
    cmd += ["--output", str(MODELS_JSON_SRC)]
    rc = run_cmd(cmd, desc=f"generate_models core={core_ref} plugins={plugins_ref}")
    if rc != 0:
        return rc
    if not MODELS_JSON_SRC.exists():
        print(f"ERROR: {MODELS_JSON_SRC} not created", file=sys.stderr)
        return 1
    return 0


def step_wrappers() -> int:
    cmd = [sys.executable, str(TOOLS_DIR / "generate_wrappers.py")]
    return run_cmd(cmd, desc="generate_wrappers (all 76 modules)")


def step_sync() -> int:
    cmd = [sys.executable, str(TOOLS_DIR / "sync_extmods.py"), "--copy"]
    return run_cmd(cmd, cwd=PROJECT_ROOT, desc="sync_extmods --copy")


def step_verify() -> int:
    cmd = [sys.executable, str(TOOLS_DIR / "verify_import.py")]
    env_pythonpath = str(PROJECT_ROOT / "src")
    full_cmd = cmd
    print(f"\n=== verify_import (PYTHONPATH={env_pythonpath}) ===")
    print(f"$ PYTHONPATH={env_pythonpath} {' '.join(full_cmd)}")
    import os

    env = os.environ.copy()
    env["PYTHONPATH"] = env_pythonpath + (
        ":" + env.get("PYTHONPATH", "") if env.get("PYTHONPATH") else ""
    )
    result = subprocess.run(full_cmd, cwd=str(PROJECT_ROOT), env=env)
    if result.returncode != 0:
        print(f"!! verify_import FAILED ({result.returncode})", file=sys.stderr)
    else:
        print("OK: verify_import")
    return result.returncode


def step_tests() -> int:
    pytest_bin = shutil.which("pytest") or "pytest"
    has_pytest = shutil.which("pytest") is not None
    if not has_pytest:
        try:
            subprocess.run(
                [sys.executable, "-m", "pytest", "--version"], check=True, capture_output=True
            )
            pytest_bin = f"{sys.executable} -m pytest"
            cmd = [sys.executable, "-m", "pytest", "tests/unit", "-q"]
        except Exception:
            print("WARN: pytest not found, skipping tests (pip install pytest)")
            return 0
    else:
        cmd = [pytest_bin, "tests/unit", "-q"]
    return run_cmd(cmd if isinstance(cmd, list) else ["sh", "-c", cmd], desc="pytest tests/unit -q")


def main():
    parser = argparse.ArgumentParser(
        description="Orchestrate full codegen pipeline for saltext-opnsense"
    )
    parser.add_argument(
        "--core-ref", default="master", help="git ref for opnsense/core (default: master)"
    )
    parser.add_argument(
        "--plugins-ref", default="master", help="git ref for opnsense/plugins (default: master)"
    )
    parser.add_argument("--skip-sync", action="store_true", help="skip sync_extmods.py --copy step")
    parser.add_argument(
        "--skip-live", action="store_true", help="skip pytest tests (alias for --skip-tests)"
    )
    parser.add_argument("--skip-tests", action="store_true", help="skip pytest tests/unit")
    parser.add_argument("--skip-verify", action="store_true", help="skip verify_import.py")
    parser.add_argument("--skip-wrappers", action="store_true", help="skip generate_wrappers.py")
    parser.add_argument("--skip-models", action="store_true", help="skip generate_models.py")
    parser.add_argument("--skip-spec", action="store_true", help="skip generate_spec.py")
    parser.add_argument(
        "--only", help="run only one phase: spec, models, wrappers, sync, verify, test"
    )
    parser.add_argument("--dry-run", action="store_true", help="print steps without executing")
    args = parser.parse_args()

    if args.skip_live:
        args.skip_tests = True

    only = args.only.lower() if args.only else None

    def should_run(name: str) -> bool:
        if only:
            if only == "gen-spec":
                return name == "spec"
            return name == only or (only == "gen" and name in ("spec", "models", "wrappers"))
        return True

    print("== saltext-opnsense generate_all ==")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Core ref: {args.core_ref}  Plugins ref: {args.plugins_ref}")
    print(
        f"Only: {only or 'all'}  skip_sync={args.skip_sync} skip_tests={args.skip_tests} dry_run={args.dry_run}"
    )

    rc = 0

    if should_run("spec") and not args.skip_spec:
        if args.dry_run:
            print(
                f"[dry-run] would run: generate_spec.py --core-ref {args.core_ref} --plugins-ref {args.plugins_ref}"
            )
        else:
            rc = step_spec(args.core_ref, args.plugins_ref)
            if rc != 0:
                return rc
    elif args.skip_spec:
        print("SKIP: spec (--skip-spec)")

    if should_run("models") and not args.skip_models:
        if args.dry_run:
            print(
                f"[dry-run] would run: generate_models.py --core-ref {args.core_ref} --plugins-ref {args.plugins_ref}"
            )
        else:
            rc = step_models(args.core_ref, args.plugins_ref)
            if rc != 0:
                return rc
    elif args.skip_models:
        print("SKIP: models (--skip-models)")

    if should_run("wrappers") and not args.skip_wrappers:
        if args.dry_run:
            print("[dry-run] would run: generate_wrappers.py")
        else:
            rc = step_wrappers()
            if rc != 0:
                return rc
    elif args.skip_wrappers:
        print("SKIP: wrappers (--skip-wrappers)")

    if should_run("sync") and not args.skip_sync:
        if args.dry_run:
            print("[dry-run] would run: sync_extmods.py --copy")
        else:
            rc = step_sync()
            if rc != 0:
                return rc
    else:
        if args.skip_sync:
            print("SKIP: sync (--skip-sync)")
        elif only and only != "sync":
            pass
        else:
            if should_run("sync"):
                print("SKIP: sync (only filter)")

    if should_run("verify") and not args.skip_verify:
        if args.dry_run:
            print("[dry-run] would run: verify_import.py")
        else:
            rc = step_verify()
            if rc != 0:
                return rc
    elif args.skip_verify:
        print("SKIP: verify (--skip-verify)")

    if should_run("test") and not args.skip_tests:
        if args.dry_run:
            print("[dry-run] would run: pytest tests/unit -q")
        else:
            rc = step_tests()
            if rc != 0:
                return rc
    else:
        if args.skip_tests:
            print("SKIP: tests (--skip-tests / --skip-live)")

    print("\n== generate_all DONE ==")
    if args.dry_run:
        print(
            "Dry run — no files modified beyond earlier steps that already ran (spec is dry-only)."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
