# Convenience / high-level wrappers

The generic `opnsense.item_present` works for all 76 modules but requires 6 fields:
`module`, `controller`, `type`, `match`, `data`, `reconfigure`. The convenience layer hides that.

## Why convenience layer?

OPNsense API uses UUIDs for relations (e.g. host_alias `host` field is UUID of host_override), while humans think in FQDNs. Convenience wrappers auto-resolve human FQDN → UUID via search and auto-infer reconfigure path.

### Before – generic

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

Problems: UUID hunting, 6 args, Jinja loops, reconfigure tribal knowledge.

### After – convenience single

```yaml
www:
  opnsense_unbound.alias_present:
    - parent: cluster.example.com
    - domain: example.com
```

Parent `cluster.example.com` auto-resolved to UUID. `reconfigure` auto-inferred to `unbound/service/reconfigure`.

### After – convenience batch (replaces Jinja loops)

```yaml
dns_batch:
  opnsense_unbound.aliases_managed:
    - parent: cluster.example.com
    - aliases:
        example.com: [www, git, auth]
        internal.example.com: [code, ide]
    - purge:
        example.com: [old-git]
```

One state, one reconfigure at end. Reads pillar if args omitted:

```yaml
# salt/opnsense/convenience_aliases.sls – no Jinja
dns:
  opnsense_dns.managed:
    - parent: cluster.example.com
# or fully pillar-driven:
# dns:
#   opnsense_dns.managed: []
# pillar:
#   opnsense:
#     cluster_parent: {hostname: cluster, domain: example.com}
#     aliases: {example.com: [www, git]}
#     purge_aliases: {example.com: [old-git]}
```

## What it provides

- `opnsense_unbound.alias_present(name, parent, domain, description, enabled, reconfigure)` – human parent FQDN
- `opnsense_unbound.alias_absent(name, domain, reconfigure)`
- `opnsense_unbound.aliases_managed(name, parent, aliases={domain:[...]}, purge={domain:[...]})` – batch
- `opnsense_bind.domain_present(name, domain_type, description, enabled, reconfigure)`
- `opnsense_bind.record_present(name, domain, type, value, ttl, enabled, reconfigure)` – human domain auto-resolved
- `opnsense_dns.managed(name, parent=None, aliases=None, purge=None)` – pillar-aware, reads `opnsense:aliases`

Execution helpers:
- `opnsense_unbound.list_aliases()` → `{fqdn: {parent, uuid, enabled}}`
- `opnsense_unbound.list_aliases_simple()` → `{fqdn: parent}`
- `opnsense_unbound.resolve_parent(fqdn)` → UUID
- `opnsense_bind.list_domains()`, `list_records(domain=...)`
- `opnsense_dns.managed_preview()` – shows desired vs live without changes

## Idempotency – diff engine

OPNsense API returns bools as `"1"/"0"`, lists as CSV `"lan,wan"`, relations as UUID or dict, FQDN with trailing dot `example.com.`. Generic `str() == str()` diff flapped every run.

`utils/diff.py` centralizes normalization:
- Bools: `"1", true, yes, enabled` → True
- Relations: UUID ↔ human FQDN equivalence when `parent_human` given, plus dict `{hostname,domain}` reduction
- Lists/CSV: `["lan","wan"]` ↔ `"lan,wan"` → sorted tuple, order-agnostic
- Numbers: `"80"` ↔ `80` → int
- FQDN trailing dot stripped
- Ignores `uuid` key

States use `diff_models(existing, desired, parent_human=...)` instead of manual loops. Includes auto-resolve of `match` dict and full `get` after search to obtain canonical server representation.

## When to use generic vs convenience

- **Generic `opnsense.item_present`** – any of 76 modules, explicit control, explicit reconfigure path, works for all module/controller/type combos.
- **Convenience (`opnsense_unbound.*`, `opnsense_bind.*`, `opnsense_dns.managed`)** – only for DNS/BIND/KEA/ACME where human refs matter; better UX, fewer mistakes. Uses `watch_in` pattern or `reconfigure: true` for reload.

Both support `test=True` (would_add/update/delete) and salt `changes` dict.

## Deprecated names

`delightful_aliases.sls` → `convenience_aliases.sls` – old file kept as shim including new file, will be removed 0.2.0. `state.apply opnsense.aliases_delightful` still works via shim.

## See also

- `docs/USAGE.md` – usage examples
- `docs/ARCHITECTURE.md` – three layers + diff engine
- `docs/tutorials/states/convenience_aliases.sls` – canonical SLS
