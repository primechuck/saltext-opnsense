"""
Unit tests for Salt Resource type opnsense – API-only, 2 SRN default.
Tests discover/init/grains/ping/shutdown and delegation via resource_funcs.
"""

import types

import pytest


def _make_mock_client(host="fw-01.example.com"):
    class MockSession:
        def close(self):
            pass

    class MockClient:
        def __init__(self, config=None):
            self.config = config or types.SimpleNamespace(host=host, proto="https")
            self.session = MockSession()

        def search(self, module, controller, type_name=None, row_count=-1, **kw):
            return {"total": 1, "rows": [{"uuid": "test-uuid"}]}

        def call(self, module, controller, action, data=None, method=None, uuid=None):
            if module == "core" and controller == "firmware" and action == "status":
                return {"product_version": "25.7.11"}
            return {}

        def get(self, *a, **kw):
            return {}

        def add(self, *a, **kw):
            return {"result": "ok"}

        def set(self, *a, **kw):
            return {"result": "ok"}

        def delete(self, *a, **kw):
            return {"result": "ok"}

        def toggle(self, *a, **kw):
            return {"result": "ok"}

        def reconfigure(self, *a, **kw):
            return {"status": "ok"}

    return MockClient()


@pytest.fixture
def resource_module(monkeypatch):
    # Import connection module
    import sys

    # Ensure salt.utils.resources can be mocked
    # Create dummy salt.utils.resources module with pillar_resources_tree
    salt_mod = types.ModuleType("salt")
    utils_mod = types.ModuleType("salt.utils")
    res_mod = types.ModuleType("salt.utils.resources")

    def pillar_resources_tree(opts):
        # Return structure matching pillar.example resources fleet
        return {
            "opnsense": {
                "hosts": {
                    "fw-01": {"host": "fw-01.example.com", "api_key": "k1", "api_secret": "s1"},
                    "fw-02": {"host": "fw-02.example.com", "api_key": "k2", "api_secret": "s2"},
                }
            }
        }

    res_mod.pillar_resources_tree = pillar_resources_tree
    utils_mod.resources = res_mod
    salt_mod.utils = utils_mod
    sys.modules["salt"] = salt_mod
    sys.modules["salt.utils"] = utils_mod
    sys.modules["salt.utils.resources"] = res_mod

    # Now import our resource module fresh
    import importlib

    # Clear any cached version
    mod_name = "saltext.opnsense.resources.opnsense"
    if mod_name in sys.modules:
        del sys.modules[mod_name]

    mod = importlib.import_module(mod_name)
    # Setup dunder globals expected by Salt loader
    mod.__context__ = {}
    mod.__opts__ = {"pillar": {"resources": pillar_resources_tree({})}}
    mod.__pillar__ = {"resources": pillar_resources_tree({})}

    yield mod

    # cleanup
    del sys.modules[mod_name]
    if "salt.utils.resources" in sys.modules:
        del sys.modules["salt.utils.resources"]
    if "salt.utils" in sys.modules:
        del sys.modules["salt.utils"]
    if "salt" in sys.modules:
        del sys.modules["salt"]


def test_discover(resource_module):
    mod = resource_module
    opts = {"pillar": {"resources": {"opnsense": {"hosts": {"fw-01": {}}}}}}
    # Our mock pillar_resources_tree ignores opts and returns 2 hosts
    ids = mod.discover(opts)
    assert set(ids) == {"fw-01", "fw-02"}


def test_init_and_initialized(resource_module):
    mod = resource_module
    mod.__context__ = {}
    opts = {}
    assert mod.init(opts) is True
    assert mod.initialized() is True
    assert "fw-01" in mod._ctx()["hosts"]
    assert "fw-02" in mod._ctx()["hosts"]


