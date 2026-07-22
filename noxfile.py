import nox

@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session):
    session.install(".[dev]" if False else ".")
    session.install("pytest", "pytest-salt-factories", "requests", "salt>=3008")
    session.run("pytest", "tests/unit", "-v")


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "src", "tests", "tools")
