# Contributing — saltext-opnsense

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"  # dev: pytest, ruff, towncrier, nox
# or:
pip install -e . && pip install pytest ruff towncrier requests "salt>=3008"

# generate everything (spec + wrappers + verify + sync)
make gen-all
# or manually:
make gen-spec
make gen-wrappers
make verify
```

## Running tests

```bash
# unit (no live OPNsense, mocked)
PYTHONPATH=src pytest tests/unit -v

# import proof: 76 exec + 76 state + 1816 dynamic wrappers
PYTHONPATH=src python3 tools/verify_import.py
PYTHONPATH=src python3 tools/verify_import.py

# lint
ruff check src tests tools
ruff format src tests tools --check

# full nox matrix (needs salt installed)
nox -e tests
nox -e lint

# live smoke (read-only, no Salt) against opnsense-router
OPNSENSE_HOST=opnsense.example.com OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... python tools/test_live.py
# or:
python tools/test_live.py --host opnsense.example.com --key $KEY --secret $SECRET

# integration (gated, live)
OPNSENSE_LIVE_TEST=1 PYTHONPATH=src pytest tests/integration -v -k live
```

## Adding a new test

Tests live in `tests/unit/`:
- `utils/test_client.py` — mock `requests.Session.request`, test `OPNsenseClient.search/get/add`
- `modules/test_modules_opnsense.py` — mock `_get_client`, test execution module proxy/direct branching
- `states/test_opnsense.py` — mock `__salt__` (search/add/set/del), test `item_present/absent` idempotency
- `test_free_modules_import.py` — proves all 76 generated wrappers import

Example:

```python
from unittest.mock import MagicMock, patch
from saltext.opnsense.utils.opnsense import OPNsenseClient, OPNsenseClientConfig

@patch("saltext.opnsense.utils.opnsense.requests.Session.request")
def test_my_feature(mock_req):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"rows": [], "total": 0}
    mock_resp.text = '{"rows":[]}'
    mock_req.return_value = mock_resp
    cfg = OPNsenseClientConfig(host="opnsense-router", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    res = client.search("unbound", "settings", "host_alias", search_phrase="www")
    assert "rows" in res
```

Run `pytest tests/unit -v --collect-only` to verify discovery.

## Regenerating code

- Spec: `tools/generate_spec.py --core-ref 25.7 --plugins-ref 25.7 --output src/saltext/opnsense/utils/controllers.json`
- Wrappers: `tools/generate_wrappers.py` (emits 76 exec + 76 state modules)
- Verify: `tools/verify_import.py`
`make gen-all` does all three in order.

## Changelog — towncrier

We use towncrier. Fragments live in `changelog/`:

```
changelog.feature.  — new features
changelog.bugfix.   — bug fixes
changelog.doc.      — docs
changelog.removal.  — deprecation/removal
changelog.misc.     — trivial (no changelog entry)
```

Create fragment:

```bash
towncrier create 123.feature --edit
# writes changelog/123.feature.md with your text
# commit it with your PR
```

Build on release:

```bash
towncrier build --version 0.2.0
# appends to CHANGELOG.md, deletes fragments
```

A changelog fragment is optional for small PRs but encouraged.

## Submitting PR

1. Branch from `main`: `git checkout -b fix/unbound-search`
2. Make change + regenerate if needed: `make gen-all`
3. Run `PYTHONPATH=src pytest tests/unit -v` and `tools/verify_import.py`
4. Run `ruff check src tests tools`
5. Add towncrier fragment: `towncrier create <pr>.feature --edit`
6. Push, open PR to `main` at `https://github.com/primechuck/saltext-opnsense`. Mention Renovate / OPNsense version if relevant.

See `docs/MAINTENANCE.md` for OPNsense release sprint workflow.

## Code style

- `ruff` with `line-length=100`, `target-version=py310`
- Builtins allowed: `__opts__`, `__salt__`, `__proxy__`, `__context__`, `__grains__`, `__utils__` (declared in `pyproject.toml`)
- No comments unless comstream — rely on docstrings in generated wrappers
- Prefer `file-based` vs `pip install` note in docs when adding new modules
