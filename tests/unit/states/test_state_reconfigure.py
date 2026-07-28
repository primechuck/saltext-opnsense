from unittest.mock import MagicMock, patch


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
        "opnsense.list_api_controllers": MagicMock(return_value=[]),
        "opnsense.list_api_actions": MagicMock(return_value=[]),
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
    assert rc["controller"] == "service"
    assert rc["action"] == "reconfigure"


def test_infer_reconfigure_kea():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("kea", "dhcpv4", "reservation")
    assert rc["module"] == "kea"
    assert rc["controller"] == "service"
    assert rc["action"] == "reconfigure"


def test_infer_reconfigure_acmeclient():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("acmeclient", "certificates", "certificate")
    assert rc["module"] == "acmeclient"
    assert rc["controller"] == "service"
    assert rc["action"] == "reconfigure"


def test_infer_reconfigure_firewall_alias():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("firewall", "alias", "item")
    assert rc["module"] == "firewall"
    assert rc["controller"] == "alias"
    assert rc["action"] == "reconfigure"


def test_infer_reconfigure_firewall_filter():
    mod = _get_state_mod()
    rc = mod._infer_reconfigure("firewall", "filter", "rule")
    assert rc["module"] == "firewall"
    assert rc["controller"] == "filter_base"
    assert rc["action"] == "apply"


def test_infer_reconfigure_uses_service_controller_detection():
    mod = _get_state_mod()
    with patch.object(mod, "_safe_list_controllers", return_value=["settings", "service", "diagnostics"]):
        with patch.object(mod, "_safe_list_actions", return_value=["reconfigure"]):
            rc = mod._infer_reconfigure("unbound", "settings", "host_alias")
            assert rc == {"module": "unbound", "controller": "service", "action": "reconfigure"}

    with patch.object(mod, "_safe_list_controllers", return_value=["alias", "filter", "filter_base"]):
        rc = mod._infer_reconfigure("firewall", "filter", "rule")
        assert rc["module"] == "firewall"
        assert "filter_base" in rc["controller"]
        assert rc["action"] == "apply"


def test_get_reconfigure_none_and_true_infers():
    mod = _get_state_mod()
    rc_none = mod._get_reconfigure("unbound", "settings", "host_alias", None)
    assert rc_none is not None
    assert rc_none["module"] == "unbound"

    rc_true = mod._get_reconfigure("unbound", "settings", "host_alias", True)
    assert rc_true is not None
    assert rc_true["module"] == "unbound"


def test_get_reconfigure_false_skips():
    mod = _get_state_mod()
    rc = mod._get_reconfigure("unbound", "settings", "host_alias", False)
    assert rc is None


def test_get_reconfigure_string_parses():
    mod = _get_state_mod()
    rc = mod._get_reconfigure("unbound", "settings", "host_alias", "unbound/service/reconfigure")
    assert rc["module"] == "unbound"
    assert rc["controller"] == "service"
    assert rc["action"] == "reconfigure"

    rc2 = mod._get_reconfigure("firewall", "alias", "item", "firewall/alias/reconfigure")
    assert rc2["module"] == "firewall"
    assert rc2["controller"] == "alias"


def test_get_reconfigure_auto_string_infers():
    mod = _get_state_mod()
    rc = mod._get_reconfigure("unbound", "settings", "host_alias", "auto")
    assert rc is not None
    assert rc["module"] == "unbound"


def test_human_diff_host_alias():
    mod = _get_state_mod()
    match = {"hostname": "www", "domain": "example.com"}
    diff = {"host": {"old": "stream", "new": "cluster.example.com"}}
    data = {"hostname": "www", "domain": "example.com", "host": "cluster.example.com"}
    found = {"hostname": "www", "domain": "example.com", "host": "stream"}
    human = mod._human_diff("host_alias", match, diff, data, found=found, module="unbound", controller="settings", name="www.example.com")
    assert human is not None
    assert "www.example.com" in human
    assert "cluster.example.com" in human
    assert "stream" in human


def test_human_diff_bind_record():
    mod = _get_state_mod()
    match = {"name": "pihole", "type": "A"}
    diff = {"value": {"old": "1.2.3.4", "new": "5.6.7.8"}}
    data = {"name": "pihole", "type": "A", "value": "5.6.7.8"}
    found = {"name": "pihole", "type": "A", "value": "1.2.3.4"}
    human = mod._human_diff("record", match, diff, data, found=found, module="bind", controller="record", name="pihole")
    assert human is not None
    assert "pihole" in human
    assert "1.2.3.4" in human
    assert "5.6.7.8" in human
    assert "->" in human


