# Usage — saltext-opnsense

## Convenience / high-level wrappers (human-friendly)

Salt thinking is tedious when you have to remember `module: unbound`, `controller: settings`, `type: host_alias`, `match: {hostname: ..., domain: ...}`, and `reconfigure: unbound/service/reconfigure` every time. The convenience layer hides all that.

### Before — clunky generic

```yaml
www_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: www, domain: example.com}
    - data:
        enabled: "1"
        host: 550e8400-e29b-41d4-a716-446655440000
        hostname: www
        domain: example.com
        description: "managed by salt"
    - reconfigure: unbound/service/reconfigure
```

Problems: 6 fields to remember, UUID hunting, Jinja loops everywhere, reconfigure path is tribal knowledge.

### After — convenience single-alias (high-level)

```yaml
www:
  opnsense_unbound.alias_present:
    - parent: cluster.example.com
    - domain: example.com
```

Parent is human FQDN `cluster.example.com`, not UUID — auto-resolved via search. `reconfigure` is auto-inferred to `unbound/service/reconfigure` when `True`/`None`. No `module/controller/type/match` dance.

CLI equally friendly:

```bash
salt opnsense-router opnsense_unbound.list_aliases
# {'www.example.com': {'parent': 'cluster.example.com', 'uuid': '...', ...}}

salt opnsense-router opnsense_unbound.list_host_overrides
# {'cluster.example.com': {'ip': '192.0.2.10', 'uuid': '...'}}

salt opnsense-router opnsense_unbound.resolve_parent cluster.example.com
# 550e8400-...

salt opnsense-router opnsense_bind.list_domains
salt opnsense-router opnsense_bind.list_records domain=example.com
salt opnsense-router opnsense_kea.list_subnets
salt opnsense-router opnsense_kea.list_reservations subnet=192.0.2.0/24
salt opnsense-router opnsense_acmeclient.list_certificates
```

### After — convenience batch (replaces Jinja loops, one reconfigure)

```yaml
dns_batch:
  opnsense_unbound.aliases_managed:
    - parent: cluster.example.com
    - aliases:
        example.com:
          - www
          - git
          - auth
          - admin
        internal.example.com:
          - code
          - ide
          - ai
    - purge:
        example.com:
          - old-git
          - old-service
```

One state, single reconfigure at end, no Jinja loop explosion. Reads pillar automatically if you omit args:

```yaml
# salt/opnsense/aliases_convenience.sls — no Jinja, pure pillar
dns:
  opnsense_dns.managed:
    - parent: cluster.example.com
# or even:
# dns:
#   opnsense_dns.managed: []
# which reads pillar opnsense:aliases + opnsense:purge_aliases + opnsense:cluster_parent

# pillar/hosts/opnsense-router.sls stays simple:
# opnsense:
#   cluster_parent: {hostname: cluster, domain: example.com}
#   aliases:
#     example.com: [git, www, ...]
#     internal.example.com: [code, ...]
#   purge_aliases:
#     example.com: [old-git]
```

Why happier?

- Hides `module/controller/type` + `match` dict behind domain vocabulary.
- Human parent `cluster.example.com` not UUID.
- Auto-inferred reconfigure (`unbound/service/reconfigure`, `bind/service/reconfigure`, `kea/service/reconfigure` automatically when `reconfigure: True/None`).
- Batch `aliases_managed` / `opnsense_dns.managed` eliminates N*N states → 1 state, 1 reconfigure.
- Pillar-direct reading removes Jinja loops from SLS — edit pillar, not SLS.
- Execution modules return `www.example.com -> cluster.example.com` dicts, not raw API rows.

Full convenience state modules (high-level wrappers):

- `opnsense_unbound.alias_present(name, parent, domain="example.com", description=None, enabled=True, reconfigure=True)`
- `opnsense_unbound.alias_absent(name, domain="example.com", reconfigure=True)`
- `opnsense_unbound.aliases_managed(name, parent, aliases={domain:[...]}, purge={domain:[...]}, reconfigure=True)`
- `opnsense_bind.domain_present(name, ...)` + `record_present(name, domain, type="A", value=...)`
- `opnsense_dns.managed(name, parent=None, aliases=None, purge=None)` — high-level, pillar-aware

