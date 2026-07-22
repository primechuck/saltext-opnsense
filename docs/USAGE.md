# Usage — saltext-opnsense

## Installation (two methods)

### Method 1: File-based sync via Salt file roots (dev, no pip) — RECOMMENDED short-term

No `salt-pip` needed. Extension files live in `projects/saltext-opnsense/src/` and are exposed via symlinks in `infra/salt/states/_modules/`, `_states/`, `_proxy/`, `_grains/`, `_utils/` (including `_utils/saltext/opnsense/...` tree for `saltext.*` import compatibility).

- `infra/salt/states` is gitfs root.
- Salt's fileserver serves `_modules/` etc.
- `salt sparky saltutil.sync_all` → `salt sparky saltutil.list_extmods` → `salt sparky opnsense.list_api_modules`
- Execution module `modules/opnsense.py` includes fallback import (`_try_import`) trying `saltext.opnsense.utils.*`, `salt.utils.opnsense`, `opnsense`, so both pip and file-based work.

See `infra/salt/extensions/README.md` for verification steps and master.d alternative `extension_modules: /srv/.../src`.

### Method 2: Pip as saltext (production)

```bash
salt-pip install -e /srv/configurations/projects/saltext-opnsense
# or from gitfs cache:
salt-pip install -e /var/cache/salt/master/gitfs/refs/base_root/infra/salt/states/extensions/saltext-opnsense

salt sparky saltutil.sync_all
salt sparky opnsense.list_api_modules
```

## Proxy minion dance — file-based vs pillar (Q2)

Salt proxy minion `jrbob` (id `jrbob`) can get credentials two ways:

**A. File-based `/etc/salt/proxy` (flat YAML, no outer `proxy:` wrapper):**

```yaml
# /etc/salt/proxy — lives on sparky host running salt-proxy, NOT in pillar
proxytype: opnsense
host: jrbob.bierce.org
proto: https
verify_ssl: false
api_key: REAL_KEY
api_secret: REAL_SECRET
timeout: 30
```

- Salt proxy loader reads this file directly into `opts['proxy']`.
- No pillar round-trip, no Vault slot resolution (plain text). Good for bootstrap/testing.
- `utils/opnsense.py:get_client_from_opts` merges opts `proxy` last, so file wins.

**B. Pillar-based `pillars/hosts/jrbob.sls` (nested `proxy:` dict, with Vault `__slot__`):**

```yaml
# pillars/hosts/jrbob.sls
proxy:
  proxytype: opnsense
  host: jrbob.bierce.org
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
  api_secret: __slot__:salt:vault.read(secret/opnsense/api_secret)
```

- Master compiles pillar for minion id `jrbob` (via `top.sls` entry `'jrbob': - hosts.jrbob`), resolves `__slot__` on master, sends encrypted to proxy minion.
- Proxy `init(opts)` gets `opts['proxy']` from pillar transport (or from file if both exist, file wins per merge order: pillar opnsense, pillar proxy, opts opnsense, opts proxy).
- Allows Vault/OpenBao secrets without plaintext file.

**Hybrid:**

- Minimal file with only `proxytype: opnsense`, rest from pillar `opnsense:` (direct fallback).
- `opnsense:` pillar always kept for direct mode `salt sparky opnsense.call ...` and CMDB (aliases, bind_zone, cluster_parent).

See:

- `examples/pillars/file-based-proxy.yaml` — annotated file-based example + dance explanation
- `examples/pillars/top.sls.example` — how to add jrbob to pillar top.sls
- `infra/salt/pillars/hosts/jrbob.sls` — simplified, comments both options, always keeps `opnsense:` CMDB

Run proxy:

```bash
salt-proxy --proxyid=jrbob -l debug --log-file=/var/log/salt/proxy
# systemd unit on sparky recommended long-term
```

## Direct execution from Sparky (no proxy) vs proxy

- **Proxy mode** `salt jrbob ...`: goes via `__proxy__` thin wrapper, client lives in proxy process `DETAILS['client']`. Supports grains.
- **Direct mode** `salt sparky opnsense.call ...`: execution module calls `get_client_from_opts(__opts__, __pillar__)` directly, using pillar `opnsense:`. No proxy minion needed, simpler for one-off queries.
- `get_client_from_opts` merging allows both simultaneously.

```bash
salt sparky pillar.get opnsense
salt sparky opnsense.call unbound settings searchHostAlias
salt sparky opnsense.search unbound settings host_alias search_phrase=grafana
salt sparky opnsense.search bind record record row_count=-1

salt jrbob test.ping
salt jrbob opnsense.ping
salt jrbob opnsense.list_api_modules
salt jrbob opnsense.list_api_controllers unbound
salt jrbob opnsense.list_api_actions unbound settings
```

