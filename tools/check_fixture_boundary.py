#!/usr/bin/env python3
"""Fixture boundary guard — no private IPs/domains in fixtures."""

import pathlib
import re
import sys

ROOT = (pathlib.Path(__file__).parent / ".." / "fixtures" / "opnsense").resolve()

JR = "jr" + "bob"
BC = "bierce" + r"\.org"
IP18 = r"172" + r"\.18\.\d+\.\d+"
ULA = "fd46" + ":d7ce:64eb"
PRIV1 = r"10\.0\.0\.\d+"
PRIV2 = r"192\.168\.\d+\.\d+"
LEG = "opnsense" + "-router"

FORBIDDEN = [
    (JR, "hostname"),
    (BC, "domain"),
    (IP18, "lab net"),
    (ULA, "ULA"),
    (PRIV1, "RFC1918 10/8"),
    (PRIV2, "RFC1918 192.168"),
    (LEG, "legacy id"),
]
COMPILED = [(re.compile(p, re.IGNORECASE), m) for p, m in FORBIDDEN]
err = 0
for path in ROOT.rglob("*"):
    if path.is_dir():
        continue
    if path.name == "README.md":
        continue
    try:
        txt = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for rgx, msg in COMPILED:
        if rgx.search(txt):
            print(f"FORBIDDEN {msg} in {path.relative_to(ROOT)} matched {rgx.pattern}")
            err += 1
if err:
    print(f"FAIL {err}")
    sys.exit(1)
print("PASS: fixture boundary clean")
sys.exit(0)
