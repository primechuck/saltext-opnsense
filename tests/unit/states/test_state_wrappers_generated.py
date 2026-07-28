import importlib
from unittest.mock import MagicMock


def _setup_state(mod_name="opnsense"):
    full = f"saltext.opnsense.states.{mod_name}"
    mod = importlib.import_module(full)
    mock_salt = {
        "opnsense.item_present": MagicMock(return_value={"result": True, "changes": {}, "comment": "present"}),
        "opnsense.item_absent": MagicMock(return_value={"result": True, "changes": {}, "comment": "absent"}),
        "opnsense.reconfigure": MagicMock(return_value={"result": "reconfigured"}),
        "opnsense.call": MagicMock(return_value={}),
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }
    mod.__salt__ = mock_salt
    mod.__opts__ = {"test": False}
    return mod, mock_salt

def _has_any(mod, substrings):
    return any(any(s in name for s in substrings) for name in dir(mod) if not name.startswith("_"))

def test_dynamic_state_wrappers():
    mod, mocks = _setup_state("opnsense")
    assert _has_any(mod, ["unbound_settings_host_alias_present", "host_alias_present"])
    assert _has_any(mod, ["bind_record_present", "record_present"])
    assert any(m.endswith("_present") for m in dir(mod))
    assert any(m.endswith("_absent") for m in dir(mod))

def test_item_present_exists():
    mod, _ = _setup_state("opnsense")
    assert hasattr(mod, "item_present")
    assert hasattr(mod, "item_absent")
    assert hasattr(mod, "items_present")
    assert hasattr(mod, "items_absent")
    assert hasattr(mod, "reconfigured")

def test_all_modules_dynamic_present():
    import json
    import pathlib
    spec_path = pathlib.Path(__file__).parent.parent.parent / "src" / "saltext" / "opnsense" / "utils" / "controllers.json"
    if not spec_path.exists():
        spec_path = pathlib.Path(__file__).parent.parent.parent / "tools" / "controllers.json"
    if not spec_path.exists():
        return
    data = json.loads(spec_path.read_text())
    modules = data.get("modules", {})
    mod, _ = _setup_state("opnsense")
    count = 0
    for mod_name in modules.keys():
        for name in dir(mod):
            if mod_name in name and name.endswith("_present"):
                count += 1
                break
    assert count >= 5
