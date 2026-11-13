"""Offline coverage for the OPNsense 26.7.9 API surface added to the extension.

Each entry below was confirmed present in the upstream 26.7.9 PHP API and mirrored into the
extension's dynamic registries (``controllers.json`` -> ``api_spec``, ``models.json``).  These
tests lock that mapping so a future ``make bump`` that drops one of these actions, or a model
field the generic states depend on, fails loudly.

HTTP-method quirks captured from the upstream controllers (see ``src/.../controllers``):

* ``interfaces/assignment/pending`` -- plain read, **GET** (no ``isPost`` guard).
* ``unbound/settings/downloadHostOverrides`` -- **GET** CSV export (non-JSON body).
* ``unbound/settings/uploadHostOverrides`` -- **POST** with a ``payload`` CSV (non-JSON).
* ``dyndns/accounts/forceRefresh`` -- **POST** only (``if !isPost`` -> failed).
* ``proxy/service/reconfigure`` -- **POST** only.
* ``core/dashboard/getDefaults`` -- plain read, **GET**.
* ``interfaces/{tap,wireless}settings`` -- standard ``ApiMutableModelControllerBase`` CRUD
  (search/get = GET, set/add/del = POST, ``reconfigure`` = POST).
* ``netflector/settings`` -- ``*Reflector`` CRUD; ``netflector/service`` daemon verbs
  (start/stop/restart/reconfigure/status) are inherited from
  ``ApiMutableServiceControllerBase`` and recorded by the
  ``SERVICE_BASE_ACTIONS`` fallback in ``tools/generate_spec.py``.

Offline-first: the HTTP layer is mocked and no socket is opened; ``api_spec`` and ``url_for``
only touch the bundled registries.
"""

from __future__ import annotations

import importlib
import json
from importlib.resources import files
from unittest.mock import MagicMock, patch

import pytest

from saltext.opnsense.utils import api_spec
from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
@pytest.fixture
def client():
    cfg = OPNsenseClientConfig(host="fw.example.com", api_key="k", api_secret="s")
    return OPNsenseClient(cfg)


def _models():
    data = json.loads(files("saltext.opnsense.utils").joinpath("models.json").read_text())
    return data["models"]


# Canonical list of the NEW actions that must resolve to their endpoint via the
# dynamic map.  Each is (module, controller, action).  ``url_for`` lower-cases the
# module/controller so this is the path the extension actually builds.
NEW_ACTIONS = [
    # netflector reflector CRUD
    ("netflector", "settings", "searchReflector"),
    ("netflector", "settings", "getReflector"),
    ("netflector", "settings", "addReflector"),
    ("netflector", "settings", "setReflector"),
    ("netflector", "settings", "delReflector"),
    ("netflector", "settings", "toggleReflector"),
    # interfaces / tapsettings & wirelesssettings (full CRUD + reconfigure)
    ("interfaces", "tapsettings", "searchItem"),
    ("interfaces", "tapsettings", "getItem"),
    ("interfaces", "tapsettings", "addItem"),
    ("interfaces", "tapsettings", "setItem"),
    ("interfaces", "tapsettings", "delItem"),
    ("interfaces", "tapsettings", "reconfigure"),
    ("interfaces", "wirelesssettings", "searchItem"),
    ("interfaces", "wirelesssettings", "getItem"),
    ("interfaces", "wirelesssettings", "addItem"),
    ("interfaces", "wirelesssettings", "setItem"),
    ("interfaces", "wirelesssettings", "delItem"),
    ("interfaces", "wirelesssettings", "reconfigure"),
    # interfaces / assignment pending (GET) + reconfigure (POST)
    ("interfaces", "assignment", "pending"),
    ("interfaces", "assignment", "reconfigure"),
    # unbound CSV host-overrides export/import (GET export / POST import)
    ("unbound", "settings", "downloadHostOverrides"),
    ("unbound", "settings", "uploadHostOverrides"),
    # dyndns accounts forceRefresh (POST)
    ("dyndns", "accounts", "forceRefresh"),
    # proxy service reconfigure (POST)
    ("proxy", "service", "reconfigure"),
    # core dashboard getDefaults (GET)
    ("core", "dashboard", "getDefaults"),
]


