#!/usr/bin/env python3
"""
Sync extension modules to infra/salt/states/_* for file-based install without pip.

GitFS file_roots is infra/salt/states — it serves _modules, _states, _proxy, _grains, _utils
as extension modules via `saltutil.sync_all`. Symlinks escaping root (../../../../projects/...)
are blocked by gitfs for security, so this script copies real files.

Usage:
    python tools/sync_extmods.py [--check]
    python tools/sync_extmods.py --copy

--check: fail if copies are out-of-sync (CI)
--copy: copy src -> infra/salt/states/_*
"""

import argparse
import pathlib
import shutil

REPO_ROOT_CANDIDATES = [
    pathlib.Path(__file__).resolve().parent.parent.parent.parent,
    pathlib.Path.cwd(),
    pathlib.Path.cwd() / ".." / ".." / "..",
]

def find_repo_root():
    for cand in REPO_ROOT_CANDIDATES:
        try:
            cand = cand.resolve()
        except Exception:
            continue
        if (cand / "infra" / "salt" / "states").exists() and (cand / "projects" / "saltext-opnsense").exists():
            return cand
    # fallback: walk up
    p = pathlib.Path(__file__).resolve()
    for _ in range(10):
        p = p.parent
        if (p / "infra" / "salt" / "states").exists():
            return p
    raise RuntimeError("Could not find repo root with infra/salt/states")

SRC_BASE = pathlib.Path(__file__).resolve().parent.parent / "src" / "saltext" / "opnsense"
REPO_ROOT = find_repo_root()
DEST_BASE = REPO_ROOT / "infra" / "salt" / "states"

MAPPINGS = [
    ("modules/opnsense.py", "_modules/opnsense.py"),
    ("proxy/opnsense.py", "_proxy/opnsense.py"),
    ("states/opnsense.py", "_states/opnsense.py"),
    ("grains/opnsense.py", "_grains/opnsense.py"),
    ("utils/opnsense.py", "_utils/opnsense.py"),
    ("utils/api_spec.py", "_utils/opnsense_api_spec.py"),
]

def _ensure_wrappers_mappings():
    src_modules = SRC_BASE / "modules"
    if not src_modules.exists():
        return []
    wrappers = []
    for f in src_modules.glob("opnsense_*.py"):
        wrappers.append((f"modules/{f.name}", f"_modules/{f.name}"))
    src_states = SRC_BASE / "states"
    for f in src_states.glob("opnsense_*.py"):
        wrappers.append((f"states/{f.name}", f"_states/{f.name}"))
    return wrappers

def _copy_file(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.is_symlink():
        dst.unlink()
    shutil.copy2(src, dst)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check if copies are in sync, fail if not")
    parser.add_argument("--copy", action="store_true", help="copy files")
    args = parser.parse_args()

    if not args.copy and not args.check:
        args.copy = True

    mappings = MAPPINGS + _ensure_wrappers_mappings()

    out_of_sync = []

    for src_rel, dst_rel in mappings:
        src_path = SRC_BASE / src_rel
        dst_path = DEST_BASE / dst_rel

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

    # Also handle saltext namespace tree for import compatibility: _utils/saltext/opnsense/...
    if not args.check:
        saltext_dest_base = DEST_BASE / "_utils" / "saltext" / "opnsense"
        for sub in ["utils", "modules", "states", "proxy", "grains", "version"]:
            src_sub = SRC_BASE / sub
            dst_sub = saltext_dest_base / sub
            if not src_sub.exists():
                continue
            dst_sub.mkdir(parents=True, exist_ok=True)
            for f in src_sub.glob("*.py"):
                _copy_file(f, dst_sub / f.name)
                print(f"Copied saltext/opnsense/{sub}/{f.name} -> _utils/saltext/opnsense/{sub}/{f.name}")

        # Also need __init__.py files for namespace packages
        for init_path in [DEST_BASE / "_utils" / "saltext" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "modules" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "states" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "proxy" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "grains" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "utils" / "__init__.py",
                          DEST_BASE / "_utils" / "saltext" / "opnsense" / "version" / "__init__.py",
                         ]:
            init_path.parent.mkdir(parents=True, exist_ok=True)
            if not init_path.exists():
                init_path.write_text("")
                print(f"Created {init_path.relative_to(DEST_BASE)}")

    if args.check:
        if out_of_sync:
            print(f"\n{len(out_of_sync)} file(s) out of sync. Run with --copy to fix.")
            return 1
        else:
            print("All extmod copies in sync.")
            return 0

    print("\nDone. Now salt file roots serve real files (not symlinks), gitfs compatible.")
    print("Commit with: git add infra/salt/states/_modules infra/salt/states/_states infra/salt/states/_proxy infra/salt/states/_grains infra/salt/states/_utils")


if __name__ == "__main__":
    exit(main())
