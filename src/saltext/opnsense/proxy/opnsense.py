import logging

log = logging.getLogger(__name__)


def _load_client_deps():
    import importlib

    for mod_name in ["saltext.opnsense.utils.opnsense", "opnsense", "salt.utils.opnsense"]:
        try:
            m = importlib.import_module(mod_name)
            return (
                getattr(m, "OPNsenseClient"),
                getattr(m, "OPNsenseClientConfig"),
                getattr(m, "get_client_from_opts"),
                True,
                "",
            )
        except Exception as exc:
            last = str(exc)
            continue
    return None, None, None, False, last


OPNsenseClient, OPNsenseClientConfig, get_client_from_opts, HAS_DEPS, HAS_DEPS_ERROR = (
    _load_client_deps()
)

__proxyenabled__ = ["opnsense"]
__virtualname__ = "opnsense"


def _ctx():
    return __context__.setdefault("opnsense", {})


def __virtual__():
    if not HAS_DEPS:
        return (False, f"saltext-opnsense deps missing: {HAS_DEPS_ERROR}")
    return __virtualname__


def init(opts):
    ctx = _ctx()
    proxy_conf = opts.get("proxy", {}) or opts.get("opnsense", {})
    if not proxy_conf:
        log.error("Proxy config missing for opnsense")
        ctx["initialized"] = False
        return False
    try:
        client = get_client_from_opts(opts, pillar=proxy_conf)
    except Exception as exc:
        log.error("Failed to create client: %s", exc)
        ctx["initialized"] = False
        return False
    ctx["client"] = client
    ctx["initialized"] = True
    ctx["opts"] = opts
    log.info("OPNsense proxy initialized host=%s proto=%s", client.config.host, client.config.proto)
    return True


def initialized():
    return _ctx().get("initialized", False)


def shutdown(opts=None):
    __context__.pop("opnsense", None)
    return True


def ping():
    ctx = _ctx()
    client = ctx.get("client")
    if not client:
        return False
    for mod, ctrl, typ in [
        ("unbound", "settings", "host_alias"),
        ("bind", "domain", "primary_domain"),
        ("firewall", "alias", "item"),
        ("unbound", "settings", "host_override"),
    ]:
        try:
            client.search(mod, ctrl, typ, row_count=1)
            return True
        except Exception as exc:
            log.debug("ping %s/%s/%s failed: %s", mod, ctrl, typ, exc)
            continue
    try:
        client.call(
            "unbound",
            "settings",
            "searchHostAlias",
            data={"rowCount": 1, "current": 1, "searchPhrase": ""},
            method="POST",
        )
        return True
    except Exception as exc:
        log.debug("ping fallback failed: %s", exc)
        return False


def alive(opts=None):
    return ping()


def grains():
    ctx = _ctx()
    client = ctx.get("client")
    if not client:
        return {}
    out = {"opnsense_host": client.config.host}
    try:
        fw = client.search("unbound", "settings", "host_alias", row_count=1)
        out["opnsense_unbound_alias_count"] = fw.get("total", 0)
    except Exception:
        pass
    try:
        info = client.call("core", "firmware", "status", data={}, method="POST")
        if isinstance(info, dict):
            out["opnsense_version"] = info.get("product_version") or info.get(
                "product_version_string", "unknown"
            )
    except Exception:
        pass
    try:
        diag = client.search("bind", "domain", "primary_domain", row_count=1)
        out["opnsense_bind_domain_count"] = diag.get("total", 0)
    except Exception:
        pass
    return out


def call(module, controller, action, uuid=None, data=None, method=None):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.call(module, controller, action, uuid=uuid, data=data, method=method)


def search(module, controller, type_name=None, **kwargs):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    kwargs = {k: v for k, v in kwargs.items() if not k.startswith("__")}
    search_phrase = kwargs.pop("search_phrase", "")
    row_count = kwargs.pop("row_count", -1)
    current = kwargs.pop("current", 1)
    sort = kwargs.pop("sort", None)
    return client.search(
        module,
        controller,
        type_name,
        search_phrase=search_phrase,
        row_count=row_count,
        current=current,
        sort=sort,
        extra=kwargs if kwargs else None,
    )


def get(module, controller, type_name=None, uuid=None):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.get(module, controller, type_name, uuid=uuid)


def add(module, controller, type_name, data):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.add(module, controller, type_name, data)


def set_item(module, controller, type_name, uuid, data):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.set(module, controller, type_name, uuid, data)


def delete(module, controller, type_name, uuid):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.delete(module, controller, type_name, uuid)


def toggle(module, controller, type_name, uuid, enabled=None):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.toggle(module, controller, type_name, uuid, enabled)


def reconfigure(module, controller, action="reconfigure", data=None):
    client = _ctx().get("client")
    if not client:
        raise Exception("OPNsense proxy not initialized")
    return client.reconfigure(module, controller, action, data=data)
