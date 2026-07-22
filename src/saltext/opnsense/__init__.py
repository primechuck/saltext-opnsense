try:
    from saltext.opnsense.version._version import __version__
except Exception:
    __version__ = "0.0.0.dev"

__all__ = ["__version__"]
