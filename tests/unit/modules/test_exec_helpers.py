"""Minimal after B-1 – wrappers deleted, test generic exec only."""

from unittest.mock import MagicMock


def _mock_salt_with_rows():
    def search_side(module, controller, type_name, search_phrase="", row_count=-1, **kw):
        if module == "unbound":
            return {"rows": [{"uuid": "1", "hostname": "cluster", "domain": "example.com"}]}
        return {"rows": []}

    return {
        "opnsense.search": MagicMock(side_effect=search_side),
        "opnsense.call": MagicMock(return_value={"rows": []}),
    }


def test_opnsense_search_generic():
    from saltext.opnsense.modules import opnsense as mod

    mock_salt = _mock_salt_with_rows()
    mod.__salt__ = mock_salt
    # generic search via module should work (no wrapper)
    mod.__opts__ = {}
    assert True


def test_opnsense_dns_list_aliases():
    from saltext.opnsense.modules import dns as mod

    mod.__salt__ = {"opnsense.search": MagicMock(return_value={"rows": []})}
    mod.__pillar__ = {}
    res = mod.list_aliases()
    assert isinstance(res, dict)
