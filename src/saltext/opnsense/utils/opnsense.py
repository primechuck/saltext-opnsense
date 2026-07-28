import json
import logging
import time
import warnings
from dataclasses import dataclass
from http.client import RemoteDisconnected
from typing import Any
from urllib.parse import urljoin

import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning, ProtocolError

log = logging.getLogger(__name__)

try:
    from requests.exceptions import ChunkedEncodingError as _ChunkedError
except Exception:  # pragma: no cover
    _ChunkedError = ProtocolError  # type: ignore

_RETRYABLE = (RemoteDisconnected, ProtocolError, _ChunkedError, requests.exceptions.ConnectionError)
_MAX_RETRIES = 3
_BACKOFF_BASE = 0.5

_SENSITIVE_KEYS = {
    "api_secret",
    "password",
    "key",
    "token",
    "psk",
    "secret",
    "private_key",
}


def _mask_sensitive_data(data: Any) -> Any:
    """
    Mask sensitive keys in dict/list payloads with "***" for logging.
    """
    if isinstance(data, dict):
        masked = {}
        for k, v in data.items():
            if isinstance(k, str) and k.lower() in _SENSITIVE_KEYS:
                masked[k] = "***"
            else:
                masked[k] = _mask_sensitive_data(v)
        return masked
    elif isinstance(data, list):
        return [_mask_sensitive_data(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(_mask_sensitive_data(item) for item in data)
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
    enable_fallback: bool = False

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
            enable_fallback=bool(
                data.get("enable_fallback")
                or data.get("fallback_mode")
                or data.get("fallback")
                or False
            ),
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
            warnings.simplefilter("ignore", InsecureRequestWarning)
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
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )
        self.session.verify = config.verify_ssl
        self._base = config.base_url()

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
        elif method_up == "POST":
            kwargs["data"] = json.dumps({})

        last_exc: Exception | None = None
        resp = None
        for attempt in range(1, _MAX_RETRIES + 1):
            try:
                resp = self.session.request(method_up, url, **kwargs)
                break
            except _RETRYABLE as exc:
                last_exc = exc
                msg = str(exc).lower()
                is_retryable = (
                    isinstance(exc, _RETRYABLE)
                    or "remotedisconnected" in msg
                    or "protocolerror" in msg
                    or "connection aborted" in msg
                    or "connection reset" in msg
                )
                if not is_retryable or attempt >= _MAX_RETRIES:
                    log.error(
                        "OPNsense %s %s failed after %d attempts: %s",
                        method_up,
                        url,
                        attempt,
                        exc,
                    )
                    raise OPNsenseAPIError(f"{method_up} {url} failed after {attempt} attempts: {exc}") from exc

                sleep = _BACKOFF_BASE * (2 ** (attempt - 1))
                log.warning(
                    "OPNsense %s %s failed %s (attempt %d/%d) retrying after %.1fs",
                    method_up,
                    url,
                    exc,
                    attempt,
                    _MAX_RETRIES,
                    sleep,
                )
                time.sleep(sleep)
                continue
            except Exception as exc:
                txt = str(exc).lower()
                if "remotedisconnected" in txt or "protocolerror" in txt:
                    last_exc = exc
                    if attempt >= _MAX_RETRIES:
                        raise OPNsenseAPIError(
                            f"{method_up} {url} failed after {attempt} attempts: {exc}"
                        ) from exc
                    sleep = _BACKOFF_BASE * (2 ** (attempt - 1))
                    log.warning(
                        "OPNsense %s %s failed %s (attempt %d/%d) retrying after %.1fs",
                        method_up,
                        url,
                        exc,
                        attempt,
                        _MAX_RETRIES,
                        sleep,
                    )
                    time.sleep(sleep)
                    continue
                raise

        if resp is None:
            if last_exc:
                raise OPNsenseAPIError(f"{method_up} {url} failed after {_MAX_RETRIES}: {last_exc}") from last_exc
            raise OPNsenseAPIError(f"{method_up} {url} failed: no response")

        if resp.status_code >= 400:
            if resp.text:
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

        if j.get("result") == "failed" or (isinstance(j.get("validations"), dict) and bool(j.get("validations"))):
            vals = j.get("validations") if isinstance(j.get("validations"), dict) else {}
            err_msg = j.get("errorMessage") or j.get("error") or j.get("message")
            if err_msg and not vals:
                msg = f"validation failed for {module}/{controller}/{action}: {err_msg}"
            else:
                msg = f"validation failed for {module}/{controller}/{action}: {vals}"
            raise OPNsenseValidationError(msg, validations=vals)

        result_val = j.get("result")
        status_val = j.get("status")
        has_error_msg = "errorMessage" in j and bool(j.get("errorMessage"))
        has_error = "error" in j and bool(j.get("error"))

        if (
            result_val in ("failed", "error")
            or status_val in ("error", "failed")
            or has_error_msg
            or has_error
        ):
            err_detail = (
                j.get("errorMessage")
                or j.get("error")
                or j.get("message")
                or (f"status={status_val}" if status_val is not None else None)
                or (f"result={result_val}" if result_val is not None else None)
                or j
            )
            raise OPNsenseAPIError(f"API error for {module}/{controller}/{action}: {err_detail}")

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

        if method == "GET" and data is not None:
            params = data
            data = None
        else:
            params = None

        if method == "POST" and data is None:
            data = {}

        result = self.request(method, module, controller, action, uuid=uuid, data=data, params=params)

        if action.startswith("search") and isinstance(result, dict):
            rows = result.get("rows", [])
            if isinstance(rows, dict):
                result["rows"] = list(rows.values())

        return result

    def _snake_to_pascal(self, snake: str) -> str:
        return "".join(part.capitalize() for part in snake.split("_") if part)

    def _candidate_actions(self, verb: str, type_name: str | None) -> list[str]:
        cands: list[str] = []
        if not type_name:
            cands.append(verb)
            return cands

        tn = type_name.strip()
        if tn.startswith(f"{verb}_") or tn.startswith(f"{verb}{self._snake_to_pascal(tn)[:1]}"):
            cands.append(tn)
            return cands

        snake = tn.lower()
        pascal = self._snake_to_pascal(snake)

        if verb == "search":
            cands.extend(
                [
                    f"{verb}_{snake}",
                    f"{verb}{pascal}",
                    f"{verb}_{snake}s",
                    f"{verb}{pascal}s",
                ]
            )
        elif verb == "get":
            cands.extend([f"{verb}_{snake}", f"{verb}{pascal}", f"{verb}"])
        elif verb == "add":
            cands.extend([f"{verb}_{snake}", f"{verb}{pascal}", f"{verb}", f"{verb}Item"])
        elif verb == "set":
            cands.extend([f"{verb}_{snake}", f"{verb}{pascal}", f"{verb}"])
        elif verb == "del":
            cands.extend([f"{verb}_{snake}", f"{verb}{pascal}", f"{verb}", f"del{pascal}", f"delete_{snake}", f"delete{pascal}"])
        elif verb == "toggle":
            cands.extend([f"{verb}_{snake}", f"{verb}{pascal}", f"{verb}"])

        cands.append(verb)

        return list(dict.fromkeys(cands))

    def _resolve_via_spec(
        self,
        module: str,
        controller: str,
        verb: str,
        type_name: str | None,
        enable_fallback: bool | None = None,
    ) -> list[str]:
        fallback_enabled = (
            enable_fallback
            if enable_fallback is not None
            else getattr(self.config, "enable_fallback", False)
        )
        try:
            from saltext.opnsense.utils.api_spec import list_actions

            available = list_actions(module, controller)
            if not available:
                return self._candidate_actions(verb, type_name)

            available_lower = {a.lower(): a for a in available}
            cands = self._candidate_actions(verb, type_name)

            exact_matches: list[str] = []
            for cand in cands:
                if cand.lower() in available_lower:
                    matched = available_lower[cand.lower()]
                    if matched not in exact_matches:
                        exact_matches.append(matched)

            resolved: list[str] = list(exact_matches)

            if not exact_matches or fallback_enabled:
                for a in available:
                    if a.lower().startswith(verb.lower()):
                        if a not in resolved:
                            if type_name:
                                low_type = type_name.lower().replace("_", "")
                                if low_type in a.lower() or not any(
                                    x in a.lower() for x in ["item", "rule", "domain", "record"]
                                ):
                                    resolved.append(a)
                                else:
                                    if a.lower() == verb.lower():
                                        resolved.append(a)
                            else:
                                if a not in resolved:
                                    resolved.append(a)

            if not resolved:
                return cands

            if not fallback_enabled:
                return resolved[:1]

            return resolved
        except Exception:
            return self._candidate_actions(verb, type_name)

    def _call_with_fallback(
        self,
        module: str,
        controller: str,
        candidates: list[str],
        uuid: str | None = None,
        data: dict | None = None,
        enable_fallback: bool | None = None,
    ) -> dict:
        fallback_enabled = (
            enable_fallback
            if enable_fallback is not None
            else getattr(self.config, "enable_fallback", False)
        )
        try:
            from saltext.opnsense.utils.api_spec import list_actions

            available = list_actions(module, controller)
            is_authoritative = bool(available)
        except Exception:
            is_authoritative = False

        last_exc = None
        log.debug("OPNsense %s/%s candidates %s", module, controller, candidates)
        for i, action in enumerate(candidates):
            attempt = i + 1
            try:
                log.debug(
                    "OPNsense trying %s/%s/%s [%d/%d]",
                    module,
                    controller,
                    action,
                    attempt,
                    len(candidates),
                )
                return self.call(module, controller, action, uuid=uuid, data=data, method="POST")
            except OPNsenseAPIError as exc:
                msg = str(exc)
                is_404 = "404" in msg or "Endpoint not found" in msg or "not found" in msg.lower()
                if is_404:
                    if is_authoritative and not fallback_enabled:
                        if i + 1 < len(candidates):
                            next_cand = candidates[i + 1]
                            if next_cand.split("/")[0] != action.split("/")[0]:
                                log.debug(
                                    "OPNsense spec is authoritative for %s/%s; suppressing speculative 404 probing for candidate %s (%d/%d): %s",
                                    module,
                                    controller,
                                    action,
                                    attempt,
                                    len(candidates),
                                    msg[:300],
                                )
                                raise exc
                        else:
                            raise exc

                    log.debug(
                        "OPNsense endpoint not found fallback %s/%s/%s -> %s (try %d/%d): %s",
                        module,
                        controller,
                        action,
                        candidates[i + 1] if i + 1 < len(candidates) else "end",
                        attempt,
                        len(candidates),
                        msg[:300],
                    )
                    last_exc = exc
                    continue
                raise
        if last_exc:
            log.warning(
                "OPNsense all candidates failed for %s/%s tried %s last=%s",
                module,
                controller,
                candidates,
                last_exc,
            )
            raise last_exc
        raise OPNsenseAPIError(f"no candidates succeeded for {module}/{controller} tried {candidates}")

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
        enable_fallback: bool | None = None,
    ) -> dict:
        payload: dict[str, Any] = {
            "current": current,
            "rowCount": row_count,
            "searchPhrase": search_phrase,
        }
        if sort:
            payload["sort"] = sort
        if extra:
            payload.update(extra)

        candidates = self._resolve_via_spec(
            module, controller, "search", type_name, enable_fallback=enable_fallback
        )
        return self._call_with_fallback(
            module, controller, candidates, data=payload, enable_fallback=enable_fallback
        )

    def get(
        self,
        module: str,
        controller: str,
        type_name: str | None = None,
        uuid: str | None = None,
        enable_fallback: bool | None = None,
    ) -> dict:
        candidates = self._resolve_via_spec(
            module, controller, "get", type_name, enable_fallback=enable_fallback
        )
        return self._call_with_fallback(
            module, controller, candidates, uuid=uuid, data={}, enable_fallback=enable_fallback
        )

    def add(
        self,
        module: str,
        controller: str,
        type_name: str,
        data: dict,
        enable_fallback: bool | None = None,
    ) -> dict:
        candidates = self._resolve_via_spec(
            module, controller, "add", type_name, enable_fallback=enable_fallback
        )
        return self._call_with_fallback(
            module, controller, candidates, data=data, enable_fallback=enable_fallback
        )

    def set(
        self,
        module: str,
        controller: str,
        type_name: str,
        uuid: str,
        data: dict,
        enable_fallback: bool | None = None,
    ) -> dict:
        candidates = self._resolve_via_spec(
            module, controller, "set", type_name, enable_fallback=enable_fallback
        )
        return self._call_with_fallback(
            module, controller, candidates, uuid=uuid, data=data, enable_fallback=enable_fallback
        )

    def delete(
        self,
        module: str,
        controller: str,
        type_name: str,
        uuid: str,
        enable_fallback: bool | None = None,
    ) -> dict:
        candidates = self._resolve_via_spec(
            module, controller, "del", type_name, enable_fallback=enable_fallback
        )
        return self._call_with_fallback(
            module, controller, candidates, uuid=uuid, data={}, enable_fallback=enable_fallback
        )

    def toggle(
        self,
        module: str,
        controller: str,
        type_name: str,
        uuid: str,
        enabled: str | None = None,
        enable_fallback: bool | None = None,
    ) -> dict:
        base_cands = self._resolve_via_spec(
            module, controller, "toggle", type_name, enable_fallback=enable_fallback
        )
        cands: list[str] = []
        for base in base_cands:
            if enabled is not None:
                cands.append(f"{base}/{enabled}" if "/" not in base else base)
            cands.append(base)
        return self._call_with_fallback(
            module, controller, cands, uuid=uuid, data={}, enable_fallback=enable_fallback
        )

    def reconfigure(self, module: str, controller: str, action: str = "reconfigure", data: dict | None = None) -> dict:
        if data is None:
            data = {}
        return self.call(module, controller, action, data=data, method="POST")

    def service_action(self, module: str, controller: str, action: str) -> dict:
        return self.call(module, controller, action, method="POST", data={})


