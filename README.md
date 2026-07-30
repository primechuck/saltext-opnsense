# saltext-opnsense

SaltStack extension for managing OPNsense firewalls via the REST API.

Manage OPNsense services (Unbound DNS, Kea DHCP, BIND, ACME certs, firewall aliases, interfaces) declaratively with Salt states or programmatically via execution modules. API bindings are generated directly from upstream OPNsense schemas.

> **Target Release**: Built for **OPNsense 25.7.11** (75 modules, 1,736 API endpoints – 76 on master).
> **Core Design Goal**: Maintainer laziness. Never hand-code API wrappers. When OPNsense ships a new release, all 75+ modules and 1,700+ endpoints are regenerated directly from upstream schemas via `make bump CORE=25.7.11`.


## Features

- **Execution Modules**: Direct API calls to 75 modules (25.7.11) / 1736 endpoints, human-friendly listers (`list_aliases`, `resolve_parent`).
- **State Modules**: Generic `item_present/absent` for all modules + convenience wrappers `alias_present`, `record_present`, `aliases_managed`, `dns.managed` – idempotent second-run 0 changes via diff engine.
- **Idempotency Diff Engine** (`utils/diff.py`): Normalizes bool `"1"` ↔ True, UUID ↔ FQDN, CSV ↔ list, trailing dot, numbers – fixes Salt flapping on non-idempotent OPNsense API.
- **Proxy Minion Support**: Agentless management, Vault `__slot__` for secrets, grains for version targeting.
- **Auto-Generated Spec**: 75 modules (25.7.11) from upstream `opnsense/core` + `plugins` via `make bump CORE=25.7.11`, no hand-coded wrappers.
- **Diagnostics (`opnsense.doctor`)**: Quick CLI check for credentials, API connectivity, and firmware status.
- **Documentation**: `docs/CONVENIENCE.md`, `ARCHITECTURE.md`, `MAINTENANCE.md`, `USAGE.md`.

## Quick Start — Novice 15 min

See **[docs/QUICKSTART.md](docs/QUICKSTART.md)** for step-by-step novice path (no Vault, no Jinja).

Summary:

### 1. Installation

Install on the Salt Master and Proxy Minion:

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```

Or file-based (no pip):

```bash
python3 tools/sync_extmods.py --copy
salt '*' saltutil.sync_all
```

### 2. Configuration (minimal flat file)

`/etc/salt/proxy` on master:

```yaml
proxytype: opnsense
host: opnsense.example.com
proto: https
api_key: "your_api_key"
api_secret: "your_api_secret"
```

See [pillar.example](pillar.example) and `docs/tutorials/pillars/file-based-proxy.yaml`.

### 3. Diagnostics

```bash
salt opnsense-router opnsense.doctor
# should be OK, spec_version 25.7.11
```

## Usage

### Execution Module

```bash
# Search Unbound DNS host aliases
salt opnsense-router opnsense.search unbound settings host_alias

# Call endpoint directly
salt opnsense-router opnsense_unbound.search_host_alias
```

### State Module – convenience wrappers (human FQDN, idempotent)

```yaml
# Single alias – human parent auto-resolved to UUID, idempotent diff engine
www:
  opnsense_unbound.alias_present:
    - parent: cluster.example.com
    - domain: example.com

# Batch – one state, one reconfigure, pillar-driven
dns_batch:
  opnsense_unbound.aliases_managed:
    - parent: cluster.example.com
    - aliases:
        example.com: [www, git, auth]
    - purge:
        example.com: [old-git]

# Fully pillar-driven – zero Jinja
dns:
  opnsense_dns.managed:
    - name: dns
    - parent: cluster.example.com

# Generic fallback for any of 75+ modules (TEST-NET RFC5737)
testnet_alias:
  opnsense.item_present:
    - module: firewall
    - controller: alias
    - type: item
    - match: {name: TESTNET}
    - data: {name: TESTNET, type: network, content: "192.0.2.0/24"}
```

## Maintenance & Upgrades

API spec bindings are generated from upstream `opnsense/core` and `opnsense/plugins`.

When OPNsense ships a new release (e.g. `26.1`), regenerate bindings with:

```bash
make bump CORE=26.1
```

For developer documentation and full maintenance details, see [docs/MAINTENANCE.md](docs/MAINTENANCE.md).

## Testing

```bash
# Run unit tests
PYTHONPATH=src pytest tests/unit -v

# Verify module imports
PYTHONPATH=src python3 tools/verify_import.py
```
