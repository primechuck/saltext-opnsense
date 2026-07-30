#!/usr/bin/env python3
"""
Local State Simulator & Idempotency Tester for saltext-opnsense.

Usage:
    # Test state idempotency against mock data (no network / no router needed):
    python tools/test_state.py --mock

    # Test state against a live OPNsense router:
    OPNSENSE_HOST=192.168.1.1 OPNSENSE_API_KEY=xxx OPNSENSE_API_SECRET=yyy \
    python tools/test_state.py --live unbound settings host_alias --hostname www --domain example.com
"""

import argparse
import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

# Add src to python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from saltext.opnsense.states import unbound as state_unbound


def print_result(title: str, ret: dict):
    print(f"\n{'=' * 20} {title} {'=' * 20}")
    print(f"Result  : {ret.get('result')}")
    print(f"Comment : {ret.get('comment')}")
    print("Changes :")
    print(json.dumps(ret.get("changes", {}), indent=2))


def test_mock_idempotency():
    print("Running Mock Idempotency Verification...")

    # Mock Salt environment
    def mock_search(module, controller, typ, search_phrase="", row_count=-1, **kwargs):
        if typ == "host_override":
            return {
                "rows": [
                    {
                        "uuid": "550e8400-e29b-41d4-a716-446655440000",
                        "hostname": "cluster",
                        "domain": "example.com",
                    }
                ]
            }
        if typ == "host_alias":
            return {
                "rows": [
                    {
                        "uuid": "alias-uuid-9999",
                        "hostname": "www",
                        "domain": "example.com",
                        "host": "cluster.example.com",  # Grid returns human FQDN
                        "enabled": "1",  # Grid returns string "1"
                        "description": "managed by salt - www.example.com",
                    }
                ]
            }
        return {"rows": []}

    state_unbound.__opts__ = {"test": False}
    state_unbound.__salt__ = {
        "opnsense.search": MagicMock(side_effect=mock_search),
        "opnsense.set_item": MagicMock(return_value={"result": "saved"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    # Run 1
    ret1 = state_unbound.alias_present(
        name="www.example.com",
        parent="cluster.example.com",
        enabled=True,
    )
    print_result("Run 1 (Existing Item Present)", ret1)

    # Run 2 (Should be 100% idempotent -> changes == {})
    ret2 = state_unbound.alias_present(
        name="www.example.com",
        parent="cluster.example.com",
        enabled=True,
    )
    print_result("Run 2 (Idempotency Check)", ret2)

    if ret2["result"] is True and ret2["changes"] == {}:
        print("\n✅ IDEMPOTENCY PASSED: Run 2 reported 0 changes!")
    else:
        print("\n❌ IDEMPOTENCY FAILED: Run 2 reported changes or failed!")


def main():
    parser = argparse.ArgumentParser(description="Test saltext-opnsense states locally")
    parser.add_argument("--mock", action="store_true", help="Run mock idempotency verification")
    args = parser.parse_args()

    if args.mock or len(sys.argv) == 1:
        test_mock_idempotency()
        return


if __name__ == "__main__":
    main()
