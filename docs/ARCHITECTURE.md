# Architecture — saltext-opnsense (Salt 3008+ Resources only)

Requires salt>=3008. No proxy minion.

## Why templated, not hand-coded?

OPNsense API has 26 core modules + 80 plugin modules, each with ~5-15 actions. Hand-coding = 400+ functions, brittle.

Templated approach:
- Generator parses Api/*Controller.php for *Action
- Produces controllers.json registry (75 modules, 249 controllers, 1736 actions for 25.7.11)
- Execution module opnsense.call generic works for any registry entry
- Resource connection resources/opnsense/__init__.py reuses same client
- No code change needed when OPNsense adds new module — regen registry, CI drift check catches mismatch

## Three layers — Resource-native (3008+)

### Layer 1: utils/opnsense.py — OPNsenseClient

- Dataclass OPNsenseClientConfig: host, api_key, api_secret, proto=https, verify_ssl, timeout, base_path=/api/
- requests.Session with BasicAuth, session reuse, retry on RemoteDisconnected/ProtocolError/ConnectionError exponential backoff
- Methods: call, search, get, add, set, delete, toggle, reconfigure, service_action
- get_client_from_opts: Resources first:
  1. Resource context __resource__[id] → resources:opnsense:hosts:{id} via pillar_resources_tree
  2. Direct pillar opnsense:{host, api_key, api_secret} or opts:opnsense (masterless)
  3. Pillar itself as host config {host, api_key} (masterless local)
- No proxy merging. Removed in 1.0.0, reason for salt>=3008.

Secrets masked via _mask_sensitive_data. Validation errors raise OPNsenseValidationError.

Fallback: _resolve_via_spec + _call_with_fallback — authoritative spec suppresses 404 probing unless enable_fallback=True.

### Layer 2: resources/opnsense — Connection module (3008+)

Requires Salt 3008+ Resources. No proxy daemon.

Implements __virtual__, init, initialized, discover, grains, ping, and closes clients via OPNsenseClient.close.

Context cache: __context__[opnsense][conns][id] per-resource.

Thin delegation via __resource_funcs__ using __resource__[id]. Re-exports via namespaced_function for merged mode state.apply.

Why Resources: one managing minion → dozens FWs, first-class targeting T@opnsense, G@opnsense_version, composable with SSH resource same ID fw-01.

### Layer 3: modules + states — Execution + States (resource-aware)

Execution modules/opnsense.py: _get_client, ensure_present/absent, doctor, discovery list_api_modules/controllers/actions, dynamic injection via __getattr__/__dir__ 1736 funcs lazy via context + Lock.

States states/opnsense.py: generic item_present/absent/items_present/reconfigured/assert_resolves, convenience.

Convenience modules: acmeclient,bind,dns,firewall,kea,unbound — listers.

## Idempotency — diff engine

utils/diff.py:
1. search all rows rowCount=-1
2. Match via match dict auto-resolved human ref → UUID via models.json
3. get full object by UUID for canonical diff
4. diff_models: Bools 1/True, Relations UUID↔FQDN, Lists/CSV order-agnostic, Numbers, trailing dot stripped, ignores uuid
5. If diff → set merged, optionally reconfigure with verification

## Spec + Models codegen

controllers.json via generate_spec.py, models.json via generate_models.py, wrappers via generate_wrappers.py, pipeline generate_all.py.

Versioning setuptools_scm, py.typed marker PEP 561.

## Packaging — 3008+ only

pyproject.toml dependencies salt>=3008, requires-python >=3.10, entry-point salt.loader, builtins includes __resource__, __resource_funcs__.

Install salt-pip install saltext-opnsense or pip install -e . File-based sync_extmods.py.

No pre-3008 support, no proxy code ships.

## Testing

Unit mocked, test_resources_opnsense.py, verify_import.py 75 modules.

## Fleet topology

[salt-master] -> [managing-minion 3008+ saltext-opnsense pillar resources:opnsense:hosts] -> T@opnsense:fw-01 via API.

Targeting: salt -C T@opnsense, G@opnsense_version. See docs/RESOURCES.md.
