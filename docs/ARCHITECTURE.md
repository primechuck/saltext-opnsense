# Architecture — saltext-opnsense

## Why templated, not hand-coded?

OPNsense API has 26 core modules + 80 plugin modules, each with ~5-15 actions. Hand-coding each as separate execution function = 400+ functions, brittle to upstream changes.

Templated approach:
- Generator parses `src/opnsense/mvc/app/controllers/OPNsense/*/Api/*Controller.php` for `public function xxxAction`
- Produces `controllers.json` registry
- Execution module `opnsense.call` generic works for any registry entry
- No code change needed when OPNsense adds new module — just regenerate registry, tests compare committed vs generated to detect drift

## Three layers

### Layer 1: utils/opnsense.py — OPNsenseClient

- Dataclass config, base_url building
- `requests.Session` with BasicAuth (key:secret)
- Methods: `call`, `search`, `get`, `add`, `set`, `delete`, `toggle`, `reconfigure`, `service_action`
- `get_client_from_opts` merges pillar (`opnsense`, `proxy`) + `__opts__` — allows both proxy and direct modes

Proxy config dance (file vs pillar):

- **File-based** `/etc/salt/proxy` (flat YAML, no outer `proxy:` wrapper) → `opts['proxy']` populated by Salt proxy loader directly, no pillar round-trip. Simplest for bootstrap.
- **Pillar-based** `pillars/hosts/opnsense-router.sls` → `proxy:` nested dict → master compiles pillar for minion id `opnsense-router`, resolves `__slot__:salt:vault.read` on master, sends via encrypted transport to proxy minion. Allows Vault.
- `get_client_from_opts` merges in order: pillar `opnsense`, pillar `proxy`, opts `opnsense`, opts `proxy` (opts wins). So hybrid works: minimal file with `proxytype: opnsense`, rest from pillar `opnsense:`.

### Layer 2: proxy/opnsense.py + modules/opnsense.py

Proxy:
- `__proxyenabled__ = ["opnsense"]`
- `init(opts)` creates client → `__context__` / `DETAILS`
- `ping()` tries `core/firmware/status` fallback `unbound/overview/isEnabled`
- Exposes `call, search, get, add, set_item, delete, toggle, reconfigure`

Execution module:
- Thin wrapper: if proxy mode (`salt.utils.platform.is_proxy()` + `opnsense.call` in `__proxy__`), delegate to proxy
- Else direct: `get_client_from_opts(__opts__, __pillar__)`
- Also helpers: `_find_existing`, `ensure_present`, `ensure_absent` for state use
- Discovery helpers: `list_api_modules`, `list_api_controllers`, `list_api_actions`, `spec`
- Supports both pip (`saltext.opnsense.utils.*`) and file-based sync (`_utils/saltext/...` symlink tree + fallback to `salt.utils.opnsense` import) via `_try_import()`.

### Layer 3: states/opnsense.py

Generic states:
- `item_present(name, module, controller, type, data, match, reconfigure)`
- `item_absent(name, module, controller, type, match, reconfigure)`
- `reconfigured(name, module, controller, action)`

Idempotency (v2 – diff engine):
1. `search` all rows `rowCount=-1` (with pagination handling)
2. Match via `match` dict – auto-resolved (human ref → UUID) via relation_targets
3. `get` full object by UUID to obtain canonical server representation (not summary)
4. Normalize via `utils/diff.py` – `diff_models`:
   - Bools: "1"/True/yes/enabled/on ↔ True
   - Relations: UUID ↔ FQDN ↔ dict{hostname,domain} equivalence when parent_human given
   - Lists/CSV: ["lan","wan"] ↔ "lan,wan" → sorted tuple
   - Numbers: "80" ↔ 80, trailing dot stripped, whitespace trimmed
   - Ignores uuid key
5. If diff → `set` with merged payload (existing ⋈ desired to avoid wipe)
6. Optionally `reconfigure` after mutation with verification

Test mode (`__opts__["test"]`) returns `result=None` + changes dict.
Mock helper `tools/test_state.py --mock` proves idempotency second run reports 0 changes even when API returns human FQDN grid and "1" bool.

#### Present/absent pattern rationale (Q11)

