#!/usr/bin/env python3
"""
Live smoke test against jrbob — no Salt required.
Uses pillar env vars or args.

Usage:
    OPNSENSE_HOST=jrbob.bierce.org OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... python tools/test_live.py
    python tools/test_live.py --host jrbob.bierce.org --key ... --secret ...
"""

import argparse
import os
import sys

sys.path.insert(0, "src")

from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=os.getenv("OPNSENSE_HOST", "jrbob.bierce.org"))
    parser.add_argument("--key", default=os.getenv("OPNSENSE_API_KEY"))
    parser.add_argument("--secret", default=os.getenv("OPNSENSE_API_SECRET"))
    parser.add_argument("--no-verify", action="store_true", default=True)
    args = parser.parse_args()

    if not args.key or not args.secret:
        print("Missing OPNSENSE_API_KEY/SECRET")
        sys.exit(1)

    cfg = OPNsenseClientConfig(
        host=args.host,
        api_key=args.key,
        api_secret=args.secret,
        verify_ssl=False,
        timeout=15,
    )
    client = OPNsenseClient(cfg)

    print(f"Testing {cfg.base_url()}...")

    tests = [
        ("core", "firmware", "status", None),
        ("unbound", "overview", "isEnabled", None),
        ("unbound", "settings", "searchHostAlias", {"rowCount": 5}),
        ("bind", "domain", "searchPrimaryDomain", {"rowCount": 5}),
        ("firewall", "alias", "searchItem", {"rowCount": 5}),
    ]

    for mod, ctrl, act, data in tests:
        try:
            if data is not None:
                res = client.call(mod, ctrl, act, data=data, method="POST")
            else:
                res = client.call(mod, ctrl, act, method="GET")
            rows = res.get("rows", res)
            count = len(rows) if isinstance(rows, list) else 1
            print(f"  OK {mod}/{ctrl}/{act} -> {count} rows / keys={list(res.keys())[:5]}")
        except Exception as exc:
            print(f"  FAIL {mod}/{ctrl}/{act}: {exc}")

    print("Done — if OK, proxy should work.")


if __name__ == "__main__":
    main()
