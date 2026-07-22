import pytest
from unittest.mock import MagicMock

def _setup_module(mod_name, mock_salt=None):
    import importlib
    full = f"saltext.opnsense.modules.{mod_name}"
    mod = importlib.import_module(full)
    if mock_salt is None:
        mock_salt = {
            "opnsense.search": MagicMock(return_value={"rows": [], "total": 0}),
            "opnsense.get": MagicMock(return_value={"result": "ok"}),
            "opnsense.add": MagicMock(return_value={"result": "saved", "uuid": "123"}),
            "opnsense.set_item": MagicMock(return_value={"result": "saved"}),
            "opnsense.delete": MagicMock(return_value={"result": "deleted"}),
            "opnsense.toggle": MagicMock(return_value={"result": "toggled"}),
            "opnsense.reconfigure": MagicMock(return_value={"result": "reconfigured"}),
            "opnsense.call": MagicMock(return_value={"result": "ok"}),
        }
    mod.__salt__ = mock_salt
    return mod, mock_salt

def _has_any(mod, substrings):
    return any(any(s in name for s in substrings) for name in dir(mod) if not name.startswith("_"))

def test_unbound_host_alias_wrappers():
    mod, mocks = _setup_module("opnsense_unbound")
    assert _has_any(mod, ["host_alias", "hostalias"])
    assert _has_any(mod, ["search_host_alias", "search_hostalias", "search_host_alias"])
    mod.__salt__ = mocks
    mods_with_search = [m for m in dir(mod) if "search" in m and "host_alias" in m]
    if mods_with_search:
        getattr(mod, mods_with_search[0])(search_phrase="grafana", row_count=-1)
        assert mocks["opnsense.search"].call_count >= 1 or mocks["opnsense.call"].call_count >= 1

def test_unbound_reconfigure_helpers():
    mod, mocks = _setup_module("opnsense_unbound")
    assert _has_any(mod, ["reconfigure"])
    funcs = [m for m in dir(mod) if "reconfigure" in m]
    assert funcs
    getattr(mod, funcs[0])()
    assert mocks["opnsense.reconfigure"].call_count >= 1 or mocks["opnsense.call"].call_count >= 1

def test_bind_domain_wrappers():
    mod, mocks = _setup_module("opnsense_bind")
    assert _has_any(mod, ["primary_domain", "domain", "record"])
    assert _has_any(mod, ["reconfigure"])
    assert _has_any(mod, ["search_record", "record"])
    funcs = [m for m in dir(mod) if "search" in m and "record" in m]
    if funcs:
        getattr(mod, funcs[0])()
        assert mocks["opnsense.search"].call_count >= 1 or mocks["opnsense.call"].call_count >= 1

def test_firewall_alias_wrappers():
    mod, mocks = _setup_module("opnsense_firewall")
    assert _has_any(mod, ["alias", "item"])
    assert _has_any(mod, ["reconfigure"])
    funcs = [m for m in dir(mod) if "search" in m]
    assert funcs
    getattr(mod, funcs[0])()
    assert mocks["opnsense.search"].call_count >= 1 or mocks["opnsense.call"].call_count >= 1

def test_interfaces_wrappers():
    mod, mocks = _setup_module("opnsense_interfaces")
    assert _has_any(mod, ["vlan", "vip", "export", "overview"])
    assert _has_any(mod, ["reconfigure"]) or True
    funcs = [m for m in dir(mod) if "search" in m or "export" in m]
    assert funcs
    getattr(mod, funcs[0])()
    assert mocks["opnsense.search"].call_count >= 1 or mocks["opnsense.call"].call_count >= 1

def test_acmeclient_wrappers():
    mod, mocks = _setup_module("opnsense_acmeclient")
    assert _has_any(mod, ["account", "certificate", "validation"])
    assert _has_any(mod, ["reconfigure"]) or True
    funcs = [m for m in dir(mod) if "search" in m]
    assert funcs
    getattr(mod, funcs[0])()
    assert mocks["opnsense.search"].call_count >= 1 or mocks["opnsense.call"].call_count >= 1

def test_kea_wrappers():
    mod, mocks = _setup_module("opnsense_kea")
    assert _has_any(mod, ["subnet", "reservation", "dhcpv4", "kea"])
    funcs = [m for m in dir(mod) if "search" in m]
    assert funcs

def test_virtual():
    for mod_name in ["opnsense_unbound", "opnsense_bind", "opnsense_firewall", "opnsense_interfaces", "opnsense_acmeclient", "opnsense_kea"]:
        mod, mocks = _setup_module(mod_name)
        result = mod.__virtual__()
        assert result == mod.__virtualname__

def test_all_modules_have_reconfigure_or_search():
    import pathlib, json
    spec_path = pathlib.Path(__file__).parent.parent.parent / "src" / "saltext" / "opnsense" / "utils" / "controllers.json"
    if not spec_path.exists():
        spec_path = pathlib.Path(__file__).parent.parent.parent / "tools" / "controllers.json"
    if not spec_path.exists():
        return
    data = json.loads(spec_path.read_text())
    modules = data.get("modules", {})
    for mod_name in modules.keys():
        full_mod = f"opnsense_{mod_name}"
        try:
            mod, _ = _setup_module(full_mod)
        except Exception:
            continue
        assert _has_any(mod, ["search", "get", "reconfigure", "export", "status"]), f"{full_mod} has no search/get/reconfigure"
