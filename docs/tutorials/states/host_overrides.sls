{% set overrides = pillar.get('opnsense', {}).get('host_overrides_direct', []) %}

{% for ov in overrides %}
unbound_host_override_{{ ov.hostname }}_{{ ov.domain }}:
  opnsense.item_present:
    - name: {{ ov.hostname }}.{{ ov.domain }}
    - module: unbound
    - controller: settings
    - type: host_override
    - match:
        hostname: {{ ov.hostname }}
        domain: {{ ov.domain }}
    - data:
        enabled: "1"
        hostname: {{ ov.hostname }}
        domain: {{ ov.domain }}
        description: {{ ov.description | default("managed by salt") }}
        server: {{ ov.ip }}
    - reconfigure: unbound/service/reconfigure

{% endfor %}
