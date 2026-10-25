"""
HTTP client for the OPNsense REST API (``/api/<module>/<controller>/<action>[/<uuid>]``).

Hand-written. The API registry it validates against (``controllers.json``) is generated; see
``AGENTS.md`` and ``tools/README.md``.

Credential resolution
---------------------
``get_client_from_opts`` (non-resource calls) resolves the first match of:

1. ``opts["pillar"]["resources"]["opnsense"]["hosts"]``: the *first* host that has ``host``.
2. ``opts["pillar"]["opnsense"]`` when it has ``host``.
3. The same two pillar shapes in the ``pillar`` argument.
4. ``opts["opnsense"]`` (minion/master config) when it has ``host``.

Salt Resource targets (``T@opnsense:<id>``) are resolved earlier, per resource id, from
``resources:opnsense:hosts:<id>`` by ``resources/opnsense/__init__.py``. Grains and proxy
minion configuration are **not** consulted (proxy support was removed in 1.0.0). Accepted keys:
``host``, ``api_key``/``key``/``username``, ``api_secret``/``secret``/``password``, ``proto``,
``verify_ssl`` (default ``True``), ``timeout``, ``base_path``. Do not invent new auth parameters.

Payload contract: GET vs POST are asymmetric
--------------------------------------------
Reading and writing the same item uses different shapes. Diffing raw GET output against the POST
payload makes a state report changes on every run (a state diff loop). Normalize both sides with
``saltext.opnsense.utils.diff`` first.

* ``get*`` returns the model wrapped by its root key (``{"alias": {...}}``). Option fields
  (dropdowns, multi-selects) are nested maps keyed by option key::

      {"opt1": {"value": "<display label>", "selected": 1}, "opt2": {"value": "...", "selected": 0}}

* ``search*`` returns flat rows (``rows`` is coerced to a list by ``OPNsenseClient.call``), with
  relation fields as UUIDs and no selection maps.
* ``add*`` / ``set*`` expect the model root wrapper with **flat** values: one key, or
  **comma-joined keys** for multi-select (``"opt1,opt2"``), never the nested map or a list.
* Booleans are the strings ``"0"`` / ``"1"``. Relations are UUIDs; resolve natural keys
  (hostname, FQDN, name) to a UUID with ``search*`` before any mutation.
* Mutations are staged. Only the service ``reconfigure`` call applies them; issue it once, and
  only after a mutation actually happened.

Failure contract
----------------
``{"result": "failed", "validations": {...}}`` raises ``OPNsenseValidationError`` (the field
errors are kept on ``.validations``). Other error payloads and HTTP >= 400 raise
``OPNsenseAPIError``. Connection resets are retried (3 attempts, exponential backoff).
``OPNsenseClient.call`` is spec-strict: an action absent from ``controllers.json`` raises
``FileNotFoundError``.
"""

import json
import logging
import time
from dataclasses import dataclass
from http.client import RemoteDisconnected
from typing import Any, Final, TypedDict
from urllib.parse import urljoin

import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning, ProtocolError

log = logging.getLogger(__name__)
try:
    from requests.exceptions import ChunkedEncodingError as _ChunkedError
except Exception:
    _ChunkedError = ProtocolError  # type: ignore

_RETRYABLE: Final = (
    RemoteDisconnected,
    ProtocolError,
    _ChunkedError,
    requests.exceptions.ConnectionError,
)
_MAX_RETRIES: Final = 3
_BACKOFF_BASE: Final = 0.5
_SENSITIVE_KEYS: Final = frozenset(
    {"api_secret", "password", "key", "token", "psk", "secret", "private_key"}
)
_SENSITIVE_SUBSTRINGS: Final = frozenset(
    {"secret", "passwd", "password", "token", "private_key", "psk"}
)


class SelectionOption(TypedDict):
    """One entry of an option field in a ``get*`` response, keyed by its option key."""

    value: str  # display label, not the key
    selected: int  # 1 when chosen, else 0 (diff.py also accepts "1"/"true"/"yes")


class MutationResponse(TypedDict, total=False):
    """
    Envelope returned by ``add*``, ``set*``, ``del*``, ``toggle*`` and ``reconfigure``.

    Exact keys vary by controller, so every key is optional. ``add*`` returns ``result`` plus the
    new ``uuid``; ``reconfigure`` endpoints usually return ``status``.
    """

    result: str  # "saved", "deleted", ... ("failed" is raised, see ValidationErrorResponse)
    status: str  # "ok" / "error" on reconfigure and service endpoints
    uuid: str  # set by add*
    changed: bool
    message: str


