from unittest.mock import MagicMock


def _get_state_mod():
    import importlib

    mod = importlib.import_module("saltext.opnsense.states.opnsense")
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.call": MagicMock(return_value={}),
        "opnsense.add": MagicMock(return_value={"result": "added"}),
        "opnsense.set_item": MagicMock(return_value={"result": "updated"}),
        "opnsense.delete": MagicMock(return_value={"result": "deleted"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }
    return mod


def test_infer_reconfigure_unbound():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("unbound", "settings", "host_alias")
    assert rc["module"] == "unbound"
    assert rc["controller"] == "service"
    assert rc["action"] == "reconfigure"


def test_infer_reconfigure_bind():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("bind", "record", "record")
    assert rc["module"] == "bind"


def test_infer_reconfigure_kea():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("kea", "dhcpv4", "reservation")
    assert rc["module"] == "kea"


def test_infer_reconfigure_acmeclient():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("acmeclient", "certificates", "certificate")
    assert rc["module"] == "acmeclient"


def test_infer_reconfigure_firewall_alias():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("firewall", "alias", "item")
    assert rc["module"] == "firewall"
    assert rc["controller"] == "alias"


def test_infer_reconfigure_firewall_filter():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("firewall", "filter", "rule")
    assert rc["module"] == "firewall"
    assert "filter_base" in rc["controller"]
    assert rc["action"] == "apply"


def test_get_reconfigure_none_and_true_infers():
    mod = _get_state_mod()
    rc_none = mod._get_reconfigure("unbound", "settings", "host_alias", None)
    assert rc_none is not None
    rc_true = mod._get_reconfigure("unbound", "settings", "host_alias", True)
    assert rc_true is not None


def test_get_reconfigure_false_skips():
    mod = _get_state_mod()
    rc = mod._get_reconfigure("unbound", "settings", "host_alias", False)
    assert rc is None


def test_get_reconfigure_string_parses():
    mod = _get_state_mod()
    rc = mod._get_reconfigure("unbound", "settings", "host_alias", "unbound/service/reconfigure")
    assert rc["module"] == "unbound"
    assert rc["controller"] == "service"


def test_get_reconfigure_auto_string_infers():
    mod = _get_state_mod()
    rc = mod._get_reconfigure("unbound", "settings", "host_alias", "auto")
    assert rc is not None


def test_item_present_auto_reconfigure_called():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}

    def search_side_effect(module, controller, type_name, search_phrase="", row_count=-1, **kwargs):
        if module == "unbound" and type_name == "host_override":
            return {
                "rows": [{"uuid": "parent-uuid", "hostname": "cluster", "domain": "example.com"}]
            }
        return {"rows": []}

    search_mock = MagicMock(side_effect=search_side_effect)
    add_mock = MagicMock(return_value={"uuid": "new-uuid"})
    reconf_mock = MagicMock(return_value={})
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": add_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
    }
    res = mod.item_present(
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
        reconfigure=None,
    )
    assert res["result"] is True
    assert reconf_mock.called


def test_item_present_no_reconfigure_when_false():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.search": MagicMock(return_value={"rows": []}),
        "opnsense.add": MagicMock(return_value={"uuid": "new-uuid"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
        "opnsense.call": MagicMock(return_value={}),
    }
    res = mod.item_present(
        name="www.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={"hostname": "www", "domain": "example.com", "enabled": "1"},
        match={"hostname": "www", "domain": "example.com"},
        reconfigure=False,
    )
    assert res["result"] is True
    assert not mod.__salt__["opnsense.reconfigure"].called


def test_assert_resolves_success_via_socket(monkeypatch):
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.call": MagicMock(side_effect=Exception("no api")),
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }
    monkeypatch.setattr(mod.socket, "gethostbyname", lambda h: "203.0.113.10")
    res = mod.assert_resolves(name="check", hostname="www.example.com", expected_ip="203.0.113.10")
    assert res["result"] is True


def test_assert_resolves_failure_via_socket(monkeypatch):
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.call": MagicMock(side_effect=Exception("no api")),
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }
    monkeypatch.setattr(mod.socket, "gethostbyname", lambda h: "198.51.100.20")
    res = mod.assert_resolves(name="check", hostname="www.example.com", expected_ip="203.0.113.10")
    assert res["result"] is False
    assert "198.51.100.20" in res["comment"]


def test_item_present_reconfigure_failed():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    search_mock = MagicMock(return_value={"rows": []})
    add_mock = MagicMock(return_value={"uuid": "new-uuid"})
    reconf_mock = MagicMock(return_value={"result": "failed", "message": "Daemon restart failed"})
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": add_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
    }
    res = mod.item_present(
        name="test_host",
        module="unbound",
        controller="settings",
        type="host_override",
        data={"hostname": "test", "domain": "local"},
        match={"hostname": "test", "domain": "local"},
        reconfigure=True,
    )
    assert res["result"] is False
    assert "failed" in res["comment"].lower()


def test_item_absent_reconfigure_failed():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    found_item = {"uuid": "uuid-del", "hostname": "old", "domain": "local"}
    search_mock = MagicMock(return_value={"rows": [found_item]})
    del_mock = MagicMock(return_value={"result": "deleted"})
    reconf_mock = MagicMock(return_value={"status": "failed"})
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.delete": del_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
    }
    res = mod.item_absent(
        name="old_host",
        module="unbound",
        controller="settings",
        type="host_override",
        match={"hostname": "old", "domain": "local"},
        reconfigure=True,
    )
    assert res["result"] is False
    assert "reconfigure" in res["comment"].lower()


def test_dns_managed_reconfigure_failed():
    import importlib

    dns_mod = importlib.import_module("saltext.opnsense.states.dns")
    dns_mod.__opts__ = {"test": False}
    dns_mod.__pillar__ = {}

    def search_side_effect(module, controller, type_name, search_phrase="", row_count=-1, **kwargs):
        if type_name == "host_override":
            return {
                "rows": [{"uuid": "parent-uuid", "hostname": "cluster", "domain": "example.com"}]
            }
        return {"rows": []}

    dns_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side_effect),
        "opnsense.add": MagicMock(return_value={"uuid": "alias-uuid"}),
        "opnsense.reconfigure": MagicMock(
            return_value={"result": "failed", "message": "DNS reload failed"}
        ),
        "opnsense.call": MagicMock(return_value={}),
    }
    res = dns_mod.managed(
        name="dns_test",
        parent="cluster.example.com",
        aliases={"example.com": ["www"]},
        reconfigure=True,
    )
    assert res["result"] is False
    assert "reconfigure" in res["comment"].lower()
