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

Fix history: the (B) assignment gap was closed by the 26.7.9 follow-up to
``tools/generate_models.py`` (``_is_array_container`` accepts dotted
``ArrayField`` subclasses), and the (A) scan artifact by the
``SERVICE_BASE_ACTIONS`` fallback in ``tools/generate_spec.py``.
"""

from __future__ import annotations

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


def test_monit_service_base_actions_scanned_from_base_class():
    """The service-base fallback keeps inherited verbs in the registry.

    ``monit/service`` declares no actions of its own; the generator records
    the five ``ApiMutableServiceControllerBase`` verbs instead of dropping
    the controller.
    """
    assert api_spec.has_action(MODULE, SERVICE_CONTROLLER, "reconfigure") is True
    assert api_spec.has_action(MODULE, SERVICE_CONTROLLER, "status") is True
    assert set(api_spec.list_actions(MODULE, SERVICE_CONTROLLER)) == {
        "reconfigure",
        "restart",
        "start",
        "status",
        "stop",
    }


# --- (B) interfaces/assignment model resolution --------------------------------------------------

# Fixed by the generate_models.py ArrayField-subclass heuristic (26.7.9 follow-up):
# the <interface type=".\NetworkInterfaceField"> wrapper is recognised again.


def test_interfaces_assignment_present_in_models_json():
    assert "NetworkInterface" in model_utils.list_models("interfaces")
    assert model_utils.get_model_arrays("interfaces", "NetworkInterface") != {}


def test_interfaces_interface_array_resolves_model():
    """The 'interface' array resolves back to the NetworkInterface model (assignment API)."""
    model_name, array, fields = model_utils.find_model_for_array("interfaces", "interface")
    assert (model_name, array) == ("NetworkInterface", "interface")
    assert fields  # field metadata is present
