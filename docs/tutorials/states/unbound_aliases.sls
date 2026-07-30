{# Human-key auto-resolution example — host can be dict or "hostname.domain" #}
{% set parent = pillar.get('opnsense', {}).get('cluster_parent', {}) %}
{% set parent_host = {'hostname': parent.get('hostname', 'cluster'), 'domain': parent.get('domain', 'example.com')} %}
{% set parent_uuid_fallback = parent.get('uuid', 'PARENT_UUID') %}
{% set aliases = pillar.get('opnsense', {}).get('aliases', {}) %}

{% for domain, hosts in aliases.items() %}
{% for hostname in hosts %}
unbound_alias_{{ domain }}_{{ hostname }}:
  opnsense.item_present:
    - name: {{ hostname }}.{{ domain }}
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: {{ hostname }}
        domain: {{ domain }}
    - data:
        enabled: "1"
        {# New: human key dict auto-resolves to parent host_override UUID #}
        {# Supports both dict and string "cluster.example.com" #}
        host:
          hostname: {{ parent_host.hostname }}
          domain: {{ parent_host.domain }}
        hostname: {{ hostname }}
        domain: {{ domain }}
        description: "managed by salt - {{ hostname }}.{{ domain }} - parent auto-resolved"
    - reconfigure: unbound/service/reconfigure

{% endfor %}
{% endfor %}

{% set purge = pillar.get('opnsense', {}).get('purge_aliases', {}) %}
{% for domain, hosts in purge.items() %}
{% for hostname in hosts %}
purge_unbound_alias_{{ domain }}_{{ hostname }}:
  opnsense.item_absent:
    - name: {{ hostname }}.{{ domain }}
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: {{ hostname }}
        domain: {{ domain }}
    - reconfigure: unbound/service/reconfigure

{% endfor %}
{% endfor %}
