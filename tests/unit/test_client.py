import pytest
from unittest.mock import MagicMock, patch

from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig, get_client_from_opts


def test_config_base_url():
    cfg = OPNsenseClientConfig(host="jrbob.bierce.org", api_key="k", api_secret="s", proto="https", verify_ssl=False)
    assert cfg.base_url() == "https://jrbob.bierce.org/api/"


def test_config_from_dict():
    cfg = OPNsenseClientConfig.from_dict({"host": "jrbob", "api_key": "a", "api_secret": "b"})
    assert cfg.host == "jrbob"


def test_url_for():
    cfg = OPNsenseClientConfig(host="jrbob", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    url = client.url_for("unbound", "settings", "searchHostAlias")
    assert url.endswith("/unbound/settings/searchHostAlias")


def test_url_for_uuid():
    cfg = OPNsenseClientConfig(host="jrbob", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    url = client.url_for("unbound", "settings", "delHostAlias", uuid="1234")
    assert url.endswith("/delHostAlias/1234")


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_search(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"rows": [{"uuid": "1", "hostname": "grafana"}], "total": 1}
    mock_resp.text = '{"rows":[]}'
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="jrbob", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    res = client.search("unbound", "settings", "host_alias")
    assert res["total"] == 1
    mock_req.assert_called()


def test_get_client_from_opts():
    opts = {"opnsense": {"host": "jrbob.bierce.org", "api_key": "key", "api_secret": "secret"}}
    client = get_client_from_opts(opts)
    assert client.config.host == "jrbob.bierce.org"
