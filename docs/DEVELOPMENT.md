# Development (Salt 3008+ Resources only)

Requires `salt>=3008`. Resources-only.

## Layout

```
src/saltext/opnsense/
  utils/opnsense.py               — Client 3008+ only, close() + context manager
  utils/api_spec.py               — Spec loader 76 modules for 26.7.3, lru_cache
  utils/models.py                 — Model relation_targets
  utils/diff.py                   — Diff engine, bool/CSV/UUID/FQDN normalization
  utils/common.py                 — helpers, strip_salt_internal_kwargs
  utils/controllers.json          — 76 modules + meta core_ref
  utils/models.json               — Model registry
  modules/opnsense.py             — Exec generic + dynamic 1815 funcs __getattr__
  modules/{acmeclient,bind,dns,firewall,kea,unbound}.py — Convenience listers
  states/opnsense.py              — Generic item_present/absent
  states/{bind,dns,unbound}.py    — Convenience states
  resources/opnsense/__init__.py  — Connection module 3008+ Resources
  resources/opnsense/modules/     — Thin delegation __resource_funcs__
  resources/opnsense/states/      — Re-export via namespaced_function
  resources/opnsense/grains/      — Resource grains
  py.typed                        — PEP 561
tools/
  generate_spec.py                — codegen core/plugins → controllers.json
  generate_models.py              — Model XML → models.json
  generate_wrappers.py            — spec → wrappers (optional)
  generate_all.py                 — pipeline: spec→models→wrappers→sync→verify→test
  verify_import.py                — import proof 76 modules, 1815 dynamic
  test_live.py                    — read-only live smoke via env
  sync_extmods.py                 — sync src → extmods Resources-only, no _proxy/_grains
  scripts/parallel-dev.sh         — isolated worktrees for parallel branches
tests/unit/                       — mocked, no live OPNsense
tests/integration/                — live gated OPNSENSE_LIVE_TEST=1
docs/                             — QUICKSTART, RESOURCES, USAGE, etc.
```

No proxy code ships — removed 1.0.0. Only `resources/opnsense/` remains.

## Salt 3008+ notes

- Packaging entry-point `salt.loader` → `saltext.opnsense`, `setuptools_scm` no-local-version
- Builtins `__opts__`, `__salt__`, `__context__`, `__grains__`, `__utils__`, `__pillar__`, `__resource__`, `__resource_funcs__`, `__minion__` — declared in `pyproject.toml` `tool.ruff.builtins`
- Install `salt-pip install -e .` into onedir
- Resources store client in `__context__[opnsense][conns][id]` per-resource, Lock thread-safety
- Thin overrides use `__resource_funcs__` + `__resource__[id]`
- State supports `test=True`

## Running tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Unit
PYTHONPATH=src pytest tests/unit -v
make test

# Import proof
PYTHONPATH=src python3 tools/verify_import.py -v
make verify

# Lint
ruff check src tests tools
ruff format --check src tests tools
make lint

# Nox matrix
nox -e tests
nox -e lint

# Live smoke read-only
OPNSENSE_HOST=... OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... python tools/test_live.py

# Integration gated
OPNSENSE_LIVE_TEST=1 PYTHONPATH=src pytest tests/integration -v -k live
```

## Codegen

```bash
make gen-all CORE_REF=26.7.3 PLUGINS_REF=26.7.3
make gen-spec
make gen-wrappers
make verify
```

See MAINTENANCE.md sprint, tools/README.md.

## Parallel development

Safe parallel branches via git worktrees — each branch own checkout + .venv, no file clobber (see `docs/plans/parallel-workspace.md`):

```bash
./tools/scripts/parallel-dev.sh ls
./tools/scripts/parallel-dev.sh new feat/my-feature main
cd .worktrees/feat__my-feature
source .venv/bin/activate
make verify && make test
```

Or hermes kanban: `hermes kanban create "fix alias diff" --project saltext-opnsense --workspace worktree`

When task completes, worktree auto-pruned if clean + pushed.
