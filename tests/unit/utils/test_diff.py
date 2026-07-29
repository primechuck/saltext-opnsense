from saltext.opnsense.utils.diff import diff_models, normalize_field_value


def test_normalize_field_value_booleans():
    for true_val in ("1", 1, True, "true", "True", "yes", "YES", "enabled", "ENABLED"):
        assert normalize_field_value("enabled", true_val) is True
        assert normalize_field_value("some_flag", true_val) is True

    for false_val in ("0", 0, False, "false", "False", "no", "NO", "disabled", "DISABLED", ""):
        assert normalize_field_value("enabled", false_val) is False
        assert normalize_field_value("some_flag", false_val) is False


def test_normalize_field_value_relation_equivalence():
    parent_fqdn = "cluster.example.com"
    uuid_str = "b6a50616-ce5b-4028-9844-8cb38531ecb8"

    # UUID vs human reference equivalence
    assert normalize_field_value("host", uuid_str, parent_human=parent_fqdn) == parent_fqdn
    assert normalize_field_value("host", parent_fqdn, parent_human=parent_fqdn) == parent_fqdn

    # Dict representation vs human reference / FQDN
    host_dict = {"hostname": "cluster", "domain": "example.com"}
    assert normalize_field_value("host", host_dict, parent_human=parent_fqdn) == parent_fqdn


def test_normalize_field_value_lists_and_csv():
    # Order agnostic list normalization
    assert normalize_field_value("interfaces", ["lan", "wan"]) == ("lan", "wan")
    assert normalize_field_value("interfaces", ["wan", "lan"]) == ("lan", "wan")

    # CSV string vs list equivalence
    assert normalize_field_value("interfaces", "lan,wan") == ("lan", "wan")
    assert normalize_field_value("interfaces", "wan, lan") == ("lan", "wan")


def test_normalize_field_value_numbers_and_strings():
    assert normalize_field_value("port", "80") == 80
    assert normalize_field_value("port", 80) == 80
    assert normalize_field_value("description", " test ") == "test"


def test_diff_models_idempotency():
    existing = {
        "uuid": "12345678-1234-1234-1234-1234567890ab",
        "enabled": "1",
        "host": "b6a50616-ce5b-4028-9844-8cb38531ecb8",
        "interfaces": "lan,wan",
        "port": "80",
        "description": "  web server  ",
    }
    desired = {
        "enabled": True,
        "host": "cluster.example.com",
        "interfaces": ["wan", "lan"],
        "port": 80,
        "description": "web server",
    }

    diff = diff_models(existing, desired, parent_human="cluster.example.com")
    assert diff == {}


def test_diff_models_detects_changes():
    existing = {"enabled": "1", "port": "80"}
    desired = {"enabled": "0", "port": 8080}

    diff = diff_models(existing, desired)
    assert diff == {
        "enabled": {"old": "1", "new": "0"},
        "port": {"old": "80", "new": 8080},
    }
