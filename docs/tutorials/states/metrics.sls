# Example: OPNsense Prometheus metrics via node_exporter textfile collector
# Example state pattern for Salt users
#
# Chef analogy: Ohai plugin writes version + alias count fact, then template resource writes prom file
# Puppet analogy: Facter fact + file resource with epp template
# Salt delight: grains already live from API, file.managed Jinja writes prom file directly
#
# Usage:
#   salt opnsense-router state.apply opnsense.metrics
#   salt opnsense-router grains.get opnsense_unbound_alias_count
#   salt opnsense-router opnsense.ping
#   cat /var/lib/node_exporter/textfile_collector/opnsense.prom
#   curl localhost:9100/metrics | grep opnsense_
#
# For k8s Alloy: prometheus.scrape node_exporter already picks up textfile. See docs/METRICS.md

{% set version = salt['grains.get']('opnsense_version', 'unknown') %}
{% set alias_count = salt['grains.get']('opnsense_unbound_alias_count', 0) %}
{% set bind_count = salt['grains.get']('opnsense_bind_domain_count', 0) %}
{% set host = salt['grains.get']('opnsense_host', grains.get('id', 'opnsense-router')) %}
{% set ping_ok = salt['opnsense.ping']() if 'opnsense.ping' in salt else False %}

{% set desired = salt['pillar.get']('opnsense:aliases', {}) %}
{% set purge = salt['pillar.get']('opnsense:purge_aliases', {}) %}
{% set ns = namespace(d=0, p=0) %}
{% for dom, hosts in desired.items() %}{% set ns.d = ns.d + (hosts|length) %}{% endfor %}
{% for dom, hosts in purge.items() %}{% set ns.p = ns.p + (hosts|length) %}{% endfor %}

opnsense_textfile_dir:
  file.directory:
    - name: /var/lib/node_exporter/textfile_collector
    - mode: '0755'
    - makedirs: True

opnsense_prom:
  file.managed:
    - name: /var/lib/node_exporter/textfile_collector/opnsense.prom
    - mode: '0644'
    - contents: |
        # HELP opnsense_up API reachability
        # TYPE opnsense_up gauge
        opnsense_up {{ 1 if ping_ok else 0 }}
        # HELP opnsense_unbound_alias_count live aliases
        # TYPE opnsense_unbound_alias_count gauge
        opnsense_unbound_alias_count {{ alias_count }}
        # HELP opnsense_bind_domain_count bind domains
        # TYPE opnsense_bind_domain_count gauge
        opnsense_bind_domain_count {{ bind_count }}
        # HELP opnsense_version_info version info
        # TYPE opnsense_version_info gauge
        opnsense_version_info{version="{{ version }}",host="{{ host }}"} 1
        # HELP opnsense_alias_desired_count desired from pillar
        # TYPE opnsense_alias_desired_count gauge
        opnsense_alias_desired_count {{ ns.d }}
        # HELP opnsense_alias_purge_count purge count
        # TYPE opnsense_alias_purge_count gauge
        opnsense_alias_purge_count {{ ns.p }}
    - require:
      - file: opnsense_textfile_dir

# Optional: verify metrics work
verify_metrics:
  cmd.run:
    - name: cat /var/lib/node_exporter/textfile_collector/opnsense.prom && echo "--- metrics ok"
    - onchanges:
      - file: opnsense_prom

# Optional: preview current delightful aliases alongside metrics
preview_aliases:
  module.run:
    - opnsense_dns.managed_preview:
    - onchanges:
      - file: opnsense_prom
