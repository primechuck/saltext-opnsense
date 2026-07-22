from unittest.mock import MagicMock
import importlib

def _setup_state(mod_name):
    full = f"saltext.opnsense.states.{mod_name}"
    mod = importlib.import_module(full)
    mock_salt = {
        "opnsense.item_present": MagicMock(return_value={"result": True, "changes": {}, "comment": "present"}),
        "opnsense.item_absent": MagicMock(return_value={"result": True, "changes": {}, "comment": "absent"}),
        "opnsense.reconfigure": MagicMock(return_value={"result": "reconfigured"}),
        "opnsense.call": MagicMock(return_value={}),
    }
    mod.__salt__ = mock_salt
    return mod, mock_salt

def _has_any(mod, substrings):
    return any(any(s in name for s in substrings) for name in dir(mod) if not name.startswith("_") and name.endswith("_present"))

def test_unbound_state_host_alias():
    mod, mocks = _setup_state("opnsense_unbound")
    assert _has_any(mod, ["host_alias", "hostalias", "host_override"])
    funcs = [m for m in dir(mod) if "host_alias" in m and m.endswith("_present")]
    if not funcs:
        funcs = [m for m in dir(mod) if m.endswith("_present")]
    assert funcs
    getattr(mod, funcs[0])(name="grafana.bierce.org", data={"hostname": "grafana"}, match={"hostname": "grafana"})
    mocks["opnsense.item_present"].assert_called()

def test_firewall_state_alias_item():
    mod, mocks = _setup_state("opnsense_firewall")
    assert any(m.endswith("_present") for m in dir(mod))
    funcs = [m for m in dir(mod) if m.endswith("_present")]
    assert funcs
    getattr(mod, funcs[0])(name="test", data={"name": "test"})
    args, _ = mocks["opnsense.item_present"].call_args
    assert args[1] == "firewall"

def test_bind_state_record():
    mod, mocks = _setup_state("opnsense_bind")
    funcs = [m for m in dir(mod) if "record" in m and m.endswith("_present")]
    if not funcs:
        funcs = [m for m in dir(mod) if m.endswith("_present")]
    assert funcs
    getattr(mod, funcs[0])(name="pihole", data={"name": "pihole"})
    mocks["opnsense.item_present"].assert_called()
    args, _ = mocks["opnsense.item_present"].call_args
    assert args[1] == "bind"

def test_acmeclient_state():
    mod, mocks = _setup_state("opnsense_acmeclient")
    funcs = [m for m in dir(mod) if m.endswith("_present")]
    assert funcs
    getattr(mod, funcs[0])(name="myaccount", data={"name": "myaccount"})
    mocks["opnsense.item_present"].assert_called()
    args, _ = mocks["opnsense.item_present"].call_args
    assert args[1] == "acmeclient"

def test_interfaces_state():
    mod, mocks = _setup_state("opnsense_interfaces")
    funcs = [m for m in dir(mod) if m.endswith("_present")]
    assert funcs
    getattr(mod, funcs[0])(name="vlan10", data={"vlan": 10})
    mocks["opnsense.item_present"].assert_called()

def test_state_virtual():
    for mod_name in ["opnsense_unbound", "opnsense_bind", "opnsense_firewall", "opnsense_interfaces", "opnsense_acmeclient", "opnsense_kea"]:
        try:
            mod, _ = _setup_state(mod_name)
        except Exception:
            continue
        assert mod.__virtual__() == mod.__virtualname__

def test_all_state_modules_have_present():
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
            mod, _ = _setup_state(full_mod)
        except Exception:
            continue
        assert any(m.endswith("_present") for m in dir(mod)), f"{full_mod} has no *_present"
        assert any(m.endswith("_absent") for m in dir(mod)), f"{full_mod} has no *_absent"
