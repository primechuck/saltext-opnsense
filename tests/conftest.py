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
