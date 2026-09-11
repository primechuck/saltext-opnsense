# pylint: disable=missing-module-docstring
import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent

try:
    from saltext.opnsense.version._version import __version__  # type: ignore
except (ImportError, ModuleNotFoundError, FileNotFoundError):  # pragma: no cover
    __version__ = "0.0.0.not-installed"
    try:
        from importlib.metadata import version, PackageNotFoundError

        try:
            __version__ = version("saltext-opnsense")
        except PackageNotFoundError:
            pass
    except ImportError:
        try:
            from pkg_resources import get_distribution, DistributionNotFound

            try:
                __version__ = get_distribution("saltext-opnsense").version
            except DistributionNotFound:
                pass
        except ImportError:
            pass

__all__ = ["__version__"]
