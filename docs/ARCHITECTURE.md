# Architecture — saltext-opnsense (Salt 3008+ Resources only)

Requires `salt>=3008`. Resources-only, no proxy.

## Why templated, not hand-coded?

OPNsense API has 26 core + ~80 plugin modules, each 5-15 actions. Hand-coding 400+ funcs brittle. Templated:

- `generate_spec.py` clones `opnsense/core` + `plugins` at tag, parses `Api/*Controller.php` for `*Action` -> `controllers.json` registry (76 modules, 258 controllers, 1815 actions for 26.7.3)
- Exec `opnsense.call` generic works for any registry entry
- Resource connection `resources/opnsense/__init__.py` reuses same client
- No code change when OPNsense adds module — regen registry, CI catches drift

## Three layers — Resource-native (3008+)

### Layer 1: `utils/opnsense.py` — `OPNsenseClient`

- Dataclass config: host, api_key, api_secret, proto=https, verify_ssl, timeout
- `requests.Session` BasicAuth, retry 3x backoff for transient disconnects
- Methods: call, search, get, add, set, delete, toggle, reconfigure, close
- `get_client_from_opts`: Resources-first `__resource__[id]` -> `resources:opnsense:hosts:{id}` via pillar_resources_tree, else direct `opnsense:{host}` pillar
- Secrets masked, validation raises `OPNsenseValidationError.validations`

### Layer 2: `resources/opnsense` — Connection module (3008+)

Resources-only, no proxy daemon.

- Context cache: `__context__[opnsense][conns][id]` per-resource, Lock
- Thin delegation via `__resource_funcs__` + `__resource__[id]`
- One managing minion -> dozens FWs, targeting `T@opnsense`, `G@opnsense_version`, composable `T@opnsense:fw-01 or T@ssh:fw-01`

### Layer 3: `modules` + `states` — Execution + States

Exec `modules/opnsense.py`: raises `SaltInvocationError` with pillar hint, `doctor`, discovery `list_api_modules/controllers/actions`, dynamic injection via `__getattr__/__dir__` 1815 funcs lazy via context+Lock.

States `states/opnsense.py`: generic `item_present/absent/reconfigured`, `__context__` caching, `test=True`.

Convenience: acmeclient,bind,dns,firewall,kea,unbound — listers + `dns.managed`.

## Idempotency — diff engine (`utils/diff.py`)

Quirks: bools 1/0 vs True, UUID vs FQDN vs dict, CSV lan,wan vs list order-agnostic, trailing dot.

`diff.py` normalizes all, `match` auto-resolves human ref->UUID via `models.json` relation_targets + candidates from `controllers.json`. Second run 0 changes.

## Spec + Models codegen

- `controllers.json` via `generate_spec.py` — clones core+plugins, regex action, groups JSON meta core_ref
- `models.json` via `generate_models.py` — Model XML -> relation_targets (653K file)
- Pipeline `generate_all.py` — `make gen-all`: spec->models->verify->test

## TODO Q5: models.json

`src/saltext/opnsense/utils/models.json` is 653K covering all modules. Keep for now. Later trim to unbound/bind/kea only ~45K or delete and hardcode 3 lookups: unbound host_alias->host_override, bind record->domain, kea reservation->subnet. See plan 2026-10-05_130000.

## Packaging — 3008+ only

`pyproject.toml` deps `salt>=3008`, `requires-python >=3.10`, entry-point `salt.loader`.

Install `salt-pip install saltext-opnsense` or `pip install -e .` dev (pip-only).

## Fleet topology

master -> managing minion 3008+ with pillar resources:opnsense:hosts -> T@opnsense:fw-01 API via client, T@opnsense:fw-02, T@ssh:fw-01 optional 2 SRN python311.

Targeting: `T@opnsense`, `G@opnsense_version:25.*`, `T@opnsense:fw-01 or T@ssh:fw-01`. See RESOURCES.md.

Vault: `__slot__:salt:vault.read(...)` via `saltext-vault`.
