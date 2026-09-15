import datetime
import os
import tempfile
from pathlib import Path

import nox

# Nox options — align with salt-extension-copier template
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_missing_interpreters = False
try:
    from importlib import metadata as importlib_metadata

    if tuple(map(int, importlib_metadata.version("nox").split("."))) >= (2024, 3):
        nox.options.default_venv_backend = "uv|virtualenv"
except Exception:
    pass

PYTHON_VERSIONS = ("3.10", "3.11", "3.12", "3.13", "3.14")
CI_RUN = (
    os.environ.get("JENKINS_URL") or os.environ.get("CI") or os.environ.get("DRONE") is not None
)
PIP_INSTALL_SILENT = CI_RUN is False
SKIP_REQUIREMENTS_INSTALL = os.environ.get("SKIP_REQUIREMENTS_INSTALL", "0") == "1"

COVERAGE_REQUIREMENT = os.environ.get("COVERAGE_REQUIREMENT") or "coverage==7.16.0"
SALT_REQUIREMENT = os.environ.get("SALT_REQUIREMENT") or "salt>=3008"
if SALT_REQUIREMENT == "salt==master":
    SALT_REQUIREMENT = "git+https://github.com/saltstack/salt.git@master"

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

REPO_ROOT = Path(__file__).resolve().parent
ARTIFACTS_DIR = REPO_ROOT / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
CUR_TIME = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
COVERAGE_REPORT_DB = REPO_ROOT / ".coverage"
JUNIT_REPORT = ARTIFACTS_DIR / "junit-report.xml"


def _install_requirements(
    session, install_coverage=True, install_salt=True, install_source=False, extras=None
):
    extras = extras or []
    from nox.virtualenv import VirtualEnv

    no_progress = "--progress-bar=off"
    if isinstance(session._runner.venv, VirtualEnv) and session._runner.venv.venv_backend == "uv":
        no_progress = "--no-progress"

    if SKIP_REQUIREMENTS_INSTALL:
        return

    session.install(no_progress, "wheel", silent=PIP_INSTALL_SILENT)

    if install_coverage:
        session.install(no_progress, COVERAGE_REQUIREMENT, silent=PIP_INSTALL_SILENT)

    if install_salt:
        with tempfile.NamedTemporaryFile(delete=False) as constraints_file:
            constraints_file.write(b"setuptools<75.6.0")
        env = {"PIP_CONSTRAINT": constraints_file.name}
        try:
            session.install(no_progress, SALT_REQUIREMENT, silent=PIP_INSTALL_SILENT, env=env)
        finally:
            os.unlink(constraints_file.name)

    if extras:
        pkg = f".[{','.join(extras)}]"
        if install_source:
            session.install("-e", pkg, silent=PIP_INSTALL_SILENT)
        else:
            session.install(pkg, silent=PIP_INSTALL_SILENT)
    elif install_source:
        session.install("-e", ".", silent=PIP_INSTALL_SILENT)


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    _install_requirements(session, install_source=True, extras=["tests"])
    session.run("pytest", "tests/unit", "-v", *session.posargs)


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "src", "tests", "tools")
    session.run("ruff", "format", "--check", "src", "tests", "tools")


@nox.session
def gen_all(session):
    """
    Full codegen pipeline: spec -> models -> wrappers -> verify
    Usage:
      nox -s gen_all
      nox -s gen_all -- --core-ref 25.7 --plugins-ref 25.7
    Requires salt>=3008 — Resources only.
    """
    session.install("requests")
    session.run("python", "tools/generate_all.py", *session.posargs)


@nox.session(name="lint-code", python="3")
def lint_code(session):
    _install_requirements(session, install_salt=False, install_coverage=False, extras=["lint"])
    session.run("pylint", "--disable=I", "setup.py", "noxfile.py", "src/")


@nox.session(name="lint-tests", python="3")
def lint_tests(session):
    _install_requirements(
        session, install_salt=False, install_coverage=False, extras=["lint", "tests"]
    )
    session.run(
        "pylint",
        "--disable=I,redefined-outer-name,no-member,missing-module-docstring,missing-function-docstring,missing-class-docstring,attribute-defined-outside-init,inconsistent-return-statements,too-few-public-methods,too-many-public-methods",
        "tests/",
    )
