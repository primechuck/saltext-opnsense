r"""Regression tests for the OPNsense 26.7.3 -> 26.7.9 spec blind spots.

Two suspected regressions were verified against the 26.7.9 upstream clones and the
extension's bundled registries (`controllers.json` / `models.json`):

(A) **monit/service lost ``check`` + ``reconfigure`` from the scan.**  ``Monit/Api/ServiceController``
    extends ``OPNsense/Base/ApiMutableServiceControllerBase``, whose explicit
    ``reconfigureAction`` / ``statusAction`` / ``startAction`` / ``stopAction`` / ``restartAction``
    are inherited, not re-declared.  The controller spec generator
    (``tools/generate_spec.py``) matches only per-file ``public function *Action`` and is blind to
    inheritance, so ``monit/service`` disappears from ``controllers.json``.  Those endpoints still
    exist at runtime (PHP dispatches ``<action>Action`` via normal method resolution).  ``check`` is
    *genuinely* removed upstream (no base-class ``checkAction`` exists), so it is gone at runtime too.

(B) **interfaces/assignment (the ``interface`` model) vanished from ``models.json``.**  The model XML
    still exists and is richer upstream, but its array wrapper's type changed from
    ``ArrayField`` to the concrete subclass ``.\NetworkInterfaceField`` (which extends ``ArrayField``).
    ``tools/generate_models.py`` only recognises wrappers whose ``type == "ArrayField"``, so the model
    silently drops.  Confirmed: regenerating ``models.json`` from the 26.7.9 core reproduces the
    committed file byte-for-byte (missing ``interfaces/assignment``).

These tests are offline-first: they touch only the bundled registries on disk and pure
path-construction helpers -- no sockets, no HTTP.
"""

from __future__ import annotations

import pytest

from saltext.opnsense.states.opnsense import _get_reconfigure, _infer_reconfigure
from saltext.opnsense.utils import api_spec
from saltext.opnsense.utils import models as model_utils

MODULE = "monit"
SERVICE_CONTROLLER = "service"

# The route the inherited base class ``ApiMutableServiceControllerBase.reconfigureAction`` exposes.
BASE_CLASS_RECONFIGURE = {
    "module": MODULE,
    "controller": SERVICE_CONTROLLER,
    "action": "reconfigure",
}


# --- (A) monit/service reconfigure route: base class still provides it at runtime --------------


def test_monit_service_reconfigure_route_matches_base_class():
    """The extension builds the monit.service reconfigure route that the base class exposes."""
    rc = _infer_reconfigure(MODULE, SERVICE_CONTROLLER, None)
    assert rc == BASE_CLASS_RECONFIGURE


def test_monit_service_reconfigure_via_public_helper():
    """``_get_reconfigure`` (used by the generic item_present/reconfigured states) resolves it too."""
    rc = _get_reconfigure(MODULE, SERVICE_CONTROLLER, None, None)
    assert rc == BASE_CLASS_RECONFIGURE


def test_monit_service_reconfigure_route_robust_to_missing_controller():
    """The base-class route is reached even when the caller omits the controller arg."""
    rc = _infer_reconfigure(MODULE, None, None)
    assert rc == BASE_CLASS_RECONFIGURE


def test_monit_service_check_absent_from_runtime():
    """``check`` was removed upstream (no inherited checkAction), so it must not be advertised."""
    assert api_spec.has_action(MODULE, SERVICE_CONTROLLER, "check") is False


def test_monit_service_not_scanned_but_route_still_constructible():
    """Lock the scan artifact: service is dropped from the registry (blind to inheritance) yet the
    generic state can still infer the correct base-class route.  Re-adding spurious actions here
    would be a regression, so the current (empty) action list is pinned as a guard."""
    assert api_spec.list_controllers(MODULE) == ["settings", "status"]
    assert api_spec.list_actions(MODULE, SERVICE_CONTROLLER) == []
    # Path construction must not depend on the missing registry entry.
    assert _infer_reconfigure(MODULE, SERVICE_CONTROLLER, None) == BASE_CLASS_RECONFIGURE


# --- (B) interfaces/assignment model resolution --------------------------------------------------

# Locked current gap: the model silently dropped from models.json at 26.7.9 (see docstring, (B)).


def test_interfaces_assignment_absent_from_models_json():
    assert "assignment" not in model_utils.list_models("interfaces")
    assert model_utils.get_model_arrays("interfaces", "assignment") == {}


def test_interfaces_interface_array_cannot_resolve_model():
    """With the assignment model gone, the ``interface`` array field no longer resolves to a model."""
    model_name, array, fields = model_utils.find_model_for_array("interfaces", "interface")
    assert (model_name, array) == ("", "")
    assert fields == {}


@pytest.mark.xfail(
    strict=False,
    reason=(
        r"REGRESSION (26.7.9): interfaces/assignment (the generic 'interface' model) dropped from "
        "models.json because generate_models.py only matches array wrappers with type == 'ArrayField', "
        "while upstream renamed the <interface> wrapper type to the concrete subclass "
        "'.\\NetworkInterfaceField' (which extends ArrayField).  Restore by fixing the generator "
        "(accept subclass ArrayField wrappers) and regenerating models.json; once shipped this "
        "find_model_for_array('interfaces', 'interface') -> ('assignment', 'interface', {...})."
    ),
)
def test_interfaces_interface_array_resolves_assignment_model():
    """Correct post-fix behavior: the 'interface' array resolves back to the assignment model."""
    model_name, array, fields = model_utils.find_model_for_array("interfaces", "interface")
    assert model_name == "assignment"
    assert array == "interface"
    assert fields  # field metadata is present
