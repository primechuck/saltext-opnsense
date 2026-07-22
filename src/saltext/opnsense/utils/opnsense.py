import json
import logging
from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin

import requests
from requests.auth import HTTPBasicAuth

log = logging.getLogger(__name__)


@dataclass
class OPNsenseClientConfig:
    host: str
    api_key: str
    api_secret: str
    proto: str = "https"
    verify_ssl: bool = False
    timeout: int = 30
    base_path: str = "/api/"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "OPNsenseClientConfig":
        return cls(
            host=data["host"],
            api_key=data.get("api_key") or data.get("key") or data.get("username", ""),
            api_secret=data.get("api_secret") or data.get("secret") or data.get("password", ""),
            proto=data.get("proto", "https"),
            verify_ssl=data.get("verify_ssl", False),
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
        log.debug("OPNsense %s %s data=%s", method.upper(), url, data)

        kwargs: dict[str, Any] = {"timeout": self.config.timeout}
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["data"] = json.dumps(data)

        resp = self.session.request(method.upper(), url, **kwargs)

        if resp.status_code >= 400:
            raise OPNsenseAPIError(f"{method} {url} failed {resp.status_code}: {resp.text[:500]}")

        if not resp.text:
            return {}

        try:
            j = resp.json()
        except Exception:
            return {"raw": resp.text}

        if isinstance(j, dict) and j.get("result") == "failed":
            vals = j.get("validations", {})
            raise OPNsenseValidationError(
                f"validation failed for {module}/{controller}/{action}: {vals}", validations=vals
            )

        return j

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
            if action.startswith("search") or action.startswith("get") or action == "status":
                method = "GET" if data is None else "POST"
            else:
                method = "POST"

        if method == "GET" and data is not None:
            params = data
            data = None
        else:
            params = None

        result = self.request(method, module, controller, action, uuid=uuid, data=data, params=params)

        if action.startswith("search") and isinstance(result, dict):
            rows = result.get("rows", [])
            if isinstance(rows, dict):
                result["rows"] = list(rows.values())

        return result

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
        if type_name:
            action = f"search_{type_name}" if not type_name.startswith("search") else type_name
        else:
            action = "search"

        payload: dict[str, Any] = {
            "current": current,
            "rowCount": row_count,
            "searchPhrase": search_phrase,
        }
        if sort:
            payload["sort"] = sort
        if extra:
            payload.update(extra)

        return self.call(module, controller, action, data=payload, method="POST")

    def get(self, module: str, controller: str, type_name: str | None = None, uuid: str | None = None) -> dict:
        if type_name:
            action = f"get_{type_name}" if not type_name.startswith("get") else type_name
        else:
            action = "get"
        return self.call(module, controller, action, uuid=uuid, method="GET")

    def add(self, module: str, controller: str, type_name: str, data: dict) -> dict:
        action = f"add_{type_name}" if not type_name.startswith("add") else type_name
        return self.call(module, controller, action, data=data, method="POST")

    def set(self, module: str, controller: str, type_name: str, uuid: str, data: dict) -> dict:
        action = f"set_{type_name}" if not type_name.startswith("set") else type_name
        return self.call(module, controller, action, uuid=uuid, data=data, method="POST")

    def delete(self, module: str, controller: str, type_name: str, uuid: str) -> dict:
        action = f"del_{type_name}" if not type_name.startswith("del") else type_name
        return self.call(module, controller, action, uuid=uuid, method="POST")

    def toggle(self, module: str, controller: str, type_name: str, uuid: str, enabled: str | None = None) -> dict:
        action = f"toggle_{type_name}" if not type_name.startswith("toggle") else type_name
        if enabled is not None:
            action = f"{action}/{enabled}" if "/" not in action else action
            return self.call(module, controller, action, uuid=uuid, method="POST")
        return self.call(module, controller, action, uuid=uuid, method="POST")

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
            cfg_sources.append(pillar["opnsense"])
        if "proxy" in pillar:
            cfg_sources.append(pillar["proxy"])

    if isinstance(opts, dict):
        if "opnsense" in opts:
            cfg_sources.append(opts["opnsense"])
        if "proxy" in opts:
            cfg_sources.append(opts["proxy"])

    merged: dict[str, Any] = {}
    for src in cfg_sources:
        if isinstance(src, dict):
            merged.update(src)

    if not merged:
        merged = opts

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
