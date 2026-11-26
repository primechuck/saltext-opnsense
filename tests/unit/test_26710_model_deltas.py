"""Offline coverage for the OPNsense 26.7.10 model-registry deltas (26.7.9 -> 26.7.10).

Each entry below is one of the four model deltas shipped between the upstream 26.7.9 and
26.7.10 releases.  Every assertion is cross-checked against the upstream XML *and* the models
registry dump at BOTH refs, so a future ``make bump`` that drops one of these shapes -- or, in
the case of the dyndns provider options, reintroduces a removal -- fails loudly instead of
silently regressing the states that depend on them.

The four locked deltas:

1. **dyndns** -- the ddclient ``DynDNS`` ``service`` option gains the ``ionos-v4`` / ``ionos-v6``
   providers (``plugins/*/dns/ddclient/.../DynDNS.xml`` <OptionValues>).  Absent at 26.7.9.
2. **routing** -- the gateway-item ``latencyhigh`` / ``latencylow`` / ``losshigh`` / ``losslow``
   ``IntegerField`` blocks lose their ``ComparedToFieldConstraint`` blocks
   (``core/.../Routing/Gateways.xml``).  ``MinimumValue`` / ``MaximumValue`` survive; the
   ``Constraints`` key disappears at 26.7.10.
3. **captiveportal** -- the ``zone`` ArrayField's ``zoneid`` AutoNumberField gains a
   ``Constraints.check001`` (a UniqueConstraint) and an updated validation message
   (``core/.../CaptivePortal/CaptivePortal.xml``).
4. **ipsec** -- ``preSharedKey.remote_ident`` restructures its ``Constraints`` from a
   ``{"reference": ...}`` block into the flat ``{"check001": ""}`` shape
   (``core/.../IPsec/IPsec.xml``).

Offline-first: only the verified upstream scratch clones on disk are read (no socket is opened,
so the loopback-only conftest transport is irrelevant).  The dumps are loaded through the same
``_models()``-style helper pattern as ``tests/unit/test_2679_new_surface.py``.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

# Scratch clones produced by the bump-diff workflow (verified, do not re-clone).
# Override with OPNSENSE_UPSTREAM_DIFF when running from a different checkout.
DIFF_ROOT = Path(
    os.environ.get(
        "OPNSENSE_UPSTREAM_DIFF",
        "/opt/data/profiles/saltext-opnsense/cache/scratch/upstream-diff",
    )
)


def _models(ref: str) -> dict:
    """Return the upstream models registry dict for a release ref (models-{ref}.json).

    Mirrors the ``_models()`` helper in ``test_2679_new_surface.py`` but loads the diff
    clones so a delta can be checked at BOTH refs.
    """
    path = DIFF_ROOT / f"models-{ref}.json"
    if not path.exists():
        pytest.skip(f"upstream scratch dump {path} not available")
    return json.loads(path.read_text())["models"]


def _dyndns_service_opts(ref: str) -> dict:
    return _models(ref)["dyndns"]["DynDNS"]["account"]["service"]["OptionValues"]


def _routing_gateway_item(ref: str) -> dict:
    return _models(ref)["routing"]["Gateways"]["gateway_item"]


# --------------------------------------------------------------------------- #
# 1. DyDNS: Ionos provider options added in 26.7.10
# --------------------------------------------------------------------------- #
def test_dyndns_service_lacks_ionos_options_at_2679():
    """The ddclient DynDNS service option did not list Ionos at 26.7.9."""
    opts = _dyndns_service_opts("26.7.9")
    assert "ionos-v4" not in opts
    assert "ionos-v6" not in opts


def test_dyndns_service_has_ionos_options_at_26710():
    """The ddclient DynDNS service option gained ionos-v4 / ionos-v6 in 26.7.10."""
    opts = _dyndns_service_opts("26.7.10")
    assert opts["ionos-v4"] == "Ionos-v4"
    assert opts["ionos-v6"] == "Ionos-v6"


# --------------------------------------------------------------------------- #
# 2. Routing: gateway-item latency/loss ComparedToFieldConstraint blocks removed
# --------------------------------------------------------------------------- #
# Field -> expected surviving bound at 26.7.10.  latency fields lose their maximum; the loss
# fields keep both bounds, and every field keeps its minimum.
_ROUTING_BOUNDS = {
    "latencyhigh": (1, None),
    "latencylow": (1, None),
    "losshigh": (1, 100),
    "losslow": (1, 99),
}


def test_routing_latency_loss_has_no_constraint_block_at_26710():
    """The four gateway-item threshold fields drop their Constraints block in 26.7.10."""
    item = _routing_gateway_item("26.7.10")
    for field, (min_val, max_val) in _ROUTING_BOUNDS.items():
        assert "Constraints" not in item[field], f"{field} still has a Constraints block"
        assert item[field]["MinimumValue"] == str(min_val), f"{field} lost its MinimumValue"
        if max_val is not None:
            assert item[field]["MaximumValue"] == str(max_val), f"{field} lost its MaximumValue"


def test_routing_latency_loss_had_constraint_block_at_2679():
    """Contrast: the same fields carried a ComparedToFieldConstraint block at 26.7.9."""
    item = _routing_gateway_item("26.7.9")
    for field in _ROUTING_BOUNDS:
        assert "Constraints" in item[field], f"{field} had no Constraints block at 26.7.9"
        assert item[field]["Constraints"]["type"] == "ComparedToFieldConstraint"


# --------------------------------------------------------------------------- #
# 3. CaptivePortal: zone/zoneid UniqueConstraint + updated message
# --------------------------------------------------------------------------- #
def _captive_zoneid(ref: str) -> dict:
    return _models(ref)["captiveportal"]["CaptivePortal"]["zone"]["zoneid"]


def test_captiveportal_zoneid_constraint_absent_at_2679():
    """The captiveportal zone AutoNumberField had no UniqueConstraint block at 26.7.9."""
    zoneid = _captive_zoneid("26.7.9")
    assert "Constraints" not in zoneid
    assert zoneid["ValidationMessage"] == "Maximum number of zones reached."


def test_captiveportal_zoneid_constraint_present_at_26710():
    """The captiveportal zone AutoNumberField gains check001 and an updated message in 26.7.10."""
    zoneid = _captive_zoneid("26.7.10")
    assert zoneid["Constraints"] == {"check001": ""}
    assert zoneid["ValidationMessage"] == ("Maximum number of zones reached or input invalid.")


# --------------------------------------------------------------------------- #
# 4. IPsec: preSharedKey.remote_ident constraint restructure
# --------------------------------------------------------------------------- #
def _ipsec_remote_ident(ref: str) -> dict:
    return _models(ref)["ipsec"]["IPsec"]["preSharedKey"]["remote_ident"]


def test_ipsec_remote_ident_reference_constraint_at_2679():
    """At 26.7.9 the remote_ident constraint was a reference-style block."""
    ident = _ipsec_remote_ident("26.7.9")
    assert ident["Constraints"] == {"reference": "ident.check001"}


def test_ipsec_remote_ident_restructured_at_26710():
    """At 26.7.10 the remote_ident constraint restructured to the flat check001 shape."""
    ident = _ipsec_remote_ident("26.7.10")
    assert ident["Constraints"] == {"check001": ""}
