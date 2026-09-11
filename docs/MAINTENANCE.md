# Maintenance — sprinting OPNsense releases (3008+ Resources)

Requires salt>=3008. No proxy.

OPNsense ships ~2/year (25.1, 25.7). MUST stay in sync with zero hand-coded functions.

## Design recap

- generate_spec.py clones opnsense/core + plugins regex public function Action → controllers.json 75 modules 25.7.11
- modules/opnsense.py loads controllers.json and injects 1736 funcs via __getattr__/__dir__ + context + Lock
- generate_wrappers.py emits convenience wrappers optional dynamic covers all
- resources/opnsense/__init__.py Resources one managing minion dozens FWs no proxy daemon

## Sprint checklist

### 1. Renovate PR bumps core_ref/plugins_ref

Renovate tracks src/.../controllers.json meta core_ref. When tag updates PR updates JSON.

Manual: python tools/generate_spec.py --core-ref {{newVersion}} --plugins-ref {{newVersion}} --output src/.../controllers.json

### 2. Run make gen-all

```bash
make gen-all
```

Does gen-spec, gen-wrappers, verify exec OK + state OK + dynamic 1736 + list_api_modules 75

### 3. Verify

```bash
PYTHONPATH=src python3 tools/verify_import.py -v
PYTHONPATH=src pytest tests/unit -v
ruff check src tests tools
```

If missing modules stale /tmp/opnsense-spec remove and retry.

### 4. Test live (read-only)

```bash
export OPNSENSE_HOST=fw-01.example.com
export OPNSENSE_API_KEY=...
export OPNSENSE_API_SECRET=...
python tools/test_live.py
salt -C 'T@opnsense:fw-01' opnsense.ping
salt -C 'T@opnsense' opnsense.doctor
```

Do NOT run add/set/del unless dedicated lab.

### 5. Commit, push, PR

```bash
git add src/ tools/
git commit -m "feat: bump core/plugins to 25.7 regenerate 75 modules"
git push
```

After merge on managing minion salt-call --local saltutil.sync_all and opnsense.doctor

## Troubleshooting

Invalid JSON → need POST default.

404 Endpoint not found → fallback candidates _resolve_via_spec + _call_with_fallback authoritative suppresses probing unless enable_fallback.

RemoteDisconnected → retry _RETRYABLE exponential backoff.

missing config host → check resources:opnsense:hosts:fw-01:host use pillar.get unmask True no flat file removed 1.0.0.

import fails → salt-pip install -e . + saltutil.sync_all file-based sync_extmods.py copy.

list_api_modules <75 → regen generate_spec.

Validation error → OPNsenseValidationError .validations.
