# Development

## Layout

```
src/saltext/opnsense/
  utils/opnsense.py   — Client (search/get/add/set/del/toggle/reconfigure)
  utils/api_spec.py   — Spec registry loader (list_modules returns 76)
  utils/controllers.json — 76 modules (acmeclient..zerotier) + meta
  proxy/opnsense.py   — Proxy minion
  modules/opnsense.py — Execution module (generic) + dynamic injection 1816 funcs for all 76 modules (free)
  modules/opnsense_{module}.py — 76 auto-generated ergonomic wrappers (caddy,haproxy,nginx etc included free)
  states/opnsense.py  — State module (generic) + dynamic injection
  states/opnsense_{module}.py — 76 auto-generated state wrappers (free)
  grains/opnsense.py  — Grains (opnsense_version, api_modules=76)
examples/states/
  free_modules_demo.sls — proves free modules importable (caddy/haproxy/nginx via generic+wrapper)
tools/
  generate_spec.py    — codegen from upstream core/plugins → controllers.json (76 modules)
  generate_wrappers.py — spec → 76+76 wrappers (free, idempotent)
  verify_import.py    — import proof: exec 76 OK + state 76 OK + dynamic 1816 + list_api_modules 76
  controllers.json    — generated registry (committed, fallback)
tests/unit/
  test_free_modules_import.py — 8 tests proving free modules import, demo exists
  modules/test_exec_wrappers_generated.py — verifies all modules have search/reconfigure
```

## Salt 3008+ notes

- `saltext-*` packaging via `setuptools`, entry-point `salt.loader`
- `__opts__`, `__pillar__`, `__proxy__`, `__salt__` builtins declared in `[tool.ruff]`
- `salt-pip install -e .` installs into onedir `/opt/saltstack/salt`
- Use `salt.utils.platform.is_proxy()` to branch proxy vs direct
- Proxy stores client in `DETAILS` / `__context__` dict (global per process)
- State must support `test=True` (check mode)

## Adding new ergonomic wrappers (optional future)

If generic `item_present` feels verbose, generate specific states:

```python
# generation target
def host_alias_present(name, hostname, domain, host_uuid, enabled="1", reconfigure=True):
    return item_present(name, "unbound", "settings", "host_alias", {...}, match, reconfigure)
```

Generator would read Model XML `src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml` to get fields + required.

For now, generic only keeps maintenance low — one file to maintain vs 100.

## Renovate integration

Add to `renovate.json5`:

```json5
{
  customManagers: [
    {
      customType: "regex",
      fileMatch: ["^src/saltext/opnsense/utils/controllers\\.json$"],
      matchStrings: ['"core_ref": "(?<currentValue>.*)"'],
      datasourceTemplate: "github-tags",
      depNameTemplate: "opnsense/core"
    }
  ]
}
```

Post-upgrade task: run `generate_spec.py`.

## Publishing

This extension is published at https://github.com/primechuck/saltext-opnsense. To install:

```bash
pip install saltext-opnsense
# or into Salt's onedir:
salt-pip install saltext-opnsense
```

## Future SSH module

Same state interface, different transport:

```python
# proxy/opnsense_ssh.py using salt.utils.vt_helper.SSHConnection
# shares utils/opnsense for secrets but talks via SSH configd cli `configctl`
```

Keep API scope only for now.