def test_human_diff_firewall_alias():
    mod = _get_state_mod()
    match = {"name": " RFC1918 "}
    diff = {"content": {"old": "10.0.0.0/8", "new": "172.18.0.0/16"}}
    data = {"name": "RFC1918", "content": "172.18.0.0/16"}
    human = mod._human_diff("item", match, diff, data, found={"name": "RFC1918", "content": "10.0.0.0/8"}, module="firewall", controller="alias", name="RFC1918")
    assert human is not None
    assert "10.0.0.0/8" in human or "RFC1918" in human
    assert "172.18.0.0/16" in human


def test_human_diff_create_host_alias():
    mod = _get_state_mod()
    data = {"hostname": "www", "domain": "example.com", "host": "cluster.example.com"}
    human = mod._human_diff("host_alias", {"hostname": "www", "domain": "example.com"}, {}, data, found=None, module="unbound", controller="settings", name="www.example.com")
    assert human is not None
    assert "www.example.com" in human


def test_item_present_auto_reconfigure_called():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}

    def search_side_effect(module, controller, type_name, search_phrase="", row_count=-1, **kwargs):
        if module == "unbound" and type_name == "host_override":
            return {"rows": [{"uuid": "parent-uuid", "hostname": "cluster", "domain": "example.com"}]}
        return {"rows": []}

    search_mock = MagicMock(side_effect=search_side_effect)
    add_mock = MagicMock(return_value={"uuid": "new-uuid"})
    reconf_mock = MagicMock(return_value={})
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": add_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
        "opnsense.list_api_controllers": MagicMock(return_value=["settings", "service"]),
        "opnsense.list_api_actions": MagicMock(return_value=["reconfigure"]),
    }

    res = mod.item_present(
        name="www.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={"hostname": "www", "domain": "example.com", "host": "cluster.example.com", "enabled": "1"},
        match={"hostname": "www", "domain": "example.com"},
        reconfigure=None,
    )
    assert res["result"] is True
    assert reconf_mock.called
    call_args = reconf_mock.call_args[0]
    assert call_args[0] == "unbound"
    assert call_args[1] == "service"


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
    monkeypatch.setattr(mod.socket, "gethostbyname", lambda h: "1.2.3.4")
    res = mod.assert_resolves(name="check", hostname="www.example.com", expected_ip="1.2.3.4")
    assert res["result"] is True
    assert "1.2.3.4" in res["comment"]


def test_assert_resolves_failure_via_socket(monkeypatch):
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.call": MagicMock(side_effect=Exception("no api")),
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }
    monkeypatch.setattr(mod.socket, "gethostbyname", lambda h: "5.6.7.8")
    res = mod.assert_resolves(name="check", hostname="www.example.com", expected_ip="1.2.3.4")
    assert res["result"] is False
    assert "5.6.7.8" in res["comment"]


def test_assert_resolves_via_unbound_localdata():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    call_mock = MagicMock(return_value={"data": "www.example.com 1.2.3.4"})
    mod.__salt__ = {
        "opnsense.call": call_mock,
        "opnsense.search": MagicMock(return_value={"rows": []}),
    }
    res = mod.assert_resolves(name="check", hostname="www.example.com", expected_ip="1.2.3.4")
    assert res["result"] is True
    assert "localData" in res["comment"] or "1.2.3.4" in res["comment"]


def test_preflight_bind_domain_missing():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    mod.__salt__["opnsense.search"] = MagicMock(return_value={"rows": []})
    mod.__salt__["opnsense.call"] = MagicMock(return_value={})
    data = {"name": "pihole", "type": "A", "value": "1.2.3.4", "domain": "missing-uuid"}
    ok, msg = mod._preflight_check("bind", "record", "record", data, match={"name": "pihole"}, found=None, is_create=True)
    assert ok is False
    assert "not found" in msg.lower()


def test_preflight_host_alias_missing_parent():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    # No parent host_override rows
    mod.__salt__["opnsense.search"] = MagicMock(return_value={"rows": []})
    mod.__salt__["opnsense.call"] = MagicMock(return_value={})
    data = {"hostname": "www", "domain": "example.com", "host": "550e8400-e29b-41d4-a716-446655440000"}
    ok, msg = mod._preflight_check("unbound", "settings", "host_alias", data, match={"hostname": "www", "domain": "example.com"}, found=None, is_create=True)
    assert ok is False
    assert "parent" in msg.lower()


