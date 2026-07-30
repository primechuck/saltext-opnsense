from unittest.mock import MagicMock


def test_state_present_already():
    from saltext.opnsense.states import opnsense as state_mod

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": MagicMock(
            return_value={
                "rows": [{"uuid": "1", "hostname": "www", "domain": "example.com", "enabled": "1"}]
            }
        ),
    }

    result = state_mod.item_present(
        name="www.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={"hostname": "www", "domain": "example.com", "enabled": "1"},
        match={"hostname": "www", "domain": "example.com"},
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
        name="old.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        match={"hostname": "old", "domain": "example.com"},
    )
    assert result["result"] is True
    assert "already absent" in result["comment"]


def test_is_uuid_helper():
    from saltext.opnsense.states import opnsense as state_mod

    assert state_mod._is_uuid("550e8400-e29b-41d4-a716-446655440000") is True
    assert state_mod._is_uuid("not-a-uuid") is False
    assert state_mod._is_uuid("192.0.2.0/24") is False
    assert state_mod._is_uuid("") is False
    assert state_mod._is_uuid(None) is False


def _make_search_mock():
    def _search(module, controller, typ, search_phrase="", row_count=-1, **kwargs):
        if module == "unbound" and typ == "host_override":
            return {
                "rows": [
                    {"uuid": "host-uuid-1111", "hostname": "cluster", "domain": "example.com"},
                    {"uuid": "host-uuid-2222", "hostname": "www", "domain": "example.com"},
                ]
            }
        if module == "kea" and typ == "subnet":
            return {
                "rows": [
                    {"uuid": "subnet-uuid-aaa", "subnet": "192.0.2.0/24", "description": "mgmt"},
                    {"uuid": "subnet-uuid-bbb", "subnet": "172.18.50.0/24", "description": "iot"},
                ]
            }
        if module == "acmeclient" and controller == "accounts" and typ == "account":
            return {
                "rows": [
                    {"uuid": "account-uuid-prod", "name": "letsencrypt-prod"},
                    {"uuid": "account-uuid-staging", "name": "letsencrypt-staging"},
                ]
            }
        if module == "acmeclient" and controller == "validations" and typ == "validation":
            return {
                "rows": [
                    {"uuid": "valid-uuid-cf", "name": "cf-dns01"},
                ]
            }
        if module == "bind" and typ == "primary_domain":
            return {
                "rows": [
                    {"uuid": "zone-uuid-example", "domainname": "example.com"},
                ]
            }
        return {"rows": []}

    return MagicMock(side_effect=_search)


def test_auto_resolve_host_dict():
    from saltext.opnsense.states import opnsense as state_mod

    search_mock = _make_search_mock()
    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": MagicMock(return_value={"result": "added"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.item_present(
        name="git.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={
            "hostname": "git",
            "domain": "example.com",
            "host": {"hostname": "cluster", "domain": "example.com"},
            "enabled": "1",
        },
        match={"hostname": "git", "domain": "example.com"},
    )
    assert result["result"] is True
    add_call = state_mod.__salt__["opnsense.add"].call_args
    assert add_call is not None
    args, _ = add_call
    payload = (
        args[3]
        if len(args) > 3
        else add_call[1].get("data")
        if isinstance(add_call[1], dict)
        else None
    )
    flat = payload.get("alias") if isinstance(payload, dict) and "alias" in payload else payload
    assert flat is not None
    assert flat.get("host") == "host-uuid-1111"


def test_auto_resolve_subnet_cidr():
    from saltext.opnsense.states import opnsense as state_mod

    def search_side_effect(module, controller, typ, search_phrase="", row_count=-1, **kwargs):
        if module == "kea" and typ == "subnet":
            if search_phrase == "192.0.2.0/24":
                return {"rows": [{"uuid": "subnet-uuid-aaa", "subnet": "192.0.2.0/24"}]}
            if search_phrase == "":
                return {"rows": [{"uuid": "subnet-uuid-aaa", "subnet": "192.0.2.0/24"}]}
            return {"rows": []}
        if module == "kea" and typ == "reservation":
            return {"rows": []}
        return (
            _make_search_mock().side_effect(
                module, controller, typ, search_phrase, row_count, **kwargs
            )
            if False
            else {"rows": []}
        )

    wrapped = MagicMock(side_effect=search_side_effect)

    def dispatch(module, controller, typ, search_phrase="", row_count=-1, **kwargs):
        if typ == "reservation":
            return {"rows": []}
        return search_side_effect(module, controller, typ, search_phrase, row_count, **kwargs)

    wrapped.side_effect = dispatch

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": wrapped,
        "opnsense.add": MagicMock(return_value={"result": "added"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.item_present(
        name="www-192.0.2.30",
        module="kea",
        controller="dhcpv4",
        type="reservation",
        data={
            "subnet": "192.0.2.0/24",
            "ip_address": "192.0.2.30",
            "hw_address": "02:42:ac:11:00:02",
            "hostname": "www",
        },
        match={"hw_address": "02:42:ac:11:00:02"},
    )
    assert result["result"] is True
    add_call = state_mod.__salt__["opnsense.add"].call_args
    assert add_call is not None
    args, _ = add_call
    payload = args[3]
    flat = (
        payload.get("reservation")
        if isinstance(payload, dict) and "reservation" in payload
        else payload
    )
    assert flat.get("subnet") == "subnet-uuid-aaa"


def test_auto_resolve_acme_account_name():
    from saltext.opnsense.states import opnsense as state_mod

    search_mock = _make_search_mock()

    def dispatch(module, controller, typ, search_phrase="", row_count=-1, **kwargs):
        if typ == "certificate":
            return {"rows": []}
        return _make_search_mock().side_effect(
            module, controller, typ, search_phrase, row_count, **kwargs
        )

    search_mock.side_effect = dispatch

    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": MagicMock(return_value={"result": "added"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.item_present(
        name="*.example.com",
        module="acmeclient",
        controller="certificates",
        type="certificate",
        data={
            "name": "*.example.com",
            "account": "letsencrypt-prod",
            "validationMethod": "cf-dns01",
            "enabled": "1",
        },
        match={"name": "*.example.com"},
    )
    assert result["result"] is True
    add_call = state_mod.__salt__["opnsense.add"].call_args
    payload = add_call[0][3]
    flat = (
        payload.get("certificate")
        if isinstance(payload, dict) and "certificate" in payload
        else payload
    )
    assert flat.get("account") == "account-uuid-prod"
    assert flat.get("validationMethod") == "valid-uuid-cf"


def test_auto_resolve_preserves_uuid():
    from saltext.opnsense.states import opnsense as state_mod

    existing_uuid = "550e8400-e29b-41d4-a716-446655440000"
    search_mock = MagicMock(return_value={"rows": []})
    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": MagicMock(return_value={"result": "added"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.item_present(
        name="keep-uuid",
        module="kea",
        controller="dhcpv4",
        type="reservation",
        data={
            "subnet": existing_uuid,
            "ip_address": "192.0.2.31",
            "hw_address": "aa:bb:cc:dd:ee:ff",
            "hostname": "test",
        },
        match={"hw_address": "aa:bb:cc:dd:ee:ff"},
    )
    assert result["result"] is True
    add_call = state_mod.__salt__["opnsense.add"].call_args
    payload = add_call[0][3]
    flat = (
        payload.get("reservation")
        if isinstance(payload, dict) and "reservation" in payload
        else payload
    )
    assert flat.get("subnet") == existing_uuid
    assert search_mock.call_count == 1