def test_connect_caches(resource_module, monkeypatch):
    mod = resource_module
    mod.__context__ = {}
    mod.init({})

    # Mock OPNsenseClientConfig.from_dict and OPNsenseClient to avoid real HTTP
    class FakeCfg:
        def __init__(self):
            self.host = "fw-01.example.com"
            self.proto = "https"

        @classmethod
        def from_dict(cls, d):
            obj = cls()
            obj.host = d.get("host", "fw-01.example.com")
            obj.proto = d.get("proto", "https")
            return obj

    monkeypatch.setattr(mod, "OPNsenseClientConfig", FakeCfg)
    mock_client = _make_mock_client()
    monkeypatch.setattr(mod, "OPNsenseClient", lambda cfg: mock_client)

    c1 = mod._connect("fw-01")
    c2 = mod._connect("fw-01")
    assert c1 is c2
    assert "fw-01" in mod._ctx()["conns"]


def test_grains(resource_module, monkeypatch):
    mod = resource_module
    mod.__context__ = {}
    mod.init({})
    mock_client = _make_mock_client()
    monkeypatch.setattr(mod, "_connect", lambda rid: mock_client)
    mod.__resource__ = {"id": "fw-01", "type": "opnsense"}
    grains = mod.grains()
    assert grains["resource_id"] == "fw-01"
    assert grains["opnsense_host"] == "fw-01.example.com"
    assert "opnsense_version" in grains
    assert grains["opnsense_version"] == "25.7.11"


def test_ping(resource_module, monkeypatch):
    mod = resource_module
    mod.__context__ = {}
    mod.init({})
    mock_client = _make_mock_client()
    monkeypatch.setattr(mod, "_connect", lambda rid: mock_client)
    mod.__resource__ = {"id": "fw-01", "type": "opnsense"}
    assert mod.ping() is True


def test_shutdown_closes(resource_module):
    mod = resource_module
    mod.__context__ = {}
    mod.init({})
    # add fake conn with close tracking
    closed = []

    class FakeSess:
        def close(self):
            closed.append(True)

    class FakeClient:
        session = FakeSess()

    mod._ctx()["conns"] = {"fw-01": FakeClient()}
    assert mod.shutdown({}) is True
    assert mod._ctx() == {} or "opnsense" not in mod._ctx()
    # Actually shutdown pops CONTEXT_KEY, we check context of module's _ctx? After shutdown _ctx should be empty because pop
    assert closed


def test_virtual():
    import importlib
    import sys

    # Mock deps present
    mod_name = "saltext.opnsense.resources.opnsense"
    if mod_name in sys.modules:
        del sys.modules[mod_name]
    mod = importlib.import_module(mod_name)
    assert mod.__virtual__() is True
    # Simulate missing deps
    mod.HAS_DEPS = False
    mod.HAS_DEPS_ERROR = "missing"
    ret = mod.__virtual__()
    assert ret[0] is False


def test_execution_override_delegation(monkeypatch):
    # Simulate __resource_funcs__ delegation used by resources/opnsense/modules/opnsense.py
    import importlib
    import sys

    # Setup resource_funcs mock
    called = {}

    def fake_call(module, controller, action, uuid=None, data=None, method=None):
        called["call"] = (module, controller, action)
        return {"result": "ok"}

    def fake_search(
        module,
        controller,
        type_name=None,
        search_phrase="",
        row_count=-1,
        current=1,
        sort=None,
        extra=None,
        **kw,
    ):
        called["search"] = True
        return {"total": 0, "rows": []}

    def fake_ping():
        called["ping"] = True
        return True

    sys.modules.pop("saltext.opnsense.resources.opnsense.modules.opnsense", None)
    mod = importlib.import_module("saltext.opnsense.resources.opnsense.modules.opnsense")
    # inject dunder
    mod.__resource_funcs__ = {
        "opnsense.call": fake_call,
        "opnsense.search": fake_search,
        "opnsense.ping": fake_ping,
        "opnsense.get": lambda *a, **k: {},
        "opnsense.add": lambda *a, **k: {},
        "opnsense.set_item": lambda *a, **k: {},
        "opnsense.delete": lambda *a, **k: {},
        "opnsense.toggle": lambda *a, **k: {},
        "opnsense.reconfigure": lambda *a, **k: {},
    }
    mod.__resource__ = {"id": "fw-01", "type": "opnsense"}

    assert mod.ping() is True
    assert "ping" in called
    mod.search("firewall", "alias", "item")
    assert "search" in called
    mod.call("core", "firmware", "status")
    assert "call" in called
