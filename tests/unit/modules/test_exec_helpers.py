from unittest.mock import MagicMock


def _mock_salt_with_rows(host_overrides=None, aliases=None, bind_domains=None, bind_records=None):
    host_overrides = host_overrides or []
    aliases = aliases or []

    def search_side(module, controller, type_name, search_phrase="", row_count=-1, **kw):
        if module == "unbound" and type_name == "host_override":
            return {"rows": host_overrides}
        if module == "unbound" and type_name == "host_alias":
            return {"rows": aliases}
        if module == "bind" and controller == "domain":
            return {"rows": bind_domains or []}
        if module == "bind" and controller == "record":
            return {"rows": bind_records or []}
        if module == "kea" and type_name == "subnet":
            return {"rows": [{"uuid": "subnet-aaa", "subnet": "172.18.60.0/24"}]}
        if module == "kea" and type_name == "reservation":
            return {"rows": [{"uuid": "res-1", "hostname": "www", "ip_address": "172.18.60.30", "hw_address": "aa:bb:cc:dd:ee:ff", "subnet": "subnet-aaa"}]}
        if module == "acmeclient":
            if type_name == "account":
                return {"rows": [{"uuid": "acc-1", "name": "letsencrypt-prod"}]}
            if type_name == "validation":
                return {"rows": [{"uuid": "val-1", "name": "cf-dns01"}]}
            if type_name == "certificate":
                return {"rows": [{"uuid": "cert-1", "name": "*.example.com", "status": "valid"}]}
            if type_name == "action":
                return {"rows": [{"uuid": "act-1", "name": "restart-haproxy"}]}
        return {"rows": []}

    return {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.call": MagicMock(return_value={"rows": []}),
    }


def test_unbound_list_host_overrides():
    from saltext.opnsense.modules import unbound as mod

    mock_salt = _mock_salt_with_rows(
        host_overrides=[
            {"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com", "server": "172.18.60.10", "enabled": "1"},
            {"uuid": "host-uuid-2", "hostname": "www", "domain": "example.com", "server": "172.18.60.30", "enabled": "1"},
        ]
    )
    mod.__salt__ = mock_salt
    result = mod.list_host_overrides()
    assert "cluster.example.com" in result
    assert result["cluster.example.com"]["ip"] == "172.18.60.10"
    assert result["cluster.example.com"]["uuid"] == "host-uuid-1"


def test_unbound_list_aliases_simple():
    from saltext.opnsense.modules import unbound as mod

    mock_salt = _mock_salt_with_rows(
        host_overrides=[
            {"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com", "enabled": "1"},
        ],
        aliases=[
            {"uuid": "alias-1", "hostname": "www", "domain": "example.com", "host": "host-uuid-1", "enabled": "1", "description": "test"},
            {"uuid": "alias-2", "hostname": "git", "domain": "example.com", "host": "host-uuid-1", "enabled": "1"},
        ],
    )
    mod.__salt__ = mock_salt
    result = mod.list_aliases()
    assert "www.example.com" in result
    assert result["www.example.com"]["parent"] == "cluster.example.com"
    assert result["www.example.com"]["parent_uuid"] == "host-uuid-1"
    simple = mod.list_aliases_simple()
    assert simple["www.example.com"] == "cluster.example.com"


def test_unbound_resolve_parent():
    from saltext.opnsense.modules import unbound as mod

    mock_salt = _mock_salt_with_rows(
        host_overrides=[
            {"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"},
        ]
    )
    mod.__salt__ = mock_salt
    uuid = mod.resolve_parent("cluster.example.com")
    assert uuid == "host-uuid-1"
    uuid2 = mod.resolve_parent("550e8400-e29b-41d4-a716-446655440000")
    assert uuid2 == "550e8400-e29b-41d4-a716-446655440000"


def test_bind_list_domains():
    from saltext.opnsense.modules import bind as mod

    mock_salt = _mock_salt_with_rows(
        bind_domains=[
            {"uuid": "zone-1", "domainname": "example.com", "enabled": "1"},
            {"uuid": "zone-2", "domainname": "internal.example.com", "enabled": "1"},
        ]
    )
    mod.__salt__ = mock_salt
    result = mod.list_domains()
    assert "example.com" in result
    assert result["example.com"]["uuid"] == "zone-1"


def test_bind_list_records():
    from saltext.opnsense.modules import bind as mod

    mock_salt = _mock_salt_with_rows(
        bind_domains=[
            {"uuid": "zone-1", "domainname": "example.com"},
        ],
        bind_records=[
            {"uuid": "rec-1", "name": "www", "domain": "zone-1", "type": "A", "value": "172.18.60.30"},
        ],
    )
    mod.__salt__ = mock_salt
    result = mod.list_records(domain="example.com")
    assert len(result) == 1
    key = list(result.keys())[0]
    assert result[key]["name"] == "www"
    assert result[key]["value"] == "172.18.60.30"


def test_kea_list():
    from saltext.opnsense.modules import kea as mod

    mock_salt = _mock_salt_with_rows()
    mod.__salt__ = mock_salt
    subnets = mod.list_subnets()
    assert "172.18.60.0/24" in subnets
    reservations = mod.list_reservations()
    assert "www" in reservations
    assert reservations["www"]["ip_address"] == "172.18.60.30"


def test_acmeclient_list():
    from saltext.opnsense.modules import acmeclient as mod

    mock_salt = _mock_salt_with_rows()
    mod.__salt__ = mock_salt
    accounts = mod.list_accounts()
    assert "letsencrypt-prod" in accounts
    certs = mod.list_certificates()
    assert "*.example.com" in certs
    assert certs["*.example.com"]["status"] == "valid"


def test_dns_module():
    from saltext.opnsense.modules import dns as mod

    mock_salt = _mock_salt_with_rows(
        host_overrides=[
            {"uuid": "host-uuid-1", "hostname": "cluster", "domain": "example.com"},
        ],
        aliases=[
            {"uuid": "alias-1", "hostname": "www", "domain": "example.com", "host": "host-uuid-1"},
        ],
    )
    mock_salt["opnsense_unbound.list_aliases"] = MagicMock(return_value={"www.example.com": {"parent": "cluster.example.com"}})
    mock_salt["opnsense_unbound.resolve_parent"] = MagicMock(return_value="host-uuid-1")
    mod.__salt__ = mock_salt
    mod.__pillar__ = {"opnsense": {"aliases": {"example.com": ["www"]}, "purge_aliases": {}, "cluster_parent": {"hostname": "cluster", "domain": "example.com"}}}

    preview = mod.managed_preview()
    assert "www.example.com" in preview["desired"]