def test_auto_resolve_host_string_dot():
    from saltext.opnsense.states import opnsense as state_mod

    search_mock = _make_search_mock()
    state_mod.__opts__ = {"test": False}
    state_mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.add": MagicMock(return_value={"result": "added"}),
        "opnsense.reconfigure": MagicMock(return_value={}),
    }

    result = state_mod.item_present(
        name="test.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={
            "hostname": "test",
            "domain": "example.com",
            "host": "cluster.example.com",
            "enabled": "1",
        },
        match={"hostname": "test", "domain": "example.com"},
    )
    assert result["result"] is True
    payload = state_mod.__salt__["opnsense.add"].call_args[0][3]
    flat = payload.get("alias") if isinstance(payload, dict) and "alias" in payload else payload
    assert flat.get("host") == "host-uuid-1111"


def test_item_present_idempotency_second_run():
    from saltext.opnsense.states import opnsense as state_mod

    state_mod.__opts__ = {"test": False}
    search_mock = MagicMock(
        return_value={
            "rows": [
                {
                    "uuid": "alias-uuid-9999",
                    "hostname": "www",
                    "domain": "example.com",
                    "enabled": "1",
                    "host": "host-uuid-1111",
                }
            ]
        }
    )
    get_mock = MagicMock(
        return_value={
            "host_alias": {
                "uuid": "alias-uuid-9999",
                "hostname": "www",
                "domain": "example.com",
                "enabled": "1",
                "host": "host-uuid-1111",
            }
        }
    )
    state_mod.__salt__ = {
        "opnsense.search": search_mock,
        "opnsense.get": get_mock,
    }

    result = state_mod.item_present(
        name="www.example.com",
        module="unbound",
        controller="settings",
        type="host_alias",
        data={"hostname": "www", "domain": "example.com", "enabled": True},
        match={"hostname": "www", "domain": "example.com"},
    )
    assert result["result"] is True
    assert result["changes"] == {}
    assert "already present" in result["comment"]


def test_alias_present_idempotency_second_run():
    from saltext.opnsense.states import unbound as unbound_mod

    unbound_mod.__opts__ = {"test": False}

    def search_side_effect(mod, ctrl, typ, **kwargs):
        if typ == "host_override":
            return {
                "rows": [{"uuid": "host-uuid-1111", "hostname": "cluster", "domain": "example.com"}]
            }
        if typ == "host_alias":
            return {
                "rows": [
                    {
                        "uuid": "alias-uuid-9999",
                        "hostname": "www",
                        "domain": "example.com",
                        "enabled": "1",
                        "host": "host-uuid-1111",
                        "description": "managed by salt - www.example.com",
                    }
                ]
            }
        return {"rows": []}

    unbound_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side_effect),
    }

    result = unbound_mod.alias_present(
        name="www.example.com",
        parent="cluster.example.com",
        enabled=True,
    )
    assert result["result"] is True
    assert result["changes"] == {}
    assert "already present" in result["comment"]


def test_record_present_idempotency_second_run():
    from saltext.opnsense.states import bind as bind_mod

    bind_mod.__opts__ = {"test": False}

    def search_side_effect(mod, ctrl, typ, **kwargs):
        if typ == "primary_domain":
            return {"rows": [{"uuid": "zone-uuid-1111", "domainname": "example.com"}]}
        if typ == "record":
            return {
                "rows": [
                    {
                        "uuid": "rec-uuid-8888",
                        "name": "www",
                        "domain": "zone-uuid-1111",
                        "type": "A",
                        "value": "192.168.1.10",
                        "enabled": "1",
                    }
                ]
            }
        return {"rows": []}

    bind_mod.__salt__ = {
        "opnsense.search": MagicMock(side_effect=search_side_effect),
    }

    result = bind_mod.record_present(
        name="www",
        domain="example.com",
        type="A",
        value="192.168.1.10",
        enabled=True,
    )
    assert result["result"] is True
    assert result["changes"] == {}
    assert "already present" in result["comment"]
