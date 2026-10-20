import importlib
from unittest.mock import MagicMock


def _setup_state(mod_name="opnsense"):
    full = f"saltext.opnsense.states.{mod_name}"
    mod = importlib.import_module(full)
    mock_salt = {
        "opnsense.item_present": MagicMock(
            return_value={"result": True, "changes": {}, "comment": "present"}
        ),
        "opnsense.item_absent": MagicMock(
            return_value={"result": True, "changes": {}, "comment": "absent"}
        ),
        "opnsense.reconfigure": MagicMock(return_value={"result": "reconfigured"}),
        "opnsense.call": MagicMock(return_value={}),
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }
    mod.__salt__ = mock_salt
    mod.__opts__ = {"test": False}
    return mod, mock_salt


def test_dynamic_state_wrappers():
    mod, _ = _setup_state("opnsense")
    # B-2 minimal – no dynamic injection, only core 5 funcs
    assert hasattr(mod, "item_present")
    assert hasattr(mod, "item_absent")


def test_item_present_exists():
    mod, _ = _setup_state("opnsense")
    assert hasattr(mod, "item_present")
    assert hasattr(mod, "item_absent")
    assert hasattr(mod, "items_present")
    assert hasattr(mod, "items_absent")
    assert hasattr(mod, "reconfigured")


def test_all_modules_dynamic_present():
    # After B-1/B-2, exec module provides dynamic map, not state. So just check exec module dynamic covers modules
    from saltext.opnsense.modules import opnsense as exec_mod

    # Need to clear cache
    try:
        exec_mod._DYNAMIC_MAP_CACHE = None
        exec_mod.__dict__["__context__"] = {}
    except Exception:
        pass
    m = exec_mod._build_dynamic_map()
    assert len(m) >= 300
