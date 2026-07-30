# States Reference

## Generic (works for all 75 modules)

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

- `match` dict locates row without UUID (API needs UUID for set/del)
- `search rowCount=-1` + `get uuid` for canonical representation
- `diff_models` normalizes bool `"1"/"0"`, CSV vs list, UUID vs FQDN, trailing dot
- `test=True` returns `result=None` + changes

## Convenience — Unbound DNS

Human parent FQDN, not UUID, auto-resolved:

```yaml
www:
  opnsense_unbound.alias_present:
    - parent: cluster.example.com
    - domain: example.com

dns_batch:
  opnsense_unbound.aliases_managed:
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

## Convenience — BIND

```yaml
example.com:
  opnsense_bind.domain_present:
    - name: example.com

www:
  opnsense_bind.record_present:
    - name: www
    - domain: example.com
    - type: A
    - value: 192.0.2.10
```

Human domain auto-resolved to UUID.

## Convenience — Kea (human CIDR)

```yaml
mgmt_subnet:
  opnsense.item_present:
    - module: kea
    - controller: dhcpv4
    - type: subnet
    - match: {subnet: 192.0.2.0/24}
    - data: {subnet: 192.0.2.0/24, description: "mgmt"}
```

Reservation `subnet: 192.0.2.0/24` auto-resolves to UUID.

## Batch vs Single

- Single `alias_present` → `add` + `reconfigure` per item (N reloads)
- Batch `aliases_managed` / `dns.managed` → one search, in-memory diff, one reconfigure (1 reload). Use for 10+ aliases.
- Firewall filter: use `onchanges` + single `firewall/filter_base/apply` to avoid lockout, see `FIREWALL_SAFETY.md`

## Idempotency

- Second run 0 changes if `diff_models` finds normalized equality
- `managed_preview` execution module shows desired vs live without changes:
  `salt opnsense-router opnsense_dns.managed_preview`
- `list_aliases_pretty --out=table` human readable

## Auto-resolve

Uses `models.json` relation_targets: e.g., `host` → `OPNsense.unbound.host` display `hostname,domain`. Searches candidate controllers from `controllers.json` to match human value.

See `CONVENIENCE.md` for full list.