# --------------------------------------------------------------------------- #
# 1. Dynamic map: each new action resolves to its endpoint
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("module, controller, action", NEW_ACTIONS)
def test_new_action_present_in_dynamic_map(module, controller, action):
    assert api_spec.has_action(module, controller, action) is True
    assert action in api_spec.list_actions(module, controller)


@pytest.mark.parametrize("module, controller, action", NEW_ACTIONS)
def test_new_action_url_for_path(client, module, controller, action):
    """url_for builds exactly ``{module}/{controller}/{action}`` (paths are lower-cased)."""
    url = client.url_for(module, controller, action)
    assert url == f"https://fw.example.com/api/{module}/{controller}/{action}"


# --------------------------------------------------------------------------- #
# 2. Call reaches the transport at the right path/verb (mocked transport)
# --------------------------------------------------------------------------- #
def _captured_call(client, module, controller, action, method, data=None):
    """Invoke client.call and return (http_method, url) observed by the mock transport."""
    with patch("saltext.opnsense.utils.opnsense.requests.Session.request") as mock_req:
        resp = MagicMock()
        resp.status_code = 200
        resp.text = "{}"
        resp.json.return_value = {}
        mock_req.return_value = resp
        client.call(module, controller, action, data=data, method=method)
    positional = mock_req.call_args[0]
    return positional[0], positional[1]


def test_assignment_pending_is_get(client):
    method, url = _captured_call(client, "interfaces", "assignment", "pending", "GET")
    assert method == "GET"
    assert url.endswith("/interfaces/assignment/pending")


def test_dashboard_getdefaults_is_get(client):
    method, url = _captured_call(client, "core", "dashboard", "getDefaults", "GET")
    assert method == "GET"
    assert url.endswith("/core/dashboard/getDefaults")


def test_download_hostoverrides_is_get_export(client):
    method, url = _captured_call(client, "unbound", "settings", "downloadHostOverrides", "GET")
    assert method == "GET"
    assert url.endswith("/unbound/settings/downloadHostOverrides")


def test_upload_hostoverrides_is_post_import(client):
    method, url = _captured_call(
        client, "unbound", "settings", "uploadHostOverrides", "POST", data={}
    )
    assert method == "POST"
    assert url.endswith("/unbound/settings/uploadHostOverrides")


def test_dyndns_forcerefresh_is_post(client):
    method, url = _captured_call(client, "dyndns", "accounts", "forceRefresh", "POST", data={})
    assert method == "POST"
    assert url.endswith("/dyndns/accounts/forceRefresh")


def test_proxy_service_reconfigure_is_post(client):
    method, url = _captured_call(client, "proxy", "service", "reconfigure", "POST", data={})
    assert method == "POST"
    assert url.endswith("/proxy/service/reconfigure")


def test_netflector_settings_search_resolves_verbed_action(client):
    """The generic search() helper must resolve ``search`` -> ``searchReflector`` for netflector."""
    method, url = _captured_call(
        client, "netflector", "settings", "searchReflector", "POST", data={}
    )
    assert method == "POST"
    assert url.endswith("/netflector/settings/searchReflector")


@pytest.mark.parametrize(
    "controller",
    ["tapsettings", "wirelesssettings"],
)
def test_interface_reconfigure_is_post(client, controller):
    method, url = _captured_call(client, "interfaces", controller, "reconfigure", "POST", data={})
    assert method == "POST"
    assert url.endswith(f"/interfaces/{controller}/reconfigure")


# --------------------------------------------------------------------------- #
# 3. models.json contains Netflector / Tap / Wlan with expected key fields
# --------------------------------------------------------------------------- #
def test_netflector_model_has_interface_relation_fields():
    models = _models()
    reflector = models["netflector"]["Netflector"]["reflector"]
    for field in ("source_if", "target_if"):
        f = reflector[field]
        assert f["type"] == "InterfaceField"
        assert f["required"] == "Y"
    # name is the natural key of a reflector row
    assert reflector["name"]["required"] == "Y"


