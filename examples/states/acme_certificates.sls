# Example ACME client management via saltext-opnsense
# Model ref: security/acme-client - AcmeClient.xml
# Docs: https://docs.opnsense.org/development/api/plugins/acmeclient.html
# Controllers: accounts, validations, certificates, actions, settings, service

{% set acme = pillar.get('opnsense', {}).get('acmeclient', {}) %}
{% set accounts = acme.get('accounts', []) %}
{% set validations = acme.get('validations', []) %}
{% set certificates = acme.get('certificates', []) %}
{% set actions_list = acme.get('actions', []) %}

# 1. Ensure accounts (Let's Encrypt etc)
{% for acc in accounts %}
acme_account_{{ acc.name }}:
  opnsense.item_present:
    - name: {{ acc.name }}
    - module: acmeclient
    - controller: accounts
    - type: account
    - match:
        name: {{ acc.name }}
    - data:
        enabled: "1"
        name: {{ acc.name }}
        description: {{ acc.description | default("managed by salt") }}
        email: {{ acc.email }}
        ca: {{ acc.ca | default("letsencrypt") }}
        # optional: custom_ca, eab_kid, eab_hmac
        {% if acc.custom_ca is defined %}
        custom_ca: {{ acc.custom_ca }}
        {% endif %}
    - reconfigure: acmeclient/service/reconfigure

{% endfor %}

# 2. Validations (DNS-01, HTTP-01, etc)
{% for val in validations %}
acme_validation_{{ val.name }}:
  opnsense.item_present:
    - name: {{ val.name }}
    - module: acmeclient
    - controller: validations
    - type: validation
    - match:
        name: {{ val.name }}
    - data:
        enabled: "1"
        name: {{ val.name }}
        description: {{ val.description | default("salt managed") }}
        method: {{ val.method | default("dns01") }}
        # DNS-01 example
        {% if val.method == "dns01" %}
        dns_service: {{ val.dns_service | default("dns_cf") }}
        dns_sleep: {{ val.dns_sleep | default("10") }}
        # Cloudflare example - store secrets via vault/encrypted pillar!
        {% if val.dns_cf_token is defined %}
        dns_cf_token: {{ val.dns_cf_token }}
        {% endif %}
        {% if val.dns_cf_email is defined %}
        dns_cf_email: {{ val.dns_cf_email }}
        {% endif %}
        {% endif %}
        {% if val.method == "http01" %}
        http_service: {{ val.http_service | default("opnsense") }}
        {% endif %}
    - reconfigure: acmeclient/service/reconfigure

{% endfor %}

# 3. Actions / automations (restart HAProxy, etc)
{% for act in actions_list %}
acme_action_{{ act.name }}:
  opnsense.item_present:
    - name: {{ act.name }}
    - module: acmeclient
    - controller: actions
    - type: action
    - match:
        name: {{ act.name }}
    - data:
        enabled: "1"
        name: {{ act.name }}
        description: {{ act.description | default("managed by salt") }}
        type: {{ act.type | default("reconfigure") }}
        # type can be: configd, custom, haproxy, etc – see UI
        {% if act.command is defined %}
        command: {{ act.command }}
        {% endif %}
    - reconfigure: acmeclient/service/reconfigure

{% endfor %}

