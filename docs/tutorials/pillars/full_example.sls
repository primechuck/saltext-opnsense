# Full boring example pillar for ALL 75 OPNsense modules — auto-generated
# Uses example.com per RFC 2606
# Spec: 75 modules, 249 controllers, 1736 actions
{
  "opnsense": {
    "host": "opnsense.example.com",
    "proto": "https",
    "verify_ssl": false,
    "api_key": "REPLACE_ME",
    "api_secret": "REPLACE_ME",
    "timeout": 30,
    "cluster_parent": {
      "hostname": "cluster",
      "domain": "example.com"
    },
    "aliases": {
      "example.com": [
        "www",
        "mail",
        "ftp"
      ],
      "internal.example.com": [
        "code",
        "api"
      ]
    },
    "purge_aliases": {
      "example.com": [
        "old-www"
      ]
    },
    "firewall": {
      "aliases": [
        {
          "name": "app_nodes",
          "type": "host",
          "content": "192.0.2.10,192.0.2.11",
          "description": "app nodes (TEST-NET-1 RFC5737)"
        },
        {
          "name": "rfc5737",
          "type": "network",
          "content": "192.0.2.0/24,198.51.100.0/24,203.0.113.0/24",
          "description": "TEST-NET RFC5737 example nets"
        }
      ],
      "filter_rules": [
        {
          "description": "allow app api",
          "action": "pass",
          "interface": "lan",
          "source": "app_nodes",
          "destination_port": "6443"
        }
      ]
    },
    "wireguard": {
      "clients": [
        {
          "name": "laptop",
          "pubkey": "PUBKEY=",
          "allowedips": "198.51.100.2/32",
          "endpoint": "vpn.example.com:51820"
        }
      ]
    },
    "interfaces": {
      "vlans": [
        {
          "description": "mgmt vlan60",
          "vlan": 60,
          "parent": "igc1"
        }
      ],
      "vips": [
        {
          "description": "carp lan",
          "mode": "carp",
          "interface": "lan",
          "subnet": "192.0.2.1/24"
        }
      ]
    },
    "kea": {
      "subnets": [
        {
          "subnet": "192.0.2.0/24",
          "description": "lan (TEST-NET-1)"
        }
      ],
      "reservations": [
        {
          "hostname": "www",
          "hw_address": "aa:bb:cc:dd:ee:ff",
          "ip_address": "192.0.2.10",
          "subnet": "192.0.2.0/24"
        }
      ]
    },
    "acmeclient": {
      "accounts": [
        {
          "name": "letsencrypt-prod",
          "email": "admin@example.com",
          "ca": "letsencrypt"
        }
      ],
      "certificates": [
        {
          "name": "*.example.com",
          "description": "wildcard"
        }
      ]
    },
    "apcupsd": {
      "example": {
        "description": "salt managed apcupsd example",
        "enabled": "1"
      }
    },
    "auth": {
      "example": {
        "description": "salt managed auth example",
        "enabled": "1"
      }
    },
    "bind": {
      "example": {
        "description": "salt managed bind example",
        "enabled": "1"
      }
    },
    "caddy": {
      "example": {
        "description": "salt managed caddy example",
        "enabled": "1"
      }
    },
    "captiveportal": {
      "example": {
        "description": "salt managed captiveportal example",
        "enabled": "1"
      }
    },
    "chrony": {
      "example": {
        "description": "salt managed chrony example",
        "enabled": "1"
      }
    },
    "cicap": {
      "example": {
        "description": "salt managed cicap example",
        "enabled": "1"
      }
    },
    "clamav": {
      "example": {
        "description": "salt managed clamav example",
        "enabled": "1"
      }
    },
    "collectd": {
      "example": {
        "description": "salt managed collectd example",
        "enabled": "1"
      }
    },
    "core": {
      "example": {
        "description": "salt managed core example",
        "enabled": "1"
      }
    },
    "cron": {
      "example": {
        "description": "salt managed cron example",
        "enabled": "1"
      }
    },
    "crowdsec": {
      "example": {
        "description": "salt managed crowdsec example",
        "enabled": "1"
      }
    },
    "dechw": {
      "example": {
        "description": "salt managed dechw example",
        "enabled": "1"
      }
    },
    "dhcpv4": {
      "example": {
        "description": "salt managed dhcpv4 example",
        "enabled": "1"
      }
    },
    "dhcpv6": {
      "example": {
        "description": "salt managed dhcpv6 example",
        "enabled": "1"
      }
    },
    "dhcrelay": {
      "example": {
        "description": "salt managed dhcrelay example",
        "enabled": "1"
      }
    },
    "diagnostics": {
      "example": {
        "description": "salt managed diagnostics example",
        "enabled": "1"
      }
    },
    "dmidecode": {
      "example": {
        "description": "salt managed dmidecode example",
        "enabled": "1"
      }
    },
    "dnscryptproxy": {
      "example": {
        "description": "salt managed dnscryptproxy example",
        "enabled": "1"
      }
    },
    "dnsmasq": {
      "example": {
        "description": "salt managed dnsmasq example",
        "enabled": "1"
      }
    },
    "dyndns": {
      "example": {
        "description": "salt managed dyndns example",
        "enabled": "1"
      }
    },
    "freeradius": {
      "example": {
        "description": "salt managed freeradius example",
        "enabled": "1"
      }
    },
    "ftpproxy": {
      "example": {
        "description": "salt managed ftpproxy example",
        "enabled": "1"
      }
    },
    "gridexample": {
      "example": {
        "description": "salt managed gridexample example",
        "enabled": "1"
      }
    },
    "haproxy": {
      "example": {
        "description": "salt managed haproxy example",
        "enabled": "1"
      }
    },
    "helloworld": {
      "example": {
        "description": "salt managed helloworld example",
        "enabled": "1"
      }
    },
    "hostdiscovery": {
      "example": {
        "description": "salt managed hostdiscovery example",
        "enabled": "1"
      }
    },
    "hwprobe": {
      "example": {
        "description": "salt managed hwprobe example",
        "enabled": "1"
      }
    },
    "ids": {
      "example": {
        "description": "salt managed ids example",
        "enabled": "1"
      }
    },
    "iperf": {
      "example": {
        "description": "salt managed iperf example",
        "enabled": "1"
      }
    },
    "ipsec": {
      "example": {
        "description": "salt managed ipsec example",
        "enabled": "1"
      }
    },
    "lldpd": {
      "example": {
        "description": "salt managed lldpd example",
        "enabled": "1"
      }
    },
    "monit": {
      "example": {
        "description": "salt managed monit example",
        "enabled": "1"
      }
    },
    "ndpproxy": {
      "example": {
        "description": "salt managed ndpproxy example",
        "enabled": "1"
      }
    },
    "netbird": {
      "example": {
        "description": "salt managed netbird example",
        "enabled": "1"
      }
    },
    "netsnmp": {
      "example": {
        "description": "salt managed netsnmp example",
        "enabled": "1"
      }
    },
    "nginx": {
      "example": {
        "description": "salt managed nginx example",
        "enabled": "1"
      }
    },
    "nrpe": {
      "example": {
        "description": "salt managed nrpe example",
        "enabled": "1"
      }
    },
    "ntopng": {
      "example": {
        "description": "salt managed ntopng example",
        "enabled": "1"
      }
    },
    "ntpd": {
      "example": {
        "description": "salt managed ntpd example",
        "enabled": "1"
      }
    },
    "nut": {
      "example": {
        "description": "salt managed nut example",
        "enabled": "1"
      }
    },
    "openvpn": {
      "example": {
        "description": "salt managed openvpn example",
        "enabled": "1"
      }
    },
    "postfix": {
      "example": {
        "description": "salt managed postfix example",
        "enabled": "1"
      }
    },
    "proxy": {
      "example": {
        "description": "salt managed proxy example",
        "enabled": "1"
      }
    },
    "proxysso": {
      "example": {
        "description": "salt managed proxysso example",
        "enabled": "1"
      }
    },
    "qfeeds": {
      "example": {
        "description": "salt managed qfeeds example",
        "enabled": "1"
      }
    },
    "quagga": {
      "example": {
        "description": "salt managed quagga example",
        "enabled": "1"
      }
    },
    "radsecproxy": {
      "example": {
        "description": "salt managed radsecproxy example",
        "enabled": "1"
      }
    },
    "redis": {
      "example": {
        "description": "salt managed redis example",
        "enabled": "1"
      }
    },
    "relayd": {
      "example": {
        "description": "salt managed relayd example",
        "enabled": "1"
      }
    },
    "routes": {
      "example": {
        "description": "salt managed routes example",
        "enabled": "1"
      }
    },
    "routing": {
      "example": {
        "description": "salt managed routing example",
        "enabled": "1"
      }
    },
    "siproxd": {
      "example": {
        "description": "salt managed siproxd example",
        "enabled": "1"
      }
    },
    "smart": {
      "example": {
        "description": "salt managed smart example",
        "enabled": "1"
      }
    },
    "sslh": {
      "example": {
        "description": "salt managed sslh example",
        "enabled": "1"
      }
    },
    "stunnel": {
      "example": {
        "description": "salt managed stunnel example",
        "enabled": "1"
      }
    },
    "syslog": {
      "example": {
        "description": "salt managed syslog example",
        "enabled": "1"
      }
    },
    "tailscale": {
      "example": {
        "description": "salt managed tailscale example",
        "enabled": "1"
      }
    },
    "tayga": {
      "example": {
        "description": "salt managed tayga example",
        "enabled": "1"
      }
    },
    "telegraf": {
      "example": {
        "description": "salt managed telegraf example",
        "enabled": "1"
      }
    },
    "tinc": {
      "example": {
        "description": "salt managed tinc example",
        "enabled": "1"
      }
    },
    "tor": {
      "example": {
        "description": "salt managed tor example",
        "enabled": "1"
      }
    },
    "trafficshaper": {
      "example": {
        "description": "salt managed trafficshaper example",
        "enabled": "1"
      }
    },
    "trust": {
      "example": {
        "description": "salt managed trust example",
        "enabled": "1"
      }
    },
    "udpbroadcastrelay": {
      "example": {
        "description": "salt managed udpbroadcastrelay example",
        "enabled": "1"
      }
    },
    "unbound": {
      "example": {
        "description": "salt managed unbound example",
        "enabled": "1"
      }
    },
    "vnstat": {
      "example": {
        "description": "salt managed vnstat example",
        "enabled": "1"
      }
    },
    "wol": {
      "example": {
        "description": "salt managed wol example",
        "enabled": "1"
      }
    },
    "zabbixagent": {
      "example": {
        "description": "salt managed zabbixagent example",
        "enabled": "1"
      }
    },
    "zerotier": {
      "example": {
        "description": "salt managed zerotier example",
        "enabled": "1"
      }
    }
  }
}
