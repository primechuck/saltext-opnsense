

# Changelog

## 2.0.0 (2026-11-16)


## Breaking changes

- BREAKING 2.0 – Pip-only, remove file-based sync script.

  - Delete `tools/sync_extmods.py` (file-based extmods sync with env var for file-based install + 10-level parent walk `find_default_dest()` + silent skip causing CI drift check no-op).
  - `Makefile`: remove `sync` target entirely (was `python tools/sync_extmods.py --copy`). Pip-only install now: `pip install -e .` + `saltutil.sync_all` or `T@opnsense` Resources targeting. Keep minimal targets: `gen-spec`, `gen-models`, `gen-wrappers`, `bump`, `verify`, `test`, `lint`, `gen-all`, `clean` per spec.
  - `bump` target: remove dead copy `cp controllers.json -> tools/controllers.json` (JSON lives in `src/.../utils/` single source).
  - `tools/generate_all.py`: remove `step_sync()`, `--skip-sync` arg, and all references to the deleted file. Pipeline now spec -> models -> wrappers -> verify -> test (pip-only). Docstring updated, `find_repo_root()` already isolated no monorepo walk.
  - `noxfile.py`: no sync mention (already clean).
  - `.github/workflows/ci.yml`: remove drift check step formerly running `sync_extmods.py --check`.
  - `.github/workflows/lint.yml`: legacy file guard obfuscated to keep env var leak out of public grep but still enforce deleted file absent.

  Migration: replace file-based `make sync` with `SALT_X` env style pointing to monorepo states and `gitfs` file-root with pip install: `pip install -e .` on master/minions or in venv, then `salt -C 'T@opnsense:fw-01' saltutil.sync_all`. No env var needed. CI drift check now relies on `verify_import.py` (76 modules 1815 actions) and boundary guards.

  Rationale: Simplest install for new user, removes parent-walk coupling to monorepo states dir, makes CI drift check not no-op public. (20261005_pip_only)
- BREAKING 2.0 – spec-strict client no fallback + hosts-only + fail loud.

  - `src/saltext/opnsense/utils/opnsense.py`: remove `enable_fallback: bool` field, delete `_candidate_actions()`, `_resolve_via_spec()`, `_call_with_fallback()` (~150 LOC fallback probing loops). `call(module, controller, action)` now spec-strict: checks `api_spec.has_action()` and raises `FileNotFoundError(f"unknown {module}/{controller}/{action} – run make bump CORE_REF=...")` if not in spec. `search/get/add/set/delete/toggle` resolve via `_resolve_action()` single deterministic action against spec, fail fast no loop. Added TODO models.json keep current per Q5 but will trim later.
  - `src/saltext/opnsense/resources/opnsense/__init__.py`: `_normalize_hosts()` hosts-only: returns only `tree.get("hosts") if dict else {}`. Delete legacy `resource_ids` flat list handling, `config` dict merging branches (:26,90,94,128-129). `_pillar_tree()` simplified to hosts-only check.
  - `src/saltext/opnsense/utils/api_spec.py`: added `# TODO Q5: keep models.json 653K for now, later trim to unbound/bind/kea only ~45K or delete hardcode 3 lookups` at top, add `has_action()` helper used by client for fail loud.
  - tests updated: `test_client.py` removed fallback probing tests, added spec-strict tests: `test_resolve_action_spec_strict`, `test_resolve_action_unknown_type_fails`, `test_call_spec_strict_success`, `test_call_spec_strict_unknown_raises`.

  Migration: if you relied on `enable_fallback=True` or undocumented probing of 404s across candidate actions, this release will now raise `FileNotFoundError` fast. Run `make bump CORE_REF=<latest>` to regenerate `controllers.json` (76 modules, 1815 actions) or use curated fallback. Use only `resources:opnsense:hosts:` pillar shape – `resource_ids` and `config` legacy shapes removed. (20261005_strict_api)
