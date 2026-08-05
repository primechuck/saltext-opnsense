#!/usr/bin/env python3
"""
Generate boring example pillar for ALL modules from controllers.json.

Reads tools/controllers.json (76 modules) and produces examples/pillars/full_example.sls
using example.com domains per RFC 2606.

Usage:
    python tools/generate_pillar_example.py
    python tools/generate_pillar_example.py --output examples/pillars/full_example.sls
"""

import json
import pathlib

SPEC_PATHS = [
    pathlib.Path(__file__).with_name("controllers.json"),
    pathlib.Path(__file__).parent.parent
    / "src"
    / "saltext"
    / "opnsense"
    / "utils"
    / "controllers.json",
    pathlib.Path.cwd() / "tools" / "controllers.json",
]


def load_spec():
    for p in SPEC_PATHS:
        if p.exists():
            try:
                data = json.loads(p.read_text())
                if data.get("modules"):
                    return data
            except Exception:
                continue
    return {"modules": {}}


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="examples/pillars/full_example.sls")
    args = parser.parse_args()

    spec = load_spec()
    mods = spec.get("modules", {})

    pillar = {
        "opnsense": {
            "host": "opnsense.example.com",
            "proto": "https",
            "verify_ssl": False,
            "api_key": "REPLACE_ME",
            "api_secret": "REPLACE_ME",
            "timeout": 30,
            "cluster_parent": {"hostname": "cluster", "domain": "example.com"},
            "aliases": {
                "example.com": ["www", "mail", "ftp"],
                "internal.example.com": ["code", "api"],
            },
            "purge_aliases": {"example.com": ["old-www"]},
            "firewall": {
                "aliases": [
                    {
                        "name": "app_nodes",
                        "type": "host",
                        "content": "192.0.2.10,192.0.2.11",
                        "description": "app nodes (TEST-NET-1 RFC5737)",
                    },
                    {
                        "name": "rfc5737",
                        "type": "network",
                        "content": "192.0.2.0/24,198.51.100.0/24,203.0.113.0/24",
                        "description": "TEST-NET RFC5737 example nets",
                    },
                ],
                "filter_rules": [
                    {
                        "description": "allow app api",
                        "action": "pass",
                        "interface": "lan",
                        "source": "app_nodes",
                        "destination_port": "6443",
                    },
                ],
            },
            "wireguard": {
                "clients": [
                    {
                        "name": "laptop",
                        "pubkey": "PUBKEY=",
                        "allowedips": "198.51.100.2/32",
                        "endpoint": "vpn.example.com:51820",
                    }
                ]
            },
            "interfaces": {
                "vlans": [{"description": "mgmt vlan60", "vlan": 60, "parent": "igc1"}],
                "vips": [
                    {
                        "description": "carp lan",
                        "mode": "carp",
                        "interface": "lan",
                        "subnet": "192.0.2.1/24",
                    }
                ],
            },
            "kea": {
                "subnets": [{"subnet": "192.0.2.0/24", "description": "lan (TEST-NET-1)"}],
                "reservations": [
                    {
                        "hostname": "www",
                        "hw_address": "aa:bb:cc:dd:ee:ff",
                        "ip_address": "192.0.2.10",
                        "subnet": "192.0.2.0/24",
                    }
                ],
            },
            "acmeclient": {
                "accounts": [
                    {"name": "letsencrypt-prod", "email": "admin@example.com", "ca": "letsencrypt"}
                ],
                "certificates": [{"name": "*.example.com", "description": "wildcard"}],
            },
        }
    }

    for mod_name in sorted(mods.keys()):
        if mod_name in pillar["opnsense"]:
            continue
        pillar["opnsense"][mod_name] = {
            "example": {"description": f"salt managed {mod_name} example", "enabled": "1"}
        }

    out_path = pathlib.Path(args.output)
    if not out_path.is_absolute():
        out_path = pathlib.Path.cwd() / out_path

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        f.write(
            f"# Full boring example pillar for ALL {len(mods)} OPNsense modules — auto-generated\n"
        )
        f.write("# Uses example.com per RFC 2606\n")
        f.write(
            f"# Spec: {len(mods)} modules, {spec.get('meta', {}).get('total_controllers', 0)} controllers, {spec.get('meta', {}).get('total_actions', 0)} actions\n"
        )
        f.write(json.dumps(pillar, indent=2))
        f.write("\n")

    print(
        f"Wrote {out_path} {out_path.stat().st_size} bytes with {len(pillar['opnsense'])} top-level keys"
    )


if __name__ == "__main__":
    main()
