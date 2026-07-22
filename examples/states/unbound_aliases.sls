{% set parent_uuid = pillar.get('opnsense', {}).get('cluster_parent', {}).get('uuid', 'PARENT_UUID') %}
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
        host: {{ parent_uuid }}
        hostname: {{ hostname }}
        domain: {{ domain }}
        description: "managed by salt - {{ hostname }}.{{ domain }}"
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
