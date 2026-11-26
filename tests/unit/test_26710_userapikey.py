"""Offline coverage for the OPNsense 26.7.10 ``auth/userapikey`` registry surface.

The 26.7.9 -> 26.7.10 delta adds a brand-new controller and model under ``auth``:

* controller ``auth/userapikey`` with actions ``search`` / ``get`` / ``set`` / ``del``
  (a plain API-key manager: no CRUD model verbs, no ``reconfigure``).
* model ``auth/ApiKey`` -- a single ``apikey`` grid whose row carries the
  ``username`` / ``key`` / ``created`` / ``descr`` fields.

This checkout's *shipped* registries (``controllers.json`` / ``models.json``) are still
26.7.9 and therefore lack ``userapikey`` / ``ApiKey``.  To lock the 26.7.10 surface we load
the verified scratch clone's 26.7.10 ``controllers.json`` and inject it into
``api_spec`` at runtime (no source edits, no commits).  ``url_for`` and the
``_infer_reconfigure`` behavior-gap check run against the live extension modules directly.

Offline-first: the HTTP layer is mocked and ``api_spec`` / ``url_for`` only touch the
bundled registries -- no socket is ever opened.
"""

from __future__ import annotations

import importlib
import json
import pathlib
from unittest.mock import MagicMock, patch

import pytest

from saltext.opnsense.utils import api_spec
from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig

# The 26.7.10 scratch clones are the source of truth for this surface.
_ROOT = pathlib.Path(__file__).resolve().parents[2]  # .../repos/saltext-opnsense
_CACHE = _ROOT.parent.parent / "cache" / "scratch" / "upstream-diff"
_SPEC_26710 = _CACHE / "spec-26.7.10.json"
_MODELS_26710 = _CACHE / "models-26.7.10.json"

USERAPIKEY_ACTIONS = ("search", "get", "set", "del")
_APIKEY_ROW_FIELDS = ("username", "key", "created", "descr")


def _skip_if_no_scratch():
    if not _SPEC_26710.is_file() or not _MODELS_26710.is_file():
        pytest.skip(f"26.7.10 scratch clones missing under {_CACHE} (do not re-clone)")


def _load_26710(name: pathlib.Path) -> dict:
    return json.loads(name.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
@pytest.fixture
def client():
    cfg = OPNsenseClientConfig(host="fw.example.com", api_key="k", api_secret="s")
    return OPNsenseClient(cfg)


@pytest.fixture
def auth_userapikey_spec(monkeypatch):
    """Inject the verified 26.7.10 controllers.json into ``api_spec`` so the registry
    helpers resolve the newly added ``auth/userapikey`` surface."""
    _skip_if_no_scratch()
    spec = _load_26710(_SPEC_26710)
    monkeypatch.setattr(api_spec, "load_spec", lambda: spec)
    return spec


def _models_26710():
    """The 26.7.10 models registry (extension's shipped ``models.json`` is 26.7.9)."""
    _skip_if_no_scratch()
    data = _load_26710(_MODELS_26710)
    return data["models"]


def _state_module():
    mod = importlib.import_module("saltext.opnsense.states.opnsense")
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.call": MagicMock(return_value={}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    return mod


# --------------------------------------------------------------------------- #
# 1. Registry surface: the 26.7.10 actions resolve through api_spec
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("action", USERAPIKEY_ACTIONS)
def test_userapikey_action_in_registry(action, auth_userapikey_spec):
    assert api_spec.has_action("auth", "userapikey", action) is True
    assert action in api_spec.list_actions("auth", "userapikey")


@pytest.mark.parametrize("action", USERAPIKEY_ACTIONS)
def test_userapikey_url_for_path(client, action):
    """url_for builds exactly ``https://fw.example.com/api/auth/userapikey/<action>``."""
    url = client.url_for("auth", "userapikey", action)
    assert url == f"https://fw.example.com/api/auth/userapikey/{action}"


def test_userapikey_controller_listed(auth_userapikey_spec):
    assert "userapikey" in api_spec.list_controllers("auth")


# --------------------------------------------------------------------------- #
# 2. models.json: the ApiKey model entry exists with its row fields
# --------------------------------------------------------------------------- #
def test_apikey_model_entry_exists():
    models = _models_26710()
    assert "ApiKey" in models["auth"]
    row = models["auth"]["ApiKey"]["apikey"]
    for field in _APIKEY_ROW_FIELDS:
        assert field in row, f"missing field {field!r} in auth/ApiKey model"


def test_apikey_model_field_shape():
    """username/key/created are plain text; descr is the human-facing description field."""
    models = _models_26710()
    row = models["auth"]["ApiKey"]["apikey"]
    for field in ("username", "key", "created"):
        assert row[field]["type"] == "TextField"
    assert row["descr"]["type"] == "DescriptionField"


# --------------------------------------------------------------------------- #
# 3. Live behavior gap: the state's inferred reconfigure path does NOT resolve
# --------------------------------------------------------------------------- #
def test_reconfigure_inference_gap():
    """``auth/userapikey`` has no apply endpoint: inference returns None.

    The 26.7.10 ``userapikey`` controller declares search/get/set/del only;
    set/del persist synchronously (sibling ``auth/user`` applies via
    configdRun, not MVC reconfigure), so the state must skip the apply step.
    Encoded in ``states/opnsense._NO_RECONFIGURE_CONTROLLERS``.
    """
    rc = _state_module()._infer_reconfigure("auth", "userapikey", "apikey")
    assert rc is None
    # the inferred-nothing state: no reconfigure action exists in the registry
    assert api_spec.has_action("auth", "userapikey", "reconfigure") is False


def test_reconfigure_action_not_in_registry(auth_userapikey_spec):
    """Against the real 26.7.10 registry, none of the four legit actions is 'reconfigure'."""
    actions = set(api_spec.list_actions("auth", "userapikey"))
    assert set(USERAPIKEY_ACTIONS) == actions
    assert "reconfigure" not in actions


# --------------------------------------------------------------------------- #
# 4. Transport: the four real actions reach userapikey over the wire (mocked)
# --------------------------------------------------------------------------- #
def _captured_call(client, module, controller, action, method, data=None):
    with patch("saltext.opnsense.utils.opnsense.requests.Session.request") as mock_req:
        resp = MagicMock()
        resp.status_code = 200
        resp.text = "{}"
        resp.json.return_value = {}
        mock_req.return_value = resp
        client.call(module, controller, action, data=data, method=method)
    positional = mock_req.call_args[0]
    return positional[0], positional[1]


@pytest.mark.parametrize("action", USERAPIKEY_ACTIONS)
def test_userapikey_calls_reach_controller(client, action):
    method, url = _captured_call(client, "auth", "userapikey", action, "POST", data={})
    assert method == "POST"
    assert url.endswith(f"/auth/userapikey/{action}")
