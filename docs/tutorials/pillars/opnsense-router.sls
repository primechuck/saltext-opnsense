proxy:
  proxytype: opnsense
  host: opnsense.example.com
  proto: https
  verify_ssl: false
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
  api_secret: __slot__:salt:vault.read(secret/opnsense/api_secret)
  timeout: 30

opnsense:
  host: opnsense.example.com
  proto: https
  verify_ssl: false
  api_key: __slot__:salt:vault.read(secret/opnsense/api_key)
  api_secret: __slot__:salt:vault.read(secret/opnsense/api_secret)