class ValidationErrorResponse(TypedDict):
    """
    Body of a rejected ``add*`` / ``set*``; ``OPNsenseClient`` raises it as
    ``OPNsenseValidationError`` and exposes ``validations`` on the exception.
    """

    result: str  # always "failed"
    validations: dict[str, str]  # "<model>.<field>" -> message


class SearchResponse(TypedDict, total=False):
    """Envelope returned by ``search*``; ``rows`` are flat dicts, each carrying a ``uuid``."""

    rows: list[dict[str, Any]]
    rowCount: int
    total: int
    current: int


def _is_sensitive_key(k: str) -> bool:
    lk = k.lower()
    if lk in _SENSITIVE_KEYS:
        return True
    if lk in ("tokens", "keys", "secrets", "passwords", "api_keys"):
        return False
    for sub in _SENSITIVE_SUBSTRINGS:
        if sub in lk and lk != sub + "s":
            return True
    return False


def _mask_sensitive_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {
            k: "***" if isinstance(k, str) and _is_sensitive_key(k) else _mask_sensitive_data(v)
            for k, v in data.items()
        }
    if isinstance(data, list):
        return [_mask_sensitive_data(x) for x in data]
    if isinstance(data, tuple):
        return tuple(_mask_sensitive_data(x) for x in data)
    return data


@dataclass
class OPNsenseClientConfig:
    host: str
    api_key: str
    api_secret: str
    proto: str = "https"
    verify_ssl: bool = True
    timeout: int = 30
    base_path: str = "/api/"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "OPNsenseClientConfig":
        return cls(
            host=data["host"],
            api_key=data.get("api_key") or data.get("key") or data.get("username", ""),
            api_secret=data.get("api_secret") or data.get("secret") or data.get("password", ""),
            proto=data.get("proto", "https"),
            verify_ssl=data.get("verify_ssl", True),
            timeout=int(data.get("timeout", 30)),
            base_path=data.get("base_path", "/api/"),
        )

    def base_url(self) -> str:
        proto = self.proto.rstrip("://")
        host = self.host.strip("/")
        base = self.base_path.strip("/") + "/"
        return f"{proto}://{host}/{base}"


class OPNsenseAPIError(Exception):
    pass


class OPNsenseValidationError(OPNsenseAPIError):
    def __init__(self, msg: str, validations: dict | None = None):
        super().__init__(msg)
        self.validations = validations or {}