Salt state convention is `present`/`absent` (or `managed`/`absent`) rather than verbous `create/update/delete`. We follow same as `firewall.alias`, `host.present`, `user.present`:

- `item_present` ensures item exists with given fields, creates or updates idempotently.
- `item_absent` ensures item does NOT exist, deletes if found.
- Both support `match` dict to locate existing row without knowing UUID upfront (OPNsense API uses UUIDs for mutation, but search returns rows with `hostname`, `domain`, etc).
- Example:

```yaml
www_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: www, domain: example.com}
    - data: {enabled: "1", host: <uuid>, hostname: www, domain: example.com}
    - reconfigure: unbound/service/reconfigure

purge_old:
  opnsense.item_absent:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: old, domain: example.com}
    - reconfigure: unbound/service/reconfigure
```

Why not more specific states like `unbound_host_alias_present`? Initially genericity kept one file vs 400+ functions. Now we have both:

- **Generic** `opnsense.item_present/absent/items_present` – works for all 76 modules, explicit, no magic.
- **Convenience (high-level)** `opnsense_unbound.alias_present/aliases_managed`, `opnsense_bind.record_present`, `opnsense_dns.managed` – resource-specific, human FQDN auto-resolved, pillar-driven, batch with single reconfigure. See `docs/CONVENIENCE.md`.

Generic mirrors `rest_sample` pattern; convenience replaces Jinja loops. Both use same diff engine.

### Grains — why useful?

Grains module `grains/opnsense.py` runs on proxy minion `opnsense-router`:

- `opnsense_version`: from `core/firmware/status` → `product_version`. Allows targeting or reporting: `salt -G 'opnsense_version:24.*' test.ping`, Mine inclusion, dashboard.
- `opnsense_host`: host from client config, confirms which OPNsense.
- `opnsense_api_modules`: list from `opnsense.spec()` (controllers.json) — discoverability, audit.
- Extra future: plugin list, interface count.

Use cases:

- **Targeting**: `G@opnsense_version:25.*` to roll reconfigure only on specific versions.
- **Version reporting**: `salt opnsense-router grains.get opnsense_version` in monitoring, Loki labels via `www_list_loki_label_values` equivalent.
- **Mine**: `mine.send opnsense_version` to share version with master for Renovate drift detection, or push to Prometheus via exporter.
- **Orchestration**: reactor to trigger `generate_spec.py` when version changes.

Execution vs proxy grains: execution module `grains.items` shows static host facts; proxy `grains()` function enriches with live API data. Both merged.

## Codegen maintenance flow

- Tool `tools/generate_spec.py`:
  - Clones `https://github.com/opnsense/core.git` and `plugins.git` (or uses local checkout)
  - `glob` for `*Controller.php` under `src/opnsense/mvc/app/controllers/OPNsense/*/Api/`
  - Regex `public function (\w+)Action`
  - Groups → JSON `{"modules": {"unbound": {"settings": [...]}}}`
- CI: regenerate and `git diff --exit-code tools/controllers.json` fails if stale → Renovate PR includes refreshed file (similar to `vendor_charts.py` post-upgrade hook)
- Future: generate typed Python wrappers `modules/unbound.py`, `modules/bind.py` from registry + Model XML for better docs

Current coverage (Task 7 completion): **all 76 modules free via codegen**

- **Used primary (2026 lab):** `unbound`, `kea` (dhcpv4/v6 reservations), `firewall`, `interfaces`, `bind` (domain+record ACL), `acmeclient` (accounts, validations, actions, certificates)
- **Free via codegen (prove import works, generation costs nothing):** `caddy`, `haproxy`, `nginx`, `wireguard`, `openvpn`, `ipsec`, `crowdsec`, `postfix`, `redis`, `tor`, `quagga`, `auth`, `captiveportal`, `chrony`, `dhcpv4`, `dhcpv6`, `ids`, `monit`, `netbird`, `tailscale`, `zerotier` + 50 more — total 76 modules from `controllers.json`, each with exec+state wrapper (76+76 files) + 1816 dynamic funcs in `modules/opnsense.py`. See `examples/states/free_modules_demo.sls`, `tools/verify_import.py`, `tests/unit/test_free_modules_import.py`.
- **Generic fallback:** even if spec missing a module, `opnsense.call/search/add/set/del` works directly — no code change, just `generate_spec.py --core-ref new --plugins-ref new` + `generate_wrappers.py`
- **Why include free unused modules:** proves import process works end-to-end (file-based gitfs sync via `sync_extmods.py --copy` copies all 76 wrappers to target extmods `_modules/_states/_utils/saltext/...`, and Salt loader discovers them). Cost is zero disk + zero runtime unless used, but gives confidence that future use of any plugin (e.g., migrating haproxy from manual config to Salt) needs zero extension changes.

