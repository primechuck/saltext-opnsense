"""Check generic modules import after B-2 minimal trim."""


def test_generic_exec_dynamic():
    from saltext.opnsense.modules import opnsense as exec_mod

    try:
        exec_mod._DYNAMIC_MAP_CACHE = None
    except Exception:
        pass
    m = exec_mod._build_dynamic_map()
    assert len(m) >= 300


def test_generic_state_dynamic():
    from saltext.opnsense.states import opnsense as generic_state

    assert hasattr(generic_state, "item_present")
    assert hasattr(generic_state, "items_present")
    # B-2 minimal: no dynamic present funcs, only core item_present etc
    present = [x for x in dir(generic_state) if x.endswith("_present")]
    assert len(present) >= 1


def test_dns_module():
    from saltext.opnsense.modules import dns as dns_mod

    assert hasattr(dns_mod, "list_aliases")
    assert hasattr(dns_mod, "managed_preview")


def test_dns_state():
    from saltext.opnsense.states import dns as dns_state

    assert hasattr(dns_state, "managed")
