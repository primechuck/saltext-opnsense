import pytest
from unittest.mock import MagicMock, patch


def test_state_present_already():
    from saltext.opnsense.states import opnsense as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": [{"uuid": "1", "hostname": "grafana", "domain": "bierce.org", "enabled": "1"}]}),
    }

    result = state_mod.item_present(
        name="grafana.bierce.org",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={"hostname": "grafana", "domain": "bierce.org", "enabled": "1"},
        match={"hostname": "grafana", "domain": "bierce.org"},
    )
    assert result["result"] is True
    assert "already present" in result["comment"]


def test_state_absent():
    from saltext.opnsense.states import opnsense as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }

    result = state_mod.item_absent(
        name="old.bierce.org",
        module="unbound",
        controller="settings",
        type="host_alias",
        match={"hostname": "old", "domain": "bierce.org"},
    )
    assert result["result"] is True
    assert "already absent" in result["comment"]
