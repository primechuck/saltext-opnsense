# QUICKSTART — 15 min novice path

This guide gets a novice from zero to first successful state without Vault, without Jinja, without tribal knowledge.

## Prerequisites

- Salt Master running (3006+)
- OPNsense box with API key/secret: System → Access → Users → API key (create in OPNsense UI)
- `python3` on master

## 1. Install

File-based (no pip, recommended for novices, uses gitfs):

```bash
# Example if extension is in your Salt file roots via gitfs, otherwise copy:
python3 tools/sync_extmods.py --copy  # copies to _modules/_states/_proxy for file-based
salt '*' saltutil.sync_all
salt opnsense-router saltutil.sync_all  # if proxy minion id is opnsense-router
```

Pip (production):

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```

Verify:

```bash
salt opnsense-router opnsense.list_api_modules | head
# 75 modules
```

## 2. Minimal config — flat file (simplest)

On Salt Master, create `/etc/salt/proxy`:

```yaml
proxytype: opnsense
host: opnsense.example.com   # your OPNsense hostname/IP
proto: https
verify_ssl: true
api_key: YOUR_KEY
api_secret: YOUR_SECRET
timeout: 30
```

Use TEST-NET RFC5737 for examples: `192.0.2.10`, `198.51.100.10` – never your real lab IP in docs.

Start proxy:

```bash
salt-proxy --proxyid=opnsense-router -l info -d
sleep 2
salt opnsense-router test.ping
salt opnsense-router opnsense.ping
salt opnsense-router opnsense.doctor
```

`doctor` should return `status: OK` with `spec_version: 25.7.11`.

If error `missing OPNsense config host`: check file exists, mode 600, YAML flat (no outer `proxy:` wrapper). See `docs/tutorials/pillars/file-based-proxy.yaml`.

## 3. Pillar minimal (for DNS aliases)

`/srv/pillar/opnsense.sls`:

```yaml
proxy:
  proxytype: opnsense
  host: opnsense.example.com
  api_key: YOUR_KEY
  api_secret: YOUR_SECRET

opnsense:
  cluster_parent:
    hostname: cluster
    domain: example.com
  aliases:
    example.com:
      - www
      - git
  purge_aliases:
    example.com:
      - old-www
```

`/srv/pillar/top.sls`:

```yaml
base:
  'opnsense-router':
    - opnsense
```

Run:

```bash
salt opnsense-router saltutil.refresh_pillar
salt opnsense-router pillar.get opnsense:aliases
```

## 4. First state — zero Jinja

`srv/salt/opnsense/quickstart.sls`:

```yaml
dns:
  opnsense_dns.managed:
    - name: dns
    - parent: cluster.example.com
    # aliases reads from pillar automatically
```

Dry-run:

```bash
salt opnsense-router state.apply opnsense.quickstart test=True --out=table
```

If `parent host_override cluster.example.com not found`: create parent first in OPNsense UI → Services → Unbound → Host Overrides → `cluster.example.com -> 192.0.2.10`.

Apply:

```bash
salt opnsense-router state.apply opnsense.quickstart
salt opnsense-router opnsense_dns.list_aliases_pretty --out=table
```

Second run should be 0 changes (idempotent).

## 5. Next steps

- For pro features, batch management, diff engine, see `docs/CONVENIENCE.md`
- For all 75 modules, see `docs/USAGE.md`
- For Vault/OpenBao secrets, see `docs/tutorials/pillars/` and move to `vault.example.com` – not needed for quickstart
- For firewall safety (no auto-rollback since 25.7), see `docs/FIREWALL_SAFETY.md`

## Troubleshooting quick

- `opnsense.utils missing`: run `PYTHONPATH=src python3 tools/verify_import.py`
- `Proxy config missing`: ensure `/etc/salt/proxy` flat YAML, not nested `proxy:` 
- `parent resolve failed`: use `opnsense_unbound.resolve_parent cluster.example.com` to debug
- `Invalid JSON`: OPNsense API needs POST – client does this by default; check `verify_ssl: false` for self-signed
- Pillar not seen: `salt opnsense-router pillar.get proxy` must show resolved dict, not `__slot__` placeholder

All example IPs in docs use RFC5737 TEST-NET: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`. Replace with your real networks.
