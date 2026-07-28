# saltext-opnsense

SaltStack extension for managing OPNsense firewalls via the REST API.

Manage OPNsense services (Unbound DNS, Kea DHCP, BIND, ACME certs, firewall aliases, interfaces) declaratively with Salt states or programmatically via execution modules. API bindings are generated directly from upstream OPNsense schemas.

> **Target Release**: Built for **OPNsense 25.7** (76 modules, ~1,816 API endpoints).
> **Core Design Goal**: Maintainer laziness. Never hand-code API wrappers. When OPNsense ships a new release, all 76 modules and 1,800+ endpoints are regenerated directly from upstream schemas via `make bump CORE=25.7`.


## Features

- **Execution Modules**: Direct API calls to OPNsense controllers and actions.
- **State Modules**: Declarative states for OPNsense resources (`item_present`, `item_absent`, DNS aliases, DHCP leases, ACME certs).
- **Proxy Minion Support**: Agentless management of OPNsense hardware and VMs.
- **Auto-Generated Spec**: Keeps up with upstream OPNsense releases without manual code edits.
- **Diagnostics (`opnsense.doctor`)**: Quick CLI check for credentials, API connectivity, and firmware status.

## Quick Start

### 1. Installation

Install on the Salt Master and Proxy Minion:

```bash
salt-pip install saltext-opnsense
salt '*' saltutil.sync_all
```

Or copy directly into Salt's `file_roots` (for environments without `salt-pip`):

```bash
python3 tools/sync_extmods.py --copy
salt '*' saltutil.sync_all
```

### 2. Configuration

Define your OPNsense target in Pillar (e.g. `/srv/pillar/opnsense.sls`). See [pillar.example](file:///Users/dbierce/GitHub/configurations/projects/saltext-opnsense-review/pillar.example) for details.

```yaml
proxy:
  proxytype: opnsense
  host: opnsense.example.com
  proto: https
  api_key: "your_api_key"
  api_secret: "your_api_secret"
  # verify_ssl: false  # Optional; defaults to true
```

### 3. Diagnostics

Verify connectivity and credential resolution:

```bash
salt opnsense-router opnsense.doctor
```

## Usage

### Execution Module

```bash
# Search Unbound DNS host aliases
salt opnsense-router opnsense.search unbound settings host_alias

# Call endpoint directly
salt opnsense-router opnsense_unbound.search_host_alias
```

### State Module

```yaml
# Ensure an Unbound Host Alias exists
www_alias:
  opnsense_unbound.host_alias_present:
    - data:
        enabled: "1"
        hostname: www
        domain: example.com
    - reconfigure: unbound/service/reconfigure
```

## Maintenance & Upgrades

API spec bindings are generated from upstream `opnsense/core` and `opnsense/plugins`.

When OPNsense ships a new release (e.g. `26.1`), regenerate bindings with:

```bash
make bump CORE=26.1
```

For developer documentation and full maintenance details, see [docs/MAINTENANCE.md](file:///Users/dbierce/GitHub/configurations/projects/saltext-opnsense-review/docs/MAINTENANCE.md).

## Testing

```bash
# Run unit tests
PYTHONPATH=src pytest tests/unit -v

# Verify module imports
PYTHONPATH=src python3 tools/verify_import.py
```
