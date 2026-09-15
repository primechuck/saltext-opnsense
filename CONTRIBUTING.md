# Contributing — saltext-opnsense (Salt 3008+ Resources)

Requires `salt>=3008`. Resources-only, no proxy — removed 1.0.0.

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

# import proof: 76 modules + dynamic 1815 wrappers
PYTHONPATH=src python3 tools/verify_import.py

# lint
ruff check src tests tools
ruff format --check src tests tools

# full nox matrix (needs salt installed)
nox -e tests
nox -e lint
nox -e docs

# live smoke (read-only, no Salt) against OPNsense FW
OPNSENSE_HOST=fw-01.example.com OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... python tools/test_live.py
# or:
python tools/test_live.py --host fw-01.example.com --key $KEY --secret $SECRET

# integration (gated, live)
OPNSENSE_LIVE_TEST=1 PYTHONPATH=src pytest tests/integration -v -k live
```

## Adding a new test

Tests live in `tests/unit/`:
- `utils/test_client.py` — mock `requests.Session.request`, test `OPNsenseClient.search/get/add`
- `modules/test_modules_opnsense.py` — mock `_get_client`, test execution module Resources branching
- `states/test_opnsense.py` — mock `__salt__` (search/add/set/del), test `item_present/absent` idempotency
- `test_free_modules_import.py` — proves all 76 generated wrappers import
- `resources/test_*.py` — Resources connection module

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
    cfg = OPNsenseClientConfig(host="fw-01.example.com", api_key="a", api_secret="b")
    client = OPNsenseClient(cfg)
    res = client.search("unbound", "settings", "host_alias", search_phrase="www")
    assert "rows" in res
```

Run `pytest tests/unit -v --collect-only` to verify discovery.

## Regenerating code

- Spec: `tools/generate_spec.py --core-ref 26.7.3 --plugins-ref 26.7.3 --output src/saltext/opnsense/utils/controllers.json`
- Models: `tools/generate_models.py`
- Wrappers: `tools/generate_wrappers.py` (emits 76 exec + state modules + dynamic wrappers)
- Verify: `tools/verify_import.py`
`make gen-all` does all three in order. See `docs/MAINTENANCE.md` sprint workflow.

## Changelog — towncrier

We use towncrier. Fragments live in `changelog/`:

```
changelog/20260910.feature.md — new features
changelog/20260910.bugfix.md  — bug fixes
changelog/20260910.doc.md     — docs
changelog/20260910.removal.md — deprecation/removal
changelog/misc/               — trivial (no changelog entry)
```

Create fragment:

```bash
towncrier create 123.feature --edit
# writes changelog/123.feature.md with your text
# commit it with your PR
```

Build on release:

```bash
towncrier build --version 1.0.0
# appends to CHANGELOG.md, deletes fragments
```

A changelog fragment is optional for small PRs but encouraged.

## Submitting PR

1. Branch from `main`: `git checkout -b fix/unbound-search`
2. Make change + regenerate if needed: `make gen-all`
3. Run `PYTHONPATH=src pytest tests/unit -v` and `tools/verify_import.py`
4. Run `ruff check src tests tools` and `ruff format --check`
5. Add towncrier fragment: `towncrier create <pr>.feature --edit`
6. Push, open PR to `main` at `https://github.com/primechuck/saltext-opnsense`. Mention Renovate / OPNsense version if relevant.

See `docs/MAINTENANCE.md` for OPNsense release sprint workflow.

## Code style

- `ruff` with `line-length=100`, `target-version=py310`, pinned `0.14.8` in CI
- Builtins allowed: `__opts__`, `__salt__`, `__context__`, `__grains__`, `__utils__`, `__pillar__`, `__resource__`, `__resource_funcs__`, `__minion__` (declared in `pyproject.toml` `tool.ruff.builtins`)
- No `_proxy/_grains` legacy — removed 1.0.0 Resources-only
- Prefer Resources targeting `T@opnsense:fw-01` in docs/examples, not legacy minion id
- Docs: Resources-only, `salt>=3008`, no proxy references outside archived legacy

## Parallel development

Isolated worktrees via `tools/scripts/parallel-dev.sh`:

```bash
./tools/scripts/parallel-dev.sh new feat/my-feature main
cd .worktrees/feat__my-feature
source .venv/bin/activate
make verify && make test
```

Or hermes kanban: `hermes kanban create "fix alias diff" --project saltext-opnsense --workspace worktree`
