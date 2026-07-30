import sys
import types

# Mock salt modules if not installed — allows unit tests to run without salt package
# In CI with salt installed, real modules will be used via pytest-salt-factories
try:
    import salt  # noqa
except ImportError:
    salt_mock = types.ModuleType("salt")
    sys.modules["salt"] = salt_mock

    utils_mock = types.ModuleType("salt.utils")
    sys.modules["salt.utils"] = utils_mock

    platform_mock = types.ModuleType("salt.utils.platform")
    platform_mock.is_proxy = lambda: False
    sys.modules["salt.utils.platform"] = platform_mock

    json_mock = types.ModuleType("salt.utils.json")
    sys.modules["salt.utils.json"] = json_mock

    salt_mock.utils = utils_mock
    utils_mock.platform = platform_mock
    utils_mock.json = json_mock


import pytest


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
