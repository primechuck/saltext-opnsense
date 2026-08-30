# Salt Resources for saltext-opnsense (3008+)

> **BREAKING 1.0.0:** Proxy minion removed. Resources are the supported mode. Reason for `salt>=3008` requirement.

## Why Resources?

OPNsense is a BSD appliance – no minion. Previously one proxy daemon per FW. Resources: **one managing minion manages dozens of FWs**, with first-class targeting `T@opnsense`, grain targeting `G@opnsense_version`, merged `state.apply` returns prefixed by resource id.

2 SRN model: `opnsense:fw-01` (this extension, pure API) + optional `ssh:fw-01` (built-in `salt.resources.ssh` with thin requiring `python311` on OPNsense). Same human ID in both types enables `AND` composition.

## Quickstart – Masterless (10-min walk-through)

Pillar `/srv/pillar/top.sls`:

```yaml
base:
  '*':
    - resources
```

Pillar `/srv/pillar/resources.sls`:

```yaml
resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
        api_key: testkey
        api_secret: testsecret
        verify_ssl: false
        timeout: 10
      fw-02:
        host: fw-02.example.com
        api_key: testkey2
        api_secret: secret2
        verify_ssl: false
```

Minion config `/etc/salt/minion.d/resources.conf`:

```yaml
file_client: local
file_roots:
  base: [/srv/salt]
pillar_roots:
  base: [/srv/pillar]
```

Confirm:

```bash
salt-call --local pillar.get resources:opnsense:hosts unmask=True
salt-call --local saltutil.refresh_pillar
salt-call -r --tgt 'T@opnsense' --tgt-type compound test.ping
# local:
#   managing-minion: true
#   fw-01: true
#   fw-02: true
```

Per-resource exec:

```bash
salt-call -r --tgt fw-01 opnsense.search unbound settings host_alias
salt-call -r --tgt 'T@opnsense' --tgt-type compound opnsense.list_api_modules
```

State apply merged mode:

```bash
salt-call -r --tgt 'T@opnsense' --tgt-type compound state.apply fw.base
# cmd_|-fw-01 say_hello_|-fw-01 ... 
# cmd_|-fw-02 say_hello_|-fw-02 ...
# Summary: 2 succeeded
```

## Master + Registry (fleet)

On master and managing minion, pillar as above. After `saltutil.refresh_pillar` on managing minion, master registry populates:

```bash
salt-run resource.list_grains
# opnsense:fw-01: grain_keys=[resource_id, opnsense_host, opnsense_version, ...]
# opnsense:fw-02: ...

salt-run resource.show_grains type=opnsense id=fw-01

salt -C 'T@opnsense' test.ping
salt -C 'T@opnsense:fw-01' opnsense.search firewall alias item
salt -C 'T@opnsense' state.sls fw.base
```

Inspection:

```bash
salt -G 'opnsense_version:25.7.*' test.ping
salt -C 'G@opnsense_host:fw-*.example.com and T@opnsense' state.apply
```

Freshness:

```bash
salt-run resource.refresh minion=managing-minion-id
# triggers _discover + grains re-register
```

## 2 SRN Composition – API + SSH

Add built-in ssh resource with **same IDs**:

```yaml
resources:
  opnsense:
    hosts:
      fw-01: {host: fw-01.example.com, api_key: xxx, api_secret: yyy, verify_ssl: true}
  ssh:
    hosts:
      fw-01:
        host: fw-01.example.com
        user: root
        priv: /etc/salt/keys/fw-01
        thin_dir: /tmp/.salt-thin
        # sudo: false
```

Requirements for SSH:

- OPNsense: `pkg install python311` (or via bootstrap state)
- Thin dir writable, ~15MB first copy
- Key on managing minion, not master

Targets:

```bash
salt -C 'T@opnsense' opnsense.search unbound settings host_alias
salt -C 'T@ssh' cmd.run 'opnsense-version'
salt -C 'T@opnsense:fw-01 or T@ssh:fw-01' state.apply fw.base
# fw/base.sls can branch on opts["resource_type"] == "opnsense" vs "ssh"
```

Example state mixing:

```yaml
# fw/base.sls
{% if opts.get("resource_type") == "opnsense" %}
dns_alias:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match: {hostname: www}
    - data: {hostname: www, domain: example.com, host: 192.0.2.1}
{% elif opts.get("resource_type") == "ssh" %}
/usr/local/etc/unbound/conf.d/custom.conf:
  file.managed:
    - contents: "local-data: \"custom.example.com A 192.0.2.2\""
    - require_in:
      - cmd: unbound_reconfigure

unbound_reconfigure:
  cmd.run:
    - name: configctl unbound reconfigure
{% endif %}
```

## Pillar Layout

Default key `resources` (configurable via `resource_pillar_key` minion/master opts). Shape type-specific:

```yaml
resources:
  opnsense:
    hosts: {id: {host, api_key, api_secret, proto, verify_ssl, timeout}}
    # also supports resource_ids: [id, ...] + hosts optional
```

Use `salt.utils.resources.pillar_resources_tree(opts)` – honors custom key.

Secrets: Vault slots `__slot__:salt:vault.read(secret/opnsense/fw-01/api_key)` work because pillar templates render with masking disabled. CLI `pillar.get` masks by default – use `unmask=True`.

## Configuration

No new master config needed. `resource_pillar_key` defaults `resources`. For dozens FWs default `resource_index_primary_capacity 2097152` (256MiB) fine – fits 500k resources.

## Operations

- `salt-call --local saltutil.refresh_pillar` – rebuild minion view
- `salt-call -r --tgt '*' test.ping` – managing minion + resources
- `salt-run resource.list_grains / show_grains` – inspect registry
- `salt-run resource.refresh minion=<id>` – force re-register

## Packaging & Pythonic Notes

- Extension ships pure API via `controllers.json` + dynamic `__getattr__` wrappers (1736 funcs) + convenience listers. No proxy.
- `py.typed` marker present PEP 561, `setuptools_scm` no-local-version, `optional-dependencies:dev` + `dependency-groups`, `MANIFEST.in` includes `py.typed`, `tool.ruff.builtins` includes `__resource__,__resource_funcs__`.
- Client `OPNsenseClient` has `close()` + context manager, `Final`/`frozenset` constants, substring sensitive masking, specific exception handling.

## Troubleshooting

- `Resource not matching -G` → `salt-run resource.list_grains` then `resource.refresh`
- `Function X not supported for opnsense` → `saltutil.sync_all` on managing minion + refresh_pillar
- `missing config host` → check `resources:opnsense:hosts:fw-01:host` exists, `pillar.get ... unmask=True`
- `verify_ssl False` warning → logs debug, set true + CA bundle
- `thin` copy fails → ensure `python311` installed, `thin_dir` writable, SSH key perms 600

## References

- Salt Resources index, tutorial, architecture, targeting, state_authoring, authoring/connection_module, execution_modules, state_modules, pillar layout, packaging
- `salt.resources.ssh` – reference for 2 SRN ssh side
