import os

import pytest

try:
    import salt.config  # noqa

    HAS_SALT = True
except ImportError:
    HAS_SALT = False


@pytest.fixture
def minion_opts(tmp_path):  # pragma: no cover
    if not HAS_SALT:
        pytest.skip("salt not installed")
    import salt.config

    root_dir = tmp_path / "minion"
    opts = salt.config.DEFAULT_MINION_OPTS.copy()
    opts["__role"] = "minion"
    opts["root_dir"] = str(root_dir)
    for name in ("cachedir", "pki_dir", "sock_dir", "conf_dir"):
        dirpath = root_dir / name
        dirpath.mkdir(parents=True)
        opts[name] = str(dirpath)
    opts["log_file"] = "logs/minion.log"
    opts["conf_file"] = os.path.join(opts["conf_dir"], "minion")
    return opts
