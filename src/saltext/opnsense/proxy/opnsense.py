import logging

import salt.utils.json
import salt.utils.platform

log = logging.getLogger(__name__)

def _load_deps():
    import importlib
    candidates = [
        "saltext.opnsense.utils.opnsense",
        "opnsense",
        "salt.utils.opnsense",
    ]
    last_err = None
    for mod in candidates:
        try:
            m = importlib.import_module(mod)
            return (
                getattr(m, "OPNsenseClient"),
                getattr(m, "OPNsenseClientConfig"),
                getattr(m, "get_client_from_opts"),
                True,
                "",
            )
        except Exception as e:
            last_err = str(e)
            continue
    return None, None, None, False, last_err or "import failed"

OPNsenseClient, OPNsenseClientConfig, get_client_from_opts, HAS_DEPS, HAS_DEPS_ERROR = _load_deps()

__proxyenabled__ = ["opnsense"]
__virtualname__ = "opnsense"
DETAILS = {}


def __virtual__():
    if not HAS_DEPS:
        return (False, f"saltext-opnsense dependencies missing: {HAS_DEPS_ERROR}")
    return __virtualname__


def init(opts):
    proxy_conf = opts.get("proxy", {})
    if not proxy_conf:
        proxy_conf = opts.get("opnsense", {})

    if not proxy_conf:
        log.error("Proxy config missing: expected pillar/proxy or opts proxy for opnsense")
        DETAILS["initialized"] = False
        return False

    try:
        client = get_client_from_opts(opts, pillar=proxy_conf)
    except Exception as exc:
        log.error("Failed to create OPNsense client: %s", exc)
        DETAILS["initialized"] = False
        return False

    DETAILS["client"] = client
    DETAILS["initialized"] = True
    DETAILS["opts"] = opts

    log.info("OPNsense proxy initialized for host %s", client.config.host)
    return True


def initialized():
    return DETAILS.get("initialized", False)


def shutdown(opts=None):
    DETAILS.clear()
    return True


def ping():
    if not DETAILS.get("client"):
        return False
    client = DETAILS["client"]
    try:
        client.call("core", "system", "status", method="GET")
        return True
    except Exception:
        try:
            client.call("diagnostics", "interface", "getArp", method="GET")
            return True
        except Exception as exc:
            log.debug("ping failed: %s", exc)
            return False


def alive(opts=None):
    return ping()


def grains():
    if not DETAILS.get("client"):
        return {}
    try:
        client = DETAILS["client"]
        info = client.call("core", "firmware", "status", method="GET")
        return {
            "opnsense_version": info.get("product_version", "unknown"),
            "opnsense_host": client.config.host,
        }
    except Exception:
        return {}


def call(module, controller, action, uuid=None, data=None, method=None):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.call(module, controller, action, uuid=uuid, data=data, method=method)


def search(module, controller, type_name=None, **kwargs):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.search(module, controller, type_name, **kwargs)


def get(module, controller, type_name=None, uuid=None):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.get(module, controller, type_name, uuid=uuid)


def add(module, controller, type_name, data):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.add(module, controller, type_name, data)


def set_item(module, controller, type_name, uuid, data):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.set(module, controller, type_name, uuid, data)


def delete(module, controller, type_name, uuid):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.delete(module, controller, type_name, uuid)


def toggle(module, controller, type_name, uuid, enabled=None):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.toggle(module, controller, type_name, uuid, enabled)


def reconfigure(module, controller, action="reconfigure", data=None):
    if not DETAILS.get("client"):
        raise Exception("OPNsense proxy not initialized")
    client = DETAILS["client"]
    return client.reconfigure(module, controller, action, data=data)
