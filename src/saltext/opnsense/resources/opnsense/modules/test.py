"""
test module override for opnsense resource type.

Provides test.ping -> delegates to connection module ping() via __resource_funcs__.
Per resources tutorial, salt -C 'T@opnsense' test.ping should return per-resource True.
"""


def ping(**kwargs):
    # strip internal kwargs via common if needed – test.ping usually has none
    return __resource_funcs__["opnsense.ping"]()  # type: ignore[name-defined]
