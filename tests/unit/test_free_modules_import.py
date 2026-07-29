"""
Test that full 76-module API is available for free via dynamic injection,
proving import process works without static wrappers.

Generation is free: spec 76 modules -> dynamic 1814 actions injected at import.
Static wrappers are optional and now gitignored for simplicity.
"""

import json
import pathlib

import pytest

SPEC_PATHS = [
    pathlib.Path(__file__).parent.parent.parent
    / "src"
    / "saltext"
    / "opnsense"
    / "utils"
    / "controllers.json",
    pathlib.Path(__file__).parent.parent.parent / "tools" / "controllers.json",
]


def _load_spec_modules():
    for p in SPEC_PATHS:
        if p.exists():
            try:
                data = json.loads(p.read_text())
                mods = data.get("modules", {})
                if mods:
                    return mods
            except Exception:
                continue
    return {}


def test_list_api_modules_returns_76_and_includes_free():
    from saltext.opnsense.utils.api_spec import list_modules

    mods = list_modules()
    assert len(mods) == 76, f"expected 76 modules from spec, got {len(mods)}: {mods}"
    free_must_exist = [
        "caddy",
        "haproxy",
        "nginx",
        "wireguard",
        "openvpn",
        "ipsec",
        "crowdsec",
        "postfix",
        "redis",
        "tor",
    ]
    for m in free_must_exist:
        assert m in mods, f"free module {m} missing — codegen should include all for free"
    for used in ["acmeclient", "bind", "unbound", "kea", "firewall", "interfaces"]:
        assert used in mods


def test_generic_exec_import_and_dynamic():
    from saltext.opnsense.modules import opnsense as generic

    assert hasattr(generic, "call")
    assert hasattr(generic, "search")
    assert hasattr(generic, "list_api_modules")
    dynamic = [x for x in dir(generic) if "_" in x and not x.startswith("_")]
    assert len(dynamic) >= 300, f"expected >=300 dynamic funcs, got {len(dynamic)}"
    for free in ["caddy", "haproxy", "nginx", "wireguard"]:
        assert any(f.startswith(f"{free}_") for f in dynamic), (
            f"generic missing dynamic wrappers for {free}"
        )


def test_generic_state_dynamic():
    from saltext.opnsense.states import opnsense as generic_state

    assert hasattr(generic_state, "item_present")
    assert hasattr(generic_state, "items_present")
    dynamic_present = [x for x in dir(generic_state) if x.endswith("_present")]
    assert len(dynamic_present) >= 100, f"expected >=100 present funcs, got {len(dynamic_present)}"
    for free in ["unbound", "bind", "acmeclient"]:
        assert any(f.startswith(f"{free}_") for f in dynamic_present)


def test_generic_modules_importable():
    mods = _load_spec_modules()
    if not mods:
        pytest.skip("controllers.json not found")
    from saltext.opnsense.modules import opnsense as generic
    from saltext.opnsense.states import opnsense as generic_state

    assert generic.__virtual__() == "opnsense"
    assert generic_state.__virtual__() == "opnsense"


def test_free_modules_demo_state_exists():
    demo_path = (
        pathlib.Path(__file__).parent.parent.parent
        / "docs"
        / "tutorials"
        / "states"
        / "free_modules_demo.sls"
    )
    assert demo_path.exists(), (
        "docs/tutorials/states/free_modules_demo.sls must exist to demonstrate free modules import"
    )
    text = demo_path.read_text()
    for needle in ["caddy", "haproxy", "nginx", "76"]:
        assert needle in text


def test_dynamic_only_architecture():
    src_modules = (
        pathlib.Path(__file__).parent.parent.parent / "src" / "saltext" / "opnsense" / "modules"
    )
    wrappers = list(src_modules.glob("opnsense_*.py"))
    assert len(wrappers) == 0, "static wrappers replaced by dynamic injection"
    from saltext.opnsense.modules import opnsense as generic

    assert hasattr(generic, "list_api_modules")
    assert len(generic.list_api_modules()) == 76
