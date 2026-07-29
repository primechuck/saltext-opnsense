import importlib
from unittest.mock import MagicMock


def _setup_generic(mock_salt=None):
    full = "saltext.opnsense.modules.opnsense"
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


def test_dynamic_wrappers_cover_all():
    mod, mocks = _setup_generic()
    assert _has_any(mod, ["unbound_settings_search_host_alias"])
    assert _has_any(mod, ["bind_record_search_record"])
    assert _has_any(mod, ["firewall_alias_search_item"])
    assert _has_any(mod, ["kea_dhcpv4_search_subnet"])
    assert _has_any(mod, ["acmeclient_accounts_search"])


def test_dynamic_search_calls():
    mod, mocks = _setup_generic()
    import sys
    import types

    if "salt" not in sys.modules:
        salt_mock = types.ModuleType("salt")
        utils_mock = types.ModuleType("salt.utils")
        platform_mock = types.ModuleType("salt.utils.platform")
        platform_mock.is_proxy = lambda: False
        sys.modules["salt"] = salt_mock
        sys.modules["salt.utils"] = utils_mock
        sys.modules["salt.utils.platform"] = platform_mock

    mod.__opts__ = {"proxy": {}}
    mod.__pillar__ = {}

    from unittest.mock import patch

    with patch("saltext.opnsense.modules.opnsense._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.search.return_value = {"rows": [], "total": 0}
        mock_client.call.return_value = {"result": "ok"}
        mock_get_client.return_value = mock_client

        func = getattr(mod, "unbound_settings_search_host_alias")
        _ = func(search_phrase="www", row_count=1)
        assert mock_client.call.called or mock_client.search.called


def test_generic_api():
    mod, _ = _setup_generic()
    assert hasattr(mod, "call")
    assert hasattr(mod, "search")
    assert hasattr(mod, "get")
    assert hasattr(mod, "add")
    assert hasattr(mod, "list_api_modules")
    assert hasattr(mod, "spec")


def test_list_modules_full():
    mod, _ = _setup_generic()
    mods = mod.list_api_modules()
    assert len(mods) >= 6
    assert "unbound" in mods
    assert "bind" in mods
    assert "acmeclient" in mods