- BREAKING 2.0 – Delete 7 wrapper modules keep 2+2 minimal (generic dynamic).

  - Deleted 5 execution wrappers: `src/saltext/opnsense/modules/unbound.py` (307 LOC), `bind.py` (243), `firewall.py` (120), `kea.py` (226), `acmeclient.py` (184) – all same template `__virtual__` checks `opnsense.search` + `_search` -> `list_*_simple/pretty/mapping` duplicates. Dynamic `__getattr__` in `modules/opnsense.py` covers 76 modules 1815 endpoints via spec, verified `tools/verify_import.py`.
  - Deleted 2 state wrappers: `states/unbound.py` (599), `states/bind.py` (539) – duplicate `_verify_reconfigure_call` 15 LOC identical, identical pattern to `states/opnsense.py` generic.
  - Keep minimal 2+2: `modules/opnsense.py` generic dynamic (`call`, `search`, `get`, `add`, `set`, `delete`, `toggle`, `reconfigure`, `ping`, `__getattr__` 1815 funcs), `modules/dns.py` thin convenience (`list_aliases`, `resolve_parent`, `managed_preview` – now generic-only, no `opnsense_unbound.*` calls), `states/opnsense.py` generic (`item_present`, `item_absent`, `reconfigured`), `states/dns.py` managed (`dns.managed` + `aliases_managed` compat – now generic-only `__virtual__` checks `opnsense.search` not `opnsense_unbound`).
  - `tools/generate_wrappers.py` preserved for now but deprecated – it would generate `opnsense_{module}.py` 76 files, not used. Future B-2 will make it no-op or delete. Pip-only dynamic is canonical, matching `saltext-kubernetes`, `vault`, `proxmox` pattern generic call + spec JSON no 76 files.
  - Total LOC: `wc -l modules/*.py states/*.py` 5593 -> 3363 after delete (~40% drop), B-2 will trim further to ~1200 by removing duplicated helpers.

  Migration:
  - Replace `opnsense_unbound.list_aliases` -> `opnsense_dns.list_aliases` or `opnsense.search unbound settings host_alias`.
  - Replace `opnsense_bind.list_domains` -> `opnsense.search bind domain primary_domain` or `opnsense.search bind domain primary_domain | jq .rows`.
  - Replace `opnsense_firewall.list_aliases` -> `opnsense.search firewall alias item`.
  - Replace `opnsense_kea.list_subnets` -> `opnsense.search kea dhcpv4 subnet`.
  - Replace `opnsense_acmeclient.list_accounts` -> `opnsense.search acmeclient account account` or dynamic `opnsense.acmeclient_account_search_account`.
  - Generic dynamic covers all: `salt -C 'T@opnsense:fw-01' opnsense.unbound_settings_search_host_alias row_count=1 --out=table`
  - States: replace `opnsense_unbound.aliases_managed` (deprecated shim) -> `opnsense_dns.managed` fully pillar-driven, or generic `opnsense.item_present` with `module: unbound, controller: settings, type_name: host_alias`.

  Rationale: 7 wrappers were template duplication, no added value over generic dynamic that already covers 1815 endpoints. Keep 2+2+1 minimal public surface (generic exec + dns thin + generic state + dns managed + resources hosts-only). Follows other saltext pattern. (20261005_wrappers)
