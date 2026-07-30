# Maintenance — sprinting OPNsense releases

This doc is for the maintainer picking up yet another project. OPNsense ships ~2 releases/year (25.1, 25.7). This extension MUST stay in sync with zero hand-coded functions.

## Design recap

- `tools/generate_spec.py` clones `opnsense/core` + `plugins`, regex `public function (\w+)Action` in `Api/*Controller.php` → `controllers.json` (76 modules, 258 controllers, ~1814 actions).
- `src/saltext/opnsense/modules/opnsense.py` loads `controllers.json` at import and injects `unbound_settings_search_host_alias` etc (1816 funcs). **No Python edit needed** when OPNsense adds module.
- `tools/generate_wrappers.py` emits static wrappers `modules/opnsense_{module}.py` + `states/opnsense_{module}.py` (76+76 files). Optional but gives IDE completion and offline docs.
- Fallback: if spec missing, generic `opnsense.call module controller action` still works.

## Sprint checklist (Renovate → merge)

### 1. Renovate PR bumps core_ref/plugins_ref in controllers.json

Renovate config in root `renovate.json5` (see `renovate-snippet.json5`) tracks:

```json
"fileMatch": ["^src/saltext/opnsense/utils/controllers\\.json$"]
"matchStrings": ["\"core_ref\":\\s*\"(?<currentValue>[^\"]+)\""]
"depNameTemplate": "opnsense/core"
"datasourceTemplate": "github-tags"
```

When `opnsense/core` tags 25.7→26.1, Renovate opens PR updating both:

- `src/saltext/opnsense/utils/controllers.json` (`meta.core_ref`, `meta.plugins_ref`)
- `tools/controllers.json` (copy, fallback)

`postUpgradeTasks` (branch executionMode):

```bash
python tools/generate_spec.py --core-ref {{newVersion}} --plugins-ref {{newVersion}} --output src/saltext/opnsense/utils/controllers.json
cp src/saltext/opnsense/utils/controllers.json tools/controllers.json
```

If PR didn't auto-regenerate (fallback), do manually.

### 2. Run make gen-all (or steps manually)

```bash
source .venv/bin/activate  # or python3 -m venv .venv

# all-in-one
make gen-all

# equivalent manual:
python tools/generate_spec.py --core-ref 25.7 --plugins-ref 25.7 --output src/saltext/opnsense/utils/controllers.json
cp src/saltext/opnsense/utils/controllers.json tools/controllers.json
python tools/generate_wrappers.py
PYTHONPATH=src python tools/verify_import.py
```

What `make gen-all` does (see Makefile):

1. `gen-spec`: regenerate `controllers.json` from upstream (or use existing if offline)
2. `gen-wrappers`: emit 76+76 wrappers
3. `verify`: import proof — 76 exec OK + 76 state OK + dynamic >=300 + `list_api_modules` = 76

### 3. Verify with tools/verify_import.py and pytest

```bash
PYTHONPATH=src python3 tools/verify_import.py -v

PYTHONPATH=src pytest tests/unit -v
# expect 37+ tests, including free_modules_import proving caddy/haproxy/nginx importable

ruff check src tests tools
```

If `verify_import` reports missing modules (<76) — spec generation incomplete (network? clone dir stale). Remove `/tmp/opnsense-spec` and retry.

### 4. Test live via test_live.py against opnsense-router (read-only)

`opnsense-router` is the OPNsense box (router/DNS, not Salt-managed yet). Use read-only search calls:

```bash
# env var method (recommended)
export OPNSENSE_HOST=opnsense.example.com
export OPNSENSE_API_KEY=<your-api-key>
export OPNSENSE_API_SECRET=<your-api-secret>

python tools/test_live.py
# or explicit:
python tools/test_live.py --host opnsense.example.com --key $OPNSENSE_API_KEY --secret $OPNSENSE_API_SECRET
```

Expected OKs:
- `core/firmware/status`
- `unbound/overview/isEnabled`
- `unbound/settings/searchHostAlias`
- `bind/domain/searchPrimaryDomain`
- `firewall/alias/searchItem`

Then via Salt proxy (if proxy running on salt-master):

```bash
salt opnsense-router test.ping
salt opnsense-router opnsense.ping
salt opnsense-router opnsense.list_api_modules  # should be 76
salt opnsense-router opnsense.list_api_controllers unbound
salt opnsense-router opnsense.search unbound settings host_alias row_count=2
salt salt-master opnsense.call unbound settings searchHostAlias '{"rowCount":1}'  # direct mode
```

