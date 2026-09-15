# CI & Linting Audit — saltext-opnsense

**Date:** 2026-09-15  
**Auditor:** @salt agent (task t_e32ca980)  
**Scope:** `.github/workflows/*`, `Makefile`, `noxfile.py`, `pyproject.toml`, `.pre-commit-config.yaml`, `README`, formula/SLS presence, tools/, tests/, docs/  
**Upstream comparison:** 5 references — `saltstack-formulas/template-formula`, `salt-formula`, `nginx-formula`, `vault-formula` (formula side), plus `saltstack/salt` and `salt-extensions/saltext-vault` / `saltext-mysql` (saltext side)

---

## 1. Executive Summary

`saltext-opnsense` is a **Python Salt extension** (`saltext`), not a classic Salt formula. Its current CI is **better than the average formula** for Python concerns (ruff, pytest matrix, build check, spec-drift) but **lags behind the saltext-* community standard** established in `salt-extensions/saltext-vault` (and siblings) and behind formula-community hardening (pre-commit container, salt-lint/yamllint/actionlint, pinned actions, coverage).

- **What’s good:** ruff check+format, Python 3.10–3.14 matrix, isolated `verify_import`, `sync_extmods --check`, spec-drift integrity, PEP 561 `py.typed` check, PyPI Trusted Publishing (OIDC), towncrier, nox sessions, Makefile wrapper.
- **What’s missing:** No true pre-commit gate in CI, no YAML strict lint, no salt-lint for the 13 SLS in `docs/tutorials/`, no workflow lint (actionlint / check-jsonschema), no bandit/pylint/typing (ty/mypy), no coverage/codecov, no docs build, no concurrency/caching, no pinned action SHAs, no change-filter optimization.

This audit gives a phased checklist to bring the repo to **saltext-* gold standard** while keeping formula hygiene where relevant (SLS files).

---

## 2. Current State Inventory

### 2.1 GitHub Workflows

**`.github/workflows/ci.yml` (4 jobs, single file, no concurrency)**

| Job | Steps | Comments |
|-----|-------|----------|
| `lint` | checkout@v4, setup-python@v5 py3.11, `pip install ruff`, `ruff check`, `ruff format --check` | Minimal. No pre-commit, no caching, no pinned SHAs |
| `unit` | matrix py 3.10-3.14, checkout, setup-python, `pip install pytest pytest-salt-factories requests salt setuptools + -e .`, `pytest tests/unit -v`, `verify_import.py`, `sync_extmods.py --check` | Good matrix, but no coverage, no artifacts, no uv, installs salt without version pin matrix (only single latest) |
| `spec-drift` | setup py3.11, pip requests, parse `core_ref` from `controllers.json` meta, run `generate_spec.py --core-ref $REF --plugins-ref $REF --output /tmp/controllers.json`, diff ignoring `generated_at`, fail if drift | Excellent project-specific guard! Could cache clones, could also check `models.json` |
| `packaging` | setup py3.11, `build twine`, `python -m build`, `twine check`, `test -f py.typed` | Good, but no import test of sdist/wheel, no `check-manifest` logic |

**`.github/workflows/publish.yml`**

- On `v*.*.*` tags, trusted publishing OIDC (`id-token: write`), checkout with `fetch-depth: 0` for setuptools_scm, build + twine check + `pypa/gh-action-pypi-publish@release/v1`. Correct.

### 2.2 Pre-commit (`/.pre-commit-config.yaml`)

```yaml
- ruff-pre-commit v0.14.8: ruff --fix + ruff-format
- pre-commit-hooks v6.0.0: trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files --maxkb=500, check-merge-conflict
```

- Only 6 hooks, no `mixed-line-ending`, `check-ast`, `pyupgrade`, `isort` (ruff I does it but not strict), `bandit`, `actionlint`, `yamllint`, `salt-lint`, `pylint`, `ty`, `commitlint`.
- No `ci:` auto-fix config (formula template has autofix PRs).
- Docs outdated: shows old `commit-msg` workflow missing.

### 2.3 Python packaging (`pyproject.toml`)

