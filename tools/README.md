# OPNsense Extension Tools

This directory contains the code generation scripts required to maintain this Salt extension.
Since the OPNsense API is massive (1,800+ endpoints) and constantly changing, this extension dynamically generates its API bindings and data models directly from the upstream OPNsense source code.

## Generating API Definitions

When a new OPNsense release is available, you should update the API specifications:

```bash
python3 tools/generate_spec.py --core-ref 26.7.3 --plugins-ref 26.7.3 --output src/saltext/opnsense/utils/controllers.json
python3 tools/generate_models.py --core-ref 26.7.3 --plugins-ref 26.7.3 --output src/saltext/opnsense/utils/models.json
```
- `generate_spec.py`: Parses the PHP controller files in the upstream repo to discover available endpoints.
- `generate_models.py`: Parses the XML model files in the upstream repo to extract validation rules and schema constraints.

## Regenerating Wrappers (optional, dynamic covers all)

```bash
python3 tools/generate_wrappers.py
```
Reads `controllers.json` and emits human-friendly Python wrappers in `src/saltext/opnsense/modules/` and `states/`. Dynamic `__getattr__` injection already covers all 1815 funcs — wrappers optional.

## API Reference — live discovery (not generated dump)

`docs/API.md` is hand-written ~66 lines, not a 568-line stale dump. Source of truth is `utils/controllers.json` meta (26.7.3, 76 modules, 1815 actions).

Live discovery always accurate for target FW version:

```bash
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules
salt -C 'T@opnsense:fw-01' opnsense.list_api_controllers unbound
salt -C 'T@opnsense:fw-01' opnsense.list_api_actions unbound settings
```

Debug helper (not committed):

```bash
python tools/generate_api_docs.py --output /tmp/API_REFERENCE.md  # debug only
```

Tool defaults to stdout, use `--output /tmp/` for offline grepping. Do not commit `docs/API_REFERENCE.md`.

## Verifying Imports

After generation, verify that all dynamically created modules import cleanly:

```bash
PYTHONPATH=src python3 tools/verify_import.py
```

## Public Boundary Guard

```bash
python tools/check_public_boundary.py  # must PASS
```
Scans repo for private strings (lab nets, monorepo path, legacy IDs). CI hard-fails on leak.
