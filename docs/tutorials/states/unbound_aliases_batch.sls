# Better way: batch present with single reconfigure — avoids 50x reconfigure calls
# Human-key auto-resolution: host field as dict auto-resolves to parent UUID

{% set parent = pillar.get('opnsense', {}).get('cluster_parent', {}) %}
{% set parent_host = {'hostname': parent.get('hostname', 'cluster'), 'domain': parent.get('domain', 'example.com')} %}
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
    'host': {'hostname': parent_host.hostname, 'domain': parent_host.domain},
    'hostname': hostname,
    'domain': domain,
    'description': 'managed by salt - ' ~ hostname ~ '.' ~ domain ~ ' parent auto-resolved'
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
