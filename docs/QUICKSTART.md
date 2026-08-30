# QUICKSTART — 15 min novice path (Salt Resources, 3008+)

This guide gets a novice from zero to first successful state without Vault, without Jinja, using Salt Resources (fleet-ready) instead of proxy minion.

> Breaking 1.0.0: Proxy removed. Use Resources T@opnsense. See docs/RESOURCES.md.

## Prerequisites

- Salt Master + managing minion running 3008+
- OPNsense box with API key/secret: System → Access → Users → API key
- `python3` on master/managing minion

## 1. Install

Pip (production, recommended):

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```

File-based (no pip, gitfs):

```bash
# copies to _modules/_states/_utils/saltext/...
python3 tools/sync_extmods.py --copy
salt '*' saltutil.sync_all
```

Verify:

```bash
salt -C 'T@opnsense' --tgt-type compound opnsense.list_api_modules | head
# 75 modules
salt-run resource.list_grains
```

## 2. Minimal config – Resources pillar (simplest fleet)

`/srv/pillar/resources.sls`:

```yaml
resources:
  opnsense:
    hosts:
      fw-01:
        host: opnsense.example.com
        proto: https
        verify_ssl: true
        api_key: YOUR_KEY
        api_secret: YOUR_SECRET
        timeout: 30
```

`/srv/pillar/top.sls`:

```yaml
base:
  '*':
    - resources
  # or specific managing minion:
  'managing-minion-id':
    - resources
```

Refresh:

```bash
salt managing-minion-id saltutil.refresh_pillar
salt managing-minion-id pillar.get resources:opnsense:hosts unmask=True
salt -C 'T@opnsense' test.ping
salt -C 'T@opnsense:fw-01' opnsense.ping
salt -C 'T@opnsense' opnsense.doctor
```

`doctor` should return `status: OK` with `spec_version: 25.7.11`.

If `missing OPNsense config host`: check pillar path is `resources:opnsense:hosts:fw-01:host`, not flat `/etc/salt/proxy` (proxy removed in 1.0.0). See `docs/RESOURCES.md`.

Optional SSH 2 SRN side (requires python311 on OPNsense):

```yaml
resources:
  ssh:
    hosts:
      fw-01:
        host: opnsense.example.com
        user: root
        priv: /etc/salt/keys/fw-01
        thin_dir: /tmp/.salt-thin
```

Then `salt -C 'T@ssh' cmd.run 'opnsense-version'`.

## 3. Pillar for DNS aliases

`/srv/pillar/opnsense.sls`:

```yaml
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

Add to top for managing minion:

```yaml
base:
  'managing-minion-id':
    - resources
    - opnsense
```

Run:

```bash
salt managing-minion-id saltutil.refresh_pillar
salt -C 'T@opnsense:fw-01' pillar.get opnsense:aliases
```

## 4. First state – zero Jinja, merged mode

`srv/salt/opnsense/quickstart.sls`:

```yaml
dns:
  opnsense_dns.managed:
    - name: dns
    - parent: cluster.example.com
```

Dry-run via Resources merged mode:

```bash
salt -C 'T@opnsense:fw-01' state.apply opnsense.quickstart test=True --out=table
```

If `parent host_override cluster.example.com not found`: create parent in OPNsense UI → Services → Unbound → Host Overrides.

Apply:

```bash
salt -C 'T@opnsense:fw-01' state.apply opnsense.quickstart
salt -C 'T@opnsense:fw-01' opnsense_dns.list_aliases_pretty --out=table
```

Second run should be 0 changes (idempotent diff engine).

Masterless test (no master registry):

```bash
salt-call --local -r --tgt 'T@opnsense' --tgt-type compound state.apply opnsense.quickstart test=True
```

## 5. Next steps

- Full fleet tutorial `docs/RESOURCES.md` – 2 SRN composition, targeting `G@`, `resource.refresh`, `list_grains`
- Convenience wrappers `docs/CONVENIENCE.md`
- All 75 modules `docs/USAGE.md`
- Vault secrets `docs/tutorials/pillars/` – use `__slot__:salt:vault.read(...)`
- Firewall safety `docs/FIREWALL_SAFETY.md`

## Troubleshooting

- `Function X not supported for opnsense` → managing minion `saltutil.sync_all` + `refresh_pillar`
- `parent resolve failed` → `salt -C 'T@opnsense:fw-01' opnsense_unbound.resolve_parent cluster.example.com`
- `missing config host` → check `resources:opnsense:hosts:fw-01:host` exists, use `unmask=True`
- Pillar not seen → `salt managing-minion pillar.get resources:opnsense:hosts unmask=True`
- Thin copy fails for ssh → ensure `python311` on OPNsense, `thin_dir` writable, key 600

All example IPs use RFC5737 TEST-NET: `192.0.2.0/24`. Replace with real networks.
