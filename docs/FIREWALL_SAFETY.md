# Firewall filter apply / savepoint safety pattern

## Summary

The OPNsense `firewall` API historically offered a rollback safety timer for
filter rules, documented at `https://docs.opnsense.org/development/api/core/firewall.html`
as `filter_base/savepoint`, `apply(rollback_revision)`, `cancelRollback`,
`revert`. As of **core@17b84612 Jun 18 2026 PR #10411**, this mechanism was
**removed from core** — message: "Remove safepoint actions, no callers should be left".
A simplified `applyAction` was re-added Jun 23 2026 (#10440) that only does:

```php
return ["status" => (new Backend())->configdRun('filter reload')]
// current master on Jul 2026:
return ["status" => (new Backend())->configdRun('filter reload skip_alias')]
```

The docs page still lists the old endpoints at time of writing (stale gen), but
live `FilterBaseController.php` on master and in `/tmp/opnsense-spec`
contains only `apply`, not `savepoint`. Current vendored spec in this repo
`tools/controllers.json` also shows `filterbase: ["apply", "listCategories", ...]`
— no savepoint.

**Conclusion:** Do **not** implement automatic savepoint+apply+check in
`opnsense.reconfigured`. Keep simple explicit batch + apply. Document safety
separately.

## How the old pattern worked (historical)

From old core + docs + commit diff:

```
savepoint() -> returns {"status":"ok","revision":"1718...","retention":"..."}
  Config::save() first to freeze revision time.

administration: addRule/setRule/delRule/toggleRule (model changes only)

apply(rollback_revision) -> starts background rollback_timer with flock:
  configd action [rollback_timer] = flock /tmp/filter_rollback_timer.lock
    scripts/filter/rollback_timer.php <revision>
  Timer sleeps 60s, checks if cancel file exists, else rollback Filter component
  to revision backup and reload.

cancelRollback(revision) -> calls rollback_cancel.php, touches cancel marker,
  stops timer.

revert(revision) -> manual rollback: getBackupFilename, model->rollback(revision),
  save(), reload.

Note: rollback only touched OPNsense->Firewall->Filter subtree, not other
config (e.g. interfaces added between savepoint and revert stay).
```

Source: removed files `rollback_timer.php`, `rollback_cancel.php`, actions_filter.conf
entries `[rollback_timer]`, `[cancel_rollback]`, `Filter.php::rollback()`.

XXX comment in old controller: "// Not directly used by GUI, should be removed at some point"

## How other automation handles it

* **OPNsense GUI itself** — stopped using savepoint before removal (hence comment).
* **Ansible community** — `ansible` OPNsense modules (e.g. `ansibleguy.opnsense`,
  `browningluke/ansible-collection`) pattern: `setRule` / `addRule` then separate
  `apply` task. No savepoint in typical playdocs; safety handled by
  check-mode / `onchanges` and manual verification. Web search
  "opnsense firewall filter apply ansible savepoint" returns only official docs,
  no third-party usage — confirming niche adoption.

* **Terraform `browningluke/opnsense` & `bargonauts/xopnsense`** — resource lifecycle
  `Create/Update` calls `setRule` then `apply` via `filter reload`. No savepoint.
  Provider docs omit rollback; user responsible for not locking self out.

* **Go API `pmeier/opnsense-go-api`, `browningluke/opnsense-go`** — exposes
  `FilterBase/Apply`, `Savepoint` was present in older go client but marked
  deprecated; recent code only calls reload.

Overall: community treats firewall like other modules — *change then apply*.
Safety nice in theory, fiddly in practice (requires caller keep revision token,
must reliably call cancel within 60s even on network blip, only reverts one
component, adds extra config saves).

## Recommended Salt behavior

Keep explicit, no auto-savepoint:

* `item_present/absent` with `reconfigure: firewall/alias/reconfigure` or
  `firewall/filterbase/apply` for alias vs filter? Check mapping:
  - Alias controller has its own `reconfigure` (updates tables)
  - Filter rules: until Jun 2026 you could still call `filter/alias/reconfigure`
    fallback but correct is `filterbase/apply` or `filter/filter/apply`? In current
    wrapper generator, `filter` controller's apply is via `filterbase` base.
  - In generated `opnsense_firewall` state wrapper, default reconfigure was
    `firewall/alias/reconfigure` for all rule types (bug, but works because
    apply semantics overlap). Prefer explicit `filterbase/apply` for filters.

* Batch changes then single apply via `onchanges` to avoid multiple reloads:

```yaml
allow_lan_to_app:
  opnsense_firewall.filter_rule_present:
    - name: allow lan to app
    - data:
        action: pass
        interface: lan
        direction: in
        source_net: lan
        destination_net: "192.0.2.0/24"
        protocol: TCP
        description: "Salt: allow lan->app (TEST-NET-1 example)"
        enabled: "1"
    # no reconfigure here, batch

allow_wg_to_services:
  opnsense_firewall.filter_rule_present:
    - data:
        action: pass
        interface: wireguard
        destination_net: "198.51.100.0/24"
        description: "Salt: wg->services (TEST-NET-2 example)"
        enabled: "1"

apply_filter:
  opnsense_firewall.reconfigured:
    - name: apply firewall filters
    - controller: filterbase
    - action: apply
    - onchanges:
      - opnsense_firewall: allow_lan_to_app
      - opnsense_firewall: allow_wg_to_services
```

* For aliases (non-lockout risk), auto-reconfigure per rule is fine:

```yaml
svc_aliases:
  opnsense_firewall.alias_item_present:
    - data: {...}
    - reconfigure: firewall/alias/reconfigure
```

## Safety recommendations without savepoint

Since rollback timer no longer exists in >=25.7/26.x:

1. **Anti-lockout**: Keep default anti-lockout rule enabled, don't manage it
   via Salt. Put restrictive rules after anti-lockout.

2. **Test mode first**: `salt opnsense-router state.apply opnsense.firewall test=True`

3. **Out-of-band access**: Ensure IPMI / console / separate mgmt VLAN so
   failed filter doesn't brick.

4. **Separate apply**: Use `onchanges` as above — one reload after all edits,
   easier to reason about.

5. **If on older OPNsense (<25.x) where savepoint still exists**, you can
   manually implement safety if you really want:

```yaml
# optional manual safety wrapper for old hosts — only needed if host still has endpoint
manual_savepoint:
  opnsense.call:
    - module: firewall
    - controller: filterbase
    - action: savepoint
    - method: POST

# ... make changes, apply with revision from previous call ...

# cancel:
# opnsense.call firewall filterbase cancelRollback <revision>
```

But don't bake into module — opt-in SLS if operator wants it. The generic
`opnsense.call` already supports it; no code change needed.

## Migration

* Renovate bumps `core_ref` in `controllers.json`. When your host upgrades
  past removal commit, any SLS calling `savepoint` will start failing
  (404/unknown action). Replace with plain `apply`.

* Docs page `https://docs.opnsense.org/development/api/core/firewall.html`
  still shows old table — expect upstream docs update soon.

* `vendor_charts.py` post-upgrade runs regeneration — no extra work.

## Decision

* No code change in `opnsense_firewall.reconfigured` state.
* Provide this doc.
* Keep `filterbase_apply` wrapper (already generated) as primary apply entry.
* If future OPNsense re-introduces guard with different semantics (e.g. pf-safe
  with auto-rollback built into reload), reassess — but explicit remains safer
  for idempotent Salt than hidden timers.

Refs:
- Removal: opnsense/core@17b84612 #10411
- Re-add simple apply: opnsense/core@311c3c05 #10440
- Docs: firewall.rst (still lists savepoint, pending doc PR)
- Current controller: FilterBaseController.php apply => filter reload skip_alias