Apply:

```bash
salt opnsense-router state.apply opnsense.convenience_aliases
# deprecated shim still works for backward compat:
salt opnsense-router state.apply opnsense.aliases_delightful
salt opnsense-router state.apply opnsense.aliases  # legacy generic still works
```

## Installation (two methods)

### Method 1: File-based sync via Salt file roots (dev, no pip) — RECOMMENDED short-term

No `salt-pip` needed. Extension files live in `src/` and are exposed via extmods directories `_modules/`, `_states/`, `_proxy/`, `_grains/`, `_utils/` (including `_utils/saltext/opnsense/...` tree for `saltext.*` import compatibility).

- Salt file root is gitfs root.
- Salt's fileserver serves `_modules/` etc.
- `salt salt-master saltutil.sync_all` → `salt salt-master saltutil.list_extmods` → `salt salt-master opnsense.list_api_modules`
- Execution module `modules/opnsense.py` includes fallback import (`_try_import`) trying `saltext.opnsense.utils.*`, `salt.utils.opnsense`, `opnsense`, so both pip and file-based work.

See master.d alternative `extension_modules: /path/to/saltext-opnsense/src`.

### Method 2: Pip as saltext (production)

```bash
salt-pip install -e /path/to/saltext-opnsense
# or from gitfs cache:
salt-pip install -e /var/cache/salt/master/gitfs/.../extensions/saltext-opnsense

salt salt-master saltutil.sync_all
salt salt-master opnsense.list_api_modules
```

## Proxy minion dance — file-based vs pillar (Q2)

Salt proxy minion `opnsense-router` (id `opnsense-router`) can get credentials two ways:

**A. File-based `/etc/salt/proxy` (flat YAML, no outer `proxy:` wrapper):**

```yaml
# /etc/salt/proxy — lives on salt-master host running salt-proxy, NOT in pillar
proxytype: opnsense
host: opnsense.example.com
proto: https
verify_ssl: false
api_key: REAL_KEY
api_secret: REAL_SECRET
timeout: 30
```

- Salt proxy loader reads this file directly into `opts['proxy']`.
- No pillar round-trip, no Vault slot resolution (plain text). Good for bootstrap/testing.
- `utils/opnsense.py:get_client_from_opts` merges opts `proxy` last, so file wins.

**B. Pillar-based `pillars/hosts/opnsense-router.sls` (nested `proxy:` dict, with Vault `__slot__`):**

```yaml
# pillars/hosts/opnsense-router.sls
proxy:
  proxytype: opnsense
  host: opnsense.example.com
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
  api_secret: __slot__:salt:vault.read(secret/opnsense/api_secret)
```

- Master compiles pillar for minion id `opnsense-router` (via `top.sls` entry `'opnsense-router': - hosts.opnsense-router`), resolves `__slot__` on master, sends encrypted to proxy minion.
- Proxy `init(opts)` gets `opts['proxy']` from pillar transport (or from file if both exist, file wins per merge order: pillar opnsense, pillar proxy, opts opnsense, opts proxy).
- Allows Vault/OpenBao secrets without plaintext file.

**Hybrid (RECOMMENDED after Vault migration):**

After Vault, `/etc/salt/proxy.d/opnsense-router.conf` on salt-master should be MINIMAL:

```yaml
# /etc/salt/proxy.d/opnsense-router.conf — post-vault migration (production)
# Only proxytype here; rest from pillar via Vault slot.
proxytype: opnsense
```

Or file-based legacy `/etc/salt/proxy.d/opnsense-router` dir removed; keep file:

```yaml
# Legacy /etc/salt/proxy.d/opnsense-router.conf containing api_key/api_secret plaintext (600)
# DEPRECATED after vault. Move secrets to OpenBao
# and reduce file to proxytype: opnsense only.
# See master.d/vault.conf for master Vault config.
```

