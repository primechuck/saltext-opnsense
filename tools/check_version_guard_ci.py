#!/usr/bin/env python3
"""
CI helper for version-guard job: asserts <3008 is rejected.
Used by .github/workflows/ci.yml version-guard job.

Mock salt.utils.resources.pillar_resources_tree and test __virtual__
for both resource and exec modules.
"""

import importlib
import sys
import types


def main():
    import salt.version

    print(f"salt.version.__version_info__={salt.version.__version_info__}")
    assert salt.version.__version_info__ < (3008,), "test setup expects salt<3008"

    utils_mod = types.ModuleType("salt.utils")
    res_mod = types.ModuleType("salt.utils.resources")

    def pillar_resources_tree(opts):
        return {"opnsense": {"hosts": {"fw-01": {"host": "fw-01"}}}}

    res_mod.pillar_resources_tree = pillar_resources_tree
    utils_mod.resources = res_mod
    sys.modules["salt.utils"] = utils_mod
    sys.modules["salt.utils.resources"] = res_mod

    if "saltext.opnsense.resources.opnsense" in sys.modules:
        del sys.modules["saltext.opnsense.resources.opnsense"]
    rmod = importlib.import_module("saltext.opnsense.resources.opnsense")
    rmod.__context__ = {}
    rmod.__opts__ = {}
    ret = rmod.__virtual__()
    print(f"resource __virtual__ -> {ret}")
    assert isinstance(ret, tuple) and ret[0] is False
    assert "3008" in ret[1]

    if "saltext.opnsense.modules.opnsense" in sys.modules:
        del sys.modules["saltext.opnsense.modules.opnsense"]
    emod = importlib.import_module("saltext.opnsense.modules.opnsense")
    ret2 = emod.__virtual__()
    print(f"exec __virtual__ -> {ret2}")
    assert isinstance(ret2, tuple) and ret2[0] is False
    assert "3008" in ret2[1]
    print("Version guard OK: <3008 correctly rejected")


if __name__ == "__main__":
    main()