- `setuptools>=68`, `setuptools_scm>=8`, `package-dir src`, `include-package-data`, `py.typed` included.
- `requires-python >=3.10`, classifiers beta, dependencies `salt>=3008`, `requests`, `urllib3`.
- `optional-dependencies:dev` + `dependency-groups:dev` duplicate (good for new uv/pip support) – pytest, pytest-salt-factories, nox, ruff, towncrier.
- `tool.ruff`: line-length 100, target py310, builtins includes `__resource__` etc, lint select E,F,W,C90,I,N, ignore E501,N807,E731,N814,E402, mccabe 50. No config for `tool.ruff.format`.
- No `[tool.mypy]`, `[tool.bandit]`, `[tool.yamllint]`, `[tool.pylint]`.
- No `.pylintrc`.
- towncrier configured.

### 2.4 Nox & Makefile

- `noxfile.py`: 3 sessions – `tests` matrix, `lint` (ruff), `gen_all` (requests). Missing: `lint-code-pre-commit` split, `docs`, coverage, `uv` backend, artifact handling.
- `Makefile`: well-structured, help target, wrappers for gen-spec, gen-models, gen-wrappers, bump, sync, verify, test, lint, gen-all, clean. Good for maintainer ergonomics, not widely used in CI.

### 2.5 Tests

- `tests/unit/*` – 11+ files, good coverage of client, diff engine, modules, states, free modules import, resources.
- `tests/integration/test_live_opnsense.py` gated by `OPNSENSE_LIVE_TEST=1`, README for live.
- `conftest.py` mocks salt if not installed – allows unit without salt – good.
- No coverage measurement, no junit xml, no cv artifacts.

### 2.6 Formula/SLS structure

- This repo is **not a formula** but contains 13 SLS example files under `docs/tutorials/states/*.sls` + pillar examples. Those are currently **not linted** by salt-lint/yamllint. `pillar.example` top-level is example YAML, should pass yamllint.

### 2.7 Docs

- `docs/` has 12+ MD files + Sphinx `conf.py` / `index.rst`, tutorials SLS/pillars. No workflow to build docs or linkcheck.

---

## 3. Upstream Community Standards

### 3.1 saltstack-formulas (template-formula as gold)

**Repo sampled 2026-09-15:** `template-formula@master`, `salt-formula`, `nginx-formula`, `postgres-formula`, `vault-formula`, `docker-formula`

**Pre-commit hooks (template-formula v6.0.0 + extensions):**

- `pre-commit-hooks`: check-merge-conflict
- `mirrors-commitlint` 19.8.1: commitlint + commitlint-ci (conventional commits), stage manual
- `rubocop` 1.91.0: Ruby lint (for kitchen)
- `shellcheck-py` 0.9.0.6: shell
- `yamllint` 1.38.0 --strict, custom `files:` regex including `*.example`, `test/*.sls`, exclude `kitchen.vagrant.yml`, auto-generated `.copier-answers.yml`
- `salt-lint` 0.9.2: lint `*.sls, *.jinja, j2, tmpl, tst`
- `rstcheck` 6.3.0 + `mirrors-rst-lint` 1.4.0: docs
- `renovate-config-validator`
- `check-jsonschema` 0.38.0: check-github-workflows + check-gitlab-ci
- `standard` 17.1.2: JS lint

`.salt-lint` default – skips 205,207,208, excludes [].

`.yamllint` extends default, max line 88, ignores `.bundle/`, `.cache/`, `.git/`, `node_modules/`, `test/**/states/**/*.sls`, `.kitchen/`, `kitchen.vagrant.yml`, pillar heavy Jinja.

**CI workflow (`.github/workflows/main.yml`):**

- Concurrency group per ref, cancel in-progress except default branch.
- `should-run` job using `techneg-it/should-workflow-run@v1.0.1` to skip duplicate runs.
- `pre-commit` job: **container** `techneg/ci-pre-commit:v2.5.59@sha256:...`, caching `~/.cache/pre-commit` keyed by hash, installs hooks then `pre-commit run --all-files --color always --verbose` + `commitlint-ci`.
- `test` job: `ruby/setup-ruby@v1.321.0` ruby 3.1 bundler-cache, `bin/kitchen verify ${{ matrix.platform }}` matrix 15 platforms (debian-13-master, ubuntu-2604-master, 3008, 3006 etc), fail-fast false, timeout 15m, tmate debug.
- `results` job: container `techneg/ci-semantic-release`, `poseidon/wait-for-status-checks@v0.7.0` to wait for required checks, IGNORES list for non-required, `semantic-release --dry-run`.

**Key takeaways vs this repo:** formula side is Ruby+kitchen heavy, Python linting minimal (they delegate to pre-commit container). Our saltext needs Python-heavy CI, not kitchen.

