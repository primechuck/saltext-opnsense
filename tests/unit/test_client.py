import logging
from unittest.mock import MagicMock, patch

import pytest

from saltext.opnsense.utils.opnsense import (
    OPNsenseAPIError,
    OPNsenseClient,
    OPNsenseClientConfig,
    OPNsenseValidationError,
    _mask_sensitive_data,
    get_client_from_opts,
)


def test_config_base_url():
    cfg = OPNsenseClientConfig(host="opnsense.example.com", api_key="k", api_secret="s", proto="https", verify_ssl=False)
    assert cfg.base_url() == "https://opnsense.example.com/api/"


def test_config_from_dict():
    cfg = OPNsenseClientConfig.from_dict({"host": "opnsense-router", "api_key": "a", "api_secret": "b"})
    assert cfg.host == "opnsense-router"


def test_url_for():
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    url = client.url_for("unbound", "settings", "searchHostAlias")
    assert url.endswith("/unbound/settings/searchHostAlias")


def test_url_for_uuid():
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    url = client.url_for("unbound", "settings", "delHostAlias", uuid="1234")
    assert url.endswith("/delHostAlias/1234")


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_search(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"rows": [{"uuid": "1", "hostname": "www"}], "total": 1}
    mock_resp.text = '{"rows":[]}'
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    res = client.search("unbound", "settings", "host_alias")
    assert res["total"] == 1
    mock_req.assert_called()


def test_get_client_from_opts():
    opts = {"opnsense": {"host": "opnsense.example.com", "api_key": "key", "api_secret": "secret"}}
    client = get_client_from_opts(opts)
    assert client.config.host == "opnsense.example.com"


def test_config_enable_fallback():
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    assert cfg.enable_fallback is False

    cfg2 = OPNsenseClientConfig.from_dict({"host": "r", "api_key": "a", "api_secret": "b", "enable_fallback": True})
    assert cfg2.enable_fallback is True

    cfg3 = OPNsenseClientConfig.from_dict({"host": "r", "api_key": "a", "api_secret": "b", "fallback_mode": True})
    assert cfg3.enable_fallback is True


def test_resolve_via_spec_authoritative_no_fallback():
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    resolved = client._resolve_via_spec("unbound", "settings", "search", "host_alias")
    assert resolved == ["searchHostAlias"]


def test_resolve_via_spec_authoritative_with_fallback():
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b", enable_fallback=True)
    client = OPNsenseClient(cfg)
    resolved = client._resolve_via_spec("unbound", "settings", "search", "host_alias")
    assert "searchHostAlias" in resolved
    assert len(resolved) >= 1


