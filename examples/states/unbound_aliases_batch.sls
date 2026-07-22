# Better way: batch present with single reconfigure — avoids 50x reconfigure calls
# This is the recommended pattern for ALIASES lists (replaces query.sh loop efficiently)

{% set parent_uuid = pillar.get('opnsense', {}).get('cluster_parent', {}).get('uuid', 'PARENT_UUID') %}
{% set aliases = pillar.get('opnsense', {}).get('aliases', {}) %}
{% set purge = pillar.get('opnsense', {}).get('purge_aliases', {}) %}

# Build flat list for batch state
{% set alias_items = [] %}
{% for domain, hosts in aliases.items() %}
{% for hostname in hosts %}
{% set _ = alias_items.append({
  'name': hostname ~ '.' ~ domain,
  'data': {
    'enabled': '1',
    'host': parent_uuid,
    'hostname': hostname,
    'domain': domain,
    'description': 'managed by salt - ' ~ hostname ~ '.' ~ domain
  },
 'match': {'hostname': hostname, 'domain': domain}
}) %}
{% endfor %}
{% endfor %}

{% if alias_items %}
unbound_aliases_batch:
  opnsense.items_present:
    - name: ensure unbound host aliases
    - module: unbound
    - controller: settings
    - type: host_alias
    - items: {{ alias_items | json }}
    - reconfigure: unbound/service/reconfigure
{% endif %}

{% set purge_items = [] %}
{% for domain, hosts in purge.items() %}
{% for hostname in hosts %}
{% set _ = purge_items.append({
  'name': hostname ~ '.' ~ domain,
  'match': {'hostname': hostname, 'domain': domain}
}) %}
{% endfor %}
{% endfor %}

{% if purge_items %}
unbound_aliases_purge_batch:
  opnsense.items_absent:
    - name: purge old aliases
    - module: unbound
    - controller: settings
    - type: host_alias
    - items: {{ purge_items | json }}
    - reconfigure: unbound/service/reconfigure
{% endif %}
