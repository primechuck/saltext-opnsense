{% set zone_uuid = pillar.get('opnsense', {}).get('bind_zone', {}).get('uuid', 'ZONE_UUID') %}
{% set zone_name = pillar.get('opnsense', {}).get('bind_zone', {}).get('name', 'bierce.org') %}
{% set records = pillar.get('opnsense', {}).get('bind_zone', {}).get('records', []) %}

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
        domain: {{ zone_uuid }}
        name: {{ rec.name }}
        type: {{ rec.type }}
        value: {{ rec.value }}
    - reconfigure: bind/service/reconfigure
    - require:
      - opnsense: bind_zone_present_{{ zone_name }}

{% endfor %}