def test_resolve_via_spec_unlisted_controller():
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    resolved = client._resolve_via_spec("custom_module", "custom_ctrl", "search", "item")
    assert "search_item" in resolved
    assert "searchItem" in resolved


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_call_with_fallback_suppresses_404_probing_when_authoritative(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 404
    mock_resp.text = "Endpoint not found"
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b", enable_fallback=False)
    client = OPNsenseClient(cfg)

    from saltext.opnsense.utils.opnsense import OPNsenseAPIError
    with pytest.raises(OPNsenseAPIError) as exc_info:
        client._call_with_fallback("unbound", "settings", ["searchHostAlias", "searchHostOverride"])

    assert "404" in str(exc_info.value) or "not found" in str(exc_info.value).lower()
    # Ensure only 1 request was attempted, suppressing speculative probing on 404
    assert mock_req.call_count == 1


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_call_with_fallback_allows_404_probing_when_fallback_enabled(mock_req):
    mock_resp_404 = MagicMock()
    mock_resp_404.status_code = 404
    mock_resp_404.text = "Endpoint not found"

    mock_resp_200 = MagicMock()
    mock_resp_200.status_code = 200
    mock_resp_200.json.return_value = {"rows": []}
    mock_resp_200.text = '{"rows":[]}'

    mock_req.side_effect = [mock_resp_404, mock_resp_200]

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b", enable_fallback=True)
    client = OPNsenseClient(cfg)

    res = client._call_with_fallback("unbound", "settings", ["searchHostAlias", "searchHostOverride"])
    assert res == {"rows": []}
    assert mock_req.call_count == 2


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_call_with_fallback_allows_404_probing_when_spec_unlisted(mock_req):
    mock_resp_404 = MagicMock()
    mock_resp_404.status_code = 404
    mock_resp_404.text = "Endpoint not found"

    mock_resp_200 = MagicMock()
    mock_resp_200.status_code = 200
    mock_resp_200.json.return_value = {"result": "ok"}
    mock_resp_200.text = '{"result":"ok"}'

    mock_req.side_effect = [mock_resp_404, mock_resp_200]

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b", enable_fallback=False)
    client = OPNsenseClient(cfg)

    res = client._call_with_fallback("custom_module", "custom_ctrl", ["search_item", "searchItem"])
    assert res == {"result": "ok"}
    assert mock_req.call_count == 2


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_validation_error_result_failed(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"result": "failed", "validations": {"hostname": "Field is required"}}'
    mock_resp.json.return_value = {"result": "failed", "validations": {"hostname": "Field is required"}}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseValidationError) as excinfo:
        client.request("POST", "unbound", "settings", "addHostAlias")
    assert excinfo.value.validations == {"hostname": "Field is required"}


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_validation_error_validations_key(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"validations": {"domain": "Invalid domain name"}}'
    mock_resp.json.return_value = {"validations": {"domain": "Invalid domain name"}}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseValidationError) as excinfo:
        client.request("POST", "unbound", "settings", "addHostAlias")
    assert excinfo.value.validations == {"domain": "Invalid domain name"}


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_error_shape_status_error(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"status": "error", "message": "Failed to update record"}'
    mock_resp.json.return_value = {"status": "error", "message": "Failed to update record"}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseAPIError) as excinfo:
        client.request("POST", "unbound", "settings", "setHostAlias")
    assert "Failed to update record" in str(excinfo.value)


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_error_shape_status_failed(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"status": "failed", "error": "Internal server issue"}'
    mock_resp.json.return_value = {"status": "failed", "error": "Internal server issue"}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseAPIError) as excinfo:
        client.request("POST", "unbound", "settings", "setHostAlias")
    assert "Internal server issue" in str(excinfo.value)


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_error_shape_error_message(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"errorMessage": "Authentication failed for user"}'
    mock_resp.json.return_value = {"errorMessage": "Authentication failed for user"}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseAPIError) as excinfo:
        client.request("POST", "unbound", "settings", "getHostAlias")
    assert "Authentication failed for user" in str(excinfo.value)


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_error_shape_error_key_string(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"error": "Permission denied"}'
    mock_resp.json.return_value = {"error": "Permission denied"}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseAPIError) as excinfo:
        client.request("POST", "unbound", "settings", "getHostAlias")
    assert "Permission denied" in str(excinfo.value)


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_error_shape_error_key_dict(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"error": {"code": 500, "detail": "Backend process crashed"}}'
    mock_resp.json.return_value = {"error": {"code": 500, "detail": "Backend process crashed"}}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseAPIError) as excinfo:
        client.request("POST", "unbound", "settings", "getHostAlias")
    assert "Backend process crashed" in str(excinfo.value)


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_error_shape_result_error(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"result": "error", "message": "Module unavailable"}'
    mock_resp.json.return_value = {"result": "error", "message": "Module unavailable"}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseAPIError) as excinfo:
        client.request("POST", "unbound", "settings", "getHostAlias")
    assert "Module unavailable" in str(excinfo.value)


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_success_with_falsy_error(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"result": "saved", "error": null, "errorMessage": ""}'
    mock_resp.json.return_value = {"result": "saved", "error": None, "errorMessage": ""}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    res = client.request("POST", "unbound", "settings", "setHostAlias")
    assert res["result"] == "saved"


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_http_error_with_json_validation(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 400
    mock_resp.text = '{"result": "failed", "validations": {"ip": "Invalid IP address"}}'
    mock_resp.json.return_value = {"result": "failed", "validations": {"ip": "Invalid IP address"}}
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(OPNsenseValidationError) as excinfo:
        client.request("POST", "unbound", "settings", "addHostAlias")
    assert excinfo.value.validations == {"ip": "Invalid IP address"}


@pytest.mark.parametrize(
    "key",
    ["api_secret", "password", "key", "token", "psk", "secret", "private_key"],
)
def test_mask_sensitive_data_individual_keys(key):
    data = {key: "super_secret_value", "name": "normal_value"}
    masked = _mask_sensitive_data(data)
    assert masked[key] == "***"
    assert masked["name"] == "normal_value"
    assert data[key] == "super_secret_value"


def test_mask_sensitive_data_case_insensitivity():
    data = {
        "API_SECRET": "secret1",
        "Password": "secret2",
        "Token": "secret3",
        "PSK": "secret4",
    }
    masked = _mask_sensitive_data(data)
    assert masked["API_SECRET"] == "***"
    assert masked["Password"] == "***"
    assert masked["Token"] == "***"
    assert masked["PSK"] == "***"


def test_mask_sensitive_data_nested_structures():
    data = {
        "user": "admin",
        "credentials": {
            "password": "my_password",
            "tokens": [
                {"token": "token1", "type": "auth"},
                {"token": "token2", "type": "refresh"},
            ],
        },
        "keys": ({"private_key": "rsa_key"},),
    }
    masked = _mask_sensitive_data(data)
    assert masked["user"] == "admin"
    assert masked["credentials"]["password"] == "***"
    assert masked["credentials"]["tokens"][0]["token"] == "***"
    assert masked["credentials"]["tokens"][0]["type"] == "auth"
    assert masked["credentials"]["tokens"][1]["token"] == "***"
    assert masked["credentials"]["tokens"][1]["type"] == "refresh"
    assert masked["keys"][0]["private_key"] == "***"


def test_mask_sensitive_data_primitives():
    assert _mask_sensitive_data("plain_string") == "plain_string"
    assert _mask_sensitive_data(12345) == 12345
    assert _mask_sensitive_data(None) is None
    assert _mask_sensitive_data(True) is True


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_logging_masks_sensitive_data(mock_req, caplog):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"result": "saved"}
    mock_resp.text = '{"result":"saved"}'
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)

    sensitive_payload = {
        "username": "opnuser",
        "password": "my_top_secret_password",
        "api_secret": "super_secret_api_key",
        "psk": "my_pre_shared_key",
    }

    with caplog.at_level(logging.DEBUG):
        res = client.request("POST", "sys", "auth", "save", data=sensitive_payload)

    assert res == {"result": "saved"}

    logged_text = caplog.text
    assert "***" in logged_text
    assert "my_top_secret_password" not in logged_text
    assert "super_secret_api_key" not in logged_text
    assert "my_pre_shared_key" not in logged_text
    assert "opnuser" in logged_text

    mock_req.assert_called_once()
    _, kwargs = mock_req.call_args
    assert "my_top_secret_password" in kwargs["data"]
    assert "super_secret_api_key" in kwargs["data"]
