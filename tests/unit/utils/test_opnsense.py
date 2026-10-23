"""Unit tests for saltext.opnsense.utils.opnsense OPNsenseClientConfig."""

import pytest

from saltext.opnsense.utils.opnsense import OPNsenseClientConfig


def test_client_config_rejects_unresolved_salt_slots():
    """Ensure that passing unrendered ``__slot__`` expressions raises a helpful error."""
    bad_config = {
        "host": "opnsense.example.com",
        "api_key": "__slot__:salt:vault.read(secret/opnsense/api_key)",
        "api_secret": "[REDACTED]",
    }
    with pytest.raises(ValueError, match="detected unresolved Salt slot syntax"):
        OPNsenseClientConfig.from_dict(bad_config)


def test_client_config_rejects_unhandled_sdb_uris():
    """Unhandled ``sdb://`` URIs must be rejected with an actionable error."""
    bad_config = {
        "host": "opnsense.example.com",
        "api_key": "sdb://vault/api_key",
        "api_secret": "real_secret",
    }
    with pytest.raises(ValueError, match="detected unhandled SDB URI"):
        OPNsenseClientConfig.from_dict(bad_config)


def test_client_config_accepts_resolved_values():
    """Concrete (already-resolved) credentials pass through unchanged."""
    good_config = {
        "host": "opnsense.example.com",
        "api_key": "real_api_key",
        "api_secret": "real_api_secret",
    }
    cfg = OPNsenseClientConfig.from_dict(good_config)
    assert cfg.api_key == "real_api_key"
    assert cfg.api_secret == "real_api_secret"
