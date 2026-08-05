"""
State module override for opnsense resource type.

Re-exports standard saltext.opnsense.states.opnsense functions via
salt.utils.functools.namespaced_function so that __salt__, __opts__,
__grains__ etc resolve to per-resource loader (per execution_modules
and state_modules authoring guides).

This allows state.apply merge-mode to run per-resource HighState
with per-resource __salt__["opnsense.search"] etc.

If no override existed, standard salt.modules.state would run with
per-resource execution loader – also works. This explicit re-export
ensures custom diff engine and relation resolving use resource context.
"""

try:
    import salt.utils.functools

    import saltext.opnsense.states.opnsense as _src

    # Re-export core generic states
    item_present = salt.utils.functools.namespaced_function(_src.item_present, globals())
    item_absent = salt.utils.functools.namespaced_function(_src.item_absent, globals())

    # Batch helpers
    if hasattr(_src, "items_present"):
        items_present = salt.utils.functools.namespaced_function(_src.items_present, globals())
    if hasattr(_src, "items_absent"):
        items_absent = salt.utils.functools.namespaced_function(_src.items_absent, globals())
    if hasattr(_src, "reconfigured"):
        reconfigured = salt.utils.functools.namespaced_function(_src.reconfigured, globals())
    if hasattr(_src, "assert_resolves"):
        assert_resolves = salt.utils.functools.namespaced_function(_src.assert_resolves, globals())

except Exception:
    # Fallback – if salt.utils.functools not available (unit test without salt), define minimal stubs
    def item_present(*args, **kwargs):
        return {
            "name": kwargs.get("name") or args[0] if args else "unknown",
            "result": False,
            "changes": {},
            "comment": "fallback: salt not available",
        }

    def item_absent(*args, **kwargs):
        return {
            "name": kwargs.get("name") or args[0] if args else "unknown",
            "result": False,
            "changes": {},
            "comment": "fallback: salt not available",
        }
