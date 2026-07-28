try:
    from saltext.opnsense.version._version import __version__
except ImportError:
    try:
        from importlib.metadata import PackageNotFoundError, version

        __version__ = version("saltext-opnsense")
    except PackageNotFoundError:
        __version__ = "0.0.0.dev+unknown"

