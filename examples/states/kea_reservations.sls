# Example Kea DHCPv4 reservations via saltext-opnsense
# Requires: kea dhcpv4 enabled, subnets pre-created, then reservations linked by subnet uuid
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
        # optional: pools, allocator, etc.
        pools: {{ sn.pools | default('') }}
    - reconfigure: kea/service/reconfigure

{% endfor %}

# Create reservations (IP reservations)
{% for res in reservations %}
# Example res:
#  {subnet_cidr: "172.18.60.0/24", hw_address: "aa:bb:cc:dd:ee:ff", ip_address: "172.18.60.50", hostname: "grafana"}
kea_reservation_{{ res.hostname }}_{{ res.ip_address | replace('.', '_') }}:
  opnsense.item_present:
    - name: {{ res.hostname }}-{{ res.ip_address }}
    - module: kea
    - controller: dhcpv4
    - type: reservation
    - match:
        # match needs uniqueness across subnet + hw_address or ip
        # searchReservation returns rows with hw_address, ip_address, subnet, hostname
        hw_address: {{ res.hw_address }}
        ip_address: {{ res.ip_address }}
    - data:
        # reservation model fields - see KeaDhcpv4.xml
        # subnet expects UUID, but our state supports lookup by CIDR via match logic?
        # Workaround: pillar should provide subnet UUID once known. If only CIDR provided, use Jinja to look up.
        # For simplicity here we expect subnet uuid already resolved:
        # Option A: pillar provides subnet uuid directly
        subnet: {{ res.subnet_uuid | default(res.subnet) }}
        ip_address: {{ res.ip_address }}
        hw_address: {{ res.hw_address }}
        hostname: {{ res.hostname }}
        description: {{ res.description | default("managed by salt - " + res.hostname) }}
        # optional fields
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

# Example static list without pillar (hardcoded for lab):
# Uncomment to use direct values

#kea_subnet_172_18_60_0_24:
#  opnsense.item_present:
#    - name: mgmt-subnet
#    - module: kea
#    - controller: dhcpv4
#    - type: subnet
#    - match:
#        subnet: 172.18.60.0/24
#    - data:
#        subnet: 172.18.60.0/24
#        description: "mgmt net - salt managed"
#    - reconfigure: kea/service/reconfigure

#grafana_reservation:
#  opnsense.item_present:
#    - name: grafana-172.18.60.30
#    - module: kea
#    - controller: dhcpv4
#    - type: reservation
#    - match:
#        hw_address: "02:42:ac:11:00:02"
#        ip_address: "172.18.60.30"
#    - data:
#        # NOTE: subnet field must be the UUID of the subnet (obtain via searchSubnet)
#        # Example: after creating subnet, run:
#        # salt jrbob opnsense.search kea dhcpv4 subnet search_phrase=172.18.60.0/24
#        # and copy the uuid
#        subnet: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
#        ip_address: "172.18.60.30"
#        hw_address: "02:42:ac:11:00:02"
#        hostname: "grafana"
#        description: "grafana - infra svc"
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
