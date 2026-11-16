"""
Offline unit tests for the iperf plugin API rework (upstream 26.7.3 -> 26.7.9).

Upstream change summary (verified against the plugins clones at both tags):

* A new ``Api/ClientController`` appeared. The iperf *client* is brand new in
  26.7.9 and gained ``set``/``searchJobs``/``start``/``stop``/``remove``/``view``.
* The existing ``Api/InstanceController`` kept ``set`` but lost the old socket
  based ``query`` action and gained ``searchJobs``/``start``/``stop``/``remove``/
  ``view`` (server jobs).
* ``Api/ServiceController`` was **deleted** (not refactored into the base class).
  Its ``restart``/``start``/``status``/``stop`` daemon-lifecycle endpoints are
  gone from the API surface entirely.

These tests assert that the extension's spec-strict client and state layer
reflect that reality: new job actions dispatch to the correct endpoint paths,
removed service actions raise ``FileNotFoundError``, and a state-level
reconfigure lookup for iperf degrades gracefully instead of crashing.
"""

from unittest.mock import MagicMock

import pytest

from saltext.opnsense.utils.api_spec import has_action, list_controllers
from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig

_HOST = "fw-01.example.com"


def _client():
    cfg = OPNsenseClientConfig(host=_HOST, api_key="a", api_secret="b", verify_ssl=False)
    return OPNsenseClient(cfg)


# New client/instance job actions resolve to the correct endpoint paths.
_NEW_JOB_ACTIONS = [
    ("iperf", "client", "set", None),
    ("iperf", "client", "searchJobs", None),
    ("iperf", "client", "start", "job-uuid"),
    ("iperf", "client", "stop", "job-uuid"),
    ("iperf", "client", "remove", "job-uuid"),
    ("iperf", "client", "view", "job-uuid"),
    ("iperf", "instance", "set", None),
    ("iperf", "instance", "searchJobs", None),
    ("iperf", "instance", "start", "job-uuid"),
    ("iperf", "instance", "stop", "job-uuid"),
    ("iperf", "instance", "remove", "job-uuid"),
    ("iperf", "instance", "view", "job-uuid"),
]


@pytest.mark.parametrize(("module", "controller", "action", "uuid"), _NEW_JOB_ACTIONS)
def test_url_for_new_job_actions(module, controller, action, uuid):
    url = _client().url_for(module, controller, action, uuid)
    expected = f"/{module}/{controller}/{action}"
    if uuid:
        expected += f"/{uuid}"
    assert url.endswith(expected)


@pytest.mark.parametrize(("module", "controller", "action", "uuid"), _NEW_JOB_ACTIONS)
def test_call_dispatches_new_job_actions(module, controller, action, uuid, monkeypatch):
    captured = {}

    def spy_request(method, module, controller, action, uuid=None, data=None, params=None):
        captured.update(
            method=method, module=module, controller=controller, action=action, uuid=uuid
        )
        return {"status": "ok"}

    client = _client()
    monkeypatch.setattr(client, "request", spy_request)
    res = client.call(module, controller, action, uuid=uuid, data={}, method="POST")
    assert res == {"status": "ok"}
    assert captured["method"] == "POST"
    assert captured["module"] == module
    assert captured["controller"] == controller
    assert captured["action"] == action
    assert captured["uuid"] == uuid


@pytest.mark.parametrize(("module", "controller", "action", "uuid"), _NEW_JOB_ACTIONS)
def test_has_action_membership_new_job_actions(module, controller, action, uuid):
    assert has_action(module, controller, action), f"{module}/{controller}/{action}"


# Removed service actions are gone (not served via a base class).
_REMOVED_SERVICE_ACTIONS = ["start", "stop", "restart", "status"]


@pytest.mark.parametrize("action", _REMOVED_SERVICE_ACTIONS)
def test_service_action_absent_from_spec(action):
    assert not has_action("iperf", "service", action)
    assert "service" not in list_controllers("iperf")


@pytest.mark.parametrize("action", _REMOVED_SERVICE_ACTIONS)
def test_service_action_call_raises_file_not_found(action):
    with pytest.raises(FileNotFoundError, match=f"unknown iperf/service/{action}"):
        _client().call("iperf", "service", action, data={}, method="POST")


@pytest.mark.parametrize("action", _REMOVED_SERVICE_ACTIONS)
def test_service_action_helper_raises_file_not_found(action):
    with pytest.raises(FileNotFoundError):
        _client().service_action("iperf", "service", action)


def test_instance_query_gone_but_set_retained():
    # Instance lost the old socket-based `query`; `set` is retained.
    assert not has_action("iperf", "instance", "query")
    assert has_action("iperf", "instance", "set")


# State-level reconfigure lookup for iperf degrades gracefully.
def test_infer_reconfigure_iperf_falls_back_without_service():
    import importlib

    mod = importlib.import_module("saltext.opnsense.states.opnsense")
    mod.__opts__ = {"test": False}
    mod.__salt__ = {}
    rc_instance = mod._infer_reconfigure("iperf", "instance", None)
    assert rc_instance == {"module": "iperf", "controller": "instance", "action": "reconfigure"}
    rc_client = mod._infer_reconfigure("iperf", "client", None)
    assert rc_client["controller"] == "client"
    assert rc_client["action"] == "reconfigure"


def test_verify_reconfigure_iperf_degrades_no_crash():
    import importlib

    mod = importlib.import_module("saltext.opnsense.states.opnsense")
    mod.__opts__ = {"test": False}

    def raising_reconfigure(module, controller, action):
        raise FileNotFoundError(f"unknown {module}/{controller}/{action} – run make bump")

    mod.__salt__ = {"opnsense.reconfigure": raising_reconfigure}
    ok, err = mod._verify_reconfigure("iperf", "instance", "reconfigure")
    assert ok is False
    assert "unknown iperf/instance/reconfigure" in err


def test_item_present_iperf_reconfigure_missing_endpoint_no_crash():
    import importlib

    mod = importlib.import_module("saltext.opnsense.states.opnsense")
    mod.__opts__ = {"test": False}

    def raising_reconfigure(module, controller, action):
        raise FileNotFoundError(f"unknown {module}/{controller}/{action} – run make bump")

    mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.add": MagicMock(return_value={"uuid": "new-job"}),
        "opnsense.reconfigure": raising_reconfigure,
    }
    # Should not raise; the missing reconfigure endpoint degrades to result:False.
    ret = mod.item_present(
        name="iperf-job",
        module="iperf",
        controller="instance",
        type="instance",
        data={"interface": "lan", "port": "5001"},
        match={"interface": "lan"},
        reconfigure=True,
    )
    assert ret["result"] is False
    assert "reconfigure" in ret["comment"].lower()
    assert "unknown iperf/instance/reconfigure" in ret["comment"]
