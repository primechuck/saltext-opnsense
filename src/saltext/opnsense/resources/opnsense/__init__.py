"""
Connection module for Salt Resource type ``opnsense`` – API-only.

Implements required interface for Salt 3008+ Resources:
__virtual__, init, initialized, discover, grains, ping, shutdown

Also exposes execution functions that are callable via
__resource_funcs__["opnsense.call"] etc. Each per-resource dispatch
uses __resource__["id"] to select the correct cached client.

Pillar layout (hosts pattern like ssh resource):

resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
        proto: https
        api_key: xxx
        api_secret: yyy
        verify_ssl: true
        timeout: 30
      fw-02:
        ...

Alternative legacy shape ``resource_ids`` also supported.

After implementing this type, operator can:

  salt -C 'T@opnsense' test.ping
  salt -C 'T@opnsense:fw-01' opnsense.search unbound settings host_alias
  salt -C 'T@opnsense' state.apply fw.base

And for 2 SRN composition with built-in ssh resource:

  salt -C 'T@opnsense:fw-01 or T@ssh:fw-01' state.apply fw.base
"""

import logging
from typing import Any, Final

log = logging.getLogger(__name__)

try:
    from saltext.opnsense.utils.opnsense import (
        OPNsenseClient,
        OPNsenseClientConfig,
    )

    HAS_DEPS = True
    HAS_DEPS_ERROR = ""
except Exception as exc:  # pragma: no cover
    OPNsenseClient = None  # type: ignore
    OPNsenseClientConfig = None  # type: ignore
    HAS_DEPS = False
    HAS_DEPS_ERROR = str(exc)

CONTEXT_KEY: Final = "opnsense"
CONN_KEY: Final = "conns"
HOSTS_KEY: Final = "hosts"
INIT_KEY: Final = "initialized"


def _ctx():
    return __context__.setdefault(CONTEXT_KEY, {})  # type: ignore[name-defined]


def _pillar_tree(opts: dict[str, Any]) -> dict[str, Any]:
    try:
        import salt.utils.resources

        tree = salt.utils.resources.pillar_resources_tree(opts)
        return tree.get("opnsense", {}) if isinstance(tree, dict) else {}
    except Exception as exc:
        log.debug("pillar_resources_tree failed: %s", exc)
        # Fallback for masterless without salt.utils.resources – read opts pillar directly
        pillar = opts.get("pillar", {}) if isinstance(opts, dict) else {}
        if not pillar and "__pillar__" in globals():
            try:
                pillar = __pillar__  # type: ignore[name-defined]
            except Exception:
                pillar = {}
        resources = {}
        if isinstance(pillar, dict):
            resources = pillar.get("resources", {}) or pillar.get("opnsense", {})
            # support both resources.opnsense and top-level opnsense for masterless
            if "opnsense" in resources and isinstance(resources["opnsense"], dict):
                return (
                    resources["opnsense"]
                    if "hosts" in resources["opnsense"] or "resource_ids" in resources["opnsense"]
                    else resources
                )
            if isinstance(resources, dict) and (
                "hosts" in resources or "resource_ids" in resources
            ):
                return resources
        # last resort: check __opts__ pillar key
        try:
            from saltext.opnsense.utils.opnsense import get_client_from_opts  # noqa

            # if get_client_from_opts available, we rely on its merging – but for resources we already tried
            pass
        except Exception:
            pass
        return {}


