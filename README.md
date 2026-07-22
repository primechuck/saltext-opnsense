# saltext-opnsense

SaltStack 3008+ extension for managing OPNsense via its API — templated for easy OPNsense release sprints.

> **Status:** Beta — generic + dynamic wrappers + static ergonomic wrappers (unbound/bind/acmeclient/kea/firewall/interfaces), 27 unit tests, file-based install ready, proxy+direct modes.

## Why this design is maintainable

Previous OPNsense Salt modules hand-coded 400+ functions. This extension does **codegen + dynamic injection**:

1. **Spec:** `tools/generate_spec.py` clones `opnsense/core` + `plugins`, regex `public function (\w+)Action` from `.../Api/*Controller.php` → `controllers.json` (module → controller → actions). Both camelCase + snake_case kept.
2. **Dynamic injection (runtime):** `modules/opnsense.py` loads `controllers.json` at import and injects `unbound_settings_search_host_alias`, `bind_record_add_record`, etc. New OPNsense release = change `core_ref`/`plugins_ref` in JSON, no Python edit. Salt loader picks up injected functions automatically.
3. **Static ergonomic wrappers (optional, explicit):** `tools/generate_wrappers.py` reads same spec and emits `modules/opnsense_unbound.py` etc with docstrings (`/api/{module}/{controller}/{action}`) and `states/opnsense_unbound.py` with `host_alias_present/absent`. Good for offline docs + IDE completion; can be skipped because dynamic injection already guarantees coverage.
4. **Model registry (future):** `tools/generate_models.py` parses `Model.xml` (Unbound.xml, Bind.xml, KeaDhcpv4.xml, AcmeClient.xml) → `models.json` for field validation, required flags, help text.

Result: 1 generic execution module + 1 generic state module handle **all** endpoints. Spriting OPNsense 25.7 → 26.1 = regenerating JSON via Renovate PR + running wrapper generator.

## Two install methods — pip vs file-based (no pip)

User wants short-term no-pip:

- **Method 1 (dev, no pip, recommended now):** File-based via gitfs file roots.
  `infra/salt/states` is gitfs root. Salt serves `_modules/`, `_states/`, `_proxy/`, `_grains/`, `_utils/` as extmods via `saltutil.sync_all`. 
  - Symlinks `states/_modules/opnsense.py -> ../../../../projects/saltext-opnsense/src/...` work for local file roots.
  - For gitfs (symlinks escaping root blocked), `tools/sync_extmods.py --copy` copies real files into `infra/salt/states/_modules/` etc plus `_utils/saltext/opnsense/...` namespace tree. Those real files are committed and served via gitfs, fully compatible. CI `sync_extmods.py --check` ensures sync.
  - Verification: `salt sparky saltutil.sync_all && salt sparky opnsense.list_api_modules`

- **Method 2 (prod, long-term):** Pip as saltext.
  ```bash
  salt-pip install -e projects/saltext-opnsense
  salt sparky saltutil.sync_all
  ```
  Also `master.d/opnsense.conf` example for `extension_modules: /srv/.../src` alternative.

See `infra/salt/extensions/README.md` for both paths.

## Proxy dance — file-based `/etc/salt/proxy` vs pillar

OPNsense uses API key/secret BasicAuth. Salt proxy minion `jrbob` can get creds two ways:

- **File `/etc/salt/proxy` (flat YAML, no outer `proxy:` wrapper, short-term/bootstrap):**
  ```yaml
  proxytype: opnsense
  host: jrbob.bierce.org
  proto: https
  verify_ssl: false
  api_key: REAL
  api_secret: REAL
  ```
  Loader reads file directly into `opts['proxy']`, no Vault. Good for bootstrap.

- **Pillar `pillars/hosts/jrbob.sls` (nested `proxy:` with `__slot__`):**
  ```yaml
  proxy:
    proxytype: opnsense
    host: jrbob.bierce.org
    api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
  ```
  Master resolves `__slot__` and sends to proxy. Allows OpenBao secrets.

Hybrid: minimal file with only `proxytype: opnsense`, rest from pillar `opnsense:` (direct fallback). `get_client_from_opts` merges pillar `opnsense`, pillar `proxy`, opts `opnsense`, opts `proxy` — file wins last.

`opnsense:` pillar always kept for direct mode `salt sparky opnsense.call ...` and CMDB (aliases, kea subnets, acme accounts).

Examples: `examples/pillars/file-based-proxy.yaml`, `examples/pillars/jrbob.sls`, `examples/pillars/top.sls.example`

## Execution API — generic + dynamic + static wrappers

Generic (always works for any endpoint, even without spec):

```bash
salt jrbob opnsense.call unbound settings searchHostAlias rowCount=-1
salt jrbob opnsense.search unbound settings host_alias
salt jrbob opnsense.get unbound settings host_alias <uuid>
salt jrbob opnsense.add unbound settings host_alias '{"alias":{"enabled":"1","host":"<uuid>","hostname":"grafana","domain":"bierce.org"}}'
salt jrbob opnsense.reconfigure unbound service
```

Dynamic wrappers auto-injected at import from spec (312 functions):

```bash
salt jrbob opnsense.unbound_settings_search_host_alias
salt jrbob opnsense.bind_record_search_record
salt jrbob opnsense.kea_dhcpv4_search_reservation
salt jrbob opnsense.acmeclient_certificates_search_certificate
```

Static ergonomic wrappers (also available, explicit docs):

```bash
salt jrbob opnsense_unbound.search_host_alias
salt jrbob opnsense_bind.search_record
salt jrbob opnsense_kea.search_reservation
salt jrbob opnsense_acmeclient.search_certificate
```

