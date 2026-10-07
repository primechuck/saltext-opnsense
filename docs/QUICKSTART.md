# QUICKSTART — 15 min novice path (Salt 3008+ Resources)

Requires salt>=3008. No proxy minion. For full fleet tutorial see `docs/RESOURCES.md`.

> Breaking 1.0.0: Proxy removed. Use Resources T@opnsense. See docs/RESOURCES.md.

## Prerequisites

- Salt Master + managing minion running 3008+
- OPNsense box with API key/secret: System → Access → Users → API key
- `python3` on master/managing minion

## 1. Install (PyPI canonical)

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```


Verify:

```bash
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules | head
# 76 modules, 1815 endpoints
salt -C 'T@opnsense:fw-01' opnsense.list_api_controllers unbound
salt -C 'T@opnsense:fw-01' opnsense.list_api_actions unbound settings
salt -C 'T@opnsense:fw-01' opnsense.doctor
salt-run resource.list_grains
```

Discovery is live — `docs/API.md` is hand-written, not a stale dump. Query target FW version for truth.

## 2. Minimal config – Resources pillar (simplest fleet)

`/srv/pillar/resources.sls`:

```yaml
resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
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
  'managing-minion-id':
    - resources
```

Refresh:

```bash
salt -C 'T@opnsense' saltutil.refresh_pillar
salt -C 'T@opnsense:fw-01' pillar.get resources:opnsense:hosts unmask=True
salt -C 'T@opnsense' test.ping
salt -C 'T@opnsense:fw-01' opnsense.ping
salt -C 'T@opnsense:fw-01' opnsense.doctor
```

`doctor` returns `status: OK` with `spec_version: 26.7.3`.

If `missing OPNsense config host`: check pillar path is `resources:opnsense:hosts:fw-01:host`, not legacy path. See `docs/RESOURCES.md`.

Optional SSH 2 SRN side (requires python311 on OPNsense):

```yaml
resources:
  ssh:
    hosts:
      fw-01:
        host: fw-01.example.com
        user: root
```

Then `salt -C 'T@opnsense:fw-01 or T@ssh:fw-01' state.apply fw.base`.

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
salt -C 'T@opnsense:fw-01' saltutil.refresh_pillar
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
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_aliases
```

Second run 0 changes (idempotent diff engine).

Masterless:

```bash
salt-call --local -r --tgt 'T@opnsense' --tgt-type compound state.apply opnsense.quickstart test=True
```

## 5. Friendly CLI listers (human maps)

Raw `opnsense.search` returns `{"rows": [...]}`. Convenience modules return sorted dicts:

```bash
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_aliases
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_aliases_simple
salt -C 'T@opnsense:fw-01' opnsense_unbound.list_host_overrides
salt -C 'T@opnsense:fw-01' opnsense_bind.list_domains
salt -C 'T@opnsense:fw-01' opnsense_bind.list_records domain=example.com
salt -C 'T@opnsense:fw-01' opnsense_kea.list_subnets
salt -C 'T@opnsense:fw-01' opnsense_dns.managed_preview
```

All listers call `search rowCount=-1`, auto-resolve relations via `models.json` + `controllers.json`.

See `docs/STATES.md` for batch `aliases_managed` and `docs/API.md` for live discovery.

## 6. Troubleshooting

- `Function X not supported for opnsense` → `salt -C 'T@opnsense' saltutil.sync_all` + `refresh_pillar`
- `missing config host` → check `resources:opnsense:hosts:fw-01:host` exists, `unmask=True`, not flat file
- `parent resolve failed` → `salt -C 'T@opnsense:fw-01' opnsense_unbound.resolve_parent cluster.example.com`
- `Invalid JSON syntax` → OPNsense expects POST, client defaults POST, pass `{}` not empty
- `404 Endpoint not found` → renamed action, regen `make bump CORE=26.7.3`
- `RemoteDisconnected` → Kea restart slow, retry 3x backoff, batch + `onchanges`
- `validations` failed → `OPNsenseValidationError.validations` in comment, fix data
- Flap bool `1` vs True / CSV `lan,wan` vs list → fixed by `utils/diff.py` normalization
- Grains empty → `resources/opnsense/__init__.py:grains()` needs `resources:opnsense:hosts:fw-01` + `ping()` ok
- Vault `__slot__` placeholder → `salt -C 'T@opnsense:fw-01' pillar.get ... --out=yaml` + check master vault.conf

All example IPs use RFC5737 TEST-NET: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `fw-01.example.com`. Replace with real networks.
