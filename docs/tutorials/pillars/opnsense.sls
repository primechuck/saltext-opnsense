opnsense:
  host: opnsense.example.com
  proto: https
  verify_ssl: false
  api_key: {{ pillar.get('opnsense_api_key') or 'REPLACE_ME' }}
  api_secret: {{ pillar.get('opnsense_api_secret') or 'REPLACE_ME' }}
  timeout: 30

  # Human-key auto-resolution (new in feat/saltext-opnsense):
  # - unbound host_alias host can be dict {hostname, domain} or "hostname.domain" → auto-resolved to host_override UUID
  # - kea reservation subnet can be CIDR like "192.0.2.0/24" (TEST-NET-1 RFC5737) → auto-resolved to subnet UUID
  # - acme certificate account, validationMethod, restartActions can be names → auto-resolved to UUIDs
  # - bind record domain can be zone name "example.com" → auto-resolved to primary_domain UUID

  cluster_parent:
    hostname: cluster
    domain: example.com
    # legacy uuid field still supported but optional; new way is to use dict in state data:
    # host: {hostname: cluster, domain: example.com} or "cluster.example.com"
    # uuid: REPLACE_WITH_REAL_UUID_FROM_searchHostOverride  # optional fallback

  aliases:
    example.com:
      - git
      - www
      - auth
      - admin
      - media
      - stream
      - s3
      - fs
    internal.example.com:
      - code
      - ide
      - ai
      - auth
      - admin

  host_overrides_direct:
    - hostname: server1
      domain: internal.example.com
      ip: 192.0.2.181
      description: "App node direct IP (TEST-NET-1)"
    - hostname: server2
      domain: internal.example.com
      ip: 192.0.2.180
      description: "Server2 (TEST-NET-1)"

  bind_zone:
    name: example.com
    # uuid optional — state can auto-resolve domain name to UUID for records
    uuid: ""  # leave empty to use name-based resolution
    records:
      - {name: ns1, type: A, value: 192.0.2.10}
      - {name: www, type: A, value: 192.0.2.11}

  # Kea DHCPv4 - subnets and reservations — human keys auto-resolved
  kea:
    subnets:
      - subnet: 192.0.2.0/24
        description: "mgmt vlan60 - salt managed (TEST-NET-1)"
        pools: ""
      - subnet: 198.51.100.0/24
        description: "iot vlan50 - salt (TEST-NET-2)"
    reservations:
      - hostname: www
        ip_address: 192.0.2.30
        hw_address: "02:42:ac:11:00:02"
        subnet: 192.0.2.0/24
        description: "www infra — subnet CIDR auto-resolves to UUID"
      - hostname: server1
        ip_address: 192.0.2.10
        hw_address: "aa:bb:cc:dd:ee:01"
        subnet: 192.0.2.0/24
        description: "Server1 - dhcp reservation with human key"

  # ACME client — human names auto-resolved to UUIDs
  acmeclient:
    accounts:
      - name: letsencrypt-prod
        description: "LE prod - salt managed"
        email: admin@example.com
        ca: letsencrypt
      - name: letsencrypt-staging
        description: "LE staging - salt"
        email: admin@example.com
        ca: letsencrypt_test

    validations:
      - name: cf-dns01
        description: "Cloudflare DNS-01 - salt"
        method: dns01
        dns_service: dns_cf
        dns_sleep: "20"
        dns_cf_token: "REPLACE_WITH_VAULT_SECRET"

    actions:
      - name: restart-haproxy
        description: "Restart HAProxy after renew"
        type: haproxy

    certificates:
      - name: "*.example.com"
        description: "wildcard example.com - salt"
        altNames: "example.com,*.internal.example.com"
        account: letsencrypt-prod
        validationMethod: cf-dns01
        keyLength: key_4096
        autoRenewal: "1"
        renewInterval: "60"
        aliasmode: none
        restartActions: restart-haproxy