### 3.2 saltstack/salt (master branch)

- **Pre-commit:** enormous file, ~600 lines. Highlights:
  - `pyupgrade --py310-plus` (or py3.9 depending branch) but excludes `salt/ext`, `ssh_py_shim`.
  - `salt-rewrite` 2.5.2 for docstring + test auto-fixes.
  - `isort` 5.13.2, `black` 24.2.0, `blacken-docs`.
  - `bandit` 1.7.7 dual – `bandit-salt` excluding tests and `bandit-tests`.
  - Local hooks: `lint-salt-pre-commit` and `lint-tests-pre-commit` via nox (`nox -e lint-salt-pre-commit`), requirement `nox==2022.11.21`, pip pin 25.2, setuptools pin, python 3.14 interpreter.
  - `mypy` pre-commit mirror for `tools/*` only.
  - `pip-compile` hooks compiling `requirements/static/ci/...` lock files for reproducibility (Linux/Windows/Darwin).
- **Noxfile:** even larger – creates artifacts dir, coverage, `lint-salt`, `lint-tests`, tests sessions, CI optimization env vars, `SKIP_REQUIREMENTS_INSTALL`, `EXTRA_REQUIREMENTS_INSTALL`, handles darwin/windows/literally constraints.
- **CI:** uses nox + pytest + coverage + junit. No single workflow file – many workflows.

**Takeaway:** Shows direction – use nox to run pylint, use bandit, use pyupgrade+isort+black (or ruff equivalent), use pip-compile or uv for lock.

### 3.3 salt-extensions/saltext-vault (representative gold for saltext)

**Workflows (modular, reusable via `workflow_call`):**

- `ci.yml`: calls `get-changed-files.yml` (dorny/paths-filter@ v4.0.1 token) → categorizes into `repo`, `pre-commit`, `release`, `deleted`. Then 4 sub-workflows:
  - `pre-commit-action.yml`: container `python:3.10.20-slim-trixie@sha256:...`, apt installs `enchant-2 git gcc make zlib... libxml2...`, checkout@v7.0.0 pinned, pip install pre-commit, `pre-commit run --all-files` on push or `--files changed` on PR if `pre-commit` filter true.
  - `test-action.yml`: matrix Linux 3 jobs: salt 3006.27 py3.11 vault:1.14.8, 3008.2 py3.10 openbao:latest, 3008.2 py3.14 vault:latest; plus Windows & macOS matrices; sets `TESTING_CONTAINER`, uses `eLco/setup-vault@1.0.4`, `setup-python@v6.3.0` pinned via sha, nox `2026.4.10` + uv `0.11.26`, `nox -e tests-3 --install-only` then `nox -e tests-3 -- -vv --instafail` with `CHANGED_FILES` optimization, uploads coverage to codecov with OIDC, artifacts logs, upload-exitstatus action.
  - `docs-action.yml`: Sphinx build linkcheck coverage html.
  - `package-action.yml`: build wheel/sdist artifact upload.

**Pre-commit (saltext-vault @ 2026-09):**

- `minimum_pre_commit_version 2.4.0`
- `pre-commit-hooks`: check-merge-conflict, trailing-whitespace --markdown-linebreak-ext=md, mixed-line-ending --fix=lf, end-of-file-fixer, check-ast
- `pre-commit-remove-import-headers`
- Local `check-cli-examples` (`.pre-commit-hooks/check-cli-examples.py`), `check-docs` (`make-autodocs.py` pass_filenames false)
- `salt-rewrite` docstrings + tests auto-fixes
- `pyupgrade --py310-plus`
- `isort 8.0.1 --py 310`
- `black 26.5.1 -l 100`
- `blacken-docs`
- `bandit 1.9.4`: bandit-salt + bandit-tests (skip B701)
- Local `nox` lint: `nox -e lint-code-pre-commit` for `setup, noxfile, src` and `lint-tests-pre-commit` for `tests/`, require_serial true, deps `nox==2026.4.10 uv==0.11.26`
- `ty-pre-commit 0.0.59`: `ty --isolated --extra=tests` typing
- `actionlint-py 1.7.11.24 + shellcheck-py 0.11.0.1`

**Noxfile (key):**

