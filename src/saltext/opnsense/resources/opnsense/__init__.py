"""Connection module for Salt Resource type ``opnsense`` – API-only, hosts-only."""

import logging
from typing import Any, Final

log = logging.getLogger(__name__)

try:
    from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig

    HAS_DEPS = True
    HAS_DEPS_ERROR = ""
except Exception as exc:
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
    except Exception:
        pillar = opts.get("pillar", {}) if isinstance(opts, dict) else {}
        if not pillar and "__pillar__" in globals():
            try:
                pillar = __pillar__  # type: ignore[name-defined]
            except Exception:
                pillar = {}
        resources = pillar.get("resources", {}) if isinstance(pillar, dict) else {}
        if (
            isinstance(resources, dict)
            and "opnsense" in resources
            and isinstance(resources["opnsense"], dict)
        ):
            inner = resources["opnsense"]
            return inner if "hosts" in inner else resources
        if isinstance(resources, dict) and "hosts" in resources:
            return resources
        if (
            isinstance(pillar, dict)
            and "opnsense" in pillar
            and isinstance(pillar["opnsense"], dict)
        ):
            return pillar["opnsense"]
        return {}


def _normalize_hosts(tree: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if not isinstance(tree, dict):
        return {}
    hosts = tree.get("hosts")
    if isinstance(hosts, dict):
        return {str(k): (v if isinstance(v, dict) else {}) for k, v in hosts.items()}
    return {}


def _connect(resource_id: str) -> Any:
    ctx = _ctx()
    conns = ctx.setdefault(CONN_KEY, {})
    if resource_id in conns:
        return conns[resource_id]
    hosts = ctx.get(HOSTS_KEY, {})
    cfg_dict = hosts.get(resource_id)
    if not isinstance(cfg_dict, dict):
        try:
            tree = _pillar_tree(__opts__)  # type: ignore[name-defined]
            normalized = _normalize_hosts(tree)
            cfg_dict = normalized.get(resource_id)
        except Exception:
            cfg_dict = None
    if not isinstance(cfg_dict, dict) or not cfg_dict:
        raise Exception(
            f"OPNsense resource {resource_id} config not found in pillar resources:opnsense:hosts"
        )
    cfg = OPNsenseClientConfig.from_dict(cfg_dict)
    client = OPNsenseClient(cfg)
    conns[resource_id] = client
    return client


def __virtual__():
    from saltext.opnsense.utils.common import is_salt_version_ok as _ok

    v = _ok((3008,))
    if v is not True:
        return v
    if not HAS_DEPS:
        return (False, f"deps missing: {HAS_DEPS_ERROR}")
    return True


def init(opts: dict[str, Any]):
    ctx = _ctx()
    if ctx.get(INIT_KEY):
        try:
            tree = _pillar_tree(opts)
            ctx[HOSTS_KEY] = _normalize_hosts(tree)
        except Exception as exc:
            log.debug("init refresh failed: %s", exc)
        return True
    try:
        tree = _pillar_tree(opts)
        ctx[HOSTS_KEY] = _normalize_hosts(tree)
        ctx.setdefault(CONN_KEY, {})
        ctx[INIT_KEY] = True
        return True
    except Exception as exc:
        log.error("init failed: %s", exc)
        ctx[INIT_KEY] = False
        return False


def initialized():
    return _ctx().get(INIT_KEY, False)


def discover(opts: dict[str, Any]):
    try:
        tree = _pillar_tree(opts)
        return list(_normalize_hosts(tree).keys())
    except Exception:
        return []


def grains():
    try:
        rid = __resource__["id"]  # type: ignore[name-defined]
    except Exception:
        return {}
    ctx = _ctx()
    out: dict[str, Any] = {"resource_id": rid, "opnsense_id": rid}
    try:
        client = _connect(rid)
        out["opnsense_host"] = client.config.host
        out["opnsense_proto"] = client.config.proto
    except Exception:
        cfg = ctx.get(HOSTS_KEY, {}).get(rid, {})
        if isinstance(cfg, dict) and cfg.get("host"):
            out["opnsense_host"] = cfg["host"]
        return out
    try:
        fw = client.search("unbound", "settings", "host_alias", row_count=1)
        if isinstance(fw, dict):
            out["opnsense_unbound_alias_count"] = fw.get("total", 0)
    except Exception:
        pass
    try:
        info = client.call("core", "firmware", "status", data={}, method="POST")
        if isinstance(info, dict):
            ver = (
                info.get("product_version")
                or info.get("product_version_string")
                or info.get("product_version")
            )
            if ver:
                out["opnsense_version"] = ver
    except Exception:
        pass
    return out


def shutdown(opts: dict[str, Any] | None = None):
    ctx = _ctx()
    for client in list(ctx.get(CONN_KEY, {}).values()):
        try:
            client.session.close()
        except Exception:
            pass
    __context__.pop(CONTEXT_KEY, None)  # type: ignore[name-defined]
    return True


def ping():
    try:
        rid = __resource__["id"]  # type: ignore[name-defined]
    except Exception:
        return False
    ctx = _ctx()
    client = ctx.get(CONN_KEY, {}).get(rid)
    if not client:
        try:
            client = _connect(rid)
        except Exception:
            return False
    try:
        client.search("unbound", "settings", "host_alias", row_count=1)
        return True
    except Exception:
        return False


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
