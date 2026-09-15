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

### Method 1: Pip as saltext (production, canonical)

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```

See `docs/INSTALL.md`. Requires `salt>=3008`.

### Method 2: File-based sync via Salt file roots (dev, no pip)

```bash
python3 tools/sync_extmods.py --copy
salt '*' saltutil.sync_all
```

Execution files live in `src/` and are exposed via extmods `_modules/`, `_states/`, `_utils/` including `_utils/saltext/opnsense/...` tree for `saltext.*` import compatibility. Requires `salt>=3008`, Resources-only, no `_proxy/_grains`.

- Salt file root is gitfs root.
- Salt's fileserver serves `_modules/` etc.
- `salt '*' saltutil.sync_all` → `salt '*' saltutil.list_extmods` → `salt -C 'T@opnsense' opnsense.list_api_modules`
- Execution module `modules/opnsense.py` uses `saltext.opnsense.utils.*` imports.

See `extension_modules:` alternative in `docs/INSTALL.md`.

## Resources fleet — pillar `resources:opnsense:hosts:{id}` (Q2 migration from proxy)

Requires `salt>=3008`. Proxy minion removed in 1.0.0 — use Resources. See `docs/RESOURCES.md`.

`/srv/pillar/resources.sls`:

```yaml
resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
        api_key: __slot__:salt:vault.read(secret/opnsense/fw-01/api_key)
        api_secret: __slot__:salt:vault.read(secret/opnsense/fw-01/api_secret)
        verify_ssl: true
        timeout: 30
```

Targeting:

```bash
salt-call --local saltutil.refresh_pillar
salt -C 'T@opnsense' test.ping
salt -C 'T@opnsense' opnsense.list_api_modules
salt -C 'T@opnsense:fw-01' opnsense.doctor
```

Vault via `saltext-vault`:

```yaml
# master.d/vault.conf
vault:
  url: https://vault.example.com:8200
  auth:
    method: token
    token_file: /etc/salt/vault/token
```

```bash
salt jrbob vault.read secret/opnsense/fw-01/api_key
salt -C 'T@opnsense:fw-01' pillar.get resources:opnsense:hosts:fw-01 --out=yaml
```

Optional 2-SRN composition with built-in `ssh` Resource (requires `python311` package on OPNsense `fw-01`):

```yaml
resources:
  ssh:
    hosts:
      fw-01:
        host: fw-01.example.com
        user: root
```

```bash
salt -C 'T@opnsense:fw-01 or T@ssh:fw-01' state.apply fw.base
```

## Execution from managing minion — Resources targeting

Requires `salt>=3008`, `saltext-opnsense` on managing minion, pillar `resources:opnsense:hosts:{id}`.

```bash
salt -C 'T@opnsense' opnsense.call unbound settings searchHostAlias
salt -C 'T@opnsense' opnsense.search unbound settings host_alias search_phrase=www
salt -C 'T@opnsense' opnsense.search bind record record row_count=-1
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules
salt -C 'T@opnsense' opnsense.list_api_controllers unbound
salt -C 'T@opnsense' opnsense.list_api_actions unbound settings
```

## State usage — present/absent pattern

Salt convention is `present`/`absent` (like `host.present`). We follow same with generic `opnsense.item_present` / `item_absent`:

- `item_present`: ensure item exists, creates via `add_{type}` or updates via `set_{type}` if `match` found but diff engine says data differs.
- `item_absent`: ensure missing, deletes via `del_{type}` if `match` found.
- Both use `match` dict to locate existing row without knowing UUID (OPNsense API requires UUID for set/del).
- `reconfigure: <module>/<controller>/<action>` optional, explicit batching.
- Auto-resolve human FQDN/IP/CIDR → UUID via `models.json` `ModelRelationField` relation_targets.
- `test=True` support — `result=None` + changes dict.

Example generic:

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
        host: "{{ salt['pillar.get']('opnsense:cluster_parent') }}"
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

## Grains — Resource grains (3008+)

Resource connection `resources/opnsense/__init__.py` implements `grains` via `resources:opnsense:hosts:{id}` discovery.

```bash
salt -C 'T@opnsense' grains.get opnsense_version
salt -C 'T@opnsense' grains.get opnsense_host
salt -C 'T@opnsense' grains.items
salt-run resource.list_grains
```

Use cases:

- **Targeting**: `salt -C 'G@opnsense_version:26.*' test.ping`
- **Version audit**: daily `grains.get opnsense_version` logged to Loki, alert drift vs Renovate-tracked core_ref.

## Kea DHCPv4 reservations

OPNsense Kea API: https://docs.opnsense.org/development/api/core/kea.html

Reservation fields: subnet (UUID auto-resolved from CIDR), ip_address, hw_address, hostname, description.

Execution:

```bash
salt -C 'T@opnsense' opnsense.search kea dhcpv4 subnet row_count=-1
salt -C 'T@opnsense' opnsense.search kea dhcpv4 reservation search_phrase=aa:bb:cc row_count=-1
salt -C 'T@opnsense' opnsense.get kea dhcpv4 reservation <uuid>
```

State (human CIDR auto-resolved):

```yaml
www_reservation:
  opnsense.item_present:
    - module: kea
    - controller: dhcpv4
    - type: reservation
    - match:
        hw_address: "02:42:ac:11:00:02"
        ip_address: "192.0.2.30"
    - data:
        subnet: "192.0.2.0/24"  # human CIDR, resolved to UUID via models.json
        ip_address: "192.0.2.30"
        hw_address: "02:42:ac:11:00:02"
        hostname: "www"
        description: "www svc - salt managed"
    - reconfigure: kea/service/reconfigure