class OPNsenseClient:
    def __init__(self, config: OPNsenseClientConfig):
        self.config = config
        if not config.verify_ssl:
            try:
                import urllib3

                urllib3.disable_warnings(InsecureRequestWarning)
            except Exception:
                try:
                    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # type: ignore
                except Exception:
                    pass
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(config.api_key, config.api_secret)
        self.session.headers.update(
            {"Content-Type": "application/json", "Accept": "application/json"}
        )
        self.session.verify = config.verify_ssl
        self._base = config.base_url()
        self._spec = None

    @property
    def _api_spec(self):
        if self._spec is None:
            try:
                from saltext.opnsense.utils import api_spec as _api_spec_mod

                self._spec = _api_spec_mod
            except Exception:
                self._spec = None
        return self._spec

    def close(self) -> None:
        try:
            self.session.close()
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def url_for(self, module: str, controller: str, action: str, uuid: str | None = None) -> str:
        module = module.strip("/").lower()
        controller = controller.strip("/").lower()
        action = action.strip("/")
        path = f"{module}/{controller}/{action}"
        if uuid:
            path = f"{path}/{uuid}"
        return urljoin(self._base, path)

    def request(
        self,
        method: str,
        module: str,
        controller: str,
        action: str,
        uuid: str | None = None,
        data: dict | None = None,
        params: dict | None = None,
        row_count: int | None = None,
    ) -> dict:
        url = self.url_for(module, controller, action, uuid)
        method_up = method.upper()
        if method_up == "POST" and data is None:
            data = {}
        log.debug("OPNsense %s %s data=%s", method_up, url, _mask_sensitive_data(data))
        kwargs: dict[str, Any] = {"timeout": self.config.timeout}
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["data"] = json.dumps(data)
        resp = None
        last_exc = None
        for attempt in range(1, _MAX_RETRIES + 1):
            try:
                resp = self.session.request(method_up, url, **kwargs)
                break
            except _RETRYABLE as exc:
                last_exc = exc
                if attempt >= _MAX_RETRIES:
                    raise OPNsenseAPIError(
                        f"{method_up} {url} failed after {attempt}: {exc}"
                    ) from exc
                time.sleep(_BACKOFF_BASE * (2 ** (attempt - 1)))
            except Exception as exc:
                txt = str(exc).lower()
                if "remotedisconnected" in txt or "protocolerror" in txt:
                    last_exc = exc
                    if attempt >= _MAX_RETRIES:
                        raise OPNsenseAPIError(
                            f"{method_up} {url} failed after {attempt}: {exc}"
                        ) from exc
                    time.sleep(_BACKOFF_BASE * (2 ** (attempt - 1)))
                    continue
                raise
        if resp is None:
            raise OPNsenseAPIError(f"{method_up} {url} no response: {last_exc}") from last_exc
        if resp.status_code >= 400:
            try:
                j = resp.json()
                self._check_json_for_errors(j, module, controller, action)
            except (OPNsenseAPIError, OPNsenseValidationError):
                raise
            except Exception:
                pass
            raise OPNsenseAPIError(f"{method} {url} failed {resp.status_code}: {resp.text[:500]}")
        if not resp.text:
            return {}
        try:
            j = resp.json()
        except Exception:
            return {"raw": resp.text}
        self._check_json_for_errors(j, module, controller, action)
        return j

    def _check_json_for_errors(self, j: Any, module: str, controller: str, action: str) -> None:
        if not isinstance(j, dict):
            return
        if j.get("result") == "failed" or (
            isinstance(j.get("validations"), dict) and j.get("validations")
        ):
            vals = j.get("validations") if isinstance(j.get("validations"), dict) else {}
            err = j.get("errorMessage") or j.get("error") or j.get("message")
            msg = f"validation failed for {module}/{controller}/{action}: {err or vals}"
            raise OPNsenseValidationError(msg, validations=vals)
        if (
            j.get("result") in ("failed", "error")
            or j.get("status") in ("error", "failed")
            or j.get("errorMessage")
            or j.get("error")
        ):
            err = j.get("errorMessage") or j.get("error") or j.get("message") or j
            raise OPNsenseAPIError(f"API error for {module}/{controller}/{action}: {err}")

    def call(
        self,
        module: str,
        controller: str,
        action: str,
        uuid: str | None = None,
        data: dict | None = None,
        method: str | None = None,
    ) -> dict:
        if method is None:
            method = "POST"
        params = None
        if method == "GET" and data is not None:
            params = data
            data = None
        if method == "POST" and data is None:
            data = {}
        spec_mod = self._api_spec
        if spec_mod is not None:
            base_action = action.split("/")[0]
            try:
                has = spec_mod.has_action(module, controller, base_action)
            except AttributeError:
                try:
                    has = base_action in spec_mod.list_actions(module, controller)
                except Exception:
                    has = True
            if not has:
                raise FileNotFoundError(f"unknown {module}/{controller}/{action} – run make bump")
        result = self.request(
            method, module, controller, action, uuid=uuid, data=data, params=params
        )
        if action.startswith("search") and isinstance(result, dict):
            rows = result.get("rows", [])
            if isinstance(rows, dict):
                result["rows"] = list(rows.values())
        return result

    def _snake_to_pascal(self, snake: str) -> str:
        return "".join(p.capitalize() for p in snake.split("_") if p)

    def _resolve_action(
        self, module: str, controller: str, verb: str, type_name: str | None
    ) -> str:
        candidates = []
        if type_name:
            pas = self._snake_to_pascal(type_name)
            candidates.append(f"{verb}{pas}")
            candidates.append(f"{verb}_{type_name}")
        candidates.append(verb)
        spec_mod = self._api_spec
        if spec_mod:
            try:
                avail = spec_mod.list_actions(module, controller)
                lower_map = {a.lower(): a for a in avail}
                for cand in candidates:
                    if not cand:
                        continue
                    if cand in avail:
                        return cand
                    if cand.lower() in lower_map:
                        return lower_map[cand.lower()]
                # spec-strict: if type provided and no matching action found, raise
                if type_name:
                    raise FileNotFoundError(
                        f"unknown {module}/{controller}/{verb}{self._snake_to_pascal(type_name)} – run make bump"
                    )
            except FileNotFoundError:
                raise
            except Exception:
                pass
        return candidates[0] if candidates else verb

    def search(
        self,
        module: str,
        controller: str,
        type_name: str | None = None,
        search_phrase: str = "",
        row_count: int = -1,
        current: int = 1,
        sort: dict | None = None,
        extra: dict | None = None,
    ) -> dict:
        verb_action = self._resolve_action(module, controller, "search", type_name)
        data: dict[str, Any] = {
            "current": current,
            "rowCount": row_count,
            "searchPhrase": search_phrase,
        }
        if sort:
            data["sort"] = sort
        if extra:
            data.update(extra)
        return self.call(module, controller, verb_action, data=data, method="POST")

    def get(
        self, module: str, controller: str, type_name: str | None = None, uuid: str | None = None
    ) -> dict:
        act = self._resolve_action(module, controller, "get", type_name)
        return self.call(
            module,
            controller,
            act,
            uuid=uuid,
            method="GET" if uuid else "POST",
            data={} if not uuid else None,
        )

    def add(self, module: str, controller: str, type_name: str, data: dict) -> dict:
        act = self._resolve_action(module, controller, "add", type_name)
        return self.call(module, controller, act, data=data, method="POST")

    def set(self, module: str, controller: str, type_name: str, uuid: str, data: dict) -> dict:
        act = self._resolve_action(module, controller, "set", type_name)
        return self.call(module, controller, act, uuid=uuid, data=data, method="POST")

    def delete(self, module: str, controller: str, type_name: str, uuid: str) -> dict:
        act = self._resolve_action(module, controller, "del", type_name)
        return self.call(module, controller, act, uuid=uuid, data={}, method="POST")

    def toggle(
        self,
        module: str,
        controller: str,
        type_name: str,
        uuid: str,
        enabled: bool | str | None = None,
    ) -> dict:
        act = self._resolve_action(module, controller, "toggle", type_name)
        if enabled is None:
            return self.call(module, controller, act, uuid=uuid, data={}, method="POST")
        return self.call(
            module,
            controller,
            f"{act}/{1 if enabled else 0}" if isinstance(enabled, bool) else act,
            uuid=uuid,
            data={},
            method="POST",
        )

    def reconfigure(
        self, module: str, controller: str, action: str = "reconfigure", data: dict | None = None
    ) -> dict:
        return self.call(module, controller, action, data=data or {}, method="POST")

    def service_action(self, module: str, controller: str, action: str) -> dict:
        return self.call(module, controller, action, data={}, method="POST")


