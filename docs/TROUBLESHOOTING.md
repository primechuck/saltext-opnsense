# Troubleshooting

Requires `salt>=3008`, Resources-only, no proxy. Proxy removed 1.0.0.

## Install

**`opnsense utils missing` in __virtual__**
```bash
PYTHONPATH=src python3 tools/verify_import.py
# should show 76 modules
salt -C 'T@opnsense' saltutil.sync_all
```

**`missing OPNsense config host` / `SaltInvocationError`**
- Pillar path is `resources:opnsense:hosts:fw-01:{host, api_key, api_secret}`, not flat `/etc/salt/proxy` (removed 1.0.0). See `docs/RESOURCES.md`.
- Check `salt -C 'T@opnsense:fw-01' pillar.get resources:opnsense:hosts:fw-01 --out=yaml`
- For masterless `salt-call --local pillar.get resources:opnsense --out=yaml`

## API

**`Invalid JSON syntax`**
OPNsense expects POST with JSON body even for search. Client defaults to POST. If you call `opnsense.call` directly, pass `{}` not empty.

**`404 Endpoint not found` → fallback**
Renamed in 24.x→25.x `searchAlias` → `searchItem`. Client tries candidates via `_resolve_via_spec` + `_call_with_fallback`. Regen spec:
```bash
make bump CORE=26.7.3
```

**`RemoteDisconnected` / `Connection aborted`**
Kea restart slow. Retry 3x with backoff in `utils/opnsense.py`. Batch changes then single reconfigure to reduce churn.

**`result: failed` + `validations`**
Validation error duplicate hostname. `OPNsenseClient` raises `OPNsenseValidationError` with `.validations` dict. Shown in state comment.

## Idempotency flapping

- First run creates, second run should 0 changes. If second run still shows changes:
  - Check bool `"1"` vs `True` — fixed by `diff.py`
  - CSV `"lan,wan"` vs `["wan","lan"]` — fixed by sorted tuple
  - UUID vs FQDN — auto-resolve via `models.json` + `controllers.json`
  - Trailing dot `example.com.` — stripped
  - Description default `managed by salt - fqdn` — pin description in pillar to avoid churn

Mock helper: `PYTHONPATH=src python3 tools/test_state.py --mock` proves second run 0 changes even when API returns `"1"` bool and human grid.

## Grains

**`grains empty / opnsense_version missing`**
Grains now come from Resource connection module `resources/opnsense/__init__.py:grains()`, not legacy `grains/opnsense.py` (removed 1.0.0).

```bash
salt -C 'T@opnsense' grains.get opnsense_version
salt -C 'T@opnsense' grains.get opnsense_host
salt -C 'T@opnsense' grains.items
salt-run resource.list_grains
```

Ensure `resources:opnsense:hosts:fw-01` exists and `ping()` succeeds.

## Firewall

**Filter apply locks you out**
No savepoint since 25.7 (removed in core PR #10411). Only `filter_base/apply` = `filter reload skip_alias`. See `docs/FIREWALL_SAFETY.md`:
- Keep anti-lockout rule enabled
- Use `onchanges` single apply after all rules
- Out-of-band access IPMI/mgmt VLAN

## Resources connection

**`ping` false / discover 0**
```bash
salt -C 'T@opnsense:fw-01' opnsense.doctor
salt -C 'T@opnsense:fw-01' test.ping
salt-call --local -l debug saltutil.sync_all  # check pillar Resources tree
```

Check API key from OPNsense UI `System > Access > Users > API`.

**Vault `__slot__` shows placeholder not resolved**
```bash
salt jrbob vault.read secret/opnsense/fw-01/api_key
salt -C 'T@opnsense:fw-01' pillar.get resources:opnsense:hosts:fw-01 --out=yaml
```

If still placeholder, check `master.d/vault.conf` url and token file `/etc/salt/vault/token` 600.

## Pillar

**`aliases must be dict domain->list`**
`aliases_managed` expects `{"example.com": [www, git]}` not flat list.

**`parent required`**
Provide `parent: cluster.example.com` or pillar `opnsense:cluster_parent: {hostname: cluster, domain: example.com}`. Ensure parent host_override exists: `salt -C 'T@opnsense' opnsense_unbound.list_host_overrides`.

## Testing

```bash
PYTHONPATH=src pytest tests/unit -v
PYTHONPATH=src python3 tools/verify_import.py
# live read-only:
OPNSENSE_HOST=fw-01.example.com OPNSENSE_API_KEY=xxx OPNSENSE_API_SECRET=yyy python3 tools/test_live.py
```
