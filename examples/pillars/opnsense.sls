opnsense:
  host: jrbob.bierce.org
  proto: https
  verify_ssl: false
  api_key: {{ pillar.get('opnsense_api_key') or 'REPLACE_ME' }}
  api_secret: {{ pillar.get('opnsense_api_secret') or 'REPLACE_ME' }}
  timeout: 30

  cluster_parent:
    hostname: cluster
    domain: bierce.org
    uuid: REPLACE_WITH_REAL_UUID_FROM_searchHostOverride

  aliases:
    bierce.org:
      - forgejo
      - grafana
      - authentik
      - argocd
      - jellyfin
      - plex
      - s3
      - seaweedfs
    internal.bierce.org:
      - opencode
      - vscode
      - llms
      - auth
      - argocd

  host_overrides_direct:
    - hostname: hal
      domain: internal.bierce.org
      ip: 172.18.4.181
      description: "LLM node direct IP"
    - hostname: fry
      domain: internal.bierce.org
      ip: 172.18.4.180
      description: "Storage hub"

  bind_zone:
    name: bierce.org
    uuid: REPLACE_WITH_ZONE_UUID
    records:
      - {name: pihole, type: A, value: 172.18.4.10}
      - {name: traefik, type: A, value: 172.18.4.175}

  # Kea DHCPv4 - subnets and reservations
  kea:
    subnets:
      - subnet: 172.18.60.0/24
        description: "mgmt vlan60 - salt managed"
        pools: ""  # optional: leave empty for auto, or define pools CSV
      - subnet: 172.18.50.0/24
        description: "iot vlan50 - salt"
    reservations:
      - hostname: grafana
        ip_address: 172.18.60.30
        hw_address: "02:42:ac:11:00:02"
        subnet: 172.18.60.0/24
        subnet_uuid: "REPLACE_WITH_UUID_AFTER_searchSubnet"
        description: "grafana infra"
      - hostname: hal
        ip_address: 172.18.60.10
        hw_address: "aa:bb:cc:dd:ee:01"
        subnet: 172.18.60.0/24
        subnet_uuid: "REPLACE_WITH_UUID"
        description: "LLM node hal - dhcp reservation"

  # ACME client - accounts, validations, actions, certificates
  acmeclient:
    accounts:
      - name: letsencrypt-prod
        description: "LE prod - salt managed"
        email: admin@bierce.org
        ca: letsencrypt
      - name: letsencrypt-staging
        description: "LE staging - salt"
        email: admin@bierce.org
        ca: letsencrypt_test

    validations:
      - name: cf-dns01
        description: "Cloudflare DNS-01 - salt"
        method: dns01
        dns_service: dns_cf
        dns_sleep: "20"
        dns_cf_token: "REPLACE_WITH_VAULT_SECRET"
        # dns_cf_email optional for token+email combos

    actions:
      - name: restart-haproxy
        description: "Restart HAProxy after renew"
        type: haproxy

    certificates:
      - name: "*.bierce.org"
        description: "wildcard bierce.org - salt"
        altNames: "bierce.org,*.internal.bierce.org"
        account: "REPLACE_WITH_ACCOUNT_UUID_OR_NAME"
        account_uuid: "UUID_OF_letsencrypt-prod"
        validationMethod: "UUID_OF_cf-dns01"
        validation_uuid: "UUID_OF_cf-dns01"
        keyLength: key_4096
        autoRenewal: "1"
        renewInterval: "60"
        aliasmode: none
        # restartActions: UUID_OF_restart-haproxy (comma separated if multiple)