# 4. Certificates
{% for cert in certificates %}
acme_certificate_{{ cert.name | replace('.', '_') | replace('*', 'wildcard') }}:
  opnsense.item_present:
    - name: {{ cert.name }}
    - module: acmeclient
    - controller: certificates
    - type: certificate
    - match:
        name: {{ cert.name }}
    - data:
        enabled: "1"
        name: {{ cert.name }}
        description: {{ cert.description | default("managed by salt - " + cert.name) }}
        # altNames CSV - comma separated
        altNames: {{ cert.altNames | default('') }}
        # account and validationMethod expect UUIDs of previously created items
        # Salt workflow: first create account+validation, then lookup UUID via search
        # Workaround: allow pillar to provide UUID directly, or name lookup via Jinja in orchestration
        account: {{ cert.account_uuid | default(cert.account) }}
        validationMethod: {{ cert.validation_uuid | default(cert.validationMethod) }}
        keyLength: {{ cert.keyLength | default("key_4096") }}
        ocsp: "{{ cert.ocsp | default("0") }}"
        autoRenewal: "{{ cert.autoRenewal | default("1") }}"
        renewInterval: "{{ cert.renewInterval | default("60") }}"
        {% if cert.restartActions is defined %}
        restartActions: {{ cert.restartActions }}
        {% endif %}
        aliasmode: {{ cert.aliasmode | default("none") }}
    - reconfigure: acmeclient/service/reconfigure
    {% if accounts or validations %}
    - require:
      {% for acc in accounts %}
      - opnsense: acme_account_{{ acc.name }}
      {% endfor %}
      {% for val in validations %}
      - opnsense: acme_validation_{{ val.name }}
      {% endfor %}
    {% endif %}

{% endfor %}

# Hardcoded lab example (no pillar) - Let's Encrypt prod + Cloudflare DNS-01 for *.bierce.org

#acme_account_letsencrypt_prod:
#  opnsense.item_present:
#    - name: letsencrypt-prod
#    - module: acmeclient
#    - controller: accounts
#    - type: account
#    - match:
#        name: letsencrypt-prod
#    - data:
#        enabled: "1"
#        name: letsencrypt-prod
#        description: "LE prod - salt"
#        email: "admin@bierce.org"
#        ca: "letsencrypt"
#    - reconfigure: acmeclient/service/reconfigure

#acme_validation_cf_dns01:
#  opnsense.item_present:
#    - name: cf-dns01
#    - module: acmeclient
#    - controller: validations
#    - type: validation
#    - match:
#        name: cf-dns01
#    - data:
#        enabled: "1"
#        name: cf-dns01
#        description: "Cloudflare DNS-01 - salt"
#        method: "dns01"
#        dns_service: "dns_cf"
#        dns_sleep: "20"
#        dns_cf_token: "__vault_cf_token__"
#    - reconfigure: acmeclient/service/reconfigure

#acme_action_restart_haproxy:
#  opnsense.item_present:
#    - name: restart-haproxy
#    - module: acmeclient
#    - controller: actions
#    - type: action
#    - match:
#        name: restart-haproxy
#    - data:
#        enabled: "1"
#        name: restart-haproxy
#        description: "Restart HAProxy on renew"
#        type: "haproxy"
#    - reconfigure: acmeclient/service/reconfigure

#acme_cert_wildcard_bierce_org:
#  opnsense.item_present:
#    - name: "*.bierce.org"
#    - module: acmeclient
#    - controller: certificates
#    - type: certificate
#    - match:
#        name: "*.bierce.org"
#    - data:
#        enabled: "1"
#        name: "*.bierce.org"
#        description: "wildcard bierce.org - salt managed"
#        altNames: "bierce.org"
#        # Resolve these UUIDs via:
#        # salt jrbob opnsense.search acmeclient accounts account search_phrase=letsencrypt-prod
#        # salt jrbob opnsense.search acmeclient validations validation search_phrase=cf-dns01
#        account: "ACCOUNT_UUID"
#        validationMethod: "VALIDATION_UUID"
#        keyLength: "key_4096"
#        autoRenewal: "1"
#        renewInterval: "60"
#        restartActions: "ACTION_UUID"
#        aliasmode: "none"
#    - reconfigure: acmeclient/service/reconfigure

# Trigger sign / renew (exec module, not state)
# Use after cert definition:
# salt jrbob opnsense.call acmeclient certificates sign <uuid>
# salt jrbob opnsense.call acmeclient service signallcerts

# Settings singleton (optional)
#acme_settings:
#  opnsense.item_present:
#    - name: acme_settings
#    - module: acmeclient
#    - controller: settings
#    - type: settings
#    - match:
#        description: acme_settings
#    - data:
#        enabled: "1"
#        autoRenewal: "1"
#        environment: "prod"
#        challengePort: "43580"
#    - reconfigure: acmeclient/service/reconfigure
