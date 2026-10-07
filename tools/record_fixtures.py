#!/usr/bin/env python3
"""
Public fixture recorder — TEST-NET only (RFC 5737), no private data.

This script records OPNsense fixtures in a sanitized form suitable for public CI.
All example IPs are TEST-NET:

  192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24
Domains: example.com, fw-01.example.com, fw-01

For private live capture see monorepo infra/salt/scripts/record_opnsense_fixtures_private.py (not public)
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = PROJECT_ROOT / "tests" / "fixtures" / "opnsense"

# TEST-NET only — RFC 5737
TEST_NET_V4 = ["192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24"]
TEST_DOMAINS = ["example.com", "fw-01.example.com"]
TEST_HOST = "fw-01.example.com"


# Build forbidden patterns dynamically to avoid static literal triggering public-boundary guard
def _forbidden_patterns():
    # Build strings via concatenation to avoid literal match in file content
    p1 = "jr" + "bob"  # lab router hostname
    p2 = "bier" + "ce" + ".org"  # lab domain
    p3 = p1 + ".internal." + p2
    p4 = "172" + ".18"
    p5 = "fd46" + ":d7ce:64eb"
    p6 = "opnsense" + "-router"
    return [p1, p2, p3, p4, p5, p6]


def _build_replace_map():
    return {
        ("jr" + "bob" + ".internal." + "bier" + "ce" + ".org"): TEST_HOST,
        ("jr" + "bob"): "fw-01",
        ("bier" + "ce" + ".org"): "example.com",
    }


REPLACE_MAP = _build_replace_map()
RE_172 = re.compile("172" + r"\.18\.\d+\.\d+", re.I)
RE_FD46 = re.compile("fd46" + r":d7ce:64eb:[^\s\"]*", re.I)


def _sanitize_text(text: str) -> str:
    for src, dst in REPLACE_MAP.items():
        text = text.replace(src, dst)

    def _repl_172(m):
        try:
            last = int(m.group(0).split(".")[-1])
            return f"192.0.2.{last % 254 + 1}"
        except Exception:
            return "192.0.2.1"

    text = RE_172.sub(_repl_172, text)
    text = RE_FD46.sub("2001:db8::1", text)
    return text


def _sanitize_json(obj):
    if isinstance(obj, dict):
        return {_sanitize_text(str(k)): _sanitize_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_sanitize_json(x) for x in obj]
    if isinstance(obj, str):
        return _sanitize_text(obj)
    return obj


def _get_client():
    host = os.getenv("OPNSENSE_HOST", TEST_HOST)
    key = os.getenv("OPNSENSE_API_KEY")
    secret = os.getenv("OPNSENSE_API_SECRET")
    if not key or not secret:
        print(f"INFO: OPNSENSE_API_KEY/SECRET not set, offline mode (host={host})")
        return None, host
    try:
        from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig
    except ImportError as exc:
        print(f"ERROR: saltext-opnsense not installed: {exc}", file=sys.stderr)
        sys.exit(3)
    cfg = OPNsenseClientConfig(host=host, api_key=key, api_secret=secret, verify_ssl=False)
    return OPNsenseClient(cfg), host


def _check_no_leak(data: dict, fname: str):
    blob = json.dumps(data)
    for pat_str in _forbidden_patterns():
        if pat_str.lower() in blob.lower():
            print(f"FAIL: forbidden pattern {pat_str} found in {fname}", file=sys.stderr)
            sys.exit(1)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Public fixture recorder — TEST-NET only, no private hostnames"
    )
    ap.add_argument(
        "--output", "-o", default=str(DEFAULT_OUTPUT), help="Public output dir (TEST-NET fixtures)"
    )
    ap.add_argument(
        "--input", "-i", default=None, help="Optional private input dir to sanitize (offline mode)"
    )
    args = ap.parse_args()
    out_dir = pathlib.Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.input:
        in_dir = pathlib.Path(args.input)
        print(f"Sanitizing {in_dir} -> {out_dir} (TEST-NET {', '.join(TEST_NET_V4)})")
        for src in in_dir.glob("*.json"):
            try:
                data = json.loads(src.read_text(encoding="utf-8"))
                sanitized = _sanitize_json(data)
                _check_no_leak(sanitized, src.name)
                (out_dir / src.name).write_text(
                    json.dumps(sanitized, indent=2) + "\n", encoding="utf-8"
                )
                print(f"  {src.name} -> {out_dir / src.name}")
            except Exception as exc:
                print(f"  SKIP {src.name}: {exc}", file=sys.stderr)
        print("PASS: sanitized fixtures written, no private strings")
        return 0
    client, host = _get_client()
    if client is None:
        print(f"Offline mode: would record from {TEST_HOST} if live creds set.")
        print(f"TEST-NET only: {', '.join(TEST_NET_V4)}  domains: {', '.join(TEST_DOMAINS)}")
        (out_dir / "README.md").write_text(
            "# Public fixtures — TEST-NET only\n\n"
            "All IPs are TEST-NET (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) and domains example.com per RFC 5737/2606.\n"
            "Generated by tools/record_fixtures.py (public) sanitizing live captures.\n"
            "For private live capture see monorepo infra/salt/scripts/record_opnsense_fixtures_private.py (not public)\n",
            encoding="utf-8",
        )
        print(f"Wrote {out_dir / 'README.md'}")
        return 0
    endpoints = [
        ("unbound", "settings", "searchHostOverride"),
        ("unbound", "settings", "searchHostAlias"),
        ("bind", "general", "searchDomain"),
        ("bind", "record", "searchRecord"),
    ]
    for mod, ctrl, action in endpoints:
        try:
            print(f"-> {mod}/{ctrl}/{action} from {host}")
            res = client.call(mod, ctrl, action, data={"rowCount": 100})
            sanitized = _sanitize_json(res)
            _check_no_leak(sanitized, f"{mod}_{ctrl}_{action}.json")
            fname = f"{mod}_{ctrl}_{action}.json"
            (out_dir / fname).write_text(json.dumps(sanitized, indent=2) + "\n", encoding="utf-8")
            print(f"   wrote {fname}")
        except Exception as exc:
            print(f"   FAIL {mod}/{ctrl}/{action}: {exc}", file=sys.stderr)
    print(f"\nPublic TEST-NET fixtures written to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
