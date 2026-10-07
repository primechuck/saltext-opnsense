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
    cfg = OPNsenseClientConfig(
        host="opnsense.example.com", api_key="k", api_secret="s", proto="https", verify_ssl=False
    )
    assert cfg.base_url() == "https://opnsense.example.com/api/"


def test_config_from_dict():
    cfg = OPNsenseClientConfig.from_dict(
        {"host": "fw-01.example.com", "api_key": "a", "api_secret": "b"}
    )
    assert cfg.host == "fw-01.example.com"


def test_url_for():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    url = client.url_for("unbound", "settings", "searchHostAlias")
    assert url.endswith("/unbound/settings/searchHostAlias")


def test_url_for_uuid():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    res = client.search("unbound", "settings", "host_alias")
    assert res["total"] == 1
    mock_req.assert_called()


def test_get_client_from_opts():
    opts = {"opnsense": {"host": "opnsense.example.com", "api_key": "key", "api_secret": "secret"}}
    client = get_client_from_opts(opts)
    assert client.config.host == "opnsense.example.com"


def test_config_no_fallback():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    assert not hasattr(cfg, "enable_fallback")
    cfg2 = OPNsenseClientConfig.from_dict(
        {"host": "r", "api_key": "a", "api_secret": "b", "enable_fallback": True}
    )
    # enable_fallback should be ignored – spec-strict, no fallback field
    assert not hasattr(cfg2, "enable_fallback")


def test_resolve_action_spec_strict():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    # unbound settings host_alias should resolve to searchHostAlias via spec
    action = client._resolve_action("unbound", "settings", "search", "host_alias")
    assert action == "searchHostAlias"


def test_resolve_action_unknown_type_fails():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(FileNotFoundError, match="unknown"):
        client._resolve_action("unbound", "settings", "search", "nonexistent_xyz_type")


def test_call_spec_strict_success():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with patch.object(client, "request", return_value={"rows": []}) as mock_req:
        # call known action via spec should succeed
        res = client.call("unbound", "settings", "searchHostAlias", data={}, method="POST")
        assert res == {"rows": []}
        mock_req.assert_called_once()


def test_call_spec_strict_unknown_raises():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(FileNotFoundError, match="unknown unbound/settings/unknownAction"):
        client.call("unbound", "settings", "unknownAction", data={}, method="POST")


def test_call_spec_strict_unknown_with_suffix_raises():
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    with pytest.raises(FileNotFoundError):
        client.call("unbound", "settings", "unknownAction/0", data={}, method="POST")


@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_request_validation_error_result_failed(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = '{"result": "failed", "validations": {"hostname": "Field is required"}}'
    mock_resp.json.return_value = {
        "result": "failed",
        "validations": {"hostname": "Field is required"},
    }
    mock_req.return_value = mock_resp

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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

    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
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
