# Installation (Salt 3008+ only)

Requires salt>=3008. No proxy minion, no pre-3008.

## Option A: Pip (production, canonical public path)

```bash
salt-pip install saltext-opnsense
# or editable dev:
salt-pip install -e /path/to/saltext-opnsense

salt '*' saltutil.sync_all
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules
```

Works with onedir /opt/saltstack/salt. Entry-point `saltext.opnsense` auto-discovers. Failure mode via `__virtual__` hides functions cleanly; `doctor/ping` returns dict OK/ERROR. Use `salt -C 'T@opnsense:fw-01' opnsense.ping` to verify.

## Option B: File-based via gitfs (no pip, fallback)

```bash
python3 tools/sync_extmods.py --copy
salt '*' saltutil.sync_all
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules
```

## Verify

```bash
PYTHONPATH=src python3 tools/verify_import.py
salt -C 'T@opnsense:fw-01' opnsense.doctor
salt-run resource.list_grains
```

If missing config host: check `resources:opnsense:hosts:fw-01:host` exists (Resources fleet) or `opnsense:host` direct. See `docs/RESOURCES.md`.

## Upgrade

OPNsense ships ~2 releases/year. To bump:

```bash
make bump CORE=26.1
# regenerates controllers.json + models.json + verifies import
# then:
make test
git commit -m "bump 26.1" src/saltext/opnsense/utils/controllers.json
```

See docs/MAINTENANCE.md.