Do NOT run `add/set/del` against opnsense-router in maintenance sprint unless in dedicated test lab. Read-only search is enough to prove client works.

### 5. Commit, push, and open a PR

```bash
git add src/ tools/
git status
git commit -m "feat(opnsense): bump core/plugins to 25.7, regenerate 76 modules"
git push origin feat/saltext-opnsense-25.7
# open PR → merge to main at https://github.com/primechuck/saltext-opnsense
```

After merge, update your Salt master:

```bash
ssh salt-master
sudo salt salt-master fileserver.update
sudo salt salt-master saltutil.sync_all
sudo salt opnsense-router grains.items
```

## Troubleshooting

### `Invalid JSON syntax` on call → need POST

OPNsense API expects POST with JSON body even for search. GET with empty body returns `{"result":"failed","validations":...}` or "Invalid JSON syntax" when content-type missing. **Fix:** always POST with `{"rowCount": -1, "current":1, "searchPhrase":""}` for search. Client defaults to POST (`method=None → POST`, empty data `{}`).

Check `src/saltext/opnsense/utils/opnsense.py: call()`: if `method==POST and data is None → data={}`.

### `404 Endpoint not found` → fallback candidates

OPNsense renamed `searchAlias` → `searchItem` in firewall alias (24.x→25.x). Our client tries multiple candidates via `_resolve_via_spec` + `_call_with_fallback`:

```python
candidates = ["search_host_alias", "searchHostAlias", "search_host_aliases", ...]
for action in candidates:
  try: call(...)
  except OPNsenseAPIError as e:
    if "404" in str(e) or "Endpoint not found" in str(e): continue
    else: raise
```

If new OPNsense version renames again, add pattern to `_candidate_actions`. Usually spec regen picks up new name automatically.

### `RemoteDisconnected` / `Connection aborted` → retry

Seen when Kea restart is slow or many searches parallel. Client timeout 30s. Retry is manual currently (not auto). In state, ensure `reconfigure` is explicit and after all changes, not per item, to reduce API churn. For live test, just re-run `test_live.py`.

### `grains __virtual__ None` → fixed

Early version had `grains/opnsense.py` returning `(False, ...)` when proxy down, causing grains not to load anywhere. **Fix:** grains always return True in `__virtual__` (see current implementation) and empty dict if proxy down. `opnsense_grains()` checks `__salt__["opnsense.ping"]()` with try/except, returns `{}` if not reachable.

### `saltext.opnsense.utils.opnsense` import fails → _try_import fallback

`modules/opnsense.py` tries 4 import paths in `_try_import()`:

1. `saltext.opnsense.utils.opnsense` + `saltext.opnsense.utils.api_spec`
2. `saltext.opnsense.utils.opnsense` + `opnsense_api_spec` (flat)
3. `opnsense` + `opnsense_api_spec` (legacy)
4. `salt.utils.opnsense` + `salt.utils.opnsense_api_spec` (old)

If all fail, `__virtual__` returns `(False, "opnsense utils missing: ...")`. Run `tools/sync_extmods.py --copy` and `salt salt-master saltutil.sync_all`.

### `list_api_modules` returns <76

Spec file missing or outdated. Check:

```bash
cat src/saltext/opnsense/utils/controllers.json | jq .meta
ls -lh tools/controllers.json src/saltext/opnsense/utils/controllers.json
```

Regen: `python tools/generate_spec.py --core-ref 25.7 --plugins-ref 25.7 --output src/.../controllers.json && cp ... tools/`

### OPNsense API returns `result: failed` with `validations`

Validation error (e.g., duplicate hostname, missing required field). `OPNsenseClient.request()` raises `OPNsenseValidationError` with `.validations` dict. In state, comment shows validations.

### Pillar merging confusion (proxy file vs pillar)

`get_client_from_opts` merge order: `pillar.opnsense`, `pillar.proxy`, `opts.opnsense`, `opts.proxy`. Last wins. So `/etc/salt/proxy` file (flat YAML → `opts.proxy`) overrides pillar. For Vault migration, file should be minimal `proxytype: opnsense` only. See `docs/USAGE.md` Proxy dance.

## Future sprints automation

Goal: Renovate PR alone should be merge-ready (already regenerates JSON). Add to `renovate.json5` postUpgradeTasks:

```bash
python tools/generate_wrappers.py
PYTHONPATH=src python tools/verify_import.py
```

Currently these are manual; add after proving stability.
