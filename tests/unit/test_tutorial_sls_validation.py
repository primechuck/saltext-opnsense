"""
test_tutorial_sls_validation.py — smoke test that tutorial SLS examples are valid YAML+Jinja.

This satisfies CI acceptance: clearly fails if SLS is invalid, and gives confidence
package isn't broken beyond just Python import.

Uses tools.validate_tutorials.render_sls to avoid reimplementing logic.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

# Import render_sls robustly — tools/ is not in src/ and pytest pythonpath=[src] only
# Review #9:15 flagged fragile import that relies on repo root being on sys.path.
# Fix: try direct import, fallback to importlib.util loader from tools/validate_tutorials.py


def _load_render_sls():
    try:
        from tools.validate_tutorials import render_sls as _render

        return _render
    except ModuleNotFoundError:
        # Fallback: load via file path
        tools_path = pathlib.Path(__file__).resolve().parents[2] / "tools" / "validate_tutorials.py"
        spec = importlib.util.spec_from_file_location("validate_tutorials", tools_path)
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            sys.modules["validate_tutorials"] = mod
            spec.loader.exec_module(mod)
            return mod.render_sls
        raise


render_sls = _load_render_sls()

STATES_DIR = pathlib.Path(__file__).resolve().parents[2] / "docs" / "tutorials" / "states"


def _all_sls_files():
    return sorted(STATES_DIR.glob("*.sls"))


@pytest.mark.parametrize("sls_path", _all_sls_files(), ids=lambda p: p.name)
def test_tutorial_sls_renders_valid_yaml(sls_path):
    ok, err_or_rendered, parsed = render_sls(sls_path, strict=False)
    assert ok, f"SLS {sls_path.name} failed validation: {err_or_rendered}"
    # Parsed should be dict or empty
    assert isinstance(parsed, (dict, list)) or parsed == {}, (
        f"Unexpected parsed type for {sls_path.name}: {type(parsed)}"
    )


def test_at_least_some_tutorial_sls_present():
    sls_files = _all_sls_files()
    # We expect 10 tutorial SLS as of 2026-09-15
    assert len(sls_files) >= 5, f"Expected >=5 SLS, got {len(sls_files)}: {sls_files}"
    # Spot-check known ones
    names = {p.name for p in sls_files}
    for expected in ["unbound_aliases.sls", "acme_certificates.sls", "free_modules_demo.sls"]:
        assert expected in names, f"Expected tutorial {expected} missing, have {names}"


def test_invalid_sls_would_fail():
    """
    Sanity check: ensure our validator would fail on deliberately broken YAML.
    Creates a temp file, validates, expects failure.
    """
    import tempfile

    broken_content = """
    this is not: valid: yaml: [:
      - broken
        - indentation: wrong
          - also: [unclosed
    """

    with tempfile.NamedTemporaryFile(suffix=".sls", mode="w", delete=False) as tf:
        tf.write(broken_content)
        tf_path = pathlib.Path(tf.name)

    try:
        ok, err, _ = render_sls(tf_path, strict=False)
        assert not ok, f"Validator should have failed on broken YAML but got OK: {err}"
        assert "YAML" in err or "parse" in err.lower()
    finally:
        tf_path.unlink(missing_ok=True)
