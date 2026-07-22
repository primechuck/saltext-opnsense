# Open Questions for saltext-opnsense

This scaffold is intentional — templated to cover ALL API endpoints. Before hardening to production, decisions needed:

## 1. Proxy vs Direct Execution Primary?

- Current scripts run from LAN laptop (`personal/scripts/query.sh`) hitting `jrbob.bierce.org` directly.
- Salt can either:
  - A) Run execution module on `sparky` (master) with pillar `opnsense:host/key/secret` — simplest, no proxy minion.
  - B) Run proxy minion `jrbob` (`salt-proxy --proxyid=jrbob`) — gives `salt jrbob state.apply` parity and grains.
  - C) Both (proxy thin wrapper, direct fallback).

**Preference?** I implemented C (both) — proxy if `__opts__['proxytype']==opnsense`, else direct from master opts/pillar.

Should jrbob become a real proxy minion in `pillars/top.sls`? Where should `hosts/jrbob.sls` live?

## 2. Secrets Backend

- Pillar plain `opnsense:api_key/secret` now.
- Options: SOPS (age), OpenBao (via saltext-vault), or file `/etc/salt/opnsense`?
- Current hardcoded keys in `personal/scripts/*.sh` must be purged after migration.

**Decision needed:** plain pillar for now + SOPS later? Or integrate with openbao state already present?

## 3. Scope: Core Only or All Plugins?

- Core: 26 modules (firewall, unbound, interfaces, kea, wireguard, etc)
- Plugins: 80+ (bind, caddy, haproxy, acmeclient, etc)
- jrbob runs `bind` plugin (for `bierce.org` zone) + `unbound` core.

**Preference:** scaffold supports all via `controllers.json`, but should initial implementation focus on `unbound` + `bind` to replace scripts, then add firewall/interfaces? Or attempt full coverage day1 via codegen?

## 4. Reconfigure Handling

OPNsense pattern is: `add/set/del` → then `reconfigure` to apply via configd.

State option `reconfigure: unbound/service/reconfigure` does explicit second call. Alternative: auto-reconfigure after every mutation (easier but may cause many reloads in batch).

**Preference?** Explicit is implemented; allows batching. Should we add `auto_reconfigure: true` pillar default?

## 5. State Ergonomics

Generic state `opnsense.item_present` works for all endpoints but is verbose:

```yaml
grafana:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: grafana, domain: bierce.org}
    - data: {...}
```

Alternative: generate specific wrappers like `unbound_host_alias_present` via codegen for nicer docs.

**Preference:** keep generic + generate ergonomic wrappers later? Or generate now?

## 6. BIND Zone Sync

`sync-bind-zone.sh` parses Cloudflare BIND export `personal/bierce.org.txt` and upserts A/CNAME/MX/TXT ignoring SOA/NS.

Should Salt state:
- A) Keep same source file and sync via `opnsense_zone` state reading zone file?
- B) Move source of truth to pillar `bind_records:` CMDB (per `cmdb-thought.md`)?
- C) Both — zone file stays fallback, pillar preferred?

## 7. API Spec Generation Process

`tools/generate_spec.py` clones upstream core/plugins and parses PHP controllers via regex.

- Should Renovate track `opnsense/core` and `opnsense/plugins` tags and auto-regenerate `controllers.json` via post-upgrade hook (similar to `vendor_charts.py`)?
- Where to store controllers.json? In extension repo or mirrored to Forgejo `mirrors/opnsense-core.git`?

## 8. Testing Strategy

Salt way: unit (mocked), functional (loader fixtures), integration (live or mock server).

- Do we have a test OPNsense instance or mock server (e.g., `httpbin` style)?
- Should we add `docker-compose` with OPNsense API mock (WireMock recording from live jrbob search responses) for CI?

## 9. Publishing as Own Repo

`projects/` expects submodules from Forgejo `empire/<repo>.git`.

Should:
- Create Forgejo repo `empire/saltext-opnsense` now?
- Start as directory in this monorepo branch `feat/saltext-opnsense`, then `git filter-branch` to extract later?
- License MIT + Python 3.10+, Salt >=3008?

## 10. Salt Integration Details

- Where should master.d config ensure `saltext.opnsense` loader present? Add to `master.d/main.conf`?
- Should we add Salt state `states/opnsense/init.sls` that installs extension via `salt-pip`?
- Node topology: jrbob is NOT Salt-managed per AGENTS.md (deferred). Enabling proxy minion would make it managed — is that intended now or later?

## 11. Existing Scripts Migration

`query.sh` has multi-domain ALIASES/PURGE lists; `sync-bind-zone.sh` has RECORD_TYPES filter.

Should new states:
- replicate exact behavior (skip exact match, update single-valued A/CNAME in place)?
- Or simplify to pure present/absent?

## 12. Additional Requirements

- Do you want grains for OPNsense version/plugin list?
- Do you want execution module helpers like `opnsense_unbound.list_aliases` convenience wrappers?
- Any interest in supporting Kea DHCPv4 reservations via Salt soon? (current k8s uses static IPs but IoT VLAN 50 maybe).

Please answer in priority order — unblocks implementation.
