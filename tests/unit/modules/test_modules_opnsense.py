import pytest
from unittest.mock import MagicMock, patch


def test_module_virtual():
    from saltext.opnsense.modules import opnsense as mod
    assert mod.__virtual__() == "opnsense"


@patch("saltext.opnsense.modules.opnsense._get_client")
def test_call_direct(mock_get_client):
    from saltext.opnsense.modules import opnsense as mod

    mock_client = MagicMock()
    mock_client.call.return_value = {"rows": []}
    mock_get_client.return_value = mock_client

    mod.__opts__ = {}
    mod.__pillar__ = {}

    with patch("salt.utils.platform.is_proxy", return_value=False):
        result = mod.call("unbound", "settings", "searchHostAlias")
        assert result == {"rows": []}