- Minimal file ensures Vault is authoritative (file wins if both present, so keep it minimal).
- `opnsense:` pillar always kept for direct mode `salt salt-master opnsense.call ...` and CMDB (aliases, bind_zone, cluster_parent).

### Vault migration steps (Task 4)

1. **Install saltext-vault on master (salt-master):**
   ```bash
   sudo salt-pip install saltext-vault
   sudo salt salt-master sys.list_modules | tr ',' '\n' | grep vault
   # should show vault.read
   ```

2. **Configure master.d/vault.conf:**
   - `vault:url: http://vault.example.com:8200`  # RFC2606 example, replace with your Vault/OpenBao URL
   - auth method token (file `/etc/salt/vault/token`, 600) or approle
   - cache disk `/var/cache/salt/master/vault/cache`
   - restart salt-master: `sudo systemctl restart salt-master`

3. **Create secret in OpenBao (on vault server):**
   ```bash
   export VAULT_ADDR=http://127.0.0.1:8200
   export VAULT_TOKEN=<root-token>
   # KV v1 example (path matches pillar slot secret/opnsense/api_key):
   bao secrets enable -path=secret kv-v1  # or kv-v2, handle data/ prefix
   bao kv put secret/opnsense/api_key value=<API_KEY from query.sh>
   bao kv put secret/opnsense/api_secret value=<API_SECRET from query.sh>
   # Verify:
   bao kv get secret/opnsense/api_key
   bao kv get secret/opnsense/api_secret
   # Or single path variant:
   # bao kv put secret/opnsense api_key=<key> api_secret=<secret>
   ```

4. **Create policy + token for Salt:**
   ```bash
   cat > salt-reader.hcl <<'EOF'
   path "secret/*" { capabilities = ["read", "list"] }
   path "secret/data/*" { capabilities = ["read", "list"] }  # for KV v2
   EOF
   bao policy write salt-reader salt-reader.hcl
   bao token create -policy=salt-reader -orphan -period=768h
   # Save token to /etc/salt/vault/token on salt-master, chmod 600 root:root
   ```

5. **Test Vault integration:**
   ```bash
   salt salt-master vault.read secret/opnsense/api_key
   salt salt-master pillar.get proxy --out=yaml
   salt opnsense-router pillar.get proxy --out=yaml  # requires top.sls entry for opnsense-router
   # Both should show resolved secrets, not __slot__ placeholder
   ```

6. **Migrate proxy.d file to minimal:**
   ```bash
   sudo cat /etc/salt/proxy.d/opnsense-router.conf  # backup
   echo "proxytype: opnsense" | sudo tee /etc/salt/proxy.d/opnsense-router.conf
   sudo chmod 600 /etc/salt/proxy.d/opnsense-router.conf
   sudo rm -rf /etc/salt/proxy.d/opnsense-router/  # old _schedule.conf dir if unused
   sudo systemctl restart salt-proxy@opnsense-router || sudo pkill -f salt-proxy; salt-proxy --proxyid=opnsense-router -l info -d
   salt opnsense-router test.ping
   salt opnsense-router opnsense.ping
   ```

7. **Cleanup:**
   - Remove hardcoded keys from legacy custom scripts (replace with salt call)
   - Verify no plaintext secrets remain in `/etc/salt/proxy.d/` or pillar files (grep api_key)
   - Rotate OPNsense API key in OPNsense UI after migration, update Vault.

8. **Failure rollback:**
   - If vault.read fails, restore full file from backup and restart proxy.
   - Check master logs `journalctl -u salt-master -f` for vault auth errors.

See:

- `docs/tutorials/pillars/file-based-proxy.yaml` — annotated file-based example + dance explanation
- `docs/tutorials/pillars/top.sls.example` — how to add opnsense-router to pillar top.sls
- `pillar/hosts/opnsense-router.sls` — simplified, comments both options, always keeps `opnsense:` CMDB

Run proxy:

