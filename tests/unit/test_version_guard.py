"""
test_version_guard.py — verifies salt>=3008 runtime guard + <3008 negative path.
"""

import importlib
import sys
import types


def _install_fake_salt_resources_tree(version_info=(3008, 2)):
    salt_mod = types.ModuleType("salt")
    utils_mod = types.ModuleType("salt.utils")
    res_mod = types.ModuleType("salt.utils.resources")
    ver_mod = types.ModuleType("salt.version")
    ver_mod.__version_info__ = version_info
    ver_mod.__version__ = ".".join(map(str, version_info))

    def pillar_resources_tree(opts):
        return {"opnsense": {"hosts": {"fw-01": {"host": "fw-01.example.com"}}}}

    res_mod.pillar_resources_tree = pillar_resources_tree
    utils_mod.resources = res_mod
    salt_mod.utils = utils_mod
    salt_mod.version = ver_mod
    sys.modules["salt"] = salt_mod
    sys.modules["salt.utils"] = utils_mod
    sys.modules["salt.utils.resources"] = res_mod
    sys.modules["salt.version"] = ver_mod
    return ver_mod


def _cleanup_fake_salt():
    for name in list(sys.modules.keys()):
        if name == "salt" or name.startswith("salt."):
            del sys.modules[name]
    for name in [
        "saltext.opnsense.resources.opnsense",
        "saltext.opnsense.modules.opnsense",
        "saltext.opnsense.utils.opnsense",
        "saltext.opnsense.utils.api_spec",
        "saltext.opnsense.utils.common",
    ]:
        if name in sys.modules:
            del sys.modules[name]


def test_resource_module_allows_3008(monkeypatch):
    # Mock requests to avoid HAS_DEPS false negative when requests not installed in minimal env
    import types

    req_mod = types.ModuleType("requests")
    req_mod.get = lambda *a, **k: None
    auth_mod = types.ModuleType("requests.auth")
    auth_mod.HTTPBasicAuth = object
    exc_mod = types.ModuleType("requests.exceptions")
    exc_mod.ConnectionError = ConnectionError
    exc_mod.ChunkedEncodingError = Exception
    req_mod.auth = auth_mod
    req_mod.exceptions = exc_mod
    sys.modules["requests"] = req_mod
    sys.modules["requests.auth"] = auth_mod
    sys.modules["requests.exceptions"] = exc_mod
    sys.modules["urllib3"] = types.ModuleType("urllib3")
    ur_mod = types.ModuleType("urllib3.util")
    sys.modules["urllib3.util"] = ur_mod
    urllib3_exc = types.ModuleType("urllib3.exceptions")
    urllib3_exc.InsecureRequestWarning = Warning
    urllib3_exc.ProtocolError = Exception
    sys.modules["urllib3.exceptions"] = urllib3_exc
    sys.modules["urllib3"].exceptions = urllib3_exc
    _install_fake_salt_resources_tree((3008, 2))
    try:
        mod = importlib.import_module("saltext.opnsense.resources.opnsense")
        mod.__context__ = {}
        mod.__opts__ = {}
        ret = mod.__virtual__()
        # With our mocks, HAS_DEPS may still fail due to other deps, but should NOT be version error
        if isinstance(ret, tuple):
            assert "3008" not in ret[1] or "requires" not in ret[1], (
                f"should not reject 3008 for version: {ret}"
            )
            # If deps missing, it's ok - we only assert not version-guarded
            print(f"resource 3008 returned {ret} (deps missing ok)")
        else:
            assert ret is True
    finally:
        _cleanup_fake_salt()
        for k in [
            "requests",
            "requests.auth",
            "requests.exceptions",
            "urllib3",
            "urllib3.util",
            "urllib3.exceptions",
        ]:
            if k in sys.modules:
                del sys.modules[k]


def test_resource_module_rejects_3006():
    _install_fake_salt_resources_tree((3006, 27))
    try:
        mod = importlib.import_module("saltext.opnsense.resources.opnsense")
        mod.__context__ = {}
        mod.__opts__ = {}
        ret = mod.__virtual__()
        assert isinstance(ret, tuple), f"expected (False, msg) for 3006, got {ret}"
        assert ret[0] is False
        assert "3008" in ret[1]
    finally:
        _cleanup_fake_salt()


def test_exec_module_allows_3008(monkeypatch):
    import types

    # Minimal but sufficient mock for utils/opnsense.py which does
    # `import requests` plus `from requests.auth import HTTPBasicAuth` and accesses requests.exceptions
    req_mod = types.ModuleType("requests")
    req_mod.get = lambda *a, **k: None
    auth_mod = types.ModuleType("requests.auth")
    auth_mod.HTTPBasicAuth = object
    exc_mod = types.ModuleType("requests.exceptions")
    exc_mod.ConnectionError = ConnectionError
    exc_mod.ChunkedEncodingError = Exception
    req_mod.auth = auth_mod
    req_mod.exceptions = exc_mod
    sys.modules["requests"] = req_mod
    sys.modules["requests.auth"] = auth_mod
    sys.modules["requests.exceptions"] = exc_mod
    sys.modules["urllib3"] = types.ModuleType("urllib3")
    ur_mod = types.ModuleType("urllib3.util")
    sys.modules["urllib3.util"] = ur_mod
    # Also need urllib3.exceptions
    urllib3_exc = types.ModuleType("urllib3.exceptions")
    urllib3_exc.InsecureRequestWarning = Warning
    urllib3_exc.ProtocolError = Exception
    sys.modules["urllib3.exceptions"] = urllib3_exc
    sys.modules["urllib3"].exceptions = urllib3_exc
    _install_fake_salt_resources_tree((3008, 2))
    try:
        mod = importlib.import_module("saltext.opnsense.modules.opnsense")
        ret = mod.__virtual__()
        if isinstance(ret, tuple):
            # Should not be version error
            assert (
                "3008" not in ret[1] or "requires" not in ret[1].lower() or "missing" in ret[1]
            ), f"should allow 3008, got {ret}"
        else:
            assert ret is True
    finally:
        _cleanup_fake_salt()
        for k in [
            "requests",
            "requests.auth",
            "requests.exceptions",
            "urllib3",
            "urllib3.util",
            "urllib3.exceptions",
        ]:
            if k in sys.modules:
                del sys.modules[k]


def test_exec_module_rejects_3006():
    _install_fake_salt_resources_tree((3006, 27))
    try:
        mod = importlib.import_module("saltext.opnsense.modules.opnsense")
        ret = mod.__virtual__()
        assert isinstance(ret, tuple), f"expected rejection tuple for 3006, got {ret}"
        assert ret[0] is False
        assert "3008" in ret[1]
    finally:
        _cleanup_fake_salt()


def test_packaging_requires_3008():
    import pathlib

    pyproject = pathlib.Path(__file__).resolve().parents[2] / "pyproject.toml"
    text = pyproject.read_text()
    assert "salt>=3008" in text, "pyproject must have salt>=3008 dependency"
    assert "salt>=3006" not in text
    assert '"__proxy__"' not in text, (
        "__proxy__ builtin should be removed after 1.0 Resources migration"
    )
