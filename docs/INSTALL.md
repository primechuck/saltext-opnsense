# Installation

Three supported ways, pick one. File-based is fastest for novices.

## Option A: File-based via gitfs (15-min novice path, no pip)

Your Salt master file roots is a gitfs repo. Extension files live in `src/` and are exposed via `_modules/`, `_states/`, `_proxy/`, `_grains/`, `_utils/`.

```bash
# In your salt repo that is gitfs root:
# Copy extension extmods for file-based (keeps symlinks safe)
python3 tools/sync_extmods.py --copy
# Or on master:
salt '*' saltutil.sync_all
salt opnsense-router saltutil.sync_all  # proxy id
salt opnsense-router opnsense.list_api_modules
```

- No `salt-pip` needed
- Master picks up commit via `fileserver.update`
- Verify: `salt salt-master saltutil.list_extmods | grep opnsense`

See `docs/tutorials/pillars/file-based-proxy.yaml` for flat `/etc/salt/proxy` format.

## Option B: Pip as saltext (production)

```bash
salt-pip install saltext-opnsense
# or editable dev:
salt-pip install -e /path/to/saltext-opnsense

salt '*' saltutil.sync_all
salt opnsense-router opnsense.list_api_modules
```

`pyproject.toml` entry point `saltext.opnsense` exposes to loader. Works with onedir `/opt/saltstack/salt`.

Benefits: versioned, dependency managed. Drawback: need pip upgrade after bump.

Alternative `master.d`:

```yaml
# /etc/salt/master.d/opnsense.conf
extension_modules: /path/to/saltext-opnsense/src
```

## Option C: Salt file roots copy (air-gapped)

```bash
# Copy src/saltext/opnsense/* into your file_roots extmods:
# _modules/opnsense.py, _states/opnsense.py, _proxy/opnsense.py, _grains/opnsense.py, _utils/...
python3 tools/sync_extmods.py --copy --dest /srv/salt/_modules
salt '*' saltutil.sync_all
```

## Verify install

```bash
PYTHONPATH=src python3 tools/verify_import.py
# expect 75 modules, >=300 dynamic exec funcs

salt opnsense-router opnsense.doctor
# spec_version 25.7.11, loaded_modules_count 75, status OK
```

## Upgrade

OPNsense ships ~2 releases/year. To bump:

```bash
make bump CORE=26.1
# regenerates controllers.json + models.json + verifies import
# then:
make test
git commit -m "bump 26.1" src/saltext/opnsense/utils/controllers.json
```

See `docs/MAINTENANCE.md`.

## Uninstall

```bash
salt-pip uninstall saltext-opnsense
# or remove file-based extmods and sync_all
```