## Secrets

Pillar `opnsense:` holds host/key/secret. Example for plain:

```yaml
opnsense:
  host: opnsense.example.com
  api_key: ABC
  api_secret: XYZ
```

For vault (saltext-vault):

```yaml
opnsense:
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
```

For SOPS: use `sops:` renderer (future).

Hardcoded keys in legacy custom scripts must be removed after migration.

## Testing (Salt way)

- `tests/unit/utils/test_client.py` — mock requests.Session
- `tests/unit/proxy/test_proxy.py` — mock get_client_from_opts
- `tests/unit/modules/test_opnsense.py` — mock _get_client
- `tests/unit/states/test_opnsense.py` — mock __salt__ search/add/set
- Functional: `loaders.modules.opnsense` fixture provided by pytest-salt-factories
- Integration: optional live against opnsense-router (see `tests/integration/test_live_opnsense.py` placeholder, gated by `OPNSENSE_LIVE_TEST=1`) or MockServer recording

Run: `pytest`, `nox -e tests-3-10`

## Integration with Salt Environment

- Extension file-based (no pip): `_modules/_states/_proxy/_grains/_utils` directories in file root → `salt salt-master saltutil.sync_all`
- Extension pip: `salt-pip install -e .` on salt-master (long-term)
- Alternative master.d: `extension_modules: /path/to/saltext-opnsense/src`
- Pillar `hosts/opnsense-router.sls` with `proxy:` section or file `/etc/salt/proxy` (see `docs/tutorials/pillars/file-based-proxy.yaml` and `top.sls.example`)
- State `opnsense/init.sls` can include example aliases from pillar
- Deployment: `salt-proxy --proxyid=opnsense-router` via systemd on salt-master. Proxy is simpler.

## Future: SSH module

API scope only today. Future SSH module would reuse same state interface but talk via `salt.utils.vt_helper.SSHConnection` for tasks API doesn't cover (e.g., firmware upgrade needing console). Architecture allows second proxytype `opnsense_ssh` sharing utils.

## Comparison with Arista / Cisco proxy examples

- Arista `arista` proxy uses `pyeapi` lib, proxy holds `DEVICE_DETAILS`, execution module `eos` thin wrapper via `__proxy__`.
- Our `opnsense` proxy similar but uses `requests` not `pyeapi`, no need for enable mode, uses key/secret not user/pass
- Cisco NXOS supports both `ssh` and `nxapi` transports; we support `proto` + `verify_ssl` for flexible transport (https verify toggle)
- SaltStack community-extensions-holding pattern: `rest_sample` uses `REST_SAMPLE` dict in proxy, client in utils — we follow same

## Maintainability — dynamic injection vs static wrappers, embedded data, file vs pip

### Dynamic injection (runtime, zero-cost coverage)

`modules/opnsense.py: _inject_dynamic_wrappers()` loads `controllers.json` at import and creates `unbound_settings_search_host_alias`, `bind_record_add_record`, etc in `globals()`. 1816 functions for 76 modules. Salt loader sees them as regular execution functions.

- **Pros:** New OPNsense release = bump `core_ref`/`plugins_ref` in JSON, no Python edit. Works even if `generate_wrappers.py` not run.
- **Cons:** No explicit docstring in source file (doc generated at runtime), IDE may not autocomplete unless Jedi inspects runtime. Debugging stack trace shows wrapper name but file is generic.

### Static ergonomic wrappers (generated, optional, explicit)

