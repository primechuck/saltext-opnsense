# Delightful examples — replaces Jinja loops
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

# After — single-alias (human parent, auto-inferred reconfigure)

www_dev:
  opnsense_unbound.alias_present:
    - parent: cluster.example.com
    - domain: example.com
    - description: "www dashboard"
    - enabled: true
    # reconfigure auto-inferred to unbound/service/reconfigure

# Batch — one state, one reconfigure, no Jinja

example_dns_batch:
  opnsense_unbound.aliases_managed:
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

# Even more delightful — completely pillar-driven, no args

dns_auto:
  opnsense_dns.managed:
    - name: dns
    # reads parent, aliases, purge from pillar:
    # opnsense:
    #   cluster_parent: {hostname: cluster, domain: example.com}
    #   aliases: {example.com: [www, git], internal.example.com: [code]}

# Bind examples

example_zone:
  opnsense_bind.domain_present:
    - name: example.com
    - description: "example.com primary"
    - reconfigure: true

www_bind_record:
  opnsense_bind.record_present:
    - name: www
    - domain: example.com
    - type: A
    - value: 172.18.60.30
    - reconfigure: true
