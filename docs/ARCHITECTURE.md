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
- **Pillar-based** `pillars/hosts/jrbob.sls` → `proxy:` nested dict → master compiles pillar for minion id `jrbob`, resolves `__slot__:salt:vault.read` on master, sends via encrypted transport to proxy minion. Allows Vault.
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

Idempotency:
1. `search` all rows `rowCount=-1`
2. Match via `match` dict (e.g., `hostname+domain`)
3. If missing → `add`
4. If exists, diff fields (string compare, handles "1"/"0" bool style)
5. If diff → `set`
6. Optionally `reconfigure` after mutation

Test mode (`__opts__["test"]`) returns `result=None` + changes dict.

#### Present/absent pattern rationale (Q11)

Salt state convention is `present`/`absent` (or `managed`/`absent`) rather than verbous `create/update/delete`. We follow same as `firewall.alias`, `host.present`, `user.present`:

- `item_present` ensures item exists with given fields, creates or updates idempotently.
- `item_absent` ensures item does NOT exist, deletes if found.
- Both support `match` dict to locate existing row without knowing UUID upfront (OPNsense API uses UUIDs for mutation, but search returns rows with `hostname`, `domain`, etc).
- Example:

```yaml
grafana_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: grafana, domain: bierce.org}
    - data: {enabled: "1", host: <uuid>, hostname: grafana, domain: bierce.org}
    - reconfigure: unbound/service/reconfigure

purge_old:
  opnsense.item_absent:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: old, domain: bierce.org}
    - reconfigure: unbound/service/reconfigure
```

Why not more specific states like `unbound_host_alias_present`? Genericity keeps one file vs 400+ hand-coded functions. Ergonomic wrappers can be code-generated later from Model XML + controllers.json, but present/absent generic is sufficient for day 1. It mirrors `rest_sample` pattern.

### Grains — why useful?

Grains module `grains/opnsense.py` runs on proxy minion `jrbob`:

- `opnsense_version`: from `core/firmware/status` → `product_version`. Allows targeting or reporting: `salt -G 'opnsense_version:24.*' test.ping`, Mine inclusion, dashboard.
- `opnsense_host`: host from client config, confirms which OPNsense.
- `opnsense_api_modules`: list from `opnsense.spec()` (controllers.json) — discoverability, audit.
- Extra future: plugin list, interface count.

Use cases:

- **Targeting**: `G@opnsense_version:25.*` to roll reconfigure only on specific versions.
- **Version reporting**: `salt jrbob grains.get opnsense_version` in monitoring, Loki labels via `grafana_list_loki_label_values` equivalent.
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

Current coverage focus (per feedback): **core + bind + acme**:

- core: `unbound`, `kea` (dhcpv4/v6 reservations), `firewall`, `interfaces`, `wireguard`, `core/firmware`
- plugins: `bind` (domain+record ACL), `acmeclient` (accounts, validations, actions, certificates), `caddy`/`haproxy` future
- All others templated via generic `opnsense.call/search/add/set/del` — no code change needed, just registry refresh.

## Secrets

Pillar `opnsense:` holds host/key/secret. Example for plain:

```yaml
opnsense:
  host: jrbob.bierce.org
  api_key: ABC
  api_secret: XYZ
```

For vault (saltext-vault):

```yaml
opnsense:
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
```

For SOPS: use `sops:` renderer (future).

Hardcoded keys in `personal/scripts/query.sh` must be removed after migration.

## Testing (Salt way)

- `tests/unit/utils/test_client.py` — mock requests.Session
- `tests/unit/proxy/test_proxy.py` — mock get_client_from_opts
- `tests/unit/modules/test_opnsense.py` — mock _get_client
- `tests/unit/states/test_opnsense.py` — mock __salt__ search/add/set
- Functional: `loaders.modules.opnsense` fixture provided by pytest-salt-factories
- Integration: optional live against jrbob (see `tests/integration/test_live_opnsense.py` placeholder, gated by `OPNSENSE_LIVE_TEST=1`) or MockServer recording

Run: `pytest`, `nox -e tests-3-10`

## Integration with infra/salt monorepo

- Extension file-based (no pip): `infra/salt/states/_modules/_states/_proxy/_grains/_utils` symlinks to `projects/saltext-opnsense/src/...` → `salt sparky saltutil.sync_all`
- Extension pip: `salt-pip install -e projects/saltext-opnsense` on sparky master (long-term)
- Alternative master.d: `extension_modules: /srv/configurations/projects/saltext-opnsense/src` (see `infra/salt/extensions/README.md`)
- Pillar `hosts/jrbob.sls` with `proxy:` section or file `/etc/salt/proxy` (see `examples/pillars/file-based-proxy.yaml` and `top.sls.example`)
- State `opnsense/init.sls` in `infra/salt/states/` can include example aliases from pillar
- Deployment: `salt-proxy --proxyid=jrbob` via systemd on sparky? Or use `salt-ssh` with roster `jrbob` as `thin`? Proxy is simpler.

## Future: SSH module

API scope only today. Future SSH module would reuse same state interface but talk via `salt.utils.vt_helper.SSHConnection` for tasks API doesn't cover (e.g., firmware upgrade needing console). Architecture allows second proxytype `opnsense_ssh` sharing utils.

## Comparison with Arista / Cisco proxy examples

- Arista `arista` proxy uses `pyeapi` lib, proxy holds `DEVICE_DETAILS`, execution module `eos` thin wrapper via `__proxy__`.
- Our `opnsense` proxy similar but uses `requests` not `pyeapi`, no need for enable mode, uses key/secret not user/pass
- Cisco NXOS supports both `ssh` and `nxapi` transports; we support `proto` + `verify_ssl` for flexible transport (https verify toggle)
- SaltStack community-extensions-holding pattern: `rest_sample` uses `REST_SAMPLE` dict in proxy, client in utils — we follow same

## Open questions -> QUESTIONS.md

Q2 (secrets backend): file-based `/etc/salt/proxy` for bootstrap, pillar + Vault `__slot__` for prod — both supported via `get_client_from_opts` merging. See `file-based-proxy.yaml`.

Q11 (present/absent): confirmed pure present/absent pattern, matching legacy script ALIASES/PURGE lists but simplified idempotency without exact shell diff logic. Replicates behavior: create if missing, update if val diff, delete if in purge list.

Q12 (additional): grains yes for version/plugin, Kea DHCPv4 reservations supported via `kea/dhcpv4/reservation` API (search/add/set/del) — example in USAGE.md + `kea_reservations.sls`.
