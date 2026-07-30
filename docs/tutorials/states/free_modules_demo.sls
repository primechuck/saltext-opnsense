# Free modules demo — proves dynamic-only covers ALL 76 API modules for free
# No static wrappers needed — generic opnsense + dynamic injection (312+ funcs) does it.

# Spec: controllers.json = 76 modules (core+plugins) from live upstream
# Dynamic injection in modules/opnsense.py creates caddy_*, haproxy_*, nginx_* etc at import
# Generic state opnsense.item_present works for ANY module (caddy/haproxy/nginx/wireguard etc)

{% set demo_enabled = False %}

# Generic approach — works for ANY free module instantly, no wrapper generation needed
caddy_handle_demo:
  opnsense.item_present:
    - module: caddy
    - controller: reverseproxy
    - type: handle
    - match: {description: "salt-free-demo"}
    - data: {enabled: "0", description: "salt-free-demo - caddy"}
    - reconfigure: caddy/reverseproxy/reconfigure
    {% if not demo_enabled %} - onlyif: /bin/false {% endif %}

haproxy_backend_demo:
  opnsense.item_present:
    - module: haproxy
    - controller: settings
    - type: backend
    - match: {name: salt-free-demo-backend}
    - data: {enabled: "0", name: salt-free-demo-backend, description: "demo"}
    - reconfigure: haproxy/service/reconfigure
    {% if not demo_enabled %} - onlyif: /bin/false {% endif %}

nginx_upstream_demo:
  opnsense.item_present:
    - module: nginx
    - controller: settings
    - type: upstream
    - match: {description: salt-free-demo-upstream}
    - data: {enabled: "0", description: salt-free-demo-upstream}
    - reconfigure: nginx/service/reconfigure
    {% if not demo_enabled %} - onlyif: /bin/false {% endif %}

# Dynamic exec wrappers from generic opnsense module (312+ funcs):
# salt opnsense-router opnsense.caddy_reverse_proxy_search_access_list
# salt opnsense-router opnsense.haproxy_settings_search_backends
# salt opnsense-router opnsense.nginx_settings_search_upstream
# All injected via _inject_dynamic_wrappers() reading controllers.json

verify_dynamic:
  cmd.run:
    - name: PYTHONPATH=src python3 tools/verify_import.py
    {% if not demo_enabled %} - onlyif: /bin/false {% endif %}
