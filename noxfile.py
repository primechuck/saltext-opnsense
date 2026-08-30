import nox


@nox.session(python=["3.10", "3.11", "3.12", "3.13", "3.14"])
def tests(session):
    session.install(".[dev]")
    session.install("pytest", "pytest-salt-factories", "requests", "salt>=3008")
    session.run("pytest", "tests/unit", "-v")


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "src", "tests", "tools")


@nox.session
def gen_all(session):
    """
    Full codegen pipeline: spec -> models -> wrappers -> verify -> tests

    Usage:
      nox -s gen_all
      nox -s gen_all -- --core-ref 25.7 --plugins-ref 25.7
      nox -s gen_all -- --skip-sync --skip-live
      nox -s gen_all -- --only wrappers
    """
    session.install("requests")
    session.run("python", "tools/generate_all.py", *session.posargs)