```

## Bind and Unbound full coverage

- unbound settings: host_override, host_alias, dot, forward, get/set singleton, ACL, DNSBL.
- bind domain: Primary/Secondary/Forward CRUD + master/slave legacy.
- See `docs/API.md` for 76-module / 1815 endpoint matrix.

```bash
salt -C 'T@opnsense' opnsense.list_api_actions bind domain
```

## ACME client

Docs: https://docs.opnsense.org/development/api/plugins/acmeclient.html

```bash
salt -C 'T@opnsense' opnsense.list_api_controllers acmeclient
salt -C 'T@opnsense' opnsense.search acmeclient accounts account row_count=-1
salt -C 'T@opnsense' opnsense.call acmeclient service status
```

## Friendly CLI listers — human maps not raw rows

Raw `opnsense.search` returns `{"rows": [...]}`. Convenience modules return sorted dicts keyed by human name:

```bash
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_aliases
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_aliases_simple
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_host_overrides
salt -C 'T@opnsense:fw-01' opnsense_unbound.resolve_parent cluster.example.com
salt -C 'T@opnsense:fw-01' opnsense_bind.list_domains
salt -C 'T@opnsense:fw-01' opnsense_bind.list_records domain=example.com
salt -C 'T@opnsense:fw-01' opnsense_kea.list_subnets
salt -C 'T@opnsense:fw-01' opnsense_acmeclient.list_certificates
salt -C 'T@opnsense:fw-01' opnsense_firewall.list_aliases
salt -C 'T@opnsense:fw-01' opnsense_dns.managed_preview
```

All listers call `search ... rowCount=-1` internally, auto-resolve relations via `models.json` + `controllers.json` candidates (replaces old hardcoded `_RESOLVE_MAP`).

## Free modules — all 76 available

Codegen is free: wrappers for every OPNsense API module discovered:

- `src/saltext/opnsense/modules/opnsense_*.py`: 76 files
- `src/saltext/opnsense/states/opnsense_*.py`: 76 files
- `modules/opnsense.py` dynamic `__getattr__` injection: 1815 funcs.

See `examples/states/free_modules_demo.sls`.

## Codegen refresh on OPNsense release

```bash
make bump CORE=26.7.3  # spec -> models -> wrappers -> verify
python3 tools/verify_import.py
python3 tools/sync_extmods.py --copy
towncrier create --edit
```

## Testing

```bash
PYTHONPATH=src pytest tests/unit -v
PYTHONPATH=src python3 tools/verify_import.py
OPNSENSE_LIVE_TEST=1 pytest tests/integration/test_live_opnsense.py -v
```

- Unit: mock `requests.Session`, resource `__resource__`/`__resource_funcs__` — no live FW needed.
- Integration: gated live read-only.

## Pillar examples reference

- `docs/PILLAR.md` — canonical `resources:opnsense:hosts:{id}` format, Vault `__slot__`
- `docs/RESOURCES.md` — fleet tutorial 10 min masterless walk-through + 2 SRN composition
- `docs/INSTALL.md` — PyPI canonical + file-based dev
- `pillars/hosts/sparky.sls` analogue: `resources:opnsense:hosts:fw-01` example