```bash
salt-proxy --proxyid=opnsense-router -l debug --log-file=/var/log/salt/proxy
# systemd unit on salt-master recommended long-term
```

## Direct execution from Salt-Master (no proxy) vs proxy

- **Proxy mode** `salt opnsense-router ...`: goes via `__proxy__` thin wrapper, client lives in proxy process `DETAILS['client']`. Supports grains.
- **Direct mode** `salt salt-master opnsense.call ...`: execution module calls `get_client_from_opts(__opts__, __pillar__)` directly, using pillar `opnsense:`. No proxy minion needed, simpler for one-off queries.
- `get_client_from_opts` merging allows both simultaneously.

```bash
salt salt-master pillar.get opnsense
salt salt-master opnsense.call unbound settings searchHostAlias
salt salt-master opnsense.search unbound settings host_alias search_phrase=www
salt salt-master opnsense.search bind record record row_count=-1

salt opnsense-router test.ping
salt opnsense-router opnsense.ping
salt opnsense-router opnsense.list_api_modules
salt opnsense-router opnsense.list_api_controllers unbound
salt opnsense-router opnsense.list_api_actions unbound settings
```

## State usage — present/absent pattern (Q11 confirmed)

Salt convention is `present`/`absent` (like `host.present`, `user.present`, `firewall.alias`). We follow same with generic `opnsense.item_present` / `item_absent`:

- `item_present`: ensure item exists with given fields, creates via `add_{type}` or updates via `set_{type}` if `match` found but fields differ.
- `item_absent`: ensure item does NOT exist, deletes via `del_{type}` if `match` found.
- Both use `match` dict to locate existing row without knowing UUID (OPNsense API requires UUID for set/del, but search returns `hostname`, `domain`, `ip`, etc). No UUID needed in SLS.
- `reconfigure: <module>/<controller>/<action>` optional triggers configd apply (e.g., `unbound/service/reconfigure`). Explicit rather than auto, allows batching multiple changes then one reconfigure (or omit and rely on separate `reconfigured` state).

Why not specific wrappers like `unbound_host_alias_present`? Genericity keeps one state file vs 400+ hand-coded functions. Ergonomic wrappers can be code-generated later from Model XML + `controllers.json`, but present/absent generic is sufficient day 1 and mirrors `rest_sample` pattern. It also directly replaces legacy manual shell scripts:

```yaml
# Before: query.sh had ALIASES=(git www ...) and PURGE=(old-git ...)
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
ensure_www_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: www
        domain: example.com
    - data:
        enabled: "1"
        host: {{ pillar['opnsense']['cluster_parent']['uuid'] }}
        hostname: www
        domain: example.com
        description: "managed by salt"
    - reconfigure: unbound/service/reconfigure

remove_old:
  opnsense.item_absent:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: old
        domain: example.com
    - reconfigure: unbound/service/reconfigure
```

Behavior details:

- Search all rows `rowCount=-1`, linear match on `match` dict string compare.
- If missing → add.
- If exists, diff flat_data vs existing (handles OPNsense `"1"/"0"` bool style via str compare).
- If diff → set.
- Test mode `test=True` returns `result=None` + changes dict without calling API.

Replaces legacy curl scripts:

```bash
# Before: manual curl script
# Now:
salt opnsense-router state.apply opnsense.aliases
```

Replaces legacy bind zone scripts:
```bash
salt opnsense-router state.apply opnsense.bind_records  # examples/states/bind_records.sls
```

## Grains — why useful?

Grains module `grains/opnsense.py` runs only when proxy minion is up (or via `__proxy__`):

```bash
salt opnsense-router grains.get opnsense_version
salt opnsense-router grains.get opnsense_host
salt opnsense-router grains.get opnsense_api_modules
salt opnsense-router grains.items
```

Implementation:

- `grains()` in `proxy/opnsense.py` returns `opnsense_version` from `core/firmware/status` + `opnsense_host` from client config.
- `grains/opnsense.py` (`opnsense_grains`) calls `opnsense.ping()` then `opnsense.spec()` for module list and firmware version.

Use cases:

