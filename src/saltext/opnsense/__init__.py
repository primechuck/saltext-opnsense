try:
    from saltext.opnsense.version._version import __version__  # type: ignore
except (ImportError, ModuleNotFoundError, FileNotFoundError):
    __version__ = "0.0.0.dev"

__all__ = ["__version__"]
