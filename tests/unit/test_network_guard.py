"""Contract tests for the offline-first guard defined in tests/conftest.py."""

import socket

import pytest
import requests

from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig

# Captured at import (collection) time, before any fixture patches the socket class.
_REAL_CONNECT = socket.socket.connect

# Failed derives from BaseException so ``except Exception`` in production code cannot swallow it.
Failed = pytest.fail.Exception


def test_requests_transport_is_blocked():
    with pytest.raises(Failed, match="Live network access is blocked"):
        requests.Session().get("https://fw-01.example.com/api/core/firmware/status")


def test_client_call_cannot_reach_the_network():
    client = OPNsenseClient(
        OPNsenseClientConfig(host="fw-01.example.com", api_key="k", api_secret="s")
    )
    with pytest.raises(Failed, match="POST https://fw-01.example.com/api/"):
        client.search("unbound", "settings", "host_alias")


def test_guard_failure_is_not_swallowed_by_broad_except():
    swallowed = False
    with pytest.raises(Failed):
        try:
            requests.Session().get("https://fw-01.example.com/")
        except Exception:  # noqa: BLE001 - mirrors the swallow-everything pattern in states/modules
            swallowed = True
    assert swallowed is False


@pytest.mark.parametrize("address", [("192.0.2.10", 443), ("2001:db8::1", 443, 0, 0)])
def test_non_loopback_socket_connect_is_blocked(address):
    family = socket.AF_INET6 if ":" in address[0] else socket.AF_INET
    with socket.socket(family, socket.SOCK_STREAM) as sock, pytest.raises(Failed):
        sock.connect(address)
    with socket.socket(family, socket.SOCK_STREAM) as sock, pytest.raises(Failed):
        sock.connect_ex(address)


def test_loopback_socket_connect_is_allowed():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(server.getsockname())


@pytest.mark.allow_network
def test_allow_network_marker_disables_the_guard():
    assert socket.socket.connect is _REAL_CONNECT
    assert requests.adapters.HTTPAdapter.send.__qualname__ == "HTTPAdapter.send"
