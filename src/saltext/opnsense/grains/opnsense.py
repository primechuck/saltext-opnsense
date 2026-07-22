import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.ping" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not available")


def opnsense_grains():
    grains = {}
    try:
        if __salt__["opnsense.ping"]():
            spec = __salt__["opnsense.spec"]()
            grains["opnsense_api_modules"] = spec.get("modules", {}).keys() if isinstance(spec, dict) else []
            try:
                fw_status = __salt__["opnsense.call"]("core", "firmware", "status", method="GET")
                if isinstance(fw_status, dict):
                    grains["opnsense_version"] = fw_status.get("product_version")
            except Exception:
                pass
    except Exception as exc:
        log.debug("opnsense grains failed: %s", exc)
    return grains
