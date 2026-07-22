"""
Integration live test — skipped unless OPNSENSE_LIVE_TEST=1

Requires real jrbob credentials via env:
  OPNSENSE_HOST=jrbob.bierce.org OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... OPNSENSE_LIVE_TEST=1 pytest tests/integration -v

This is intentionally not run in CI. Use for local validation after `salt-proxy` is up.
"""
import os
import pytest

pytestmark = pytest.mark.skipif(os.getenv("OPNSENSE_LIVE_TEST") != "1", reason="live test disabled — set OPNSENSE_LIVE_TEST=1")

try:
    from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig
    HAS_CLIENT = True
except Exception:
    HAS_CLIENT = False

def _client():
    host = os.getenv("OPNSENSE_HOST", "jrbob.bierce.org")
    key = os.getenv("OPNSENSE_API_KEY")
    secret = os.getenv("OPNSENSE_API_SECRET")
    assert key and secret, "OPNSENSE_API_KEY/SECRET required for live test"
    cfg = OPNsenseClientConfig(host=host, api_key=key, api_secret=secret, verify_ssl=False)
    return OPNsenseClient(cfg)

def test_live_search_host_alias():
    if not HAS_CLIENT:
        pytest.skip("client utils not available")
    client = _client()
    res = client.search("unbound", "settings", "host_alias", row_count=5)
    assert "rows" in res

def test_live_ping_via_firmware():
    if not HAS_CLIENT:
        pytest.skip("client utils not available")
    client = _client()
    try:
        res = client.call("core", "firmware", "status", method="GET")
        assert res
    except Exception:
        res = client.call("unbound", "overview", "isEnabled", method="GET")
        assert res is not None
