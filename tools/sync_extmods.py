#!/usr/bin/env python3
"""
Sync extension modules to an extmods directory (_modules, _states, _proxy, _grains, _utils)
for file-based install without pip.

GitFS file_roots serves _modules, _states, _proxy, _grains, _utils
as extension modules via `saltutil.sync_all`.

Usage:
    python tools/sync_extmods.py [--dest /path/to/states] [--check]
    python tools/sync_extmods.py [--dest /path/to/states] --copy

--check: fail if copies are out-of-sync (CI)
--copy: copy src -> destination extmods root
"""

import argparse
import os
import pathlib
import shutil
import sys

SRC_BASE = pathlib.Path(__file__).resolve().parent.parent / "src" / "saltext" / "opnsense"

MAPPINGS = [
    ("modules/opnsense.py", "_modules/opnsense.py"),
    ("proxy/opnsense.py", "_proxy/opnsense.py"),
    ("states/opnsense.py", "_states/opnsense.py"),
    ("grains/opnsense.py", "_grains/opnsense.py"),
    ("utils/opnsense.py", "_utils/opnsense.py"),
    ("utils/api_spec.py", "_utils/opnsense_api_spec.py"),
]


def find_default_dest() -> pathlib.Path | None:
    env_dest = os.environ.get("SALT_EXTMODS_DIR")
    if env_dest:
        return pathlib.Path(env_dest).resolve()
    # Check upward paths if part of a parent salt workspace
    p = pathlib.Path(__file__).resolve()
    for _ in range(10):
        p = p.parent
        cand = p / "infra" / "salt" / "states"
        if cand.exists():
            return cand
    return None


def _ensure_wrappers_mappings():
    src_modules = SRC_BASE / "modules"
    if not src_modules.exists():
        return []
    wrappers = []
    for f in src_modules.glob("*.py"):
        if f.name == "__init__.py":
            continue
        wrappers.append((f"modules/{f.name}", f"_modules/{f.name}"))
    src_states = SRC_BASE / "states"
    for f in src_states.glob("*.py"):
        if f.name == "__init__.py":
            continue
        wrappers.append((f"states/{f.name}", f"_states/{f.name}"))
    return wrappers


def _copy_file(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.is_symlink():
        dst.unlink()
    shutil.copy2(src, dst)


def main():
    parser = argparse.ArgumentParser(description="Sync extension modules to an extmods directory")
    parser.add_argument("--dest", help="Target extmods root directory (e.g. /srv/salt/states or /srv/salt)")
    parser.add_argument("--check", action="store_true", help="check if copies are in sync, fail if not")
    parser.add_argument("--copy", action="store_true", help="copy files")
    args = parser.parse_args()

    dest_path = pathlib.Path(args.dest).resolve() if args.dest else find_default_dest()

    if not dest_path or not dest_path.exists():
        print("INFO: No valid target extmods directory found or specified via --dest or SALT_EXTMODS_DIR. Skipping sync.")
        return 0

    if not args.copy and not args.check:
        args.copy = True

    mappings = MAPPINGS + _ensure_wrappers_mappings()
    out_of_sync = []

    for src_rel, dst_rel in mappings:
        src_path = SRC_BASE / src_rel
        dst_path = dest_path / dst_rel

        if not src_path.exists():
            print(f"WARN: src missing {src_path}")
            continue

        if args.check:
            if not dst_path.exists():
                print(f"OUT-OF-SYNC missing {dst_path}")
                out_of_sync.append((src_path, dst_path))
                continue
            if dst_path.is_symlink():
                print(f"OUT-OF-SYNC symlink (need real file) {dst_path} -> {dst_path.readlink()}")
                out_of_sync.append((src_path, dst_path))
                continue
            src_text = src_path.read_text()
            dst_text = dst_path.read_text() if dst_path.exists() else ""
            if src_text != dst_text:
                print(f"OUT-OF-SYNC {dst_rel}")
                out_of_sync.append((src_path, dst_path))
        else:
            _copy_file(src_path, dst_path)
            print(f"Copied {src_rel} -> {dst_rel} ({dst_path.stat().st_size} bytes)")

    if not args.check:
        saltext_dest_base = dest_path / "_utils" / "saltext" / "opnsense"
        for sub in ["utils", "modules", "states", "proxy", "grains", "version"]:
            src_sub = SRC_BASE / sub
            dst_sub = saltext_dest_base / sub
            if not src_sub.exists():
                continue
            dst_sub.mkdir(parents=True, exist_ok=True)
            for f in src_sub.glob("*.py"):
                _copy_file(f, dst_sub / f.name)
                print(f"Copied saltext/opnsense/{sub}/{f.name} -> _utils/saltext/opnsense/{sub}/{f.name}")

        for init_path in [
            dest_path / "_utils" / "saltext" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "modules" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "states" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "proxy" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "grains" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "utils" / "__init__.py",
            dest_path / "_utils" / "saltext" / "opnsense" / "version" / "__init__.py",
        ]:
            init_path.parent.mkdir(parents=True, exist_ok=True)
            if not init_path.exists():
                init_path.write_text("")
                print(f"Created {init_path.relative_to(dest_path)}")

    if args.check:
        if out_of_sync:
            print(f"\n{len(out_of_sync)} file(s) out of sync. Run with --copy to fix.")
            return 1
        else:
            print("All extmod copies in sync.")
            return 0

    print("\nDone. Target extmods directory updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
