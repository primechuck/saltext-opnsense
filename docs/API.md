# API Reference

Bundled spec: OPNsense 26.7.3 — 76 modules, 1815 endpoints, 258 controllers in `src/saltext/opnsense/utils/controllers.json`.

All endpoints are accessible via generic `opnsense.call` and dynamic wrappers `opnsense.{module}_{controller}_{action}` injected via `__getattr__` in `modules/opnsense.py`.

## Discovery (live, always accurate for target FW version)

No checked-in dump — API surface changes per OPNsense release. Query the live firewall for truth:

```bash
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules
salt -C 'T@opnsense:fw-01' opnsense.list_api_controllers unbound
salt -C 'T@opnsense:fw-01' opnsense.list_api_actions unbound settings
salt -C 'T@opnsense:fw-01' opnsense.doctor
salt -C 'T@opnsense:fw-01' opnsense.search unbound settings host_alias row_count=1
```

`doctor` returns status OK + spec_version + reachable controllers.

## Dynamic dispatch

- Generic: `opnsense.call unbound settings searchHostAlias`
- Typed: `opnsense.unbound_settings_searchHostAlias` or `opnsense.unbound_settings_search_host_alias`
- Convenience: `opnsense_unbound.list_aliases`, `opnsense_bind.list_domains`, etc.

All 1815 actions are callable without code change — dynamic `__getattr__` reads `controllers.json`.

## Official upstream docs

- https://docs.opnsense.org/development/api.html
- + `/core/{module}.html` (e.g. `/core/unbound.html`, `/core/firewall.html`)
- + `/plugins/{module}.html` (e.g. `/plugins/bind.html`, `/plugins/kea.html`)

Upstream documents request/response shapes; this extension maps 1:1 to those endpoints.

## SOT — source of truth

`src/saltext/opnsense/utils/controllers.json` meta field:

```json
{"core_ref": "26.7.3", "plugins_ref": "26.7.3", "total_modules": 76, "total_controllers": 258, "total_actions": 1815}
```

Renovate tracks `core_ref` for auto-bump PRs. Regenerate via `make bump CORE=26.7.3`.

## Debug full table (not committed)

If you need a local full reference dump for offline grepping:

```bash
python tools/generate_api_docs.py --output /tmp/API_REFERENCE.md  # debug only, not committed
```

Tool defaults to stdout; use `--output` for file. Do not commit generated reference.

## Examples

```bash
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules | wc -l         # 76
salt -C 'T@opnsense:fw-01' opnsense.search firewall alias item row_count=1
salt -C 'T@opnsense:fw-01' opnsense.get unbound settings host_override <uuid>
salt -C 'T@opnsense:fw-01' opnsense.call kea dhcpv4 searchSubnet
```

See `docs/STATES.md` for `opnsense.item_present` generic usage and `docs/QUICKSTART.md` for fleet targeting `T@opnsense:fw-01`.
