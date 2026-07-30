# Integration tests (live against opnsense-router)

These tests hit real OPNsense API. Skipped by default.

## Run read-only live tests

```bash
export OPNSENSE_LIVE_TEST=1
export OPNSENSE_HOST=opnsense.example.com
export OPNSENSE_API_KEY=xxx
export OPNSENSE_API_SECRET=yyy
pytest tests/integration/test_live_opnsense.py -v -s
```

Or via Salt proxy file (if you have /etc/salt/proxy with credentials):

```bash
OPNSENSE_LIVE_TEST=1 pytest tests/integration -v
```

Via Salt execution module (alternative, no env vars):

```bash
salt opnsense-router opnsense.ping
salt opnsense-router opnsense.search unbound settings host_alias row_count=-1
```

## Run write tests (creates temp DNS alias then deletes)

```bash
export OPNSENSE_LIVE_TEST=1
export OPNSENSE_LIVE_WRITE=1
pytest tests/integration/test_live_opnsense.py::test_write_temp_alias -v -s
```

Write test creates `test-salt-<random>.example.com` alias pointing to cluster parent, verifies search, then deletes and reconfigures unbound.

## TODO / Future

- WireMock recording: capture `searchHostOverride`, `searchHostAlias`, `searchRecord`, `searchSubnet`, `searchReservation` responses from opnsense-router, store in `tests/fixtures/recordings/`, serve via mock server for CI.
- docker-compose with mock server (e.g., `mockserver/mockserver` or `wiremock`) for fully offline integration.
- Acmeclient live tests (read-only search accounts/certificates).
