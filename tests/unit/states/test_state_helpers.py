from unittest.mock import MagicMock


def _make_search_mock():
    def _search(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if module == "unbound" and typ == "host_override":
            return {"rows": [
                {"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"},
            ]}
        if module == "unbound" and typ == "host_alias":
            if search_phrase == "www":
                return {"rows": []}
            if search_phrase == "":
                return {"rows": []}
            return {"rows": []}
        if module == "bind" and controller == "domain":
            return {"rows": [
                {"uuid": "zone-1", "domainname": "example.com"},
            ]}
        if module == "bind" and controller == "record":
            return {"rows": []}
        return {"rows": []}
    return MagicMock(side_effect=_search)


def test_unbound_alias_present_resolves_parent():
    from saltext.opnsense.states import unbound as state_mod

    search_mock = _make_search_mock()

    def search_with_alias(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if module == "unbound" and typ == "host_override":
            return {"rows": [{"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"}]}
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
    state_mod.__pillar__ = {}

    result = state_mod.alias_present(name="www", parent="cluster.example.com", domain="example.com")
    assert result["result"] is True
    assert "created" in result["comment"]
    add_call = state_mod.__salt__["opnsense.add"].call_args
    payload = add_call[0][3]
    assert payload["alias"]["hostname"] == "www"
    assert payload["alias"]["host"] == "host-uuid-1"


def test_unbound_alias_present_uuid_parent():
    from saltext.opnsense.states import unbound as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.add": MagicMock(return_value={"result": "saved"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    state_mod.__pillar__ = {}

    result = state_mod.alias_present(name="www", parent="550e8400-e29b-41d4-a716-446655440000", domain="example.com")
    assert result["result"] is True
    payload = state_mod.__salt__["opnsense.add"].call_args[0][3]
    assert payload["alias"]["host"] == "550e8400-e29b-41d4-a716-446655440000"


def test_unbound_alias_absent_already():
    from saltext.opnsense.states import unbound as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }

    result = state_mod.alias_absent(name="old", domain="example.com")
    assert result["result"] is True
    assert "already absent" in result["comment"]


def test_unbound_aliases_managed_test_mode():
    from saltext.opnsense.states import unbound as state_mod

    def search_side(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if typ == "host_override":
            return {"rows": [{"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"}]}
        if typ == "host_alias":
            return {"rows": []}
        return {"rows": []}

    state_mod.__opts__ = {"test": True}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.add": MagicMock(),
        "opnsense.set_item": MagicMock(),
        "opnsense.delete": MagicMock(),
        "opnsense.reconfigure": MagicMock(),
    }
    state_mod.__pillar__ = {}

    result = state_mod.aliases_managed(
        name="test",
        parent="cluster.example.com",
        aliases={"example.com": ["www", "git"], "internal.example.com": ["code"]},
        purge={"example.com": ["old-git"]},
    )
    assert result["result"] is None
    assert "would manage" in result["comment"]
    assert "would_add" in result["changes"]
    assert "www.example.com" in result["changes"]["would_add"]


def test_unbound_aliases_managed_actual():
    from saltext.opnsense.states import unbound as state_mod

    def search_side(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if typ == "host_override":
            return {"rows": [{"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"}]}
        if typ == "host_alias":
            return {"rows": []}
        return {"rows": []}

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.add": MagicMock(return_value={"result": "saved"}),
        "opnsense.set_item": MagicMock(return_value={"result": "saved"}),
        "opnsense.delete": MagicMock(return_value={"result": "deleted"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    state_mod.__pillar__ = {}

    result = state_mod.aliases_managed(
        name="test",
        parent="cluster.example.com",
        aliases={"example.com": ["www"]},
        purge={},
        reconfigure=True,
    )
    assert result["result"] is True
    assert "added" in result["comment"] or "managed" in result["comment"]
    assert state_mod.__salt__["opnsense.reconfigure"].call_count == 1


def test_bind_domain_present():
    from saltext.opnsense.states import bind as state_mod

    def search_side(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if controller == "domain":
            return {"rows": []}
        if controller == "record":
            return {"rows": []}
        return {"rows": []}

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.add": MagicMock(return_value={"result": "saved"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.domain_present(name="example.com")
    assert result["result"] is True
    assert "created" in result["comment"]


def test_bind_record_present():
    from saltext.opnsense.states import bind as state_mod

    def search_side(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if controller == "domain":
            return {"rows": [{"uuid": "zone-1", "domainname": "example.com"}]}
        if controller == "record":
            return {"rows": []}
        return {"rows": []}

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.add": MagicMock(return_value={"result": "saved"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.record_present(name="www", domain="example.com", type="A", value="172.18.60.30")
    assert result["result"] is True
    payload = state_mod.__salt__["opnsense.add"].call_args[0][3]
    assert payload["record"]["name"] == "www"
    assert payload["record"]["value"] == "172.18.60.30"


def test_dns_managed_pillar_read():
    from saltext.opnsense.states import dns as state_mod

    def search_side(module, controller, typ, search_phrase="", row_count=-1, **kw):
        if typ == "host_override":
            return {"rows": [{"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"}]}
        if typ == "host_alias":
            return {"rows": []}
        return {"rows": []}

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.add": MagicMock(return_value={"result": "saved"}),
        "opnsense.set_item": MagicMock(return_value={"result": "saved"}),
        "opnsense.delete": MagicMock(return_value={"result": "deleted"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    state_mod.__pillar__ = {
        "opnsense": {
            "cluster_parent": {"hostname": "cluster", "domain": "example.com"},
            "aliases": {"example.com": ["www", "git"], "internal.example.com": ["code"]},
            "purge_aliases": {"example.com": ["old-git"]},
        }
    }

    result = state_mod.managed(name="dns")
    assert result["result"] is True
    assert "www.example.com" in str(result["changes"]) or "added" in result["comment"]


def test_reconfigure_inference():
    from saltext.opnsense.states import bind as b
    from saltext.opnsense.states import dns as d
    from saltext.opnsense.states import unbound as u

    assert u._get_reconfigure(True) == "unbound/service/reconfigure"
    assert u._get_reconfigure(None) == "unbound/service/reconfigure"
    assert u._get_reconfigure(False) is None
    assert u._get_reconfigure("custom/reconf") == "custom/reconf"

    assert b._get_reconfigure(True) == "bind/service/reconfigure"
    assert d._get_reconfigure(True) == "unbound/service/reconfigure"
