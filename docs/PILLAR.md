# Pillar Reference (Salt 3008+ Resources)

Requires salt>=3008. No proxy.

All pillar keys under opnsense: optional CMDB. Connection under resources:opnsense:hosts fleet or opnsense:{host} direct. Uses RFC5737 TEST-NET + example.com.

## Resources connection fleet required

```yaml
# /srv/pillar/resources.sls
resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
        proto: https
        verify_ssl: true
        api_key: REPLACE_ME
        api_secret: REPLACE_ME
        timeout: 30
```

Only supported format. Requires salt>=3008. No flat /etc/salt/proxy, no proxy dict, no proxytype. See RESOURCES.md.

Vault:

```yaml
resources:
  opnsense:
    hosts:
      fw-01:
        host: fw-01.example.com
        api_key: __slot__:salt:vault.read(secret/opnsense/fw-01/api_key)
        api_secret: __slot__:salt:vault.read(secret/opnsense/fw-01/api_secret)
```

## Direct single-host masterless testing

```yaml
opnsense:
  host: fw-01.example.com
  api_key: REPLACE_ME
  api_secret: REPLACE_ME
```

Resolution: Resources wins, else direct opnsense:{host}, else pillar itself as host config.

## DNS convenience pillar-driven zero Jinja

```yaml
opnsense:
  cluster_parent: {hostname: cluster, domain: example.com}
  aliases:
    example.com: [www, git, auth]
  purge_aliases:
    example.com: [old-www]
```

Used by opnsense_dns.managed.

## Firewall, Kea, BIND, ACME examples see QUICKSTART and full_example.sls

No proxy-era pillar proxy or flat file — removed 1.0.0. Requires salt>=3008.