## State usage — present/absent pattern (Q11 confirmed)

Salt convention is `present`/`absent` (like `host.present`, `user.present`, `firewall.alias`). We follow same with generic `opnsense.item_present` / `item_absent`:

- `item_present`: ensure item exists with given fields, creates via `add_{type}` or updates via `set_{type}` if `match` found but fields differ.
- `item_absent`: ensure item does NOT exist, deletes via `del_{type}` if `match` found.
- Both use `match` dict to locate existing row without knowing UUID (OPNsense API requires UUID for set/del, but search returns `hostname`, `domain`, `ip`, etc). No UUID needed in SLS.
- `reconfigure: <module>/<controller>/<action>` optional triggers configd apply (e.g., `unbound/service/reconfigure`). Explicit rather than auto, allows batching multiple changes then one reconfigure (or omit and rely on separate `reconfigured` state).

Why not specific wrappers like `unbound_host_alias_present`? Genericity keeps one state file vs 400+ hand-coded functions. Ergonomic wrappers can be code-generated later from Model XML + `controllers.json`, but present/absent generic is sufficient day 1 and mirrors `rest_sample` pattern. It also directly replaces `personal/scripts/query.sh` ALIASES/PURGE lists:

```yaml
# Before: query.sh had ALIASES=(forgejo grafana ...) and PURGE=(gitea ...)
# After: pillar opnsense:aliases + purge_aliases looped in state

{% for domain, hosts in pillar.get('opnsense', {}).get('aliases', {}).items() %}
{% for hostname in hosts %}
unbound_alias_{{ domain }}_{{ hostname }}:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: {{ hostname }}, domain: {{ domain }}}
    - data:
        enabled: "1"
        host: {{ pillar['opnsense']['cluster_parent']['uuid'] }}
        hostname: {{ hostname }}
        domain: {{ domain }}
        description: "managed by salt - {{ hostname }}.{{ domain }}"
    - reconfigure: unbound/service/reconfigure
{% endfor %}
{% endfor %}

{% for domain, hosts in pillar.get('opnsense', {}).get('purge_aliases', {}).items() %}
{% for hostname in hosts %}
purge_unbound_alias_{{ domain }}_{{ hostname }}:
  opnsense.item_absent:
    - name: {{ hostname }}.{{ domain }}
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: {{ hostname }}, domain: {{ domain }}}
    - reconfigure: unbound/service/reconfigure
{% endfor %}
{% endfor %}
```

Generic item docs:

```yaml
ensure_grafana_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: grafana
        domain: bierce.org
    - data:
        enabled: "1"
        host: {{ pillar['opnsense']['cluster_parent']['uuid'] }}
        hostname: grafana
        domain: bierce.org
        description: "managed by salt"
    - reconfigure: unbound/service/reconfigure

remove_old:
  opnsense.item_absent:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: old
        domain: bierce.org
    - reconfigure: unbound/service/reconfigure
```

Behavior details:

- Search all rows `rowCount=-1`, linear match on `match` dict string compare.
- If missing → add.
- If exists, diff flat_data vs existing (handles OPNsense `"1"/"0"` bool style via str compare).
- If diff → set.
- Test mode `test=True` returns `result=None` + changes dict without calling API.

Replace `personal/scripts/query.sh`:
```bash
salt jrbob state.apply opnsense.aliases
```

Replace `personal/scripts/sync-bind-zone.sh`:
```bash
salt jrbob state.apply opnsense.bind_records  # examples/states/bind_records.sls
```

## Grains — why useful?

Grains module `grains/opnsense.py` runs only when proxy minion is up (or via `__proxy__`):

```bash
salt jrbob grains.get opnsense_version
salt jrbob grains.get opnsense_host
salt jrbob grains.get opnsense_api_modules
salt jrbob grains.items
```

Implementation:

- `grains()` in `proxy/opnsense.py` returns `opnsense_version` from `core/firmware/status` + `opnsense_host` from client config.
- `grains/opnsense.py` (`opnsense_grains`) calls `opnsense.ping()` then `opnsense.spec()` for module list and firmware version.

Use cases:

- **Targeting**: `salt -G 'opnsense_version:25.*' test.ping` or `G@opnsense_version:25.1` to roll changes only on specific OPNsense releases.
- **Version reporting**: daily `salt jrbob grains.get opnsense_version` logged to Loki, alert if drift vs Renovate-tracked core_ref.
- **Mine**: `mine.send opnsense_version` pushes version to master, master can expose to Prometheus or use in reactor to trigger `generate_spec.py` when version changes.
- **Discovery**: `opnsense_api_modules` grain lists all modules from `controllers.json` + live spec, useful for audit that codegen is up to date.
- **Dashboard**: Grafana dashboard variable filtering by version.

