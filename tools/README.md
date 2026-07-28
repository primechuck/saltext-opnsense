# OPNsense Extension Tools

This directory contains the code generation scripts required to maintain this Salt extension. 
Since the OPNsense API is massive (1,800+ endpoints) and constantly changing, this extension dynamically generates its API bindings and data models directly from the upstream OPNsense source code.

## Generating API Definitions

When a new OPNsense release is available, you should update the API specifications:

```bash
python3 tools/generate_spec.py --core-ref 25.7 --plugins-ref 25.7 --output tools/controllers.json
python3 tools/generate_models.py --core-ref 25.7 --plugins-ref 25.7 --output tools/models.json
```
- `generate_spec.py`: Parses the PHP controller files in the upstream repo to discover available endpoints.
- `generate_models.py`: Parses the XML model files in the upstream repo to extract validation rules and schema constraints.

## Regenerating Static Wrappers

After updating the definitions, regenerate the static execution and state wrapper modules:

```bash
python3 tools/generate_wrappers.py
```
This script reads `controllers.json` and emits human-friendly Python wrappers in `src/saltext/opnsense/modules/` and `src/saltext/opnsense/states/`.

## Syncing Extmods (File Roots)

If you need to distribute the extension via Salt's file roots instead of `salt-pip`, use the sync tool to copy the modules into your `_modules`, `_states`, and `_utils` directories:

```bash
python3 tools/sync_extmods.py --copy
```

## Verifying Imports

After generation, verify that all dynamically created modules import cleanly without syntax errors:

```bash
PYTHONPATH=src python3 tools/verify_import.py
```