- `PYTHON_VERSIONS = "3", "3.10" - "3.14"`
- `nox.options.reuse_existing_virtualenvs = True`, `error_on_missing_interpreters = False`, `default_venv_backend = "uv|virtualenv"`
- `COVERAGE_REQUIREMENT`, `SALT_REQUIREMENT` env controlled, supports `salt==master` and `salt==3006.x`
- `_install_requirements()` with pip constraint `setuptools<75.6.0`, wheel, coverage, salt, tests extras, source install, extras.
- `tests(session)`: session uses `salt-factories --coverage`, sets PYTHONPATH, COVERAGE_FILE, COVERAGE_PROCESS_START, `coverage erase`, pytest args with log file, junit xml, showlocals, --color, changed-files support, then combine coverage and generate xml for project vs tests, report, move db to artifacts.
- `Tee` class to mimic tee.
- `_lint()` using pylint rcfile, flags, src path.
- Sessions: `lint`, `lint-code`, `lint-tests`, `lint-code-pre-commit`, `lint-tests-pre-commit`, `docs`, `docs-dev` (sphinx-autobuild), `docs-crosslink-info`.

**Comparison:** saltext-vault is far more mature. It lints docs, cli examples, typing, security, workflow validity.

### 3.4 Tool inventory summary

| Category | saltstack-formulas | saltstack/salt | saltext-vault (and kin) | this repo now |
|----------|--------------------|----------------|--------------------------|---------------|
| Python format/lint | (pre-commit handles via? rubocop not) but indirectly none | black, isort, pyupgrade, pylint (via nox) | black, isort, pyupgrade, pylint via nox, ruff not used | ruff only |
| YAML | yamllint --strict custom regex | yamllint? | yamllint (via maybe?) but check-yaml | check-yaml only |
| Salt SLS | salt-lint | salt-lint | salt-lint? | none |
| Shell | shellcheck-py | shellcheck via tox? | shellcheck-py | none |
| Workflows | check-jsonschema | actionlint? | actionlint-py | none |
| Docs | rstcheck, rst-lint | – | check-docs hook, docs build | none |
| Security | – | bandit | bandit | none |
| Types | – | mypy tools | ty | none (py.typed only) |
| Commit style | commitlint | – | commitlint not? | none |
| Coverage | – | coverage | coverage + codecov | none |
| Kitchen/Integration | kitchen-salt matrix 15 platforms | salt integration harness | Docker container for vault/openbao | none (live test gated) |
| Caching/Pinning | pre-commit cache, container digest pinned | pip-compile locks | uv + nox pinned sha, checkout sha | no cache, floating tags |

---

## 4. Current CI Gaps – Prioritized

### P0 – Must Fix (breaks trust / diverges from saltext standard)

1. **No pre-commit CI gate** – contributors can push with `ruff` passing but `trailing-whitespace` etc fails locally. Upstream runs pre-commit in container as first job failing fast.
2. **Floating GitHub Actions** – `actions/checkout@v4`, `setup-python@v5`, `actions/setup-python@v5` are moving targets. Upstream pins to **SHA + version comment** (e.g., `actions/checkout@9c091... # v7.0.0`). Supply chain risk.
3. **No caching** – pip, pre-commit, nox caches not used. Slows CI, wastes runner minutes.
4. **No workflow lint** – invalid workflow syntax can be merged. Upstream uses `check-jsonschema` + `actionlint`.
5. **No salt-lint for SLS tutorials** – 13 SLS files exist, not linted. Could break for newcomers copying tutorials.

### P1 – Should Fix (standard in saltext-*)

6. **No bandit (security)** – OPNsense client handles API secrets, needs bandit scan. saltext-vault runs both code + tests.
7. **No pylint** – ruff catches many but not Django-like or salt specific issues. saltext-vault still runs pylint via nox.
8. **No type checking** – repo publishes `py.typed` yet no `ty`/`mypy` job. Should at least run `ty check` or `mypy --ignore-missing`.
9. **No coverage reporting** – unit jobs run pytest but don't measure coverage or upload to codecov. Hard to see regressions.
10. **Pre-commit minimal** – missing `check-ast` (syntax), `mixed-line-ending`, `pyupgrade`, `isort` strict, `blacken-docs`, `actionlint`, `bandit` etc.
11. **Tests lack salt version matrix** – current matrix is Python 3.10-3.14 with single salt latest. Upstream tests against 3006.x, 3008.x, master (via `SALT_REQUIREMENT` env). Could miss 3006 compat.
12. **No docs build** – Sphinx `make html` + linkcheck would catch broken RST.
13. **No concurrency group** – PR pushes cancel previous runs in template; current runs all.

