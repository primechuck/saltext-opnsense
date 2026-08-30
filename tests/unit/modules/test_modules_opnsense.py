from unittest.mock import MagicMock, patch


def test_module_virtual():
    from saltext.opnsense.modules import opnsense as mod

    assert mod.__virtual__() is True


@patch("saltext.opnsense.modules.opnsense._get_client")
def test_call_direct(mock_get_client):
    from saltext.opnsense.modules import opnsense as mod

    mock_client = MagicMock()
    mock_client.call.return_value = {"rows": []}
    mock_get_client.return_value = mock_client

    mod.__opts__ = {}
    mod.__pillar__ = {}

    result = mod.call("unbound", "settings", "searchHostAlias")
    assert result == {"rows": []}
