# Development (Salt 3008+ Resources only)

Requires `salt>=3008`. Resources-only.

## Layout

```
src/saltext/opnsense/
  utils/opnsense.py               — Client 3008+ only, close() + context manager
  utils/api_spec.py               — Spec loader 93 modules for 26.7.9, lru_cache
  utils/models.py                 — Model relation_targets
  utils/diff.py                   — Diff engine, bool/CSV/UUID/FQDN normalization
  utils/common.py                 — helpers
  utils/controllers.json          — 93 modules + meta core_ref
  utils/models.json               — Model registry 653K
  modules/opnsense.py             — Exec generic + dynamic 2038 funcs __getattr__
  modules/dns.py                  — Convenience Unbound DNS alias listers & preview
  states/opnsense.py              — Generic item_present/absent/reconfigured/assert_resolves
  states/dns.py                   — Pillar-driven opnsense_dns.managed batch state
  resources/opnsense/__init__.py  — Connection module 3008+ Resources
  resources/opnsense/modules/     — Thin delegation __resource_funcs__
  resources/opnsense/states/      — Re-export via namespaced_function
  py.typed                        — PEP 561
tools/
  generate_spec.py                — core/plugins -> controllers.json
  generate_models.py              — Model XML -> models.json
  generate_all.py                 — pipeline: spec->models->verify->test
  verify_import.py                — import proof 93 modules, 2038 dynamic
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
OPNSENSE_LIVE_TEST=1 PYTHONPATH=src pytest tests/integration -v -k live
```

## Codegen

```bash
make gen-all CORE_REF=26.7.9 PLUGINS_REF=26.7.9
make gen-spec
make verify
```

See `tools/README.md`.

## CI — hard-fail guards

- `ci.yml`: matrix 3.12-3.14 x 3008.3/latest =6 jobs, pytest --cov-fail-under=75 hard-fail, docs `sphinx-build -W -n` hard-fail
- `lint.yml`: ruff github format + check-json + public-boundary + actionlint, no pylint
- `check_public_boundary.py` scans repo for private strings (lab nets, monorepo path, legacy proxy id) — must PASS

## Parallel development

Worktrees per feature branch — each branch own checkout + .venv, no file clobber:

```bash
./tools/scripts/parallel-dev.sh ls
./tools/scripts/parallel-dev.sh new feat/my-feature main
```

When task completes, worktree auto-pruned if clean + pushed.

## Sprint / release checklist (was MAINTENANCE.md)

OPNsense ~2/year (25.1, 25.7). Must stay in sync — only `make bump CORE=X.Y` to regenerate from upstream.

1. Bump: `make bump CORE=26.7.9` or `python tools/generate_spec.py --core-ref 26.7.9 --output src/saltext/opnsense/utils/controllers.json`
2. Verify: `PYTHONPATH=src python3 tools/verify_import.py -v && PYTHONPATH=src pytest tests/unit -v && ruff check src tests`
3. Live smoke (lab only): `salt -C 'T@opnsense:fw-01' opnsense.ping && salt -C 'T@opnsense:fw-01' opnsense.doctor`
4. Commit, PR, merge to `main` (a dev build goes to TestPyPI automatically), then cut a release (see below)
5. After merge: `salt '*' saltutil.sync_all` + `opnsense.doctor`

Renovate tracks `controllers.json` meta `core_ref` for auto-bump PRs.

`setuptools_scm` version from git tags `vX.Y.Z`, no `+gHASH`. Writes `_version.py` gitignored.

## Releases: dev and stable

Versions are never written by hand: `setuptools_scm` derives them from git tags.

| Channel | Trigger | Index | Example version | Approval |
|---|---|---|---|---|
| Dev | every push to `main` that passes CI (`publish-dev.yml`) | TestPyPI | `2.0.1.dev3` (3rd commit after `v2.0.0`) | none |
| Stable | pushing a `vX.Y.Z` tag (`publish.yml`) | PyPI | `2.0.0` | `pypi` environment reviewer |

Both use PyPI trusted publishing (OIDC); there are no API tokens in the repository.

### Dev builds

Nothing to do: merge to `main`. Once the `CI` workflow is green the commit is built and uploaded to
TestPyPI. Install one in two steps, dependencies from PyPI first and then only this package from
TestPyPI:

```bash
pip install "salt>=3008" requests urllib3
pip install --pre --no-deps --index-url https://test.pypi.org/simple/ saltext-opnsense
```

Never combine `--index-url https://test.pypi.org/simple/` with `--extra-index-url https://pypi.org/simple/`.
pip takes the highest version across both indexes, and anyone can upload to TestPyPI under the name
of a real dependency (a `jmespath 99.99.99` that runs code at install time already exists there).

### Stable release

1. On a branch, build the changelog and open a PR (this consumes the fragments in `changelog/`):

   ```bash
   towncrier build --version 2.0.0
   ```

2. Merge the PR and wait for CI on `main` to pass.
3. Tag the merge commit on `main` and push the tag:

   ```bash
   git switch main && git pull
   git tag -a v2.0.0 -m "saltext-opnsense 2.0.0"
   git push origin v2.0.0
   ```

4. `publish.yml` runs the full CI suite, builds the sdist and wheel, and refuses to continue unless
   the tag is on `main`, `twine check --strict` passes, and the built version equals the tag.
5. Approve the pending `pypi` deployment in the Actions run. Only then is anything uploaded.

Pre-releases use the same path with a PEP 440 tag such as `v2.1.0rc1`. PyPI versions are immutable:
if a release is bad, yank it on PyPI and tag a new patch version; never move or reuse a tag.

### One-time setup (repository owner)

- PyPI: trusted publisher for workflow `publish.yml`, environment `pypi` (already configured).
- TestPyPI: add a pending trusted publisher for project `saltext-opnsense`, owner `primechuck`,
  repository `saltext-opnsense`, workflow `publish-dev.yml`, environment `testpypi`.
- GitHub: create the `testpypi` environment (no reviewers) and add required reviewers to the `pypi`
  environment (Settings -> Environments).
- Optional: a tag ruleset restricting who can create `v*` tags.
