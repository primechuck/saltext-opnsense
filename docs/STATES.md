# States Reference

## Generic (works for all 76 modules)

```yaml
rfc1918_alias:
  opnsense.item_present:
    - module: firewall
    - controller: alias
    - type: item
    - match: {name: RFC1918}
    - data: {name: RFC1918, type: network, content: "192.0.2.0/24"}
    - reconfigure: firewall/alias/reconfigure

purge_old:
  opnsense.item_absent:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: old, domain: example.com}
    - reconfigure: unbound/service/reconfigure
```

- `match` locates row without UUID (API needs UUID for set/del)
- `search rowCount=-1` + `get uuid` for canonical representation
- `diff_models` normalizes bool `"1"/"0"`, CSV vs list, UUID vs FQDN, trailing dot
- `test=True` returns `result=None` + changes

Generic CLI:

```bash
salt -C 'T@opnsense:fw-01' opnsense.call unbound settings searchHostAlias
salt -C 'T@opnsense:fw-01' opnsense.search unbound settings host_alias search_phrase=www
salt -C 'T@opnsense:fw-01' opnsense.search bind record record row_count=-1
```

## Convenience — why needed

OPNsense API uses UUIDs for relations (host_alias `host` = UUID of host_override) while humans think in FQDNs. Generic requires 6 fields. Convenience hides that.

Before (generic, clunky):

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

After (human parent auto-resolved to UUID, `reconfigure` auto-inferred):

```yaml
www_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: www, domain: example.com}
    - data:
        enabled: "1"
        host: cluster.example.com
        hostname: www
        domain: example.com
        description: "managed by salt"
```

Parent `cluster.example.com` auto-resolved to UUID. `reconfigure` auto-inferred to `unbound/service/reconfigure`.

## Convenience — Unbound DNS (`opnsense_dns`)

```yaml
dns_batch:
  opnsense_dns.managed:
    - parent: cluster.example.com
    - aliases:
        example.com: [www, git, auth]
        internal.example.com: [code, ide]
    - purge:
        example.com: [old-git]
    # one reconfigure at end

dns:
  opnsense_dns.managed:
    - name: dns
    - parent: cluster.example.com
    # reads pillar opnsense:aliases + purge_aliases if omitted
```

Zero Jinja — pillar-driven:

```yaml
# salt/opnsense/unbound.sls
dns:
  opnsense_dns.managed:
    - parent: cluster.example.com
# or fully pillar:
# dns:
#   opnsense_dns.managed: []
# pillar:
#   opnsense:
#     cluster_parent: {hostname: cluster, domain: example.com}
#     aliases: {example.com: [www, git]}
```

What it provides:

- `opnsense_dns.managed(name, parent=None, aliases=None, purge=None)` — pillar-aware batch Unbound alias management, reads `opnsense:aliases`
- `opnsense.item_present(name, module, controller, type, data, match, reconfigure)` — generic state with automatic human-to-UUID relation resolution (`host`, `domain`, `subnet`, `account`, `validationMethod`, `restartActions`)

Execution helpers:

- `opnsense_dns.list_aliases()` → `{fqdn: {parent, uuid, enabled}}`
- `opnsense_dns.list_aliases_simple()` → `{fqdn: parent}`
- `opnsense_dns.managed_preview()` — desired vs live without changes

## BIND (human domain auto-resolved)

```yaml
example_zone:
  opnsense.item_present:
    - module: bind
    - controller: domain
    - type: primary_domain
    - match: {domainname: example.com}
    - data: {domainname: example.com, enabled: "1"}

www:
  opnsense.item_present:
    - module: bind
    - controller: record
    - type: record
    - match: {domain: example.com, name: www, type: A}
    - data:
        domain: example.com
        name: www
        type: A
        value: 192.0.2.10
        enabled: "1"
```

Human `domain: example.com` auto-resolved to the zone UUID.

## Convenience — Kea (human CIDR)

```yaml
mgmt_subnet:
  opnsense.item_present:
    - module: kea
    - controller: dhcpv4
    - type: subnet
    - match: {subnet: 192.0.2.0/24}
    - data: {subnet: 192.0.2.0/24, description: "mgmt"}

www_reservation:
  opnsense.item_present:
    - module: kea
    - controller: dhcpv4
    - type: reservation
    - match:
        hw_address: "02:42:ac:11:00:02"
        ip_address: "192.0.2.30"
    - data:
        subnet: "192.0.2.0/24"  # human CIDR auto-resolved to UUID
        ip_address: "192.0.2.30"
        hw_address: "02:42:ac:11:00:02"
        hostname: "www"
```

## ACME client

```bash
salt -C 'T@opnsense:fw-01' opnsense.list_api_controllers acmeclient
salt -C 'T@opnsense:fw-01' opnsense.search acmeclient accounts account row_count=-1
```

## Batch vs Single

- Single `alias_present` → `add` + `reconfigure` per item (N reloads)
- Batch `aliases_managed` / `dns.managed` → one search, in-memory diff, one reconfigure (1 reload). Use for 10+ aliases.
- Firewall filter: use `onchanges` + single `filterbase/apply` to avoid lockout, see `FIREWALL_SAFETY.md`

## Idempotency — diff engine

- Second run 0 changes if `diff_models` normalized equality
- `managed_preview` shows desired vs live without changes: `salt -C 'T@opnsense:fw-01' opnsense_dns.managed_preview`
- `list_aliases_pretty --out=table` human readable

OPNsense quirks fixed by `utils/diff.py`:

- Bools `"1"/"0"` vs True/False
- Relations UUID vs FQDN vs dict `{hostname,domain}`
- Lists CSV `"lan,wan"` vs `["wan","lan"]` order-agnostic
- Numbers `"80"` vs 80, FQDN trailing dot stripped, ignores `uuid`

## Auto-resolve

Uses `models.json` relation_targets: e.g. `host` → `OPNsense.unbound.host` display `hostname,domain`. Searches candidate controllers from `controllers.json` to match human value. Replaces old hardcoded map.

See `docs/QUICKSTART.md` for fleet targeting `T@opnsense:fw-01` and `docs/API.md` for live discovery.

## Free modules — all 76

Codegen free: wrappers for every OPNsense API module via dynamic `__getattr__` 1815 funcs. Generic `opnsense.item_present` covers any module. See `examples` and `docs/tutorials`.

Targeting always via `T@opnsense:fw-01` (Resources). Pillar path `resources:opnsense:hosts:fw-01:{host,api_key}` or `pillars/hosts/<minion>.sls` example (replace `<minion>` with your managing minion ID).
