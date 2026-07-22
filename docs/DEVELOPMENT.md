# Development

## Layout

```
src/saltext/opnsense/
  utils/opnsense.py   — Client
  utils/api_spec.py   — Spec registry loader
  proxy/opnsense.py   — Proxy minion
  modules/opnsense.py — Execution module (generic)
  states/opnsense.py  — State module (generic)
  grains/opnsense.py  — Grains
tools/
  generate_spec.py    — codegen from upstream core/plugins
  controllers.json    — generated registry (committed)
tests/
  unit/               — mocked, no live OPNsense needed
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

## Renovate integration (TODO)

Add to `renovate.json5`:

```json5
{
  customManagers: [
    {
      customType: "regex",
      fileMatch: ["^projects/saltext-opnsense/tools/controllers.json$"],
      matchStrings: ['"core_ref": "(?<currentValue>.*)"'],
      datasourceTemplate: "github-tags",
      depNameTemplate: "opnsense/core"
    }
  ]
}
```

Post-upgrade task: run `generate_spec.py`.

## Publishing as own repo

Eventually this directory becomes submodule:

```bash
# Create Forgejo repo
ssh forgejo.bierce.org create repo empire/saltext-opnsense

# In monorepo root, filter branch to extract
git subtree split -P projects/saltext-opnsense -b saltext-opnsense-main
git push ssh://git@forgejo.bierce.org:2222/empire/saltext-opnsense.git saltext-opnsense-main:main

# Then replace directory with submodule
git rm -r projects/saltext-opnsense
git submodule add ssh://git@forgejo.bierce.org:2222/empire/saltext-opnsense.git projects/saltext-opnsense
```

## Future SSH module

Same state interface, different transport:

```python
# proxy/opnsense_ssh.py using salt.utils.vt_helper.SSHConnection
# shares utils/opnsense for secrets but talks via SSH configd cli `configctl`
```

Keep API scope only for now.