def test_item_present_reconfigure_failed_dict_result():
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
    assert "added" in res["changes"]
    assert "Daemon restart failed" in res["comment"] or "failed" in res["comment"]


def test_item_present_update_reconfigure_failed_exception():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    found_item = {"uuid": "uuid-1", "hostname": "test", "domain": "local", "server": "1.1.1.1"}
    search_mock = MagicMock(return_value={"rows": [found_item]})
    set_mock = MagicMock(return_value={"result": "updated"})
    reconf_mock = MagicMock(side_effect=Exception("Network timeout on reconfigure"))
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.set_item": set_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
    }
    res = mod.item_present(
        name="test_host",
        module="unbound",
        controller="settings",
        type="host_override",
        data={"hostname": "test", "domain": "local", "server": "2.2.2.2"},
        match={"hostname": "test", "domain": "local"},
        reconfigure=True,
    )
    assert res["result"] is False
    assert "server" in res["changes"]
    assert "Network timeout on reconfigure" in res["comment"]


def test_item_absent_reconfigure_failed_status_dict():
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
    assert res["changes"]["deleted"] == "uuid-del"
    assert "reconfigure" in res["comment"].lower()


def test_reconfigured_state_failed():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    mod.__salt__ = {
        "opnsense.reconfigure": MagicMock(return_value={"result": "failed", "error": "Config syntax error"}),
    }
    res = mod.reconfigured("reload_unbound", "unbound", "service", "reconfigure")
    assert res["result"] is False
    assert "Config syntax error" in res["comment"] or "failed" in res["comment"]


def test_items_present_reconfigure_failed():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    search_mock = MagicMock(return_value={"rows": []})
    add_mock = MagicMock(return_value={"uuid": "new-uuid"})
    reconf_mock = MagicMock(return_value={"result": "failed", "message": "Service apply failed"})
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": add_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
    }
    items = [{"name": "h1", "data": {"hostname": "h1", "domain": "local"}}]
    res = mod.items_present(
        name="batch_hosts",
        module="unbound",
        controller="settings",
        type="host_override",
        items=items,
        reconfigure=True,
    )
    assert res["result"] is False
    assert "h1" in res["changes"]
    assert "reconfigure failed" in res["comment"]


def test_items_absent_reconfigure_failed():
    mod = _get_state_mod()
    mod.__opts__ = {"test": False}
    found_item = {"uuid": "uuid-1", "hostname": "h1", "domain": "local"}
    search_mock = MagicMock(return_value={"rows": [found_item]})
    del_mock = MagicMock(return_value={"result": "deleted"})
    reconf_mock = MagicMock(return_value={"status": "failed"})
    mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.delete": del_mock,
        "opnsense.reconfigure": reconf_mock,
        "opnsense.call": MagicMock(return_value={}),
    }
    items = [{"name": "h1", "match": {"hostname": "h1", "domain": "local"}}]
    res = mod.items_absent(
        name="batch_hosts_absent",
        module="unbound",
        controller="settings",
        type="host_override",
        items=items,
        reconfigure=True,
    )
    assert res["result"] is False
    assert "h1" in res["changes"]
    assert "reconfigure failed" in res["comment"]


def test_dns_managed_reconfigure_failed():
    import importlib
    dns_mod = importlib.import_module("saltext.opnsense.states.dns")
    dns_mod.__opts__ = {"test": False}
    dns_mod.__pillar__ = {}

    def search_side_effect(module, controller, type_name, search_phrase="", row_count=-1, **kwargs):
        if type_name == "host_override":
            return {"rows": [{"uuid": "parent-uuid", "hostname": "cluster", "domain": "example.com"}]}
        return {"rows": []}

    dns_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side_effect),
        "opnsense.add": MagicMock(return_value={"uuid": "alias-uuid"}),
        "opnsense.reconfigure": MagicMock(return_value={"result": "failed", "message": "DNS reload failed"}),
        "opnsense.call": MagicMock(return_value={}),
    }

    res = dns_mod.managed(
        name="dns_test",
        parent="cluster.example.com",
        aliases={"example.com": ["www"]},
        reconfigure=True,
    )
    assert res["result"] is False
    assert "www.example.com" in res["changes"]
    assert "reconfigure" in res["comment"].lower()