`tools/generate_wrappers.py` reads same spec and emits `modules/opnsense_unbound.py` (search/get/add/set/del/toggle + reconfigure) and `states/opnsense_unbound.py` (present/absent). 76+76 files.

- **Pros:** Explicit docstring `/api/{module}/{controller}/{action}`, importable offline, IDE completion, `grep` friendly, useful for `salt-doc`. Same pattern as hand-coded modules but auto-generated, so cost is zero.
- **Cons:** Must regen on OPNsense bump; otherwise dynamic injection already covers but static file stale. `sync_extmods.py --copy` must copy them.

Both coexist: dynamic is fallback, static is convenience. Generic `opnsense.call/search/add` always works even outside spec (e.g., brand new endpoint not yet in JSON — just call directly).

### Embedded data fallback chain

Spec loader `utils/api_spec.py: load_spec()` tries multiple locations in order:

1. `tools/controllers.json` (committed, fallback for CI when src not on PYTHONPATH)
2. `src/saltext/opnsense/utils/controllers.json` (canonical)
3. `cwd/tools/controllers.json` or `cwd/src/saltext/opnsense/utils/controllers.json`
4. `controllers_data.py` (future typed DATA embed, not used yet)
5. Hardcoded tiny subset (`UNBOUND_CONTROLLERS`, `BIND_CONTROLLERS`, etc) — 6 modules only, fails graceful.

In production, (2) wins. In `verify_import.py` import proof, (1) or (2) found. Embedded fallback ensures module still loads even if JSON deleted, but with reduced coverage.

Similarly `utils/opnsense.py` merges config from 4 sources (pillar opnsense, pillar proxy, opts opnsense, opts proxy) — last wins. Supports file-based `/etc/salt/proxy` (flat) and pillar+Vault.

### File-based vs pip install

**File-based (no pip, recommended now, gitfs):**

- File root is gitfs root. Files `_modules/`, `_states/`, `_proxy/`, `_grains/`, `_utils/` served as extmods.
- Symlinks escaping root are blocked by gitfs for security.
- `tools/sync_extmods.py --copy` copies real file contents to target extmods directories `_modules/opnsense.py`, `_states/opnsense.py`, `_proxy/opnsense.py`, `_grains/opnsense.py`, `_utils/opnsense.py`, `_utils/opnsense_api_spec.py`, PLUS all 76 wrappers `opnsense_*.py` and namespace tree `_utils/saltext/opnsense/...`.
- Those real files are committed — CI `sync_extmods.py --check` ensures in sync.
- Verification: `salt salt-master saltutil.sync_all && salt salt-master opnsense.list_api_modules`.
- No `salt-pip` needed, no restart of master (fileserver picks up git commit).

**Pip as saltext (prod, long-term):**

- `salt-pip install -e .` on salt-master and minions that need it, or `extension_modules: /path/to/saltext-opnsense/src` via `master.d/opnsense.conf`.
- Entry point `saltext.opnsense` in `pyproject.toml` exposes to loader via `salt.loader`.
- Benefits: versioned, dependency managed, works with onedir `/opt/saltstack/salt`.
- Drawback: requires pip step and fileserver.update not enough (need pip upgrade).
- Hybrid: file-based now, pip later — code supports both via `_try_import()` in `modules/opnsense.py` trying 4 import paths.

Maintainability trade: file-based is cheapest (one git push), pip is cleaner for a standalone published package. Both work today.

See `CONTRIBUTING.md` for venv setup, `docs/MAINTENANCE.md` for release sprint, `docs/USAGE.md` As Maintainer link.

## Open questions -> QUESTIONS.md

Q2 (secrets backend): file-based `/etc/salt/proxy` for bootstrap, pillar + Vault `__slot__` for prod — both supported via `get_client_from_opts` merging. See `file-based-proxy.yaml`.

Q11 (present/absent): confirmed pure present/absent pattern, matching legacy script ALIASES/PURGE lists but simplified idempotency without exact shell diff logic. Replicates behavior: create if missing, update if val diff, delete if in purge list.

Q12 (additional): grains yes for version/plugin, Kea DHCPv4 reservations supported via `kea/dhcpv4/reservation` API (search/add/set/del) — example in USAGE.md + `kea_reservations.sls`.
