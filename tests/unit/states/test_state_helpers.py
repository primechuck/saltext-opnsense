"""Minimal tests for generic state after B-1 deletion of wrapper states."""

from unittest.mock import MagicMock


def _make_search_mock():
    def _search(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if module == "unbound" and typ == "host_override":
            return {
                "rows": [{"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"}]
            }
        return {"rows": []}

    return MagicMock(side_effect=_search)


def test_item_present_resolves_parent_generic():
    from saltext.opnsense.states import opnsense as state_mod

    search_mock = _make_search_mock()

    def search_with_alias(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if module == "unbound" and typ == "host_override":
            return {
                "rows": [{"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"}]
            }
        if module == "unbound" and typ == "host_alias":
            return {"rows": []}
        return {"rows": []}

    search_mock.side_effect = search_with_alias
    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": MagicMock(return_value={"result": "saved", "uuid": "new-uuid"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    result = state_mod.item_present(
        name="www.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={
            "hostname": "www",
            "domain": "example.com",
            "host": "cluster.example.com",
            "enabled": "1",
        },
        match={"hostname": "www", "domain": "example.com"},
    )
    assert result["result"] is True


def test_item_present_uuid_parent():
    from saltext.opnsense.states import opnsense as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.add": MagicMock(return_value={"result": "saved"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    result = state_mod.item_present(
        name="www",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={
            "hostname": "www",
            "domain": "example.com",
            "host": "550e8400-e29b-41d4-a716-446655440000",
        },
        match={"hostname": "www", "domain": "example.com"},
    )
    assert result["result"] is True


def test_item_absent_already():
    from saltext.opnsense.states import opnsense as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {"opnsense.search": MagicMock(return_value={"rows": []})}
    result = state_mod.item_absent(
        name="old.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        match={"hostname": "old", "domain": "example.com"},
    )
    assert result["result"] is True
    assert "already absent" in result["comment"]