- **Targeting**: `salt -G 'opnsense_version:25.*' test.ping` or `G@opnsense_version:25.1` to roll changes only on specific OPNsense releases.
- **Version reporting**: daily `salt opnsense-router grains.get opnsense_version` logged to Loki, alert if drift vs Renovate-tracked core_ref.
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
salt opnsense-router opnsense.search kea dhcpv4 subnet row_count=-1
salt opnsense-router opnsense.search kea dhcpv4 reservation search_phrase=aa:bb:cc row_count=-1
salt opnsense-router opnsense.search kea dhcpv4 reservation row_count=-1

# Get single reservation
salt opnsense-router opnsense.get kea dhcpv4 reservation <uuid>

# Call raw API (download/upload CSV)
salt opnsense-router opnsense.call kea dhcpv4 download_reservations
salt opnsense-router opnsense.call kea dhcpv4 upload_reservations '{"payload":"...csv..."}'
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
        subnet: 192.0.2.0/24
    - data:
        subnet: 192.0.2.0/24
        description: "mgmt - salt"
    - reconfigure: kea/service/reconfigure

www_reservation:
  opnsense.item_present:
    - name: www-192.0.2.30
    - module: kea
    - controller: dhcpv4
    - type: reservation
    - match:
        hw_address: "02:42:ac:11:00:02"
        ip_address: "192.0.2.30"
    - data:
        subnet: "SUBNET_UUID_FROM_searchSubnet"
        ip_address: "192.0.2.30"
        hw_address: "02:42:ac:11:00:02"
        hostname: "www"
        description: "www svc - salt managed"
    - reconfigure: kea/service/reconfigure

# Pillar-driven loop (see kea_reservations.sls full file for Jinja)
# pillar:
#   opnsense:
#     kea:
#       reservations:
#         - {hostname: www, ip_address: 192.0.2.30, hw_address: "02:42:ac:11:00:02", subnet_uuid: "<uuid>", description: "svc"}
```

Notes:
- Reservation uniqueness enforced by OPNsense: subnet+hw_address and subnet+client_id unique. ip_address also unique globally for subnet.
- Model fields accept optional option_data (domain_name_servers, routers, etc).
- After changes, reconfigure kea/service/reconfigure (also restarts Kea).
- VLAN 50 (Wireless IoT) static reservations can be managed this way even though VLAN 60+ uses K3s static IPs.

DHCPv6 reservations identical but using dhcpv6 controller:
```bash
salt opnsense-router opnsense.search kea dhcpv6 reservation row_count=-1
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
salt opnsense-router opnsense.list_api_actions bind domain
salt opnsense-router opnsense.list_api_actions bind record
salt opnsense-router opnsense.list_api_actions unbound settings
salt opnsense-router opnsense.list_api_actions unbound service
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
salt opnsense-router opnsense.list_api_controllers acmeclient
salt opnsense-router opnsense.search acmeclient accounts account row_count=-1
salt opnsense-router opnsense.search acmeclient validations validation row_count=-1
salt opnsense-router opnsense.search acmeclient certificates certificate row_count=-1
salt opnsense-router opnsense.call acmeclient service status
salt opnsense-router opnsense.call acmeclient certificates sign <uuid>
```

State example `examples/states/acme_certificates.sls` shows pillar-driven loop for accounts/validations/actions/certificates with UUID resolution workflow:

1. Create accounts/validations/actions via states
2. Lookup UUIDs: `salt opnsense-router opnsense.search acmeclient accounts account search_phrase=<name>`
3. Store UUIDs in pillar or orchestrate via Jinja.

## Friendly CLI listers (human-friendly convenience) — simplified mappings not raw rows

Raw `opnsense.search` returns `{"rows": [...]}` with raw API fields. Friendly delight modules return sorted dicts keyed by human name:

```bash
# Unbound DNS aliases — friendly
salt opnsense-router opnsense_unbound.list_aliases
# returns {"www.example.com": {"parent": "cluster.example.com", "parent_uuid": "...", "uuid": "...", "enabled": true}}
salt opnsense-router opnsense_unbound.list_aliases_simple
# returns {"www.example.com": "cluster.example.com"}
salt opnsense-router opnsense_unbound.list_aliases_pretty
# returns ["www.example.com -> cluster.example.com (enabled)", ...]

