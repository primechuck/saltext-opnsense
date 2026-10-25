import logging
import os
import sys
import types

# Reset root logger like template
logging.root.setLevel(logging.WARNING)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
    try:
        handler.close()
    except Exception:
        pass

# Mock salt modules if not installed — allows unit tests to run without salt package
try:
    import salt  # noqa
except ImportError:
    salt_mock = types.ModuleType("salt")
    sys.modules["salt"] = salt_mock
    utils_mock = types.ModuleType("salt.utils")
    sys.modules["salt.utils"] = utils_mock
    json_mock = types.ModuleType("salt.utils.json")
    sys.modules["salt.utils.json"] = json_mock
    salt_mock.utils = utils_mock
    utils_mock.json = json_mock

import pytest

try:
    from saltext.opnsense import PACKAGE_ROOT
except ImportError:
    from pathlib import Path

    PACKAGE_ROOT = Path(__file__).resolve().parent.parent / "src" / "saltext" / "opnsense"


@pytest.fixture
def opnsense_opts():
    return {
        "opnsense": {
            "host": "opnsense.example.com",
            "api_key": "testkey",
            "api_secret": "testsecret",
            "proto": "https",
            "verify_ssl": False,
            "timeout": 5,
        }
    }


# Template-compatible fixtures — needed for pytest-salt-factories and future org CI
@pytest.fixture(scope="session")
def salt_factories_config():  # pragma: no cover
    return {
        "code_dir": str(PACKAGE_ROOT),
        "inject_sitecustomize": "COVERAGE_PROCESS_START" in os.environ,
        "start_timeout": 120 if os.environ.get("CI") else 60,
    }


@pytest.fixture
def minion_opts(tmp_path):  # pragma: no cover
    try:
        import salt.config
    except ImportError:
        pytest.skip("salt not installed")
    root_dir = tmp_path / "minion"
    opts = salt.config.DEFAULT_MINION_OPTS.copy()
    opts["__role"] = "minion"
    opts["root_dir"] = str(root_dir)
    for name in ("cachedir", "pki_dir", "sock_dir", "conf_dir"):
        dirpath = root_dir / name
        dirpath.mkdir(parents=True)
        opts[name] = str(dirpath)
    opts["log_file"] = "logs/minion.log"
    opts["conf_file"] = os.path.join(opts["conf_dir"], "minion")
    return opts


# ---------------------------------------------------------------------------
# Offline-first guard: unit tests must never reach a real OPNsense appliance.
# Any HTTP send through ``requests`` or any non-loopback ``socket.connect`` fails the test
# immediately. ``pytest.fail`` raises a BaseException subclass, so the broad ``except
# Exception`` blocks in the states/modules cannot swallow it and hide a leaking test.
# Mock ``requests.Session.request`` or ``__salt__`` instead. Live tests opt out with
# ``@pytest.mark.allow_network`` (``tests/integration`` is opted out automatically).
# ---------------------------------------------------------------------------
import ipaddress  # noqa: E402
import socket  # noqa: E402

try:
    import requests.adapters
except ImportError:  # pragma: no cover - requests is a hard dependency of the package
    requests = None

_OFFLINE_MSG = (
    "Live network access is blocked in unit tests ({what}). Mock the transport "
    "(patch 'requests.Session.request' or provide a fake __salt__), or mark an opt-in live "
    "test with @pytest.mark.allow_network."
)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "allow_network: disable the offline-first socket/HTTP guard (live tests only)"
    )


def pytest_collection_modifyitems(items):
    for item in items:
        if "integration" in item.path.parts:
            item.add_marker(pytest.mark.allow_network)


def _is_local_address(address) -> bool:
    if isinstance(address, (str, bytes, bytearray)):  # AF_UNIX path
        return True
    host = address[0] if address else ""
    if isinstance(host, (bytes, bytearray)):
        host = host.decode("ascii", "ignore")
    if host in ("", "localhost"):
        return True
    try:
        ip = ipaddress.ip_address(host.split("%", 1)[0])
    except ValueError:
        return False
    return ip.is_loopback or ip.is_unspecified


@pytest.fixture(autouse=True)
def _offline_first_guard(request, monkeypatch):
    if request.node.get_closest_marker("allow_network"):
        return

    if requests is not None:

        def _blocked_send(self, req, *args, **kwargs):
            pytest.fail(_OFFLINE_MSG.format(what=f"{req.method} {req.url}"), pytrace=False)

        monkeypatch.setattr(requests.adapters.HTTPAdapter, "send", _blocked_send)

    def _guard(real):
        def guarded(self, address, *args, **kwargs):
            if not _is_local_address(address):
                pytest.fail(_OFFLINE_MSG.format(what=f"connect {address!r}"), pytrace=False)
            return real(self, address, *args, **kwargs)

        return guarded

    monkeypatch.setattr(socket.socket, "connect", _guard(socket.socket.connect))
    monkeypatch.setattr(socket.socket, "connect_ex", _guard(socket.socket.connect_ex))
