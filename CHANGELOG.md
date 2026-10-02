

# Changelog

## 1.0.0rc2 (2026-10-02)


## Features

- Add centralized diff engine (`utils/diff.py`) with value normalization for OPNsense API quirks: booleans "1"/True, UUID vs human FQDN equivalence, CSV vs list order-agnostic, number coercion, FQDN trailing-dot stripping, whitespace trimming. States (`opnsense`, `unbound`, `bind`, `dns`) now use `diff_models()` for true idempotency (second run reports 0 changes). Adds `tools/test_state.py` mock idempotency tester and unit tests for diff engine and idempotency. (#20260729)
- Add lint workflow + salt-lint/yamllint + pre-commit hardening (CI audit follow-up).

  - New .github/workflows/lint.yml (5 jobs): pre-commit, yaml-lint, salt-lint, ruff, workflow-lint (check-jsonschema + actionlint), all actions pinned to SHA + version comment, with pip/pre-commit caching, concurrency cancel-in-progress.
  - Harden existing ci.yml/publish.yml: pin checkout v4.2.2 11bd719, setup-python v5.6.0 a26af69, cache v4.2.3 5a3ec84, pypi-publish v1.14 dc37677, add concurrency group, cache pip.
  - Add .yamllint.yaml (line-length 120, ignore generated JSON, .copier-answers.yml) and .salt-lint (skip 205/207/208 per template-formula).
  - Expand .pre-commit-config.yaml to mirror saltext-vault + template-formula + copier: keep copier's salt-rewrite, pyupgrade, bandit, nox-lint (manual), add yamllint --strict, salt-lint, check-github-workflows, shellcheck. Remove conflicting isort (ruff I does it). Exclude .copier-answers.yml from check-yaml/yamllint.
  - Fix existing violations: trailing whitespace, EOF newlines, import order in docs/conf.py, salt-rewrite docstring CLI examples, pyupgrade rewrites.
  - Docs: CONTRIBUTING.md new Pre-commit & Linting section.

  Remaining TODOs: nox-lint manual due to isort/pylint dep conflict (track upstream), bandit already enabled, no ty/pylint yet (deferred to t_554b7810). (#20260910)

## Bug Fixes

- Fix state idempotency false positives: auto-resolve `match` dict human references (FQDN→UUID) via `_auto_resolve_dict`, fetch full object via `get` after search for canonical diff, fix FQDN trailing-dot normalization, fix CI spec-drift to ignore `generated_at`, fix ruff formatting and CI dependency install order. (#20260729)
- Fix Salt-native failure UX for public PyPI install.

  - modules/opnsense.py _get_client() now raises SaltInvocationError (not generic RuntimeError) with helpful pillar hint including resources:opnsense:hosts:fw-01:host vs direct opnsense:host resolution and docs links. Wraps get_client_from_opts error that already lists checked sources + example pillar.
  - Ensures failure is Salt-like: `salt -C 'T@opnsense:fw-01' opnsense.ping` shows clean error not traceback when pillar misconfigured. Existing __virtual__ in modules returns (False, "opnsense utils missing: ...") remains.
  - Docs: INSTALL.md Option A now PyPI canonical, Option B file-based fallback — public novice path 15-min. (#20260910)
- Bugfix / 3008+ polish — final proxy nit cleanup (Resources-only salt>=3008).

  - `tools/sync_extmods.py`: drop pre-1.0 `_proxy/` and `_grains/` mappings, header updated to `_modules/_states/_utils` only. File-based install now Resources-only.
  - `tools/generate_wrappers.py`: docstring updated from `proxy and direct modes` to `Resources targeting T@opnsense:fw-01` / `via Salt Resources (3008+)`.
  - `docs/USAGE.md`: full rewrite from proxy minion dance (`/etc/salt/proxy`, `proxytype: opnsense`, `salt-proxy@opnsense-router`) to Resources fleet `resources:opnsense:hosts:{id}`, `T@opnsense` targeting, Vault `__slot__` via `saltext-vault`. Convenience examples preserved.
  - `docs/TROUBLESHOOTING.md`: rewrite proxy sections to Resources `T@opnsense` grains/doctor/ping troubleshooting.
  - `src/saltext/opnsense/modules/opnsense.py`: split `HAS_API_SPEC` vs `HAS_UTILS` so spec/dynamic map works without `requests` installed (api_spec has no heavy deps). Fix `_build_dynamic_map` cache poisoning: only cache non-empty mapping, allow retry after transient load_spec failure (previously empty dict cached as valid, blocking recovery). This made `verify_import.py` flaky when salt mocked before import causing duplicate module loads + lru_cache mismatch.
  - `tools/verify_import.py`: robust against duplicate `api_spec` module objects (clear both caches, simulate Salt `__context__`), build map via explicit `_build_dynamic_map()` not dir(), PASS covers 76 modules / 1815 funcs. (#20260915)

## Improved Documentation

- Rename "delightful" semantic layer → "convenience / high-level wrappers" for public release. Add `docs/CONVENIENCE.md`, update `docs/USAGE.md`, `ARCHITECTURE.md`, `index.rst` (remove broken DELIGHTFUL_UX/WHY_SALT refs), rename `delightful_aliases.sls` → `convenience_aliases.sls` with deprecated shim `delightful_aliases.sls` including new file (shim to be removed in 0.2.0). Update src comments from delightful → convenience. (#20260729)
- Chore: 3008-only docs cleanup — PyPI (salt-pip) as canonical public install path, T@opnsense targeting, remove pre-3008 proxy docs.

  - docs/INSTALL.md flips Option A to pip (salt-pip install saltext-opnsense) as recommended public UX, file-based gitfs moves to Option B fallback.
  - All tutorials/docs slimmed from opnsense-router + flat /etc/salt/proxy references to Resources fleet T@opnsense:fw-01 compound targeting.
  - CLI examples updated from salt opnsense-router ... to salt -C 'T@opnsense:fw-01' ... .
  - pyproject.toml description and CI guard now state Salt 3008+ Resources only.
  - Makefile/noxfile: remove proxy/grains pycache cleanup, annotate Resources-only.
  - Public failure mode affirmed: entry-point saltext.opnsense auto-discovers, __virtual__ hides functions cleanly, doctor/ping dict OK/ERROR. (#20260910)

## Removals and De-precations

- BREAKING 1.0.0 – Salt Resources migration, proxy removed.

  - Hard-delete proxy minion `src/saltext/opnsense/proxy/opnsense.py` and `grains/opnsense.py`. Reason for `salt>=3008` requirement. Use `T@opnsense` Resources (see docs/RESOURCES.md).
  - Implement `resources/opnsense/` connection module API-only with per-resource caching in `__context__["conns"]`, `discover` via `pillar_resources_tree`, `grains` per-resource, `ping` single probe, `shutdown` closes sessions.
  - Thin execution overrides `resources/opnsense/modules/opnsense.py` + `test.py` delegation via `__resource_funcs__`, `states/opnsense.py` re-export via `namespaced_function` for merge-mode `state.apply`.
  - 2 SRN default: `opnsense:fw-01` (API) + optional `ssh:fw-01` built-in `salt.resources.ssh` with thin requiring `python311` on OPNsense. Composition via `T@opnsense:fw-01 or T@ssh:fw-01`.
  - Packaging polish: add `py.typed` PEP 561 marker, untrack `_version.py` (gitignore), modern PEP 621 `readme/license` as file, `Changelog` URL, `optional-dependencies:dev` + `dependency-groups`, `tool.ruff.builtins` includes `__resource__`, `nox` python 3.10-3.14.
  - Pythonic: `Final/frozenset`, `TypedDict`, `lru_cache`, `close()`+`__enter__/__exit__`, specific exceptions not bare `Exception`, `encoding=utf-8`, no `Path.cwd()` fallback, no `globals()` mutation in connection module, thread-safe `_DYNAMIC_MAP_CACHE` via `__context__` + `Lock`, replace `lambda` with `def`, `next(iter(dict))` not `list(keys())[0]`, substring sensitive masking.
  - Salty: `__virtual__` returns `True`, `__context__` caching not global `_MODELS_UTILS`, no import-time `_inject_dynamic_state_wrappers()` (now lazy via `__getattr__` + `__context__` flag), `normalize_enabled` unified, `bind.domain_absent` bug fixed to preserve actual type, `strip_salt_internal_kwargs` everywhere, reconfigure verification unified via `_verify_reconfigure_call`, masking logs.
  - Add unit tests `tests/unit/test_resources_opnsense.py` for discover/init/connect/cache/grains/ping/shutdown/delegation. Existing 113 tests still pass (now 121).
  - CI: unit matrix 3.10-3.14, `verify_import.py` + `sync_extmods.py --check`, new packaging job `py.typed` present + `twine check`.
  - Docs: new `docs/RESOURCES.md` 10-min walk-through, 2 SRN composition, `resource.list_grains`, `QUICKSTART.md` rewritten for Resources, `README.md` fleet section, `pillar.example` now `resources:opnsense:hosts` + optional `ssh:hosts` + direct mode. (#20260804)
- BREAKING-ish docs-only cleanup continued from 1.0.0 Resources migration: remove remaining pre-3008 documentation remnants that slipped past PR #3.

  - Drop mentions of `_proxy/`, `_grains/`, `extension_modules:`, `salt-proxy@`, `/etc/salt/proxy` flat file, `proxytype: opnsense` from INSTALL/QUICKSTART/RESOURCES/PILLAR/ARCHITECTURE/DEVELOPMENT/MAINTENANCE.
  - CI now pins salt>=3008 explicitly, matching requires-python and README fleet story. (#20260910)

This changelog is managed via towncrier.

Fragments in `changelog/` (feature, bugfix, doc, removal, misc) are concatenated into this file via `towncrier build`.

## 0.1.0 (unreleased)

- Initial scaffold: generic templated `opnsense` execution + state modules, proxy minion, utils client, codegen tool for all API endpoints, unit tests Salt way, examples replacing `query.sh` / `sync-bind-zone.sh`
