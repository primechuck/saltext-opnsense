# Deprecated shim – use convenience_aliases.sls – will be removed in 0.2.0
# Keeps backward compat for `state.apply opnsense.aliases_delightful`
# New canonical file: convenience_aliases.sls

include:
  - {{ slspath }}.convenience_aliases
