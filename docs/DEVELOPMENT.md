# Development (Salt 3008+ Resources only)

Requires salt>=3008. No proxy.

## Layout

```
src/saltext/opnsense/
  utils/opnsense.py               — Client 3008+ only
  utils/api_spec.py               — Spec loader 75 for 25.7.11
  utils/models.py                 — Model relation handling
  utils/diff.py                   — Diff engine
  utils/common.py                 — helpers
  utils/controllers.json          — 75 modules + meta
  utils/models.json               — Model registry
  modules/opnsense.py             — Exec generic + dynamic 1736 funcs via __getattr__
  modules/{acmeclient,bind,dns,firewall,kea,unbound}.py — Convenience listers
  states/opnsense.py              — Generic state
  states/{bind,dns,unbound}.py    — Convenience states
  resources/opnsense/__init__.py  — Connection module 3008+ Resources
  resources/opnsense/modules/     — Thin delegation via __resource_funcs__
  resources/opnsense/states/      — Re-export via namespaced_function
  resources/opnsense/grains/      — Resource grains
tools/
  generate_spec.py                — codegen core/plugins → controllers.json
  generate_models.py              — Model XML → models.json
  generate_wrappers.py            — spec → wrappers
  generate_all.py                 — pipeline
  verify_import.py                — import proof 75 modules
  test_live.py                    — read-only live smoke via env
  sync_extmods.py                 — sync src → extmods Resources-only no _proxy/_grains
tests/unit/                       — mocked
tests/integration/                — live gated
```

No proxy code ships. Removed 1.0.0.

## Salt 3008+ notes

- packaging setuptools entry-point salt.loader
- builtins __opts__, __salt__, __context__, __grains__, __utils__, __pillar__, __resource__, __resource_funcs__, __minion__
- salt-pip install -e . into onedir
- Resources store client in __context__[opnsense][conns][id] per-resource
- Thin overrides use __resource_funcs__ + __resource__[id]
- State supports test=True
