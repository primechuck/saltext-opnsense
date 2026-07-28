import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense"


def __virtual__():
    if "__proxy__" not in globals():
        return (False, "opnsense grains only run on proxy minions")
    return __virtualname__


def opnsense_grains():
    grains = {}
    try:
        if "__salt__" in globals() and "opnsense.ping" in __salt__:
            try:
                if not __salt__["opnsense.ping"]():
                    return grains
            except Exception:
                pass
            try:
                spec = __salt__["opnsense.spec"]()
                if isinstance(spec, dict):
                    mods = spec.get("modules", {})
                    meta = spec.get("meta", {})
                    grains["opnsense_api_modules"] = list(mods.keys()) if isinstance(mods, dict) else list(mods)
                    grains["opnsense_spec_version"] = meta.get("core_ref", "25.7")
            except Exception:
                pass
            try:
                fw_status = __salt__["opnsense.call"]("core", "firmware", "status", data={}, method="POST")
                if isinstance(fw_status, dict):
                    grains["opnsense_version"] = fw_status.get("product_version") or fw_status.get("product_version_string")
            except Exception:
                pass
            try:
                alias_res = __salt__["opnsense.search"]("unbound", "settings", "host_alias", row_count=1)
                if isinstance(alias_res, dict):
                    grains["opnsense_unbound_alias_count"] = alias_res.get("total", 0)
            except Exception:
                pass
    except Exception as exc:
        log.debug("opnsense grains failed: %s", exc)
    return grains
