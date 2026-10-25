# OPNsense Extension Tools

This directory holds the code generators and guards that maintain this Salt extension.
The OPNsense API is large (1,800+ endpoints) and changes every release, so the API registry and
model schemas are **generated from the upstream OPNsense source**, never hand-written.
Read [`AGENTS.md`](../AGENTS.md) first: it defines which files are generated and may not be edited.

## How upstream is ingested

```text
opnsense/core   @ core_ref ─┐   shallow clone (git clone --depth 1 --branch <tag>)
opnsense/plugins@ plugins_ref┘
   │
   ├─ generate_spec.py    regex over src/opnsense/mvc/app/controllers/OPNsense/<Module>/Api/<Ctrl>Controller.php
   │                      for `public function <name>Action(` → utils/controllers.json
   │                      {module: {controller: [actions]}} + meta (core_ref, plugins_ref, totals)
   └─ generate_models.py  parse src/opnsense/mvc/app/models/OPNsense/<Module>/<Model>.xml
                          → utils/models.json: per-field type, OptionValues, constraints,
                          relation_targets (how a field references another model by UUID)
```

At runtime nothing is code-generated: `modules/opnsense.py` builds wrappers lazily from
`controllers.json` through `__getattr__`, and `states/opnsense.py` resolves relations with
`models.json`. A new OPNsense release therefore needs a registry bump, not code changes.

## Regenerating (when a new OPNsense release is available)

Run from the repository root. Prefer the single entrypoint:

```bash
make gen-all CORE=26.7.3     # spec -> models -> verify_import -> pytest tests/unit (recommended)
# or: nox -s gen_all -- --core-ref 26.7.3 --plugins-ref 26.7.3
make gen-spec gen-models CORE=26.7.3   # registries only
make bump CORE=26.7.3        # controllers.json + import check only; does NOT refresh models.json
```

Bump `controllers.json` and `models.json` together: the drift gate regenerates both at the refs in
`controllers.json` `meta`, so a spec-only bump leaves `models.json` flagged as drifted.

Individual steps (always pass **both** refs so `meta` records what was scanned):

```bash
python3 tools/generate_spec.py   --core-ref 26.7.3 --plugins-ref 26.7.3 --output src/saltext/opnsense/utils/controllers.json
python3 tools/generate_models.py --core-ref 26.7.3 --plugins-ref 26.7.3 --output src/saltext/opnsense/utils/models.json
```

- `--local-core/--local-plugins` (spec) and `--core/--plugins` (models) reuse existing clones.
- Commit regenerated JSON on its own, separate from hand-written changes, so review can tell
  generated churn from logic changes. Expect `meta.generated_at` to change on every run.
- Generated JSON carries `meta.warning` ("DO NOT EDIT ..."). JSON cannot hold comments, so this is
  the sentinel; any generated **Python** file must instead begin with the 3-line header defined
  as `SENTINEL` in `generate_wrappers.py`.

## Overrides and what regeneration never touches

Generators write only `utils/controllers.json`, `utils/models.json` (and, for the deprecated
wrapper generator, `{modules,states}/opnsense_<module>.py`). Custom behavior lives in files the
generators never write, so there is no merge or overwrite step:

- `states/opnsense.py`: `_RESOLVE_MAP` (field → relation lookup) and `_RECONFIGURE_OVERRIDES`
  (which service endpoint applies a change).
- `states/dns.py` + `modules/dns.py`: hand-written Unbound alias helpers (`opnsense_dns`).
- `utils/diff.py`, `utils/common.py`: normalization and reconfigure-path helpers.
- `resources/opnsense/**`: Resource connection module and per-resource overrides.

If a generated result is wrong, fix the generator (or add a hand-written override), regenerate,
and run the drift check. Never patch the JSON.

## Codegen drift gate

```bash
python tools/check_codegen_drift.py               # offline: sentinels, meta totals, stray files
python tools/check_codegen_drift.py --regenerate  # + re-run generators at the pinned refs
nox -s codegen_drift                              # same as --regenerate (needs git + network)
make check-drift DRIFT_ARGS=--regenerate
```

`--regenerate` regenerates into a temp dir and compares with the committed JSON ignoring only
`meta.generated_at`, which is the deterministic equivalent of `git diff --exit-code` after a
regeneration. It fails on hand edits and on registry/generator mismatches. The offline half
also runs in the unit suite (`tests/unit/test_codegen_guardrails.py`).

## Deprecated and ancillary generators

- `generate_wrappers.py` — **deprecated**; writes static `opnsense_<module>.py` wrappers. Not run
  by `generate_all.py` and no output is committed. The runtime `__getattr__` covers every action.
- `generate_pillar_example.py` — emits the "full example" pillar. Not part of `generate_all.py`;
  the committed `docs/tutorials/pillars/full_example.sls*` is stale (75 modules). Its default
  output path (`examples/pillars/`) does not exist here, so always pass `--output`.
- `generate_api_docs.py` — debug dump, stdout by default. Do not commit its output.

## API reference — live discovery (not a generated dump)

`docs/API.md` is hand-written. The source of truth is `utils/controllers.json` meta
(26.7.3, 76 modules, 1815 actions). Live discovery is always accurate for the target firmware:

```bash
salt -C 'T@opnsense:fw-01' opnsense.list_api_modules
salt -C 'T@opnsense:fw-01' opnsense.list_api_controllers unbound
salt -C 'T@opnsense:fw-01' opnsense.list_api_actions unbound settings
```

## Verifying imports

```bash
PYTHONPATH=src python3 tools/verify_import.py
```

## Boundary guards (CI hard-fails)

```bash
python tools/check_public_boundary.py   # private strings (lab nets, monorepo paths, legacy IDs)
python tools/check_fixture_boundary.py  # RFC1918/private data in recorded fixtures
```

`check_version_guard_ci.py` is a CI-only helper: it asserts `__virtual__` rejects Salt < 3008 and
therefore needs an old Salt installed. Do not run it in a normal dev environment.