def get_client_from_opts(opts: dict, pillar: dict | None = None) -> OPNsenseClient | None:
    """
    Build a client from Salt ``opts`` and optional ``pillar``; return ``None`` if no host config.

    Resolution order is documented in the module docstring (Resources pillar, ``opnsense`` pillar,
    ``opts["opnsense"]``). Grains are intentionally ignored. Changing this order or the
    credential key aliases is a human-gated change (see ``AGENTS.md``).
    """
    cfg = None
    try:
        if isinstance(opts, dict):
            p = opts.get("pillar", {})
            if isinstance(p, dict):
                resources = p.get("resources", {})
                if isinstance(resources, dict) and "opnsense" in resources:
                    hosts = (
                        resources["opnsense"].get("hosts", {})
                        if isinstance(resources["opnsense"], dict)
                        else {}
                    )
                    if hosts:
                        first = next(iter(hosts.values()))
                        if isinstance(first, dict) and "host" in first:
                            cfg = first
                if (
                    not cfg
                    and "opnsense" in p
                    and isinstance(p["opnsense"], dict)
                    and "host" in p["opnsense"]
                ):
                    cfg = p["opnsense"]
        if not cfg and pillar and isinstance(pillar, dict):
            if (
                "opnsense" in pillar
                and isinstance(pillar["opnsense"], dict)
                and "host" in pillar["opnsense"]
            ):
                cfg = pillar["opnsense"]
            resources = pillar.get("resources", {})
            if not cfg and isinstance(resources, dict) and "opnsense" in resources:
                hosts = (
                    resources["opnsense"].get("hosts", {})
                    if isinstance(resources["opnsense"], dict)
                    else {}
                )
                if hosts:
                    first = next(iter(hosts.values()))
                    if isinstance(first, dict):
                        cfg = first
    except Exception:
        cfg = None
    if isinstance(opts, dict) and not cfg:
        ocfg = opts.get("opnsense")
        if isinstance(ocfg, dict) and "host" in ocfg:
            cfg = ocfg
    if not cfg or not isinstance(cfg, dict):
        return None
    try:
        cc = OPNsenseClientConfig.from_dict(cfg)
        return OPNsenseClient(cc)
    except Exception:
        return None
