# Architecture — saltext-opnsense (Salt 3008+ Resources only)

Requires `salt>=3008`. Resources-only, no proxy.

## Why templated, not hand-coded?

OPNsense API has 26 core + ~80 plugin modules, each 5-15 actions. Hand-coding =
400+ funcs, brittle. Templated:

- `generate_spec.py` clones `opnsense/core` + `plugins` at tag, parses
  `Api/*Controller.php` for `*Action` → `controllers.json` registry (76 modules,
  258 controllers, 1815 actions for 26.7.3)
- Exec `opnsense.call` generic works for any registry entry
- Resource connection `resources/opnsense/__init__.py` reuses same client
- No code change when OPNsense adds module — regen registry, CI `spec-drift`
  catches mismatch

## Three layers — Resource-native (3008+)

### Layer 1: `utils/opnsense.py` — `OPNsenseClient`

- Dataclass `OPNsenseClientConfig`: `host`, `api_key`, `api_secret`,
  `proto=https`, `verify_ssl`, `timeout`, `base_path=/api/`
- `requests.Session` BasicAuth, reuse, retry RemoteDisconnected /
  ProtocolError / ConnectionError exponential backoff (3x)
- Methods: `call`, `search`, `get`, `add`, `set`, `delete`, `toggle`,
  `reconfigure`, `service_action`, `close` + `__enter__/__exit__`
- `get_client_from_opts`: Resources-first:

  1. Resource context `__resource__[id]` → `resources:opnsense:hosts:{id}`
     via `pillar_resources_tree` (default key `resources`)
  2. Direct pillar `opnsense:{host, api_key}` or `opts:opnsense` (masterless)
  3. Pillar itself as host config `{host, api_key}` (local `salt-call`)

- No proxy merging, no `proxytype` — removed 1.0.0, reason `salt>=3008`
- Secrets masked via substring `_mask_sensitive`, validation raises
  `OPNsenseValidationError.validations`
- Fallback `_resolve_via_spec` + `_call_with_fallback` — spec authoritative
  suppresses 404 probing unless `enable_fallback=True`
- `Final`, `frozenset`, `TypedDict`, specific exceptions, `encoding=utf-8`,
  no `Path.cwd()` fallback, no `globals()` mutation in connection module,
  `lru_cache` for spec, thread-safe `_DYNAMIC_MAP_CACHE` via `__context__` +
  `Lock`

### Layer 2: `resources/opnsense` — Connection module (3008+)

Resources-only, no proxy daemon, no `salt-proxy@` unit.

Implements `__virtual__`, `init`, `initialized`, `discover`, `grains`, `ping`,
`shutdown` (closes via `close()`).

- Context cache: `__context__[opnsense][conns][id]` per-resource, Lock
- Thin delegation via `__resource_funcs__` + `__resource__[id]`
- Re-export via `namespaced_function` for merged `state.apply` results
  prefixed by resource id
- Why Resources: one managing minion → dozens FWs, first-class targeting
  `T@opnsense`, `G@opnsense_version`, composable with SSH same ID fw-01 for
  2 SRN `T@opnsense:fw-01 or T@ssh:fw-01`

### Layer 3: `modules` + `states` — Execution + States (resource-aware)

Exec `modules/opnsense.py`: `_get_client` raises `SaltInvocationError` with
pillar hint (not RuntimeError) — Salt-native UX, `ensure_present/absent`,
`doctor`, discovery `list_api_modules/controllers/actions`, dynamic injection
via `__getattr__/__dir__` 1815 funcs lazy via context + Lock (no import-time
global mutation).

Thin delegation `resources/opnsense/modules/opnsense.py` via
`__resource_funcs__` + `__resource__[id]`.

States `states/opnsense.py`: generic `item_present/absent/items_present/
reconfigured`, convenience, `__virtual__` returns `True`,
`__context__` caching not globals, no import-time wrapper injection,
`normalize_enabled` unified, `bind.domain_absent` bug fixed,
`strip_salt_internal_kwargs` everywhere, reconfigure verification unified,
`test=True` support.

Convenience: acmeclient,bind,dns,firewall,kea,unbound — listers
(`list_aliases`, `resolve_parent`), `alias_present`, `dns.managed`.

## Idempotency — diff engine (`utils/diff.py`)

OPNsense API quirks cause flapping if naive compare:

- Bools `"1"/"0"` vs True/False
- Relations UUID vs FQDN vs dict `{hostname,domain}`
- Lists CSV `"lan,wan"` vs `["wan","lan"]` order-agnostic
- Numbers `"80"` vs 80
- FQDN trailing dot `example.com.`

`diff.py`:

1. search all rows `rowCount=-1`
2. Match via `match` dict auto-resolved human ref → UUID via `models.json`
   relation_targets + candidates from `controllers.json`
3. get full object by UUID for canonical diff (search summary vs get full)
4. `diff_models`: Bools 1/True, Relations UUID↔FQDN, Lists/CSV sorted tuple,
   Numbers, trailing dot stripped, ignores `uuid`, whitespace trimmed
5. If diff → set merged, optionally reconfigure with verification

Proven via `tools/test_state.py --mock` + `tests/unit/utils/test_diff.py` —
second run 0 changes even when API returns `"1"` bool and human grid.

## Spec + Models codegen

- `controllers.json` via `generate_spec.py` — clones core+plugins, globs
  `*Controller.php`, regex `public function (\w+)Action`, groups → JSON with
  meta `core_ref`
- `models.json` via `generate_models.py` — parses Model XML, relation_targets
- Wrappers via `generate_wrappers.py` — spec → wrappers (optional, dynamic
  covers all)
- Pipeline `generate_all.py` — `make gen-all`: spec→models→wrappers→sync→
  verify→test, supports `--dry-run`, `--only`, `--skip-sync`

Versioning `setuptools_scm` no-local-version + `py.typed` PEP 561,
`_version.py` gitignored.

## Packaging — 3008+ only

`pyproject.toml` deps `salt>=3008`, `requires-python >=3.10`, entry-point
`salt.loader`, builtins includes `__resource__`, `__resource_funcs__`.

Install `salt-pip install saltext-opnsense` (prod canonical) or `pip install
-e .` dev or file-based `sync_extmods.py --copy` (copies real contents, no
symlink, no `_proxy/_grains`).

No pre-3008, no proxy code ships.

## Testing

Unit mocked — no live OPNsense:

- `test_client.py` — mock `requests.Session`, retry, masking
- `test_diff.py` — bool/UUID/CSV
- `test_resources_opnsense.py` — discover/init/grains/ping/close/delegation
- `test_free_modules_import.py` — proves all 76 import
- `verify_import.py` — 76 exec + 76 state + 1815 dynamic
- `test_state.py --mock` — proves second run 0 changes

Integration gated `OPNSENSE_LIVE_TEST=1`, `test_live.py` read-only env.

## Fleet topology

```
[salt-master]
  -> [managing-minion 3008+ saltext-opnsense pillar resources:opnsense:hosts]
    -> T@opnsense:fw-01 API via OPNsenseClient
    -> T@opnsense:fw-02 API
    -> T@ssh:fw-01 SSH (optional 2 SRN, python311 on OPNsense)
```

Targeting: `T@opnsense`, `G@opnsense_version:25.*`,
`T@opnsense:fw-01 or T@ssh:fw-01` composition. See RESOURCES.md.

Vault: `__slot__:salt:vault.read(...)` resolved on master via
`saltext-vault`.
