#!/usr/bin/env python3
"""Public boundary guard — no private strings in public repo."""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent.parent
EXCLUDE_DIR_NAMES = {
    ".git",
    "_build",
    "private_fixtures",
    ".hermes",
    "worktrees",
    ".worktrees",
    "dist",
    "build",
    ".venv",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    ".mypy_cache",
    ".bin",
    "egg-info",
}
ALLOW_BIERCE_FILES = {"pyproject.toml", ".copier-answers.yml"}
SKIP_FILES = {
    pathlib.Path("tools/check_public_boundary.py"),
    pathlib.Path("tools/check_fixture_boundary.py"),
}


def _pat(s):
    return re.compile(s, re.IGNORECASE)


JR = "jr" + "bob"
BC = "bierce" + r"\.org"
IP18 = r"172" + r"\.18\.\d+\.\d+"
ULA = "fd46" + ":d7ce:64eb"
MONO1 = "/usr" + "/local/src/configurations"
MONO2 = "infra" + "/salt" + "/states"
MONO3 = "SALT" + "_EXTMODS_DIR"
LEG = "opnsense" + "-router"

FORBIDDEN_RAW = [
    (JR, f"{JR} hostname"),
    (BC, "real domain"),
    (IP18, "lab net"),
    (ULA, "lab ULA"),
    (MONO1, "monorepo path"),
    (MONO2, "monorepo coupling"),
    (MONO3, "monorepo var"),
    (LEG, "legacy proxy id"),
]
COMPILED = [(_pat(p), msg, p) for p, msg in FORBIDDEN_RAW]


def should_skip(parts):
    for p in parts:
        if p in EXCLUDE_DIR_NAMES or p.endswith(".egg-info"):
            return True
    return False


errors = []
for path in ROOT.rglob("*"):
    if path.is_dir():
        continue
    rel = path.relative_to(ROOT)
    if should_skip(rel.parts):
        continue
    if rel in SKIP_FILES:
        continue
    try:
        if path.stat().st_size > 2_000_000:
            continue
    except Exception:
        continue
    try:
        text = path.read_text(encoding="utf-8", errors="strict")
    except Exception:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "\x00" in text:
                continue
        except Exception:
            continue
    allow = path.name in ALLOW_BIERCE_FILES
    for idx, line in enumerate(text.splitlines(), 1):
        for rgx, msg, _pat_str in COMPILED:
            if allow and "bierce" in _pat_str:
                continue
            if rgx.search(line):
                errors.append((rel, idx, msg, _pat_str, line.strip()[:300]))
if errors:
    for rel, lno, msg, pat, snip in errors:
        print(f"{rel}:{lno}:{msg} [{pat}] -> {snip}")
    print(f"FAIL: {len(errors)} forbidden")
    sys.exit(1)
print("PASS: public boundary clean")
sys.exit(0)
