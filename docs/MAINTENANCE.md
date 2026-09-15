# Maintenance — sprinting OPNsense releases (3008+ Resources)

Requires `salt>=3008`. Resources-only, no proxy.

OPNsense ~2/year (25.1, 25.7). Must stay in sync with zero hand-coded funcs — only `make bump CORE=X.Y` to regenerate from upstream `opnsense/core` + `plugins`.

## Design recap

- `generate_spec.py` clones core+plugins at ref, regex `public function Action` → `controllers.json` 76 modules 26.7.3
- `generate_models.py` Model XML → `models.json` relation_targets
- `modules/opnsense.py` loads `controllers.json`, injects 1815 funcs via `__getattr__/__dir__` + `__context__` + Lock (lazy, thread-safe)
- `generate_wrappers.py` emits convenience wrappers optional — dynamic covers all
- `resources/opnsense/__init__.py` Resources one managing minion dozens FWs, per-resource cache, no proxy daemon
- `setuptools_scm` + `py.typed` PEP 561, no-local-version, `_version.py` gitignored

## Sprint checklist

### 1. Renovate PR or manual bump

Renovate tracks `controllers.json` meta `core_ref`. When upstream tag updates, PR updates JSON.

Manual:

```bash
make bump CORE=26.1
# or
python tools/generate_spec.py --core-ref 26.1 --plugins-ref 26.1 --output src/saltext/opnsense/utils/controllers.json
cp src/saltext/opnsense/utils/controllers.json tools/controllers.json
python tools/generate_wrappers.py
PYTHONPATH=src python tools/verify_import.py
```

Full pipeline:

```bash
make gen-all CORE_REF=26.1 PLUGINS_REF=26.1
# or
python tools/generate_all.py --core-ref 26.1 --plugins-ref 26.1
```

Supports `--dry-run`, `--only spec,models,wrappers,verify,test`, `--skip-sync`.

### 2. Run `make gen-all`

```bash
make gen-all CORE_REF=26.1 PLUGINS_REF=26.1
```

Does gen-spec, gen-models, gen-wrappers, sync_extmods, verify 76 exec+state+dynamic 1815 + list_api_modules, test.

If stale cache: `make clean && rm -rf /tmp/opnsense-spec && make gen-all`.

### 3. Verify

```bash
PYTHONPATH=src python3 tools/verify_import.py -v
PYTHONPATH=src pytest tests/unit -v
ruff check src tests tools
make lint
make verify && make test
```

Checklist: verify_import 76 modules 1815 endpoints, pytest 121+ pass, ruff 0, meta core_ref new tag, models.json not empty, py.typed present.

### 4. Test live — read-only smoke

Lab only, no prod.

```bash
export OPNSENSE_HOST=fw-01.example.com
export OPNSENSE_API_KEY=...
export OPNSENSE_API_SECRET=...
python tools/test_live.py
salt -C 'T@opnsense:fw-01' opnsense.ping
salt -C 'T@opnsense:fw-01' opnsense.doctor
salt -C 'T@opnsense:fw-01' opnsense.search unbound settings host_alias row_count=1
salt-run resource.list_grains
```

Do NOT run add/set/del unless dedicated lab. Gated: `OPNSENSE_LIVE_TEST=1 PYTHONPATH=src pytest tests/integration -v -k live`.

### 5. Commit, push, PR

```bash
git add src/saltext/opnsense/utils/controllers.json src/saltext/opnsense/utils/models.json
git commit -m "feat: bump core/plugins to 26.7.3 — regenerate 76 modules"
git push origin feat/bump-26.7.3
```

After merge: `salt '*' saltutil.sync_all` + `opnsense.doctor`.

## CI — spec drift

CI `spec-drift` regenerates spec from `core_ref` in committed JSON, diffs ignoring `generated_at`. If drift → `make bump CORE=${CORE_REF}`.

Renovate custom manager regex tracks `core_ref` for auto-bump PRs.

## Packaging — no-local-version

`setuptools_scm` version from git tags `vX.Y.Z`, no `+gHASH`. Writes `_version.py` gitignored.

PyPI publish via `publish.yml` trusted OIDC on tag `v*.*.*`:

```bash
git tag v1.1.0 && git push origin v1.1.0
```

Local build:

```bash
pip install build twine
python -m build
twine check dist/*
```

## Troubleshooting

- Invalid JSON → need POST default, search always POST
- 404 Endpoint not found → renamed `searchAlias`→`searchItem`, fallback `_resolve_via_spec` + `_call_with_fallback`, regen `make bump`
- RemoteDisconnected → Kea/Unbound restart slow, retry 3x backoff, batch + `onchanges`
- missing config host → `resources:opnsense:hosts:fw-01:host` via `pillar.get unmask=True`, no flat file, removed 1.0.0
- import fails → `salt-pip install -e .` + `sync_all` or file-based `sync_extmods.py --copy`
- list_api_modules <76 → regen spec
- Validation error → `OPNsenseValidationError.validations`, fix data, test=True

## Parallel development

Worktrees for safe parallel branches — each branch own checkout + .venv (see `docs/plans/parallel-workspace.md`, `tools/scripts/parallel-dev.sh`):

```bash
./tools/scripts/parallel-dev.sh ls
./tools/scripts/parallel-dev.sh new feat/my-feature main
cd .worktrees/feat__my-feature
source .venv/bin/activate
make verify && make test
```

Or hermes kanban: `hermes kanban create "fix alias diff" --project saltext-opnsense --workspace worktree`.

See ARCHITECTURE.md, DEVELOPMENT.md, CONTRIBUTING.md, USAGE.md, Makefile help.
