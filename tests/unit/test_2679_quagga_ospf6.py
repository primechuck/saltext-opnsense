"""Regression tests for the FRR quagga OSPF6 *Network -> *Area rename (26.7.3 -> 26.7.9).

Upstream (plugin ``net/frr``) renamed all six Area/Network controller actions and the model
container ``networks``/``network`` -> ``areas``/``area`` (field ``ipaddr`` -> ``id``) in 26.7.9.
These tests lock the extension's dynamic registry (``controllers.json`` via ``api_spec``) and the
model map (``models.json``) to the 26.7.9 shape so a future regression that reintroduces an
``*Network`` action fails loudly.

Offline-first: the HTTP layer is mocked and no socket is opened; ``url_for`` / ``api_spec`` only
touch the bundled registries on disk.
"""

from __future__ import annotations

import json
from importlib.resources import files
from unittest.mock import MagicMock, patch

import pytest

from saltext.opnsense.utils import api_spec
from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig

# The FRR plugin exposes its OSPFv3 controller under the "quagga" module in controllers.json.
MODULE = "quagga"
CONTROLLER = "ospf6settings"

# The six verbs that became ``*Area`` in 26.7.9 (as the controller exposes them).
AREA_ACTIONS = [
    "searchArea",
    "getArea",
    "addArea",
    "delArea",
    "setArea",
    "toggleArea",
]

# Their ``*Network`` ancestors in 26.7.3 -- now absent from the registry.
NETWORK_ACTIONS = [
    "searchNetwork",
    "getNetwork",
    "addNetwork",
    "delNetwork",
    "setNetwork",
    "toggleNetwork",
]


@pytest.fixture
def client():
    cfg = OPNsenseClientConfig(host="fw.example.com", api_key="k", api_secret="s")
    return OPNsenseClient(cfg)


@pytest.fixture(scope="module")
def ospf6_items():
    """The OSPF6 model entries from models.json (renamed to expose the Area relation)."""
    data = json.loads(files("saltext.opnsense.utils").joinpath("models.json").read_text())
    return data["models"]["quagga"]["OSPF6"]


# --- 1. Dynamic map / opnsense.call endpoint construction ----------------------------


@pytest.mark.parametrize("action", AREA_ACTIONS)
def test_area_action_present_in_dynamic_map(action):
    assert api_spec.has_action(MODULE, CONTROLLER, action) is True
    assert action in api_spec.list_actions(MODULE, CONTROLLER)


@pytest.mark.parametrize("action", NETWORK_ACTIONS)
def test_network_action_absent_from_dynamic_map(action):
    assert api_spec.has_action(MODULE, CONTROLLER, action) is False


@pytest.mark.parametrize("action", AREA_ACTIONS)
def test_url_for_area_endpoint(client, action):
    url = client.url_for(MODULE, CONTROLLER, action)
    assert url == f"https://fw.example.com/api/{MODULE}/{CONTROLLER}/{action}"


@pytest.mark.parametrize("action", AREA_ACTIONS)
def test_call_area_endpoint_hits_url(client, action):
    """opnsense.call forwards to client.call -> request -> url_for; the known Area action
    must be spec-strict accepted and reach the HTTP layer at the correct path."""
    with patch("saltext.opnsense.utils.opnsense.requests.Session.request") as mock_req:
        resp = MagicMock()
        resp.status_code = 200
        resp.text = "{}"
        resp.json.return_value = {}
        mock_req.return_value = resp

        client.call(MODULE, CONTROLLER, action, data={}, method="POST")

    assert mock_req.call_args is not None
    positional = mock_req.call_args[0]
    url = positional[1]  # session.request(method, url, ...)
    assert url.endswith(f"/{MODULE}/{CONTROLLER}/{action}")
    mock_req.assert_called_once()


@pytest.mark.parametrize("action", NETWORK_ACTIONS)
def test_call_network_action_is_spec_strict_missing(client, action):
    with patch("saltext.opnsense.utils.opnsense.requests.Session.request") as mock_req:
        with pytest.raises(FileNotFoundError):
            client.call(MODULE, CONTROLLER, action, data={}, method="POST")
    # Spec-strict: a removed action never reaches the transport.
    mock_req.assert_not_called()


# --- 2. models.json: Area relation ---------------------------------------------------


def test_ospf6_model_no_network_key(ospf6_items):
    assert "network" not in ospf6_items


def test_ospf6_area_field_present(ospf6_items):
    assert "area" in ospf6_items
    # The old per-network ``ipaddr`` field was renamed to ``id`` (dotted area ID).
    assert "id" in ospf6_items["area"]
    assert ospf6_items["area"]["id"]["type"] == "NetworkField"
    assert "Please enter area ID in dotted" in ospf6_items["area"]["id"]["ValidationMessage"]


def test_ospf6_interface_area_relation(ospf6_items):
    # An interface's ``area`` field is now a relation to the areas.array, not a free text field.
    area_field = ospf6_items["interface"]["area"]
    assert area_field["type"] == "ModelRelationField"
    rel = area_field["relation"]
    assert rel["items"] == "areas.area"
    assert rel["key"] == "areas"
    assert rel["source"] == "OPNsense.quagga.ospf6"
