# Example Kea DHCPv4 reservations via saltext-opnsense
# Human-key auto-resolution: subnet can be CIDR like "10.0.60.0/24" → auto-resolved to UUID
# Pillar structure expected under opnsense:kea:reservations and opnsense:kea:subnets
# Model ref: src/opnsense/mvc/app/models/OPNsense/Kea/KeaDhcpv4.xml

{% set kea = pillar.get('opnsense', {}).get('kea', {}) %}
{% set subnets = kea.get('subnets', []) %}
{% set reservations = kea.get('reservations', []) %}

# Ensure subnets exist first
{% for sn in subnets %}
kea_subnet_{{ sn.subnet | replace('/', '_') }}:
  opnsense.item_present:
    - name: subnet-{{ sn.subnet }}
    - module: kea
    - controller: dhcpv4
    - type: subnet
    - match:
        subnet: {{ sn.subnet }}
    - data:
        subnet: {{ sn.subnet }}
        description: {{ sn.description | default("managed by salt") }}
        pools: {{ sn.pools | default('') }}
    - reconfigure: kea/service/reconfigure

{% endfor %}

# Create reservations (IP reservations) — subnet CIDR auto-resolves
{% for res in reservations %}
kea_reservation_{{ res.hostname }}_{{ res.ip_address | replace('.', '_') }}:
  opnsense.item_present:
    - name: {{ res.hostname }}-{{ res.ip_address }}
    - module: kea
    - controller: dhcpv4
    - type: reservation
    - match:
        hw_address: {{ res.hw_address }}
        ip_address: {{ res.ip_address }}
    - data:
        # New: subnet can be CIDR "10.0.60.0/24" → auto-resolved to UUID via search
        subnet: {{ res.subnet }}
        ip_address: {{ res.ip_address }}
        hw_address: {{ res.hw_address }}
        hostname: {{ res.hostname }}
        description: {{ res.description | default("managed by salt - " + res.hostname) }}
        {% if res.client_id is defined %}
        client_id: {{ res.client_id }}
        {% endif %}
        {% if res.next_server is defined %}
        next_server: {{ res.next_server }}
        {% endif %}
    - reconfigure: kea/service/reconfigure
    {% if subnets %}
    - require:
      {% for sn in subnets %}
      - opnsense: kea_subnet_{{ sn.subnet | replace('/', '_') }}
      {% endfor %}
    {% endif %}

{% endfor %}

# Example static list without pillar (hardcoded for lab) — now with human keys

#kea_subnet_10_0_60_0_24:
#  opnsense.item_present:
#    - name: mgmt-subnet
#    - module: kea
#    - controller: dhcpv4
#    - type: subnet
#    - match:
#        subnet: 10.0.60.0/24
#    - data:
#        subnet: 10.0.60.0/24
#        description: "mgmt net - salt managed"
#    - reconfigure: kea/service/reconfigure

#www_reservation:
#  opnsense.item_present:
#    - name: www-10.0.60.30
#    - module: kea
#    - controller: dhcpv4
#    - type: reservation
#    - match:
#        hw_address: "02:42:ac:11:00:02"
#        ip_address: "10.0.60.30"
#    - data:
#        # New: subnet as CIDR auto-resolves — no need to manually lookup UUID
#        subnet: "10.0.60.0/24"
#        ip_address: "10.0.60.30"
#        hw_address: "02:42:ac:11:00:02"
#        hostname: "www"
#        description: "www - infra svc - human key demo"
#    - reconfigure: kea/service/reconfigure

# Purge example:
#purge_old_reservation:
#  opnsense.item_absent:
#    - name: old-host
#    - module: kea
#    - controller: dhcpv4
#    - type: reservation
#    - match:
#        hostname: old-host
#    - reconfigure: kea/service/reconfigure
