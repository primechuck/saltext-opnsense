# Development (Salt 3008+ Resources only)

Requires `salt>=3008`. Resources-only.

## Layout

```
src/saltext/opnsense/
  utils/opnsense.py               — Client 3008+ only, close() + context manager
  utils/api_spec.py               — Spec loader 76 modules for 26.7.3, lru_cache
  utils/models.py                 — Model relation_targets
  utils/diff.py                   — Diff engine, bool/CSV/UUID/FQDN normalization
  utils/common.py                 — helpers
  utils/controllers.json          — 76 modules + meta core_ref
  utils/models.json               — Model registry 653K
  modules/opnsense.py             — Exec generic + dynamic 1815 funcs __getattr__
  modules/{acmeclient,bind,dns,firewall,kea,unbound}.py — Convenience listers
  states/opnsense.py              — Generic item_present/absent
  states/{bind,dns,unbound}.py    — Convenience states
  resources/opnsense/__init__.py  — Connection module 3008+ Resources
  resources/opnsense/modules/     — Thin delegation __resource_funcs__
  resources/opnsense/states/      — Re-export via namespaced_function
  py.typed                        — PEP 561
tools/
  generate_spec.py                — core/plugins -> controllers.json
  generate_models.py              — Model XML -> models.json
  generate_all.py                 — pipeline: spec->models->verify->test
  verify_import.py                — import proof 76 modules, 1815 dynamic
  check_public_boundary.py        — public boundary guard
tests/unit/                       — mocked, no live OPNsense
tests/integration/                — live gated OPNSENSE_LIVE_TEST=1
docs/                             — QUICKSTART, STATES, API, etc.
```

No proxy code ships — removed 1.0.0. Only `resources/opnsense/` remains.

## Salt 3008+ notes

- Packaging entry-point `salt.loader` -> `saltext.opnsense`, `setuptools_scm` no-local-version
- Builtins `__opts__`, `__salt__`, `__context__`, `__grains__`, `__utils__`, `__pillar__`, `__resource__` declared in `pyproject.toml`
- Install `salt-pip install -e .` into onedir
- Resources store client in `__context__[opnsense][conns][id]` per-resource, Lock thread-safety
- State supports `test=True`

## Running tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

PYTHONPATH=src pytest tests/unit -v
make test

PYTHONPATH=src python3 tools/verify_import.py -v
make verify

ruff check src tests tools
make lint

# Nox matrix
nox -e tests

# Live smoke read-only
OPNSENSE_HOST=fw-01.example.com OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... python tools/test_live.py
OPNSENSE_LIVE_TEST=1 PYTHONPATH=src pytest tests/integration -v -k live
```

## Codegen

```bash
make gen-all CORE_REF=26.7.3 PLUGINS_REF=26.7.3
make gen-spec
make verify
```

See `tools/README.md`.

## CI — hard-fail guards

- `ci.yml`: matrix 3.10-3.14 x 3008.11/latest =10 jobs, pytest --cov-fail-under=75 hard-fail, docs `sphinx-build -W -n` hard-fail
- `lint.yml`: ruff github format + check-json + public-boundary + actionlint, no pylint
- `check_public_boundary.py` scans repo for private strings (lab nets, monorepo path, legacy proxy id) — must PASS

## Parallel development

Worktrees per feature branch — each branch own checkout + .venv, no file clobber:

```bash
./tools/scripts/parallel-dev.sh ls
./tools/scripts/parallel-dev.sh new feat/my-feature main
```

Or hermes kanban: `hermes kanban create "fix alias diff" --project saltext-opnsense --workspace worktree`

When task completes, worktree auto-pruned if clean + pushed.

## Sprint / release checklist (was MAINTENANCE.md)

OPNsense ~2/year (25.1, 25.7). Must stay in sync — only `make bump CORE=X.Y` to regenerate from upstream.

1. Bump: `make bump CORE=26.7.3` or `python tools/generate_spec.py --core-ref 26.7.3 --output src/saltext/opnsense/utils/controllers.json`
2. Verify: `PYTHONPATH=src python3 tools/verify_import.py -v && PYTHONPATH=src pytest tests/unit -v && ruff check src tests`
3. Live smoke (lab only): `salt -C 'T@opnsense:fw-01' opnsense.ping && salt -C 'T@opnsense:fw-01' opnsense.doctor`
4. Commit, PR, tag `v*.*.*` -> publish.yml OIDC to PyPI
5. After merge: `salt '*' saltutil.sync_all` + `opnsense.doctor`

Renovate tracks `controllers.json` meta `core_ref` for auto-bump PRs.

`setuptools_scm` version from git tags `vX.Y.Z`, no `+gHASH`. Writes `_version.py` gitignored.