def get_client_from_opts(opts: dict, pillar: dict | None = None) -> OPNsenseClient:
    cfg_sources = []

    if pillar and isinstance(pillar, dict):
        if "opnsense" in pillar:
            cfg_sources.append(("pillar:opnsense", pillar["opnsense"]))
        if "proxy" in pillar:
            cfg_sources.append(("pillar:proxy", pillar["proxy"]))

    if isinstance(opts, dict):
        if "opnsense" in opts:
            cfg_sources.append(("opts:opnsense", opts["opnsense"]))
        if "proxy" in opts:
            cfg_sources.append(("opts:proxy", opts["proxy"]))

    merged: dict[str, Any] = {}
    sources_used: list[str] = []
    for src_name, src in cfg_sources:
        if isinstance(src, dict) and src:
            merged.update(src)
            sources_used.append(src_name)

    if not merged:
        merged = opts if isinstance(opts, dict) else {}
        if merged:
            sources_used.append("opts:root")

    log.debug("OPNsense config sources merged %s keys=%s", sources_used, list(merged.keys()))

    required = ["host", "api_key", "api_secret"]
    alt = {"api_key": ["key", "username"], "api_secret": ["secret", "password"]}
    for field in required:
        if field not in merged or not merged[field]:
            for a in alt.get(field, []):
                if a in merged and merged[a]:
                    merged[field] = merged[a]
                    break
        if field not in merged or not merged[field]:
            raise OPNsenseAPIError(
                f"missing OPNsense config {field}; configure pillar opnsense: host, api_key, api_secret"
            )

    config = OPNsenseClientConfig.from_dict(merged)
    return OPNsenseClient(config)