Direct mode (no proxy):

```bash
salt sparky opnsense.call unbound settings searchHostAlias
```

## State API — present/absent (confirmed pattern)

Generic state handles all endpoints, idempotent via search+match:

```yaml
grafana_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: grafana, domain: bierce.org}
    - data:
        enabled: "1"
        host: {{ cluster_parent_uuid }}
        hostname: grafana
        domain: bierce.org
    - reconfigure: unbound/service/reconfigure

remove_hermes:
  opnsense.item_absent:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: hermes, domain: bierce.org}
    - reconfigure: unbound/service/reconfigure
```

Dynamic state wrappers also injected (`unbound_settings_host_alias_present` etc) and static wrappers in `opnsense_unbound` state module:

```yaml
grafana:
  opnsense_unbound.host_alias_present:
    - data: {host: <uuid>, hostname: grafana, domain: bierce.org}
```

- `match` dict finds existing UUID without knowing it (API requires UUID for set/del).
- Diff via string compare handles OPNsense `"1"/"0"` bools.
- `reconfigure` explicit (user preference) allows batching; omit and use separate `opnsense.reconfigured` state if desired.
- `test=True` supported.

## Grains — why?

`grains/opnsense.py` exposes `opnsense_version`, `opnsense_api_modules` when proxy up. Useful for targeting (`salt -G opnsense_version:25.7 ...`), Mine, and CMDB inventory (per `cmdb-thought.md` idea).

```bash
salt jrbob grains.get opnsense_version
```

## Coverage — core + bind + acmeclient + kea reservations

From `tools/controllers.json` (curated 25.7, both camel/snake):

- **unbound:** settings (host_override, host_alias, dot, forward, acl, dnsbl), service (reconfigure, dnsbl), diagnostics (stats, listLocalZones, dumpCache), overview (isEnabled, searchQueries)
- **bind:** domain (primary/secondary/forward/master/slave), record (A/CNAME/MX/TXT), acl, general (get/set/zoneshow), service, dnsbl
- **kea:** dhcpv4/dhcpv6 full (subnet, reservation, option, peer, pd_pool, download/upload), leases (search, del_lease), ctrl_agent/ddns, service — supports reservations even if not used today
- **acmeclient:** accounts, validations, certificates (automation/import/revoke/sign), actions (sftp/ssh identity), settings (cron/haproxy/bind/gcloud status), service
- **firewall/interfaces:** alias, filter (apply/savepoint/cancelRollback), vlan, vip, etc.

Missing plugin? Run `generate_spec.py` — if controller exists upstream, it appears as new dynamic function.

## Testing — Salt way

```bash
PYTHONPATH=src pytest tests/unit -v  # 27 tests, mocked, no live OPNsense
pytest tests/integration -v           # skipped unless OPNSENSE_LIVE_TEST=1 (see test_live_opnsense.py)
python tools/test_live.py --host jrbob.bierce.org --key ... --secret ...  # direct client smoke, no Salt
python tools/sync_extmods.py --check  # CI ensures _modules copies in sync
python tools/generate_wrappers.py --dry-run
```

- Unit mocks `__proxy__`, `requests.Session`
- Functional via `pytest-salt-factories` loaders
- Integration live against jrbob via env vars

## Renovate — OPNsense release sprint

`renovate.json5` customManagers track `core_ref`/`plugins_ref` in `controllers.json` (both `tools/` and `src/.../utils/`). When `opnsense/core` tags 25.7→26.1, Renovate PR bumps JSON, postUpgradeTasks runs:

```bash
cd projects/saltext-opnsense && python tools/generate_spec.py --core-ref <new> --plugins-ref <new> --output src/.../controllers.json && cp src/.../controllers.json tools/controllers.json
cd infra/k8s && python3 vendor_charts.py all
```

Then `generate_wrappers.py` can be run manually or in same post-upgrade to refresh ergonomic wrappers.

## File layout

```
src/saltext/opnsense/
  utils/opnsense.py        — OPNsenseClient (requests, BasicAuth, search/get/add/set/del/toggle/reconfigure)
  utils/api_spec.py + controllers.json — spec loader, fallback curated unbound/bind/kea/acme
  proxy/opnsense.py        — proxy minion (DETAILS['client'] in __context__)
  modules/opnsense.py      — generic + dynamic injection (312 funcs from spec)
  modules/opnsense_{module}.py — static ergonomic wrappers (generated)
  states/opnsense.py       — generic item_present/absent/reconfigured + dynamic injection
  states/opnsense_{module}.py — static state wrappers (generated)
  grains/opnsense.py
tools/
  generate_spec.py         — clone core/plugins, parse *Controller.php → controllers.json
  generate_wrappers.py     — spec → exec+state wrappers
  generate_models.py       — Model XML → models.json (field schemas for future validation)
  sync_extmods.py          — copy src → infra/salt/states/_* for no-pip gitfs install
  test_live.py             — live smoke without Salt
infra/salt/
  states/_modules/…        — real files (copied, gitfs compatible)
  states/opnsense/         — states replacing query.sh / sync-bind-zone.sh
  pillars/hosts/jrbob.sls  — proxy + CMDB (aliases, kea, acme)
```

## Next iterations — better ways

- Parse Model XML for required fields → validation error messages surfaced in state `comment` (currently generic `validations` dict)
- Use `Model.xml` to auto-generate pillar SLS schemas for autocomplete
- Add `bind` zone transfer (AXFR) state eventually
- Publish as own repo `empire/saltext-opnsense` via `git subtree split`

See `docs/ARCHITECTURE.md`, `docs/USAGE.md`, `docs/DEVELOPMENT.md`, `QUESTIONS.md`.