### P2 – Nice to Have / Future

14. **Spec-drift only checks controllers.json, not models.json** – could check both.
15. **No coverage of `sync_extmods.py --check` failure** – it echoes ok on failure, masking errors (uses `|| echo`). Should fail if mismatch outside PR?
16. **No artifact upload for logs/coverage/builds** – makes debugging CI harder.
17. **No changed-files optimization** – every push runs full matrix even if only docs changed. saltext uses `dorny/paths-filter` to skip.
18. **No OpenSSF Scorecard/CodeQL** – added for security.
19. **No shellcheck** – tools/*.py but `tools/README` maybe shell? Actually not needed but good hygiene.
20. **No commitlint** – helps changelog, but may be heavy for small team.
21. **No Renovate/Github-dependency-security scanning**.
22. **Makefile not exercised in CI** – could add job `make lint verify`.

---

## 5. Recommended Checklist for this Repo

### Phase 0 – Immediate (this PR child tasks)

- [ ] Create `docs/ci-audit.md` (this file) + open issue/PR linking.
- [ ] Ensure `wt/t_e32ca980` branch passes current CI (ruff, unit, spec-drift, packaging).

### Phase 1 – Lint & Pre-commit Hardening (child t_0bb4c037)

Goal: green `lint.yml` or pre-commit job.

**Pre-commit config upgrades (mirror saltext-vault):**

```yaml
minimum_pre_commit_version: 3.6.0
repos:
  - pre-commit-hooks v6.0.0: check-merge-conflict, trailing-whitespace --markdown-linebreak-ext=md, mixed-line-ending --fix=lf, end-of-file-fixer, check-ast, check-yaml, check-added-large-files, debug-statements?
  - saltstack/pre-commit-remove-import-headers 1.1.0
  - local: check-cli-examples? (if docs use it) or keep simple
  - saltstack/salt-rewrite 2.5.2: rewrite-docstrings for src/
  - asottile/pyupgrade v3.21.2: py310-plus
  - isort already covered by ruff I but keep isort if ruff disabled? Option: keep ruff, drop separate isort.
  - astral-sh/ruff-pre-commit v0.14.8 existing
  - bandit 1.9.4
  - astral-sh/ty-pre-commit 0.0.59 or mypy
  - actionlint-py 1.7.11 + shellcheck-py
  - adrienverge/yamllint v1.38.0 with files regex like template
  - warpnet/salt-lint 0.9.2 for sls/jinja
  - python-jsonschema/check-jsonschema 0.38.0 for github workflows
```

**GitHub workflow `.github/workflows/lint.yml` (or enhance existing):**

- concurrency: group `${{ workflow }}-${{ ref }}` cancel true if not main
- pre-commit job using container? Could simplify: ubuntu + setup-python + `pip install pre-commit` + caching `~/.cache/pre-commit`
- Include shellcheck, yamllint, salt-lint, actionlint.
- Pin actions to SHA.
- Cache via `actions/cache`.

**Acceptance:** `pre-commit run --all-files` passes locally, CI job green.

### Phase 2 – Package & Unit Test Hardening (child t_554b7810)

- Enhance `ci.yml` unit job:
  - Use `astral-sh/setup-uv` or cache pip.
  - Matrix: python 3.10-3.14 + salt 3006.12, 3008.2, maybe master.
  - Install via `nox` instead of raw pip – aligns with saltext-vault.
  - Add coverage: `coverage run -m pytest` + `coverage xml` + upload artifact + codecov OIDC.
  - Add junit artifact.
  - Pin actions to SHA.
  - Add concurrency.

- Add docs job: `docs` – pip install sphinx + build html, linkcheck (allow failures initially).

- Packaging: test import of built wheel (`pip install dist/*.whl && python -c "import saltext.opnsense"`).

- Ensure `python -m build` uses isolated env.

**Acceptance:** CI fails if `verify_import` fails, if any pytest fails, if coverage drops below threshold (optional).

### Phase 3 – Integration Testing Strategy (child t_e6a8020d)

- Research Molecule/Docker vs Kitchen vs pytest testinfra vs OPNsense VM (QEMU) in GitHub Actions.
- Document decision in `docs/integration-testing.md`.
- PoC: keep `tests/integration/test_live_opnsense.py` low-impact, possibly add mock OPNsense API via `pytest-httpserver` or `responses`.

### Cross-cutting:

- Pin all GitHub Actions to full SHA + comment.
- Add `.yamllint.yaml` config – extends default, rule line-length 100 maybe, ignore `src/saltext/opnsense/utils/*.json` generated.
- Add `.salt-lint` config – skip 205,207,208 like formula.
- Add `bandit` baseline if false positives.
- Add `ty` or `mypy` config.
- Docs: `CONTRIBUTING.md` section on pre-commit usage (`pip install pre-commit && pre-commit install`).
- Consider adding `dependency-groups` lint extra.

---

## 6. Specific Recommendations for saltext-opnsense (not a formula)

Since this is a **saltext**, not formula, **do not over-invest in kitchen-salt**. The formula community's kitchen matrix is less relevant. Prioritize Python:

- **Keep custom `spec-drift` job** – unique value, no upstream equivalent.
- **Do add salt-lint only for `docs/tutorials/`** – not for whole repo (no top-level SLS).
- **Do add yamllint** for `pillar.example`, `.github/workflows/*.yml`, `docs/tutorials/pillars/*.sls`? Note pillar.example is purposely example – but yamllint should allow long lines.
- **Do follow saltext-* nox pattern**: replace raw pip installs with `nox --install-only` and reuse uv for speed.
- **Do adopt pre-commit container pattern** only if CI time OK (≈1 min overhead). Simpler: ubuntu + cache.
- **Do add coverage** – easy gap.
- **Do add typing** – easy with ty.

### Suggested final workflow layout (after phases):

```
.github/workflows/
  pre-commit.yml   # lint gate (bandit, ruff, yamllint, salt-lint, actionlint, ty)
  ci.yml           # tests matrix python+salt, coverage, docs, package
  publish.yml      # existing trusted publishing
  get-changed-files.yml # optional, dorny/paths-filter optimization
```

Or consolidate into single ci.yml with 3 jobs: lint/pre-commit, test, docs.

### What to keep as-is:

- `ruff` is modern replacement for flake8/black/isort – keep, don't add flake8/black separately.
- `verify_import` and `sync_extmods --check` are excellent custom guards – keep.
- `towncrier` + changelog – good, no need semantic-release (formula uses node semantic-release, saltexts don't).
- `setuptools_scm` + `py.typed` – keep.

---

## 7. References & Fetches

- template-formula pre-commit: https://raw.githubusercontent.com/saltstack-formulas/template-formula/master/.pre-commit-config.yaml (checked 2026-09-15) – 9 hooks including commitlint, rubocop, shellcheck, yamllint strict, salt-lint, rstcheck, renovate-validator, check-github-workflows.
- template-formula main workflow: container `techneg/ci-pre-commit:v2.5.59@sha256:4505383...`, cache pre-commit, kitchen verify matrix 15 platforms debian-13-master ... 3006, semantic-release dry-run.
- salt-formula / nginx / postgres / vault formula – same template, variations of rubocop version.
- salt master pre-commit: > 600 lines, pip-compile, pyupgrade, black, isort, blacken-docs, bandit x2, local nox lint-salt, lint-tests, mypy for tools.
- saltext-vault: modular ci – get-changed-files via dorny/paths-filter 4.0.1, pre-commit container python:3.10.20-slim-trixie, apt enchant etc, nox 2026.4.10 uv 0.11.26, matrix 3006.27 py3.11 vault:1.14.8, 3008.2 py3.10 openbao, 3008.2 py3.14 vault:latest, coverage codecov OIDC, docs/package actions.
- saltext-vault pre-commit: check-merge-conflict, trailing-whitespace, mixed-line-ending, end-of-file-fixer, check-ast, remove-import-headers, local check-cli-examples, check-docs, salt-rewrite, pyupgrade py310+, isort 8.0.1, black 26.5.1, blacken-docs, bandit, local nox lint-code-pre-commit, lint-tests-pre-commit, ty 0.0.59, actionlint-py 1.7.11.

All raw files cached locally under `/tmp/template-*.yaml` during audit.

---

## 8. Next Steps for Maintainer

1. Review this audit with team.
2. Assign child tasks:
   - t_0bb4c037 → lint workflow + pre-commit hardening
   - t_554b7810 → CI package/test hardening + coverage
   - t_e6a8020d → integration testing research + docs/integration-testing.md PoC
3. Iterate: after each child, ensure parent coverage not broken.
4. After P1 complete, tag checklist and archive.

---

**End of audit.** This file should be updated as gaps are closed.

