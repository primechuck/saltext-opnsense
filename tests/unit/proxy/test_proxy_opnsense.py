import pytest
from unittest.mock import MagicMock, patch


def test_proxy_virtual():
    from saltext.opnsense.proxy import opnsense as proxy_mod
    assert proxy_mod.__virtual__() == "opnsense"


def test_proxy_init():
    from saltext.opnsense.proxy import opnsense as proxy_mod

    opts = {"proxy": {"host": "jrbob.bierce.org", "api_key": "k", "api_secret": "s", "verify_ssl": False}}
    with patch("saltext.opnsense.proxy.opnsense.get_client_from_opts") as mock_get:
        mock_client = MagicMock()
        mock_client.config.host = "jrbob.bierce.org"
        mock_get.return_value = mock_client
        proxy_mod.DETAILS.clear()
        result = proxy_mod.init(opts)
        assert result is True
        assert proxy_mod.DETAILS["initialized"] is True
        proxy_mod.shutdown()


def test_proxy_ping():
    from saltext.opnsense.proxy import opnsense as proxy_mod

    mock_client = MagicMock()
    mock_client.call.return_value = {"status": "ok"}
    proxy_mod.DETAILS["client"] = mock_client
    assert proxy_mod.ping() is True
    proxy_mod.DETAILS.clear()
