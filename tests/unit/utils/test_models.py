"""Unit coverage for ``saltext.opnsense.utils.models`` registry helpers.

Offline-first: exercises every public helper against the bundled
``models.json`` on disk (plus empty-spec and empty-arg edge cases). No
sockets, no HTTP — the only I/O is reading the packaged registry file.
"""

from __future__ import annotations

import pytest

from saltext.opnsense.utils import models as m


@pytest.fixture
def spec():
    return m.load_spec()


def test_load_spec_has_models(spec):
    assert spec.get("models")
    assert "unbound" in spec["models"]


def test_list_modules_sorted(spec):
    mods = m.list_modules()
    assert mods == sorted(mods)
    assert "unbound" in mods
    assert "interfaces" in mods


def test_list_models_known_and_unknown():
    assert "Unbound" in m.list_models("unbound")
    assert m.list_models("no-such-module") == []


def test_list_arrays_known_and_unknown():
    assert "host" in m.list_arrays("unbound", "Unbound")
    assert m.list_arrays("unbound", "Nope") == []
    assert m.list_arrays("no-such-module", "Unbound") == []


def test_get_fields_known_and_unknown():
    fields = m.get_fields("unbound", "Unbound", "host")
    assert isinstance(fields, dict) and fields
    assert m.get_fields("unbound", "Unbound", "nope") == {}
    assert m.get_fields("nope", "Unbound", "host") == {}


def test_get_model_arrays_known_and_unknown():
    assert m.get_model_arrays("unbound", "Unbound") != {}
    assert m.get_model_arrays("unbound", "Nope") == {}


def test_list_module_models_known_and_unknown():
    out = m.list_module_models("unbound")
    assert out and all(isinstance(v, list) for v in out.values())
    assert m.list_module_models("no-such-module") == {}


def test_is_relation_type_matrix():
    assert m._is_relation_type("ModelRelationField") is True
    assert m._is_relation_type(".\\GroupedModelRelationField") is True
    assert m._is_relation_type("TextField") is False
    assert m._is_relation_type("") is False
    assert m._is_relation_type(None) is False  # type: ignore[arg-type]
    assert m._is_relation_type(123) is False  # type: ignore[arg-type]


def test_is_relation_field_matrix():
    assert m.is_relation_field({"type": "ModelRelationField"}) is True
    assert m.is_relation_field({"type": "TextField", "relation": {}}) is True
    assert m.is_relation_field({"type": "TextField", "relation_targets": []}) is True
    assert m.is_relation_field({"type": "TextField"}) is False
    assert m.is_relation_field({}) is False
    assert m.is_relation_field([]) is False  # type: ignore[arg-type]
    assert m.is_relation_field(None) is False  # type: ignore[arg-type]


def test_get_relation_fields_filters_to_relations():
    rels = m.get_relation_fields("interfaces", "NetworkInterface", "interface")
    assert isinstance(rels, dict)
    assert m.get_relation_fields("unbound", "Unbound", "nope") == {}


def test_get_relation_fields_for_array_known_and_miss():
    rels = m.get_relation_fields_for_array("interfaces", "interface")
    assert isinstance(rels, dict)
    assert m.get_relation_fields_for_array("no-such-module", "interface") == {}


def test_get_relation_targets_shapes():
    assert m.get_relation_targets({"relation_targets": [{"key": "a"}]}) == [{"key": "a"}]
    assert m.get_relation_targets({"relation": {"key": "a"}}) == [{"key": "a"}]
    assert m.get_relation_targets({"relation": [{"key": "a"}]}) == [{"key": "a"}]
    assert m.get_relation_targets({}) == []
    assert m.get_relation_targets(None) == []  # type: ignore[arg-type]
    assert m.get_relation_targets({"relation": "nope"}) == []


def test_parse_relation_source_shapes():
    assert m.parse_relation_source("OPNsense.Firewall.Alias") == ("firewall", "Alias")
    assert m.parse_relation_source("a.b") == ("a", "b")
    assert m.parse_relation_source("single") == ("single", "")
    assert m.parse_relation_source("") == ("", "")


def test_parse_relation_items_shapes():
    assert m.parse_relation_items("areas.area") == ("areas", "area")
    assert m.parse_relation_items("area") == ("", "area")
    assert m.parse_relation_items("") == ("", "")


def test_candidate_sort_key_orders_by_score_then_names():
    lo = (90, "b-model", "b-array", {})
    hi = (100, "a-model", "a-array", {})
    assert sorted([lo, hi], key=m._candidate_sort_key)[0] == hi


def test_find_model_for_array_miss_and_unknown_module():
    assert m.find_model_for_array("no-such-module", "interface") == ("", "", {})
    # A type string matching nothing resolves empty rather than raising.
    assert m.find_model_for_array("unbound", "zzz-no-such-array") == ("", "", {})


def test_find_model_for_array_hit_uses_registry():
    model_name, array, fields = m.find_model_for_array("interfaces", "interface")
    assert (model_name, array) == ("NetworkInterface", "interface")
    assert fields


def test_find_model_containing_field_known_and_empty():
    hits = m.find_model_containing_field("interfaces", "descr")
    assert isinstance(hits, list)
    assert m.find_model_containing_field("no-such-module", "descr") == []


def test_all_relation_fields_known_and_unknown_module():
    out = m.all_relation_fields("interfaces")
    assert isinstance(out, dict)
    assert m.all_relation_fields("no-such-module") == {}
    everything = m.all_relation_fields()
    assert isinstance(everything, dict) and everything


def test_load_spec_empty_models_falls_through(monkeypatch):
    """Empty ``models`` dicts are falsy: both file loaders are skipped."""
    m.load_spec.cache_clear()
    try:
        monkeypatch.setattr(m, "_load_from_files_resource", lambda: {"models": {}})
        monkeypatch.setattr(m, "_load_from_spec_file", lambda: {"models": {}})
        assert m.load_spec() == {"generated": False, "models": {}, "meta": {}}
    finally:
        m.load_spec.cache_clear()


def test_loaders_handle_missing_files(monkeypatch, tmp_path):
    monkeypatch.setattr(m, "SPEC_FILE", tmp_path / "missing.json")
    assert m._load_from_spec_file() is None
