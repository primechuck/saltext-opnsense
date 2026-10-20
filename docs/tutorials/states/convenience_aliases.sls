# Convenience examples — replaces Jinja loops
# High-level wrappers hide module/controller/type/match + UUID hunting
# Before (clunky, 2-3x copy-paste, UUID hunting):
# {% for domain, hosts in pillar.get('opnsense', {}).get('aliases', {}).items() %}
# {% for hostname in hosts %}
# unbound_alias_{{ domain }}_{{ hostname }}:
#   opnsense.item_present:
#     - module: unbound
#     - controller: settings
#     - type: host_alias
#     - match: {hostname: {{ hostname }}, domain: {{ domain }}}
#     - data:
#         enabled: "1"
#         host: {{ pillar['opnsense']['cluster_parent']['uuid'] }}
#         hostname: {{ hostname }}
#         domain: {{ domain }}
#         description: "managed by salt"
#     - reconfigure: unbound/service/reconfigure
# {% endfor %}
# {% endfor %}

# After — single-alias (human parent auto-resolved, auto-inferred reconfigure)

www_dev:
  opnsense.item_present:
    - module: unbound
    - controller: settings
    - type: host_alias
    - match:
        hostname: www
        domain: example.com
    - data:
        enabled: "1"
        host: cluster.example.com
        hostname: www
        domain: example.com
        description: "www dashboard"
    # reconfigure auto-inferred to unbound/service/reconfigure

# Batch — one state, one reconfigure, no Jinja

example_dns_batch:
  opnsense_dns.managed:
    - parent: cluster.example.com
    - aliases:
        example.com:
          - www
          - git
          - auth
          - admin
          - media
        internal.example.com:
          - code
          - ide
          - ai
    - purge:
        example.com:
          - old-git
          - old-service
    - reconfigure: true

# Pillar-direct — zero Jinja, reads opnsense:aliases from pillar

dns_from_pillar:
  opnsense_dns.managed:
    - name: dns
    - parent: cluster.example.com
    # aliases/purge omitted → auto-read from pillar opnsense:aliases

# Even more convenient — completely pillar-driven, no args

dns_auto:
  opnsense_dns.managed:
    - name: dns
    # reads parent, aliases, purge from pillar:
    # opnsense:
    #   cluster_parent: {hostname: cluster, domain: example.com}
    #   aliases: {example.com: [www, git], internal.example.com: [code]}

# Bind examples (human domain auto-resolved to zone UUID)

example_zone:
  opnsense.item_present:
    - module: bind
    - controller: domain
    - type: primary_domain
    - match:
        domainname: example.com
    - data:
        enabled: "1"
        domainname: example.com
        description: "example.com primary"

www_bind_record:
  opnsense.item_present:
    - module: bind
    - controller: record
    - type: record
    - match:
        domain: example.com
        name: www
        type: A
    - data:
        enabled: "1"
        domain: example.com
        name: www
        type: A
        value: 192.0.2.30
