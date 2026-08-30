# saltext-opnsense

SaltStack extension for managing OPNsense firewalls via the REST API – **3008+ Salt Resources** fleet-ready.

Manage OPNsense services (Unbound DNS, Kea DHCP, BIND, ACME certs, firewall aliases) declaratively with Salt states or programmatically via execution modules. API bindings generated from upstream OPNsense schemas (75 modules, 1,736 endpoints). Resource-based targeting replaces legacy proxy minion.

> **Breaking 1.0.0**: Proxy minion removed. Requires `salt>=3008`. Use Resources `T@opnsense`. See `docs/RESOURCES.md`.
> **Target Release**: Built for **OPNsense 25.7.11** (75 modules, 1,736 API endpoints).
> **Core Design Goal**: Maintainer laziness. Never hand-code API wrappers. `make bump CORE=25.7.11` regenerates all.

## Features

- **Execution Modules**: 75 modules / 1736 endpoints, `opnsense.search/call/get/add/set/delete`, human-friendly listers (`list_aliases`, `resolve_alias`), dynamic wrappers via `__getattr__`.
- **State Modules**: Generic `item_present/absent` for all modules + convenience `alias_present`, `record_present`, `aliases_managed`, `dns.managed` – idempotent second-run 0 changes via diff engine (bool `1`↔True, UUID↔FQDN, CSV↔list).
- **Idempotency Diff Engine** (`utils/diff.py`): Normalizes flapping API quirks, uses `Final/frozenset`, split helpers.
- **Salt Resources (3008+)**: Fleet support – one managing minion manages dozens FWs. 2 SRN composition `opnsense:fw-01` (API) + optional `ssh:fw-01` (built-in `ssh` resource with thin requiring `python311` on OPNsense). Target `T@opnsense`, `G@opnsense_version`, `T@opnsense:fw-01 or T@ssh:fw-01`.
- **Diagnostics (`opnsense.doctor`)**: Connectivity, spec version, firmware status. Client has `close()` + context manager, `Final` constants, substring sensitive masking.
- **Packaging**: PEP 420 implicit namespace, PEP 561 `py.typed` marker, `setuptools_scm` no-local-version, `optional-dependencies:dev` + `dependency-groups`, `MANIFEST.in` includes `py.typed`, Ruff builtins include `__resource__`.
- **Documentation**: `docs/RESOURCES.md` (fleet tutorial), `QUICKSTART.md`, `ARCHITECTURE.md`, `MAINTENANCE.md`.

## Quick Start – Resources (Recommended)

See **[docs/RESOURCES.md](docs/RESOURCES.md)** for 10-min masterless walk-through and 2 SRN composition.

### 1. Installation

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```

File-based (no pip):

```bash
python3 tools/sync_extmods.py --copy
salt '*' saltutil.sync_all
```

### 2. Configuration – Fleet via Pillar

`/srv/pillar/resources.sls`:

```yaml
resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
        api_key: "your_api_key"
        api_secret: "your_api_secret"
        verify_ssl: true
      fw-02:
        host: fw-02.example.com
        api_key: "..."
        api_secret: "..."
```

Optional SSH side (2 SRN):

```yaml
resources:
  ssh:
    hosts:
      fw-01:
        host: fw-01.example.com
        user: root
        priv: /etc/salt/keys/fw-01
        thin_dir: /tmp/.salt-thin
```

### 3. Diagnostics & Targeting

```bash
salt-call --local saltutil.refresh_pillar
salt-call -r --tgt 'T@opnsense' --tgt-type compound test.ping
salt -C 'T@opnsense' opnsense.search unbound settings host_alias
salt -C 'T@opnsense:fw-01 or T@ssh:fw-01' state.apply fw.base
salt-run resource.list_grains
```

## Usage – Execution & States

```bash
# API search
salt -C 'T@opnsense' opnsense.search firewall alias item

# Dynamic wrapper (generated)
salt -C 'T@opnsense:fw-01' opnsense_unbound_settings_search_host_alias search_phrase=www

# SSH side (if configured)
salt -C 'T@ssh' cmd.run 'opnsense-version'
```

States:

```yaml
# Generic – any of 75 modules
testnet_alias:
  opnsense.item_present:
    - module: firewall
    - controller: alias
    - type: item
    - match: {name: TESTNET}
    - data: {name: TESTNET, type: network, content: "192.0.2.0/24"}

# Convenience – human FQDN auto-resolved to UUID
www:
  opnsense_unbound.alias_present:
    - parent: cluster.example.com
    - domain: example.com

# Pillar-driven zero Jinja – one reconfigure
dns:
  opnsense_dns.managed:
    - name: dns
    - parent: cluster.example.com
```

For 2 SRN mixed example see `docs/RESOURCES.md`.

## Maintenance & Upgrades

API spec bindings generated from upstream `opnsense/core` + `plugins`:

```bash
make bump CORE=26.1
# regenerates controllers.json/models.json, verifies, runs tests
```

See `docs/MAINTENANCE.md`.

## Testing

```bash
PYTHONPATH=src pytest tests/unit -v
PYTHONPATH=src python3 tools/verify_import.py
```

Unit tests cover client retry/masking, diff engine bool/UUID/CSV, resource discovery/init/grains/ping/close, auto-resolve host/subnet/account.

## Packaging Polish – Pythonic & Salty

- `src/saltext/opnsense/py.typed` PEP 561, `.gitignore` untracks `_version.py`, `optional-dependencies:dev` + `dependency-groups`, `readme`/`license` as file objects, `Changelog` URL, `tool.ruff.builtins` includes `__resource__`, `nox` python 3.10-3.14.
- Client `close()` + `__enter__/__exit__`, `Final/frozenset` constants, typing `TypedDict`, specific exceptions, `encoding=utf-8`, no `Path.cwd()` fallback, no `globals()` mutation in connection module, `lru_cache` for spec, thread-safe `_DYNAMIC_MAP_CACHE` via `__context__` + `Lock`.
- States `__virtual__` returns `True`, `__context__` caching not globals, no import-time wrapper injection, `normalize_enabled` unified, `bind.domain_absent` bug fixed (preserves actual type), `strip_salt_internal_kwargs` everywhere, reconfigure verification unified.

## License

MIT