def _normalize_hosts(tree: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """
    Normalize pillar subtree to {id: config} dict.
    Supports:
      hosts: {id: cfg}
      resource_ids: [id, ...] with optional config: {id: cfg} or hosts duplicate
      config: {id: cfg}
    """
    if not isinstance(tree, dict):
        return {}
    out: dict[str, dict[str, Any]] = {}

    hosts = tree.get("hosts")
    if isinstance(hosts, dict):
        for rid, cfg in hosts.items():
            if isinstance(cfg, dict):
                out[str(rid)] = cfg
            else:
                out[str(rid)] = {}

    # resource_ids flat list – per-id config may be under "config" or "hosts" already captured, else empty
    rids = tree.get("resource_ids")
    if isinstance(rids, (list, tuple, set)):
        for rid in rids:
            rid_s = str(rid)
            if rid_s not in out:
                out[rid_s] = {}

    # legacy "config" dict
    cfg_dict = tree.get("config")
    if isinstance(cfg_dict, dict):
        for rid, cfg in cfg_dict.items():
            if rid not in out:
                out[str(rid)] = cfg if isinstance(cfg, dict) else {}
            else:
                # merge
                if isinstance(cfg, dict):
                    merged = {**out[str(rid)], **cfg}
                    out[str(rid)] = merged

    return out


def _connect(resource_id: str) -> Any:
    ctx = _ctx()
    conns = ctx.setdefault(CONN_KEY, {})
    if resource_id in conns:
        return conns[resource_id]

    hosts = ctx.get(HOSTS_KEY, {})
    cfg_dict = hosts.get(resource_id)
    if not isinstance(cfg_dict, dict):
        # fallback try to pull from opts pillar tree directly (stale context case)
        try:
            tree = _pillar_tree(__opts__)  # type: ignore[name-defined]
            normalized = _normalize_hosts(tree)
            cfg_dict = normalized.get(resource_id)
            if cfg_dict is not None and resource_id not in hosts:
                hosts[resource_id] = cfg_dict
        except Exception:
            cfg_dict = None

    if not isinstance(cfg_dict, dict) or not cfg_dict:
        raise Exception(
            f"OPNsense resource {resource_id} config not found in pillar resources:opnsense:hosts"
        )

    try:
        cfg = OPNsenseClientConfig.from_dict(cfg_dict)
    except Exception as exc:
        raise Exception(f"Invalid config for opnsense resource {resource_id}: {exc}") from exc

    client = OPNsenseClient(cfg)
    conns[resource_id] = client
    log.debug("OPNsense resource %s connected host=%s proto=%s", resource_id, cfg.host, cfg.proto)
    return client


def __virtual__():
    if not HAS_DEPS:
        return (False, f"saltext-opnsense deps missing: {HAS_DEPS_ERROR}")
    return True


def init(opts: dict[str, Any]):
    ctx = _ctx()
    # idempotent
    if ctx.get(INIT_KEY):
        # refresh hosts on every init to capture pillar changes
        try:
            tree = _pillar_tree(opts)
            ctx[HOSTS_KEY] = _normalize_hosts(tree)
        except Exception as exc:
            log.debug("init refresh hosts failed: %s", exc)
        return True

    try:
        tree = _pillar_tree(opts)
        hosts = _normalize_hosts(tree)
        ctx[HOSTS_KEY] = hosts
        ctx.setdefault(CONN_KEY, {})
        ctx[INIT_KEY] = True
        log.info("OPNsense resources init hosts=%s", list(hosts.keys()))
        return True
    except Exception as exc:
        log.error("OPNsense resources init failed: %s", exc)
        ctx[INIT_KEY] = False
        return False


def initialized():
    return _ctx().get(INIT_KEY, False)


def discover(opts: dict[str, Any]):
    try:
        tree = _pillar_tree(opts)
        hosts = _normalize_hosts(tree)
        return list(hosts.keys())
    except Exception as exc:
        log.debug("discover failed: %s", exc)
        return []


def grains():
    """
    Per-resource grains. __resource__ is set by loader per-resource dispatch.
    """
    try:
        rid = __resource__["id"]  # type: ignore[name-defined]
    except Exception:
        return {}

    ctx = _ctx()
    hosts_cfg = ctx.get(HOSTS_KEY, {})
    # basic grains always
    out: dict[str, Any] = {"resource_id": rid, "opnsense_id": rid}

    client = None
    try:
        client = _connect(rid)
        out["opnsense_host"] = client.config.host
        out["opnsense_proto"] = client.config.proto
    except Exception as exc:
        log.debug("grains connect failed for %s: %s", rid, exc)
        # if no client, try to at least return host from config
        cfg = hosts_cfg.get(rid, {})
        if isinstance(cfg, dict) and cfg.get("host"):
            out["opnsense_host"] = cfg["host"]
        return out

    # lightweight probes – keep fast, avoid heavy calls
    try:
        fw = client.search("unbound", "settings", "host_alias", row_count=1)
        if isinstance(fw, dict):
            out["opnsense_unbound_alias_count"] = fw.get("total", 0)
    except Exception:
        pass

    try:
        bind_d = client.search("bind", "domain", "primary_domain", row_count=1)
        if isinstance(bind_d, dict):
            out["opnsense_bind_domain_count"] = bind_d.get("total", 0)
    except Exception:
        pass

    try:
        info = client.call("core", "firmware", "status", data={}, method="POST")
        if isinstance(info, dict):
            ver = (
                info.get("product_version")
                or info.get("product_version_string")
                or info.get("product_version_string", "unknown")
            )
            if ver:
                out["opnsense_version"] = ver
    except Exception:
        pass

    return out


def grains_refresh():
    """
    Invalidate cached grains – re-run grains().
    Framework default calls grains() again if not implemented, but we
    clear any cached connection cache that might affect grains.
    """
    return grains()


def shutdown(opts: dict[str, Any] | None = None):
    ctx = _ctx()
    conns = ctx.get(CONN_KEY, {})
    for rid, client in list(conns.items()):
        try:
            sess = getattr(client, "session", None)
            if sess is not None:
                sess.close()
        except Exception:
            pass
    __context__.pop(CONTEXT_KEY, None)  # type: ignore[name-defined]
    return True


def ping():
    ctx = _ctx()
    try:
        rid = __resource__["id"]  # type: ignore[name-defined]
    except Exception:
        return False

    client = ctx.get(CONN_KEY, {}).get(rid)
    if not client:
        try:
            client = _connect(rid)
        except Exception:
            return False

    # cheap probe – try a known endpoint
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
            log.debug("ping %s/%s/%s failed for %s: %s", mod, ctrl, typ, rid, exc)
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
        log.debug("ping fallback failed for %s: %s", rid, exc)
        return False


# Exposed execution functions – callable via __resource_funcs__["opnsense.call"]


def call(
    module: str,
    controller: str,
    action: str,
    uuid: str | None = None,
    data: dict | None = None,
    method: str | None = None,
):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.call(module, controller, action, uuid=uuid, data=data, method=method)


def search(
    module: str,
    controller: str,
    type_name: str | None = None,
    search_phrase: str = "",
    row_count: int = -1,
    current: int = 1,
    sort: dict | None = None,
    extra: dict | None = None,
):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.search(
        module,
        controller,
        type_name,
        search_phrase=search_phrase,
        row_count=row_count,
        current=current,
        sort=sort,
        extra=extra,
    )


def get(module: str, controller: str, type_name: str | None = None, uuid: str | None = None):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.get(module, controller, type_name, uuid=uuid)


def add(module: str, controller: str, type_name: str, data: dict):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.add(module, controller, type_name, data)


def set_item(module: str, controller: str, type_name: str, uuid: str, data: dict):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.set(module, controller, type_name, uuid, data)


def delete(module: str, controller: str, type_name: str, uuid: str):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.delete(module, controller, type_name, uuid)


def toggle(module: str, controller: str, type_name: str, uuid: str, enabled: str | None = None):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.toggle(module, controller, type_name, uuid, enabled)


def reconfigure(
    module: str, controller: str, action: str = "reconfigure", data: dict | None = None
):
    client = _connect(__resource__["id"])  # type: ignore[name-defined]
    return client.reconfigure(module, controller, action, data=data)