Proxy vs execution grains: execution grains are static host facts; proxy grains enrich with live API data. Both merged in `grains.items`.

## Kea DHCPv4 reservations (Q12 — supported via API)

OPNsense Kea API docs: https://docs.opnsense.org/development/api/core/kea.html

Kea model: `src/opnsense/mvc/app/models/OPNsense/Kea/KeaDhcpv4.xml` — reservation fields: subnet (UUID), ip_address, hw_address, hostname, description, client_id, next_server, option_data, option.

API coverage in controllers.json:
- kea dhcpv4: search_subnet/get_subnet/add_subnet/set_subnet/del_subnet, search_reservation/get_reservation/add_reservation/set_reservation/del_reservation, search_option, search_peer, download/upload reservations, etc.
- kea dhcpv6: similar + pd_pool
- kea leases: search, del_lease, searchLease4/6
- kea ctrl_agent, ddns: get/set singleton
- kea service: reconfigure/restart/status

Execution module usage:

```bash
# List subnets and reservations
salt jrbob opnsense.search kea dhcpv4 subnet row_count=-1
salt jrbob opnsense.search kea dhcpv4 reservation search_phrase=aa:bb:cc row_count=-1
salt jrbob opnsense.search kea dhcpv4 reservation row_count=-1

# Get single reservation
salt jrbob opnsense.get kea dhcpv4 reservation <uuid>

# Call raw API (download/upload CSV)
salt jrbob opnsense.call kea dhcpv4 download_reservations
salt jrbob opnsense.call kea dhcpv4 upload_reservations '{"payload":"...csv..."}'
```

State usage (examples/states/kea_reservations.sls):

```yaml
# Subnet must exist first — its UUID is required in reservation.subnet field.
kea_subnet_mgmt:
  opnsense.item_present:
    - module: kea
    - controller: dhcpv4
    - type: subnet
    - match:
        subnet: 172.18.60.0/24
    - data:
        subnet: 172.18.60.0/24
        description: "mgmt - salt"
    - reconfigure: kea/service/reconfigure

grafana_reservation:
  opnsense.item_present:
    - name: grafana-172.18.60.30
    - module: kea
    - controller: dhcpv4
    - type: reservation
    - match:
        hw_address: "02:42:ac:11:00:02"
        ip_address: "172.18.60.30"
    - data:
        subnet: "SUBNET_UUID_FROM_searchSubnet"
        ip_address: "172.18.60.30"
        hw_address: "02:42:ac:11:00:02"
        hostname: "grafana"
        description: "grafana svc - salt managed"
    - reconfigure: kea/service/reconfigure

# Pillar-driven loop (see kea_reservations.sls full file for Jinja)
# pillar:
#   opnsense:
#     kea:
#       reservations:
#         - {hostname: grafana, ip_address: 172.18.60.30, hw_address: "02:42:ac:11:00:02", subnet_uuid: "<uuid>", description: "svc"}
```

Notes:
- Reservation uniqueness enforced by OPNsense: subnet+hw_address and subnet+client_id unique. ip_address also unique globally for subnet.
- Model fields accept optional option_data (domain_name_servers, routers, etc).
- After changes, reconfigure kea/service/reconfigure (also restarts Kea).
- VLAN 50 (Wireless IoT) static reservations can be managed this way even though VLAN 60+ uses K3s static IPs.

DHCPv6 reservations identical but using dhcpv6 controller:
```bash
salt jrbob opnsense.search kea dhcpv6 reservation row_count=-1
```

## Bind and Unbound full coverage (core + bind focus)

- unbound settings: searchHostOverride/getHostOverride/addHostOverride/setHostOverride/delHostOverride/toggleHostOverride, searchHostAlias/getHostAlias/addHostAlias/setHostAlias/delHostAlias/toggleHostAlias, searchDot/getDot/addDot/setDot/delDot, searchForward/getForward/addForward/setForward/delForward, get/set singleton, plus ACL, DNSBL, DOT via forward compat.
- unbound service: reconfigure, reconfigure_general, restart, start, status, stop, dnsbl
- unbound diagnostics: stats, listLocalZones, listLocalData, dumpCache, dumpInfra, testBlocklist
- unbound overview: isEnabled, isBlockListEnabled, getPolicies, searchQueries, totals
- bind domain: Primary/Secondary/Forward search/get/add/set/del/toggle + master/slave legacy
- bind record: search/get/add/set/del/toggle
- bind acl: search/get/add/set/del/toggle
- bind general: get/set/zoneshow/zonetest
- bind service: reconfigure/restart/start/status/stop/dnsbl
- bind dnsbl: get/set

