# Pillar Reference

All pillar keys under `opnsense:` are optional. Uses RFC5737 TEST-NET IPs (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`) per RFC 5737, RFC2606 `example.com`.

## Minimal connection

```yaml
# /srv/pillar/opnsense.sls or /etc/salt/proxy (flat)
proxy:
  proxytype: opnsense
  host: opnsense.example.com
  proto: https
  verify_ssl: true
  api_key: REPLACE_ME
  api_secret: REPLACE_ME
  timeout: 30
```

Vault variant:

```yaml
proxy:
  proxytype: opnsense
  host: opnsense.example.com
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
  api_secret: __slot__:salt:vault.read(secret/opnsense/api_secret)
```

## DNS convenience (pillar-driven, zero Jinja)

```yaml
opnsense:
  cluster_parent:
    hostname: cluster
    domain: example.com
  aliases:
    example.com:
      - www
      - git
      - auth
    internal.example.com:
      - code
      - ide
  purge_aliases:
    example.com:
      - old-www
      - legacy-app
  descriptions:
    www.example.com: "Primary Web Ingress"
```

Used by `opnsense_dns.managed` — reads automatically if args omitted.

## Firewall

```yaml
opnsense:
  firewall:
    aliases:
      - name: app_nodes
        type: host
        content: "192.0.2.10,192.0.2.11"
        description: "app nodes TEST-NET-1"
      - name: rfc5737
        type: network
        content: "192.0.2.0/24,198.51.100.0/24,203.0.113.0/24"
        description: "TEST-NET nets"
```

## Kea DHCP

```yaml
opnsense:
  kea:
    subnets:
      - subnet: "192.0.2.0/24"
        description: "mgmt - TEST-NET-1"
    reservations:
      - hostname: "www"
        hw_address: "aa:bb:cc:dd:ee:ff"
        ip_address: "192.0.2.10"
        subnet: "192.0.2.0/24"
```

`subnet` human CIDR auto-resolves to UUID via `searchSubnet`.

## BIND

```yaml
opnsense:
  bind:
    zones:
      - name: example.com
        records:
          - {name: www, type: A, value: 192.0.2.10}
```

## ACME

```yaml
opnsense:
  acmeclient:
    accounts:
      - name: "letsencrypt-prod"
        email: "admin@example.com"
        ca: "letsencrypt"
    certificates:
      - name: "*.example.com"
        description: "Wildcard"
```

## Full example

See `docs/tutorials/pillars/full_example.sls` — auto-generated for all 75 modules, uses `example.com` + TEST-NET only. Also `pillar.example` at repo root.