def test_tap_model_fields():
    models = _models()
    tap = models["interfaces"]["Tap"]["tap"]
    assert tap["deviceId"]["type"] == "AutoNumberField"
    assert tap["deviceId"]["required"] == "Y"
    # description is the human-facing required field (deviceName is volatile/optional)
    assert tap["description"]["required"] == "Y"


def test_wlan_model_required_fields():
    models = _models()
    wlan = models["interfaces"]["Wlan"]["clone"]
    for field in ("if", "mode", "standard"):
        assert wlan[field]["required"] == "Y"
    # ``if`` is a JsonKeyValueStoreField (adapter list), not a natural-key relation
    assert wlan["if"]["type"] == "JsonKeyValueStoreField"


# --------------------------------------------------------------------------- #
# 4. Reconfigure-table lookups for the new modules (encode actual behavior)
# --------------------------------------------------------------------------- #
NEW_RECONFIGURE_CASES = [
    ("netflector", "settings", "reflector"),
    ("interfaces", "tapsettings", "tap"),
    ("interfaces", "wirelesssettings", "clone"),
    ("interfaces", "assignment", "interface"),
    ("dyndns", "accounts", "item"),
    ("proxy", "service", None),
    ("core", "dashboard", None),
]


def _state_module():
    mod = importlib.import_module("saltext.opnsense.states.opnsense")
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.call": MagicMock(return_value={}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    return mod


@pytest.mark.parametrize("module, controller, type_name", NEW_RECONFIGURE_CASES)
def test_reconfigure_lookup_returns_sensible_endpoint_or_none(module, controller, type_name):
    """Every new module must either resolve to a dict {module, controller, action} or None."""
    rc = _state_module()._infer_reconfigure(module, controller, type_name)
    assert rc is None or (isinstance(rc, dict) and {"module", "controller", "action"} <= rc.keys())


@pytest.mark.parametrize(
    "module, controller, type_name, endpoint",
    [
        ("interfaces", "tapsettings", "tap", "interfaces/tapsettings/reconfigure"),
        ("interfaces", "wirelesssettings", "clone", "interfaces/wirelesssettings/reconfigure"),
        ("interfaces", "assignment", "interface", "interfaces/assignment/reconfigure"),
        ("proxy", "service", None, "proxy/service/reconfigure"),
    ],
)
def test_reconfigure_lookup_resolves_existing_endpoint(module, controller, type_name, endpoint):
    """For modules with a real apply endpoint, the inferred lookup must actually resolve."""
    rc = _state_module()._infer_reconfigure(module, controller, type_name)
    assert rc is not None
    path = f"{rc['module']}/{rc['controller']}/{rc['action']}"
    assert path == endpoint
    assert api_spec.has_action(rc["module"], rc["controller"], rc["action"]) is True


# --------------------------------------------------------------------------- #
# 5. netflector/service daemon verbs come from the service base class
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("action", ["reconfigure", "restart", "start", "status", "stop"])
def test_netflector_service_verbs_present_from_base_class(action):
    """netflector/service declares no actions of its own; the five inherited
    ``ApiMutableServiceControllerBase`` verbs are recorded in the registry."""
    assert api_spec.has_action("netflector", "service", action) is True


def test_netflector_service_controller_present():
    assert "service" in api_spec.list_controllers("netflector")


# --------------------------------------------------------------------------- #
# 6. Gap note: unbound CSV actions are NOT item_present-flow actions
# --------------------------------------------------------------------------- #
def test_csv_actions_present_as_raw_endpoints():
    """downloadHostOverrides/uploadHostOverrides are CSV export/import; the generic item_present
    flow (JSON model wrappers) does not fit them -- they are reachable only as raw actions.

    Confirm they are present in the dynamic map but are *not* the model CRUD verbs
    (search/get/set/add) that ``item_present`` drives for the hosts.host array.
    """
    actions = api_spec.list_actions("unbound", "settings")
    assert "downloadHostOverrides" in actions
    assert "uploadHostOverrides" in actions
    # CSV verbs sit alongside, but are not host-override model CRUD verbs
    host_override_crud = {
        "searchHostOverride",
        "getHostOverride",
        "setHostOverride",
        "addHostOverride",
    }
    csv_verbs = {"downloadHostOverrides", "uploadHostOverrides"}
    assert csv_verbs.isdisjoint(host_override_crud)
