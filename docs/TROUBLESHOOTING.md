# Troubleshooting

## Install

**`opnsense utils missing` in __virtual__**
```bash
PYTHONPATH=src python3 tools/verify_import.py
# should show 75 modules
salt '*' saltutil.sync_all
```

**`Proxy config missing`**
- File-based `/etc/salt/proxy` must be flat YAML (no outer `proxy:` wrapper):
```yaml
proxytype: opnsense
host: opnsense.example.com
api_key: ...
api_secret: ...
```
- Pillar-based: `proxy:` nested dict in `pillar/hosts/opnsense-router.sls` + `top.sls` entry for id `opnsense-router`
- `get_client_from_opts` merges in order: pillar opnsense, pillar proxy, opts opnsense, opts proxy — last wins. See `QUICKSTART.md`.

## API

**`Invalid JSON syntax`**
OPNsense expects POST with JSON body even for search. Client defaults to POST. If you call `opnsense.call` directly, pass `{}` not empty.

**`404 Endpoint not found` → fallback**
Renamed in 24.x→25.x `searchAlias` → `searchItem`. Client tries candidates via `_resolve_via_spec` + `_call_with_fallback`. Regen spec:
```bash
make bump CORE=25.7.11
```

**`RemoteDisconnected` / `Connection aborted`**
Kea restart slow. Retry 3x with backoff in `utils/opnsense.py`. Batch changes then single reconfigure to reduce churn.

**`result: failed` + `validations`**
Validation error duplicate hostname. `OPNsenseClient` raises `OPNsenseValidationError` with `.validations` dict. Shown in state comment.

## Idempotency flapping

- First run creates, second run should 0 changes. If second run still shows changes:
  - Check bool `"1"` vs `True` — fixed by `diff.py`
  - CSV `"lan,wan"` vs `["wan","lan"]` — fixed by sorted tuple
  - UUID vs FQDN — `parent_human` logic in `diff.py` + `_resolve_parent`
  - Trailing dot `example.com.` — stripped
  - Description default `managed by salt - fqdn` — pin description in pillar to avoid churn

Mock helper: `PYTHONPATH=src python3 tools/test_state.py --mock` proves second run 0 changes even when API returns `"1"` bool and human grid.

## Grains

**`grains __virtual__ None`**
Grains run only on proxy minion. `grains/opnsense.py` returns empty dict if proxy down, not `False`. Check:
```bash
salt opnsense-router grains.get opnsense_version
salt opnsense-router grains.get opnsense_host
```

## Firewall

**Filter apply locks you out**
No savepoint since 25.7 (removed in core PR #10411). Only `filter_base/apply` = `filter reload skip_alias`. See `FIREWALL_SAFETY.md`:
- Keep anti-lockout rule enabled
- Use `onchanges` single apply after all rules
- Out-of-band access IPMI/mgmt VLAN

## Proxy

**`ping` false**
`proxy/opnsense.py:ping()` tries `unbound/settings/host_alias`, `bind/domain/primary_domain`, `firewall/alias/item`, fallback `searchHostAlias`. Check `salt opnsense-router opnsense.doctor`.

**Vault `__slot__` shows placeholder not resolved**
```bash
salt salt-master vault.read secret/opnsense/api_key
salt opnsense-router pillar.get proxy --out=yaml
```
If still placeholder, check `master.d/vault.conf` url `http://vault.example.com:8200` and token file `/etc/salt/vault/token` 600.

## Pillar

**`aliases must be dict domain->list`**
`aliases_managed` expects `{"example.com": [www, git]}` not flat list.

**`parent required`**
Provide `parent: cluster.example.com` or pillar `opnsense:cluster_parent: {hostname: cluster, domain: example.com}`. Ensure parent host_override exists: `salt opnsense-router opnsense_unbound.list_host_overrides`.

## Testing

```bash
PYTHONPATH=src pytest tests/unit -v
PYTHONPATH=src python3 tools/verify_import.py
# live read-only:
OPNSENSE_HOST=opnsense.example.com OPNSENSE_API_KEY=xxx OPNSENSE_API_SECRET=yyy python3 tools/test_live.py
```
