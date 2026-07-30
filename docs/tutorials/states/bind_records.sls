{% set zone = pillar.get('opnsense', {}).get('bind_zone', {}) %}
{% set zone_name = zone.get('name', 'example.com') %}
{% set zone_uuid = zone.get('uuid', zone_name) %}
{% set records = zone.get('records', []) %}

bind_zone_present_{{ zone_name }}:
  opnsense.item_present:
    - name: {{ zone_name }}
    - module: bind
    - controller: domain
    - type: primary_domain
    - match:
        domainname: {{ zone_name }}
    - data:
        enabled: "1"
        type: primary
        domainname: {{ zone_name }}
    - reconfigure: bind/service/reconfigure

{% for rec in records %}
bind_record_{{ rec.name }}_{{ rec.type }}:
  opnsense.item_present:
    - name: {{ rec.name }}.{{ rec.type }}={{ rec.value }}
    - module: bind
    - controller: record
    - type: record
    - match:
        name: {{ rec.name }}
        type: {{ rec.type }}
        value: {{ rec.value }}
    - data:
        enabled: "1"
        # New: domain can be zone name "example.com" → auto-resolved to primary_domain UUID
        domain: {{ zone_uuid }}
        name: {{ rec.name }}
        type: {{ rec.type }}
        value: {{ rec.value }}
    - reconfigure: bind/service/reconfigure
    - require:
      - opnsense: bind_zone_present_{{ zone_name }}

{% endfor %}