salt opnsense-router opnsense_unbound.list_host_overrides
# returns {"cluster.example.com": {"ip": "192.0.2.10", "uuid": "...", "enabled": true}}
salt opnsense-router opnsense_unbound.list_host_overrides_simple
# returns {"cluster.example.com": "192.0.2.10"}
salt opnsense-router opnsense_unbound.resolve_parent cluster.example.com
# returns UUID

# Bind DNS
salt opnsense-router opnsense_bind.list_domains
# {"example.com": {"uuid": "...", "type": "primary_domain", "enabled": true}}
salt opnsense-router opnsense_bind.list_records domain=example.com
# {"www.example.com": {"name": "www", "type": "A", "value": "192.0.2.30", "uuid": "..."}}
salt opnsense-router opnsense_bind.list_records_pretty domain=example.com
# ["www A 192.0.2.30", "harbor A 192.0.2.40", ...]

# Kea DHCP
salt opnsense-router opnsense_kea.list_subnets
# {"192.0.2.0/24": {"uuid": "...", "description": "mgmt"}}
salt opnsense-router opnsense_kea.list_reservations
# {"www": {"ip_address": "192.0.2.30", "hw_address": "aa:bb:...", "subnet_cidr": "192.0.2.0/24"}}
salt opnsense-router opnsense_kea.list_reservations_pretty

# ACME client
salt opnsense-router opnsense_acmeclient.list_accounts
# {"letsencrypt-prod": {"uuid": "...", "email": "...", "ca": "letsencrypt"}}
salt opnsense-router opnsense_acmeclient.list_certificates
# {"*.example.com": {"uuid": "...", "status": "valid", "account": "..."}}

# Firewall
salt opnsense-router opnsense_firewall.list_aliases
# {"RFC1918": {"type": "network", "content": "10.0.0.0/8,...", "uuid": "..."}}
salt opnsense-router opnsense_firewall.list_aliases_pretty

# DNS managed preview (pillar-driven)
salt opnsense-router opnsense_dns.list_aliases
salt opnsense-router opnsense_dns.managed_preview
# {"parent": "cluster.example.com", "desired": ["www.example.com", ...], "purge": [], "live_count": 50, "live": {...}}
```

All listers call `search ... rowCount=-1` internally, build human maps sorted, and never expose raw rows. Pretty variants return list of `"name type value"` strings for CLI.

For relation fields, they resolve UUIDs automatically:

- Unbound alias host resolution uses `hosts.host` ModelRelationField with display `hostname,domain` — human FQDN `cluster.example.com` resolves to UUID via searchHostOverride.
- Kea reservation subnet uses `subnets.subnet4` with display `subnet` — CIDR `192.0.2.0/24` resolves to UUID via searchSubnet.
- Bind record domain uses `domains.domain` with display `domainname` — `example.com` resolves to zone UUID via searchPrimaryDomain.
- ACME certificate account/validationMethod/restartActions use `accounts.account`, `validations.validation`, `actions.action` with display `name` — name resolves to UUID.

Generic resolver lives in `states/opnsense.py`: `get_relation_fields(module, model, array)` from `utils/models.py` finds fields where `type` contains `ModelRelationField`, extracts relation_targets (`source`, `items`, `display`), and attempts search across candidate controllers/types derived from `controllers.json` to match human value by display fields. This replaces the old hardcoded `_RESOLVE_MAP`.

## Free modules — all 76 available via codegen even if unused

Code generation is free, so we ship wrappers for every OPNsense API module discovered in spec:

- `src/saltext/opnsense/modules/opnsense_*.py`: 76 files
- `src/saltext/opnsense/states/opnsense_*.py`: 76 files
- `modules/opnsense.py` dynamic injection: 1816 functions (`caddy_reverseproxy_search_access_list`, `haproxy_settings_search_backends`, `nginx_settings_search_upstream`, etc)
- `list_api_modules` returns 76, verified by `tools/verify_import.py` + `tests/unit/test_free_modules_import.py`

Used today: unbound, bind, kea, acmeclient, firewall, interfaces.

Free proof (not used but importable): caddy, haproxy, nginx, wireguard, openvpn, ipsec, crowdsec, postfix, redis, tor, etc.

See `examples/states/free_modules_demo.sls` — demonstrates:

- Generic `opnsense.item_present` for caddy reverseproxy handle, haproxy backend, nginx upstream
- Static wrappers `opnsense_caddy.reverse_proxy_present`, `opnsense_haproxy.backend_present`, `opnsense_nginx.upstream_present`
- Verification commands: `salt opnsense-router opnsense.list_api_modules | grep -E "caddy|haproxy|nginx"` and `PYTHONPATH=src python3 tools/verify_import.py`

Sync: `tools/sync_extmods.py --copy` copies all 76 wrappers to extmods `_modules/` and `_states/` plus namespace tree `_utils/saltext/opnsense/...` so gitfs serves them. `sync_extmods.py --check` CI ensures in-sync.

## Codegen refresh on OPNsense release

```bash
python tools/generate_spec.py --core-ref 25.7 --plugins-ref 25.7 --output src/saltext/opnsense/utils/controllers.json
python3 tools/generate_wrappers.py  # regenerates 76+76 wrappers for free
python3 tools/verify_import.py      # proves import works for all 76
python3 tools/sync_extmods.py --copy  # sync to extmods for file-based install
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

