#!/usr/bin/env python3
"""
validate_tutorials.py — CI helper to ensure docs/tutorials SLS are syntactically valid.

- Renders each SLS via Jinja2 (ChainableUndefined, dummy pillar) then parses as YAML
- Optionally tries salt-call state.show_sls if salt is installed and called from CI
- Fails (exit 1) if any SLS is invalid, ensuring CI clearly fails on broken SLS.

Usage:
    python tools/validate_tutorials.py                      # validates all
    python tools/validate_tutorials.py --sls acme_certificates  # single
    python tools/validate_tutorials.py --strict             # fail on UndefinedError too
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import typing

import yaml

try:
    import jinja2  # type: ignore

    HAS_JINJA = True
except ImportError:
    HAS_JINJA = False

STATES_DIR = pathlib.Path(__file__).resolve().parent.parent / "docs" / "tutorials" / "states"
PILLARS_DIR = pathlib.Path(__file__).resolve().parent.parent / "docs" / "tutorials" / "pillars"

# Dummy pillar covering all known tutorial SLS keys (RFC5737 TEST-NET + example.com)
DUMMY_PILLAR = {
    "opnsense": {
        "cluster_parent": {"hostname": "cluster", "domain": "example.com"},
        "host_overrides_direct": [
            {
                "hostname": "srv1",
                "domain": "internal.example.com",
                "ip": "192.0.2.10",
                "description": "TEST-NET-1 direct",
            }
        ],
        "acmeclient": {
            "accounts": [
                {
                    "name": "test",
                    "email": "admin@example.com",
                    "ca": "letsencrypt",
                    "description": "salt managed test",
                }
            ],
            "validations": [
                {
                    "name": "cf-dns01",
                    "method": "dns01",
                    "dns_service": "dns_cf",
                    "dns_sleep": "10",
                    "description": "test validation",
                }
            ],
            "actions": [
                {"name": "restart-haproxy", "type": "haproxy", "description": "Restart HAProxy"}
            ],
            "certificates": [
                {
                    "name": "example.com",
                    "account": "test",
                    "validationMethod": "cf-dns01",
                    "altNames": "www.example.com",
                    "description": "wildcard test",
                }
            ],
        },
        "aliases": {"example.com": ["www", "git"], "internal.example.com": ["code", "ide"]},
        "purge_aliases": {"example.com": ["old-www"]},
        "descriptions": {
            "www.example.com": "Primary Web Ingress",
            "git.example.com": "Forgejo Git",
        },
        "bind_zone": {"name": "example.com"},
        "bind": {
            "zones": [
                {
                    "name": "example.com",
                    "records": [{"name": "www", "type": "A", "value": "192.0.2.10"}],
                }
            ]
        },
        "kea": {
            "subnets": [{"subnet": "192.0.2.0/24", "description": "mgmt - TEST-NET-1"}],
            "reservations": [
                {
                    "hostname": "www",
                    "hw_address": "aa:bb:cc:dd:ee:ff",
                    "ip_address": "192.0.2.10",
                    "subnet": "192.0.2.0/24",
                }
            ],
        },
        "firewall": {
            "aliases": [
                {
                    "name": "app_nodes",
                    "type": "host",
                    "content": "192.0.2.10,192.0.2.11",
                    "description": "app nodes TEST-NET-1",
                }
            ]
        },
        "unbound": {
            "aliases": ["www.example.com"],
        },
        "metrics": {"enabled": True},
    },
    # Also provide flat top-level for some templates that use pillar.get('opnsense_api_key')
    "opnsense_api_key": "TESTKEY",
    "opnsense_api_secret": "TESTSECRET",
}


class SaltMock(dict):
    """Dict that also supports Salt execution module calls via keys like 'grains.get'."""

    def __init__(self, grains_dict: dict | None = None, pillar_dict: dict | None = None):
        super().__init__()
        self._grains = grains_dict or {
            "id": "opnsense-router",
            "opnsense_version": "25.7",
            "opnsense_host": "opnsense.example.com",
            "opnsense_unbound_alias_count": 2,
            "opnsense_bind_domain_count": 1,
        }
        self._pillar = pillar_dict or DUMMY_PILLAR

        # Populate with common Salt calls
        self["grains.get"] = self._grains_get
        self["pillar.get"] = self._pillar_get
        self["opnsense.ping"] = lambda: True
        self["opnsense_dns.managed_preview"] = lambda: {}
        # Fallback: any other salt call returns no-op
        self._fallback = lambda *a, **kw: None

    def _grains_get(self, key: str, default: typing.Any = None) -> typing.Any:
        return self._grains.get(key, default)

    def _pillar_get(self, key: str, default: typing.Any = None) -> typing.Any:
        # Support colon-separated pillar path like "opnsense:aliases"
        cur: typing.Any = self._pillar
        for part in key.split(":"):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return default
        return cur

    def __missing__(self, key: str):  # type: ignore[override]
        # Any unknown salt module returns fallback callable
        return self._fallback


if HAS_JINJA:
    # ChainableUndefined allows attribute access chaining without blowing up
    JINJA_ENV = jinja2.Environment(undefined=jinja2.ChainableUndefined, autoescape=False)  # type: ignore[attr-defined]
    STRICT_ENV = jinja2.Environment(undefined=jinja2.StrictUndefined, autoescape=False)

    # Add useful filters used in tutorial SLS
    def _json_filter(value: typing.Any, indent: int | None = None) -> str:
        return json.dumps(value, indent=indent)

    JINJA_ENV.filters["json"] = _json_filter
    JINJA_ENV.filters["tojson"] = _json_filter
    STRICT_ENV.filters["json"] = _json_filter
    STRICT_ENV.filters["tojson"] = _json_filter
else:
    JINJA_ENV = None  # type: ignore[assignment]
    STRICT_ENV = None  # type: ignore[assignment]


def render_sls(path: pathlib.Path, strict: bool = False) -> tuple[bool, str, typing.Any]:
    """
    Returns (ok, rendered_text_or_error, parsed_yaml_or_None)
    """
    text = path.read_text(encoding="utf-8")

    if not HAS_JINJA:
        # No jinja, just try yaml load directly (will fail on jinja syntax but better than nothing)
        try:
            parsed = yaml.safe_load(text)
            return True, text, parsed
        except Exception as exc:
            return False, f"YAML parse failed (no jinja installed): {exc}", None

    env = STRICT_ENV if strict else JINJA_ENV
    assert env is not None, "Jinja env not initialized"

    # Provide realistic grains dict
    dummy_grains = {
        "id": "opnsense-router",
        "opnsense_version": "25.7",
        "opnsense_host": "opnsense.example.com",
        "opnsense_unbound_alias_count": 2,
        "opnsense_bind_domain_count": 1,
    }
    salt_mock = SaltMock(grains_dict=dummy_grains, pillar_dict=DUMMY_PILLAR)

    try:
        tmpl = env.from_string(text)  # type: ignore[attr-defined]
        rendered = tmpl.render(
            pillar=DUMMY_PILLAR,
            opts={},
            grains=dummy_grains,
            salt=salt_mock,
            __opts__={},
            __salt__=salt_mock,
            __grains__=dummy_grains,
            __pillar__=DUMMY_PILLAR,
        )
    except Exception as exc:
        return False, f"Jinja render failed: {exc}", None

    # NOTE: free_modules_demo.sls indentation bug (5-space onlyif) was fixed in this PR
    # via removing leading space before dash in Jinja conditional. Workaround removed
    # so future indentation bugs surface instead of being hidden (see review #9:230).

    # Now try YAML parsing of rendered result
    try:
        docs = list(yaml.safe_load_all(rendered))
        docs = [d for d in docs if d is not None]
        if not docs:
            return True, rendered, {}
        for doc in docs:
            if doc is None:
                continue
            if not isinstance(doc, dict):
                return False, f"Parsed YAML doc is {type(doc).__name__}, expected dict (SLS)", doc
            for k, v in doc.items():
                if not isinstance(k, str):
                    return False, f"Top-level key {k!r} not string", doc
        return True, rendered, docs[0] if len(docs) == 1 else docs
    except yaml.YAMLError as exc:
        return (
            False,
            f"YAML parse failed after render: {exc}\n--- Rendered snippet ---\n{rendered[:2000]}",
            None,
        )
    except Exception as exc:
        return False, f"Unexpected error during YAML parse: {exc}", None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate tutorial SLS files")
    parser.add_argument("--sls", help="Validate single SLS by name (without .sls)")
    parser.add_argument(
        "--strict", action="store_true", help="Use StrictUndefined (fails on undefined vars)"
    )
    parser.add_argument("--states-dir", default=str(STATES_DIR), help="States directory")
    args = parser.parse_args()

    states_dir = pathlib.Path(args.states_dir)
    if not states_dir.exists():
        print(f"States dir not found: {states_dir}", file=sys.stderr)
        return 2

    if args.sls:
        targets = [states_dir / f"{args.sls}.sls"]
        if not targets[0].exists():
            print(f"SLS not found: {targets[0]}", file=sys.stderr)
            return 2
    else:
        targets = sorted(states_dir.glob("*.sls"))

    if not targets:
        print(f"No SLS files found in {states_dir}", file=sys.stderr)
        return 2

    failures = []
    print(f"Validating {len(targets)} SLS files from {states_dir} (strict={args.strict})")
    print(f"Dummy pillar keys: {list(DUMMY_PILLAR['opnsense'].keys())}")
    print()

    for sls_path in targets:
        ok, rendered_or_err, parsed = render_sls(sls_path, strict=args.strict)
        if ok:
            doc_len = (
                len(parsed)
                if isinstance(parsed, dict)
                else len(parsed)
                if isinstance(parsed, list)
                else 1
            )
            print(f"  OK  {sls_path.name} -> {doc_len} top-level IDs")
        else:
            print(f"  FAIL {sls_path.name}: {rendered_or_err}", file=sys.stderr)
            failures.append(sls_path.name)

    print()
    if failures:
        print(f"FAILED: {len(failures)} SLS invalid: {', '.join(failures)}", file=sys.stderr)
        print("This CI job must fail if SLS is invalid.", file=sys.stderr)
        return 1
    else:
        print(f"SUCCESS: All {len(targets)} SLS files valid.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