```bash
salt jrbob opnsense.list_api_actions bind domain
salt jrbob opnsense.list_api_actions bind record
salt jrbob opnsense.list_api_actions unbound settings
salt jrbob opnsense.list_api_actions unbound service
```

Examples in `examples/states/bind_records.sls` and `unbound_aliases.sls` — now driven by pillar `opnsense:aliases` + `bind_zone`.

## ACME client (acmeclient plugin) — core + acme coverage

Docs: https://docs.opnsense.org/development/api/plugins/acmeclient.html

Controllers in controllers.json (full coverage):
- acmeclient accounts: search/get/add/set/del/toggle/update/register
- acmeclient actions: search/get/add/set/del/toggle/update/sftp_get_identity/sftp_test_connection/ssh_get_identity/ssh_test_connection
- acmeclient certificates: search/get/add/set/del/toggle/update/automation/import/removekey/revoke/sign
- acmeclient service: configtest/reconfigure/reset/restart/signallcerts/start/status/stop
- acmeclient settings: get/set/fetch_cron_integration/fetch_h_a_proxy_integration/get_bind_plugin_status/get_gcloud_plugin_status
- acmeclient validations: search/get/add/set/del/toggle/update

Execution:

```bash
salt jrbob opnsense.list_api_controllers acmeclient
salt jrbob opnsense.search acmeclient accounts account row_count=-1
salt jrbob opnsense.search acmeclient validations validation row_count=-1
salt jrbob opnsense.search acmeclient certificates certificate row_count=-1
salt jrbob opnsense.call acmeclient service status
salt jrbob opnsense.call acmeclient certificates sign <uuid>
```

State example `examples/states/acme_certificates.sls` shows pillar-driven loop for accounts/validations/actions/certificates with UUID resolution workflow:

1. Create accounts/validations/actions via states
2. Lookup UUIDs: `salt jrbob opnsense.search acmeclient accounts account search_phrase=<name>`
3. Store UUIDs in pillar or orchestrate via Jinja.

## Codegen refresh on OPNsense release

```bash
cd projects/saltext-opnsense
python tools/generate_spec.py --core-ref 25.7 --plugins-ref 25.7 --output src/saltext/opnsense/utils/controllers.json
# also copy to tools/ for CI fallback:
cp src/saltext/opnsense/utils/controllers.json tools/controllers.json
towncrier create --edit
```

Add Renovate customManager regex for `core_ref` tracking (see `renovate-snippet.json5`).

## Testing

```bash
# unit only, no salt package required (mocked)
PYTHONPATH=src pytest tests/unit -v

# with salt installed (real execution modules)
pip install salt
salt-call --local --file-root=tests --pillar-root=tests opnsense.call unbound settings searchHostAlias

# integration (live against jrbob) — gated by env var
OPNSENSE_LIVE_TEST=1 pytest tests/integration/test_live_opnsense.py -v
# See tests/integration/README.md for setup
```

- Unit: mock `requests.Session`, `__proxy__`, `__salt__` — no live OPNsense needed
- Functional: `loaders.modules.opnsense` fixture via pytest-salt-factories
- Integration: TODO placeholder `test_live_opnsense.py` skipped unless `OPNSENSE_LIVE_TEST=1`, documents how to run against real jrbob (see task 6)

## Migrating hardcoded keys

1. Move keys from `personal/scripts/*.sh` into `pillar/secrets` or OpenBao `secret/opnsense/*`
2. Update `personal/scripts/query.sh` to use `salt jrbob opnsense.search` via `salt --out=json` instead of curl, or deprecate entirely
3. Ensure `purge` lists stay identical to avoid DNS churn
4. Remove hardcoded keys after migration verified via `salt jrbob state.apply opnsense.aliases --test`

## Pillar examples reference

- `examples/pillars/jrbob.sls` — legacy vault slot example for proxy + opnsense
- `examples/pillars/opnsense.sls` — full CMDB example with cluster_parent, aliases, host_overrides_direct, bind_zone records
- `examples/pillars/file-based-proxy.yaml` — file-based `/etc/salt/proxy` flat format + dance explanation (NEW)
- `examples/pillars/top.sls.example` — how to add jrbob to `infra/salt/pillars/top.sls` (NEW)
- `infra/salt/pillars/hosts/jrbob.sls` — simplified production pillar, file-based primary + vault commented, CMDB always present
