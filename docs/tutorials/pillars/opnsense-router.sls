proxy:
  proxytype: opnsense
  host: opnsense.example.com
  proto: https
  verify_ssl: false
  api_key: {{ salt['vault.read_secret']('secret/opnsense/api_key')['value'] }}
  api_secret: {{ salt['vault.read_secret']('secret/opnsense/api_secret')['value'] }}
  timeout: 30

opnsense:
  host: opnsense.example.com
  proto: https
  verify_ssl: false
  api_key: {{ salt['vault.read_secret']('secret/opnsense/api_key')['value'] }}
  api_secret: {{ salt['vault.read_secret']('secret/opnsense/api_secret')['value'] }}