- BREAKING 2.0 – Remove AI slop and proxy-era tutorial shims.

  - Delete `docs/tutorials/states/delightful_aliases.sls` (243B include shim for `convenience_aliases.sls`). Canonical is `convenience_aliases.sls`.
  - Delete `docs/tutorials/pillars/file-based-proxy.yaml` (proxy-era file-based pillar example referencing `proxytype: opnsense`).
  - Delete legacy proxy-era pillar `docs/tutorials/pillars/opnsense` + `-router.sls` (leaked internal hostname, `proxy:` dict) replaced by `resources:opnsense:hosts:fw-01` fleet example.
  - Delete `docs/tutorials/proxy/opnsense` + `-router` file (legacy proxy minion file-based example). Resources-only `T@opnsense` is canonical since 1.0.0.
  - Delete `tools/test_live.py` + `tools/test_state.py` (manual dev scripts, replaced by `tests/integration/test_live_opnsense.py` and `tools/verify_import.py`).
  - Docs `docs/CONVENIENCE.md` deprecated section updated: shim removal noted as 2.0.0, no longer references legacy filename (fixes public-boundary leak).
  - Public boundary guard `tools/check_public_boundary.py` + fixture guard clean (PASS).

  Migration: replace `state.apply opnsense.delightful_aliases` shim usage with `convenience_aliases.sls`, replace legacy proxy pillar references with `resources:opnsense:hosts` per `docs/PILLAR.md` and `docs/RESOURCES.md`, use `salt -C 'T@opnsense:fw-01'` targeting instead of legacy proxy id targeting. (#20261005)

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
- Bump bundled OPNsense API registry from 26.7.3 to 26.7.9.

  Regenerated `controllers.json` (93 modules / 299 controllers / 2038 actions)
  and `models.json` (54 modules / 103 models) from upstream `opnsense/core` and
  `opnsense/plugins` at tag 26.7.9 via `tools/generate_all.py`, plus
  pinned-version references (`spec_version`, Makefile, docs).

  Follow-up generator fixes included in this bump: `generate_spec.py` records
  inherited `ApiMutableServiceControllerBase` verbs (start/stop/restart/
  reconfigure/status) for service controllers declaring no actions of their own
  (monit/service, netflector/service and 30+ more), and `generate_models.py`
  recognises dotted `ArrayField` subclasses as array containers (restores
  firewall Alias/Filter/Group, trust Ca/Cert, wireguard, interfaces assignment
  and others). Explicit `monit: monit/service/reconfigure` in both
  reconfigure-default tables.

  Notable upstream API changes in range: new `netflector` module, new
  `interfaces/tapsettings` + `interfaces/wirelesssettings` controllers,
  `unbound/settings` CSV host-override up/download, `interfaces/assignment`
  `pending`, FRR `quagga/ospf6settings` `*Network` → `*Area` rename, `iperf`
  service/instance rework, `monit/service` base-class refactor. (#20261113)

## Bug Fixes

- Fix state idempotency false positives: auto-resolve `match` dict human references (FQDN→UUID) via `_auto_resolve_dict`, fetch full object via `get` after search for canonical diff, fix FQDN trailing-dot normalization, fix CI spec-drift to ignore `generated_at`, fix ruff formatting and CI dependency install order. (#20260729)
- Fix Salt-native failure UX for public PyPI install.

  - modules/opnsense.py _get_client() now raises SaltInvocationError (not generic RuntimeError) with helpful pillar hint including resources:opnsense:hosts:fw-01:host vs direct opnsense:host resolution and docs links. Wraps get_client_from_opts error that already lists checked sources + example pillar.
  - Ensures failure is Salt-like: `salt -C 'T@opnsense:fw-01' opnsense.ping` shows clean error not traceback when pillar misconfigured. Existing __virtual__ in modules returns (False, "opnsense utils missing: ...") remains.
  - Docs: INSTALL.md Option A now PyPI canonical, Option B file-based fallback — public novice path 15-min. (#20260910)
- Bugfix / 3008+ polish — final proxy nit cleanup (Resources-only salt>=3008).

  - `tools/sync_extmods.py`: drop pre-1.0 `_proxy/` and `_grains/` mappings, header updated to `_modules/_states/_utils` only. File-based install now Resources-only.
  - `tools/generate_wrappers.py`: docstring updated from `proxy and direct modes` to `Resources targeting T@opnsense:fw-01` / `via Salt Resources (3008+)`.
  - `docs/USAGE.md`: full rewrite from proxy minion dance (`/etc/salt/proxy`, `proxytype: opnsense`, `salt-proxy@T@opnsense:fw-01`) to Resources fleet `resources:opnsense:hosts:{id}`, `T@opnsense` targeting, Vault `__slot__` via `saltext-vault`. Convenience examples preserved.
  - `docs/TROUBLESHOOTING.md`: rewrite proxy sections to Resources `T@opnsense` grains/doctor/ping troubleshooting.
  - `src/saltext/opnsense/modules/opnsense.py`: split `HAS_API_SPEC` vs `HAS_UTILS` so spec/dynamic map works without `requests` installed (api_spec has no heavy deps). Fix `_build_dynamic_map` cache poisoning: only cache non-empty mapping, allow retry after transient load_spec failure (previously empty dict cached as valid, blocking recovery). This made `verify_import.py` flaky when salt mocked before import causing duplicate module loads + lru_cache mismatch.
  - `tools/verify_import.py`: robust against duplicate `api_spec` module objects (clear both caches, simulate Salt `__context__`), build map via explicit `_build_dynamic_map()` not dir(), PASS covers 76 modules / 1815 funcs. (#20260915)
- Fix `generate_models.py` to recognise dotted `ArrayField` subclasses as array
  containers. Upstream renamed the `<interface>` wrapper in
  `NetworkInterface.xml` to `type=".\NetworkInterfaceField"` (26.7.4), which the
  `type == "ArrayField"` check silently dropped — along with firewall Alias /
  Filter / Group, trust Ca / Cert, wireguard Client / Server, ipsec Swanctl
  sub-arrays and others. The generator now accepts leading-dot subclass types
  whose element directly wraps typed fields (nested scalar dotted fields such as
  `KeaOptionDataField` stay excluded). Regenerated `models.json` at 26.7.9: 54
  modules / 103 models / 216 arrays. (#20261113)

## Improved Documentation

- Fix the documented TestPyPI install command for dev builds: install dependencies from PyPI, then the dev build with `--no-deps`, so pip cannot pull look-alike dependencies from TestPyPI. (20261115_testpypi)
- Rename "delightful" semantic layer → "convenience / high-level wrappers" for public release. Add `docs/CONVENIENCE.md`, update `docs/USAGE.md`, `ARCHITECTURE.md`, `index.rst` (remove broken DELIGHTFUL_UX/WHY_SALT refs), rename `delightful_aliases.sls` → `convenience_aliases.sls` with deprecated shim `delightful_aliases.sls` including new file (shim to be removed in 0.2.0). Update src comments from delightful → convenience. (#20260729)
- Chore: 3008-only docs cleanup — PyPI (salt-pip) as canonical public install path, T@opnsense targeting, remove pre-3008 proxy docs.

  - docs/INSTALL.md flips Option A to pip (salt-pip install saltext-opnsense) as recommended public UX, file-based gitfs moves to Option B fallback.
  - All tutorials/docs slimmed from T@opnsense:fw-01 + flat /etc/salt/proxy references to Resources fleet T@opnsense:fw-01 compound targeting.
  - CLI examples updated from salt T@opnsense:fw-01 ... to salt -C 'T@opnsense:fw-01' ... .
  - pyproject.toml description and CI guard now state Salt 3008+ Resources only.
  - Makefile/noxfile: remove proxy/grains pycache cleanup, annotate Resources-only.
  - Public failure mode affirmed: entry-point saltext.opnsense auto-discovers, __virtual__ hides functions cleanly, doctor/ping dict OK/ERROR. (#20260910)
- Add `AGENTS.md` (symlinked as `CLAUDE.md` and `.cursorrules`) defining the generated-vs-hand-written boundary, Salt loader and OPNsense idempotency invariants, and human-gated changes. Document the PHP-to-JSON generator workflow in `tools/README.md`, and document the credential resolution order and the GET-vs-POST payload contract in `utils/opnsense.py`, `utils/diff.py` and `states/opnsense.py`. (#20261024)
- Document two Salt 3008 runtime traps that were missing from Section 3: pillar
  `MaskedDict`/`MaskedList` wrapping semantics (`salt.utils.secret.expose`, not a
  nonexistent `unmask` helper; scalar `.get()`/`[]` reads return plain strings, only
  `repr`/`str`/serialization redacts) and the 3008.0-only Resources API
  (`pillar_resources_tree`, `__resource__`/`__resource_funcs__`) with an explicit ban
  on `salt.utils.cloud`/`sdb`/legacy pooling fallbacks in `resources/opnsense/`.
  No code changes — the existing credential paths already read scalar leaves and are
  unaffected. (#20261113)

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
- Remove AI slop `delightful_aliases.sls` shim, proxy-era tutorials (`file-based-proxy.yaml`, legacy pillar `opnsense` + `-router.sls`, `proxy/opnsense` + `-router` file), and manual dev scripts (`tools/test_live.py`, `tools/test_state.py`). Docs reference in `CONVENIENCE.md` cleaned.

  Breaking 2.0 – see breaking fragment. (#20261005)
- Dropped support for Python <3.12. The extension floor is now Python `>=3.12`; `requires-python`, classifiers, the nox matrix, CI matrix, `ruff` target, `pyupgrade`, and docs all align on `>=3.12`. Salt floor (`>=3008`) is unchanged. (#20261113)

## Miscellaneous

-  (#20260730, #20261024, #20261115)

This changelog is managed via towncrier.

Fragments in `changelog/` (feature, bugfix, doc, removal, misc) are concatenated into this file via `towncrier build`.

## 0.1.0 (unreleased)

- Initial scaffold: generic templated `opnsense` execution + state modules, proxy minion, utils client, codegen tool for all API endpoints, unit tests Salt way, examples replacing `query.sh` / `sync-bind-zone.sh`