# integration (live against opnsense-router) — gated by env var
OPNSENSE_LIVE_TEST=1 pytest tests/integration/test_live_opnsense.py -v
# See tests/integration/README.md for setup
```

- Unit: mock `requests.Session`, `__proxy__`, `__salt__` — no live OPNsense needed
- Functional: `loaders.modules.opnsense` fixture via pytest-salt-factories
- Integration: `test_live_opnsense.py` skipped unless `OPNSENSE_LIVE_TEST=1`, documents how to run against real opnsense-router (see tests/integration/README.md)

## Migrating hardcoded keys

1. Move keys from legacy script files into `pillar/secrets` or OpenBao `secret/opnsense/*`
2. Update legacy automation to use `salt opnsense-router opnsense.search` via `salt --out=json` instead of curl, or deprecate entirely
3. Ensure `purge` lists stay identical to avoid DNS churn
4. Remove hardcoded keys after migration verified via `salt opnsense-router state.apply opnsense.aliases --test`

## As Maintainer

You picked up yet another project — see `docs/MAINTENANCE.md` for the 5-step OPNsense release sprint:

1. Renovate PR bumps `core_ref`/`plugins_ref` in `controllers.json`
2. `make gen-all` (spec → wrappers → verify → sync)
3. Verify: `tools/verify_import.py` + `pytest tests/unit`
4. Live test read-only: `tools/test_live.py` against opnsense-router
5. Commit, merge, `fileserver.update` on salt-master

Troubleshooting (Invalid JSON → POST, 404 → fallback, RemoteDisconnected → retry, grains `__virtual__ None` → fixed) also in `MAINTENANCE.md`. For contributing, see `CONTRIBUTING.md` (venv, towncrier, PR).

## Pillar examples reference

- `docs/tutorials/pillars/opnsense-router.sls` — legacy vault slot example for proxy + opnsense
- `docs/tutorials/pillars/opnsense.sls` — full CMDB example with cluster_parent, aliases, host_overrides_direct, bind_zone records
- `docs/tutorials/pillars/file-based-proxy.yaml` — file-based `/etc/salt/proxy` flat format + dance explanation
- `docs/tutorials/pillars/top.sls.example` — how to add opnsense-router to `pillar/top.sls`
- `pillar/hosts/opnsense-router.sls` — simplified production pillar, file-based primary + vault commented, CMDB always present
