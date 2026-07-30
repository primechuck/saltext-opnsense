# API Reference — 75 modules, 1736 endpoints

> OPNsense 25.7.11 / plugins 25.7.11 — generated 2026-07-30T02:31:15.885812+00:00

All endpoints are accessible via generic `opnsense.call` and dynamic wrappers `opnsense.{module}_{controller}_{action}`.

```bash
salt opnsense-router opnsense.list_api_modules
salt opnsense-router opnsense.list_api_controllers unbound
salt opnsense-router opnsense.list_api_actions unbound settings
salt opnsense-router opnsense.search unbound settings host_alias row_count=1
```

## Quick lookup

| Module | Controllers | Actions | Example |
|---|---|---|---|
| acmeclient | 6 | 46 | `opnsense.call acmeclient accounts add` |
| apcupsd | 1 | 1 | `opnsense.call apcupsd service getUpsStatus` |
| auth | 3 | 19 | `opnsense.call auth group add` |
| bind | 5 | 27 | `opnsense.call bind acl addAcl` |
| caddy | 3 | 49 | `opnsense.call caddy diagnostics caddyfile` |
| captiveportal | 5 | 26 | `opnsense.call captiveportal access api` |
| chrony | 1 | 4 | `opnsense.call chrony service chronyauthdata` |
| cicap | 1 | 1 | `opnsense.call cicap service checkclamav` |
| clamav | 2 | 8 | `opnsense.call clamav service freshclam` |
| collectd | 2 | 7 | `opnsense.call collectd general get` |
| core | 12 | 73 | `opnsense.call core backup backups` |
| cron | 2 | 7 | `opnsense.call cron service reconfigure` |
| crowdsec | 12 | 13 | `opnsense.call crowdsec alerts search` |
| dechw | 1 | 1 | `opnsense.call dechw info powerStatus` |
| dhcpv4 | 1 | 2 | `opnsense.call dhcpv4 leases delLease` |
| dhcpv6 | 1 | 3 | `opnsense.call dhcpv6 leases delLease` |
| dhcrelay | 2 | 12 | `opnsense.call dhcrelay service reconfigure` |
| diagnostics | 17 | 85 | `opnsense.call diagnostics activity getActivity` |
| dmidecode | 1 | 1 | `opnsense.call dmidecode service get` |
| dnscryptproxy | 5 | 25 | `opnsense.call dnscryptproxy cloak addCloak` |
| dnsmasq | 2 | 35 | `opnsense.call dnsmasq leases search` |
| dyndns | 2 | 7 | `opnsense.call dyndns accounts addItem` |
| firewall | 10 | 70 | `opnsense.call firewall alias addItem` |
| freeradius | 10 | 71 | `opnsense.call freeradius avpair addAvpair` |
| ftpproxy | 2 | 12 | `opnsense.call ftpproxy service config` |
| gridexample | 2 | 7 | `opnsense.call gridexample service reconfigure` |
| haproxy | 5 | 102 | `opnsense.call haproxy export config` |
| helloworld | 1 | 2 | `opnsense.call helloworld service reload` |
| hostdiscovery | 1 | 1 | `opnsense.call hostdiscovery service search` |
| hwprobe | 1 | 1 | `opnsense.call hwprobe service report` |
| ids | 2 | 37 | `opnsense.call ids service dropAlertLog` |
| interfaces | 10 | 61 | `opnsense.call interfaces bridgesettings addItem` |
| iperf | 2 | 6 | `opnsense.call iperf instance query` |
| ipsec | 13 | 77 | `opnsense.call ipsec connections addChild` |
| kea | 4 | 43 | `opnsense.call kea ctrlagent get` |
| lldpd | 1 | 1 | `opnsense.call lldpd service neighbor` |
| monit | 3 | 21 | `opnsense.call monit service check` |
| ndpproxy | 1 | 5 | `opnsense.call ndpproxy general addAlias` |
| netbird | 3 | 5 | `opnsense.call netbird authentication down` |
| netsnmp | 1 | 6 | `opnsense.call netsnmp user addUser` |
| nginx | 4 | 118 | `opnsense.call nginx bans delban` |
| nrpe | 1 | 6 | `opnsense.call nrpe command addCommand` |
| ntopng | 1 | 1 | `opnsense.call ntopng service checkredis` |
| ntpd | 1 | 3 | `opnsense.call ntpd service gps` |
| nut | 1 | 1 | `opnsense.call nut diagnostics upsstatus` |
| openvpn | 4 | 31 | `opnsense.call openvpn clientoverwrites add` |
| postfix | 9 | 50 | `opnsense.call postfix address addAddress` |
| proxy | 4 | 46 | `opnsense.call proxy acl addCustomPolicy` |
| proxysso | 1 | 5 | `opnsense.call proxysso service createkeytab` |
| qfeeds | 1 | 4 | `opnsense.call qfeeds settings reconfigure` |
| quagga | 6 | 145 | `opnsense.call quagga bfd addNeighbor` |
| radsecproxy | 5 | 30 | `opnsense.call radsecproxy clients addItem` |
| redis | 1 | 1 | `opnsense.call redis service resetdb` |
| relayd | 3 | 10 | `opnsense.call relayd service configtest` |
| routes | 2 | 8 | `opnsense.call routes gateway status` |
| routing | 1 | 7 | `opnsense.call routing settings addGateway` |
| siproxd | 4 | 24 | `opnsense.call siproxd domain addDomain` |
| smart | 1 | 5 | `opnsense.call smart service abort` |
| sslh | 1 | 1 | `opnsense.call sslh settings index` |
| stunnel | 1 | 7 | `opnsense.call stunnel services addItem` |
| syslog | 2 | 8 | `opnsense.call syslog service reset` |
| tailscale | 2 | 9 | `opnsense.call tailscale settings addSubnet` |
| tayga | 1 | 6 | `opnsense.call tayga mapping addStaticmapping` |
| telegraf | 5 | 17 | `opnsense.call telegraf general get` |
| tinc | 2 | 14 | `opnsense.call tinc service reconfigure` |
| tor | 6 | 39 | `opnsense.call tor exitacl addacl` |
| trafficshaper | 2 | 21 | `opnsense.call trafficshaper service flushreload` |
| trust | 4 | 25 | `opnsense.call trust ca add` |
| udpbroadcastrelay | 2 | 12 | `opnsense.call udpbroadcastrelay service config` |
| unbound | 4 | 47 | `opnsense.call unbound diagnostics dumpcache` |
| vnstat | 1 | 5 | `opnsense.call vnstat service daily` |
| wireguard | 3 | 20 | `opnsense.call wireguard client addClient` |
| wol | 1 | 8 | `opnsense.call wol wol addHost` |
| zabbixagent | 1 | 12 | `opnsense.call zabbixagent settings addAlias` |
| zerotier | 2 | 10 | `opnsense.call zerotier network add` |

## Full listing

### acmeclient

- **accounts** (7): `add, del, get, register, search, toggle, update`
- **actions** (10): `add, del, get, search, sftpGetIdentity, sftpTestConnection, sshGetIdentity, sshTestConnection, toggle, update`
- **certificates** (11): `add, automation, del, get, import, removekey, revoke, search, sign, toggle, update`
- **service** (8): `configtest, reconfigure, reset, restart, signallcerts, start, status, stop`
- **settings** (4): `fetchCronIntegration, fetchHAProxyIntegration, getBindPluginStatus, getGcloudPluginStatus`
- **validations** (6): `add, del, get, search, toggle, update`

### apcupsd

- **service** (1): `getUpsStatus`

### auth

- **group** (5): `add, del, get, search, set`
- **priv** (3): `getItem, search, setItem`
- **user** (11): `add, addApiKey, del, delApiKey, download, get, newOtpSeed, search, searchApiKey, set, upload`

### bind

- **acl** (6): `addAcl, delAcl, getAcl, searchAcl, setAcl, toggleAcl`
- **domain** (12): `addForwardDomain, addPrimaryDomain, addSecondaryDomain, delDomain, getDomain, searchForwardDomain, searchMasterDomain, searchPrimaryDomain, searchSecondaryDomain, searchSlaveDomain, setDomain, toggleDomain`
- **general** (2): `zoneshow, zonetest`
- **record** (6): `addRecord, delRecord, getRecord, searchRecord, setRecord, toggleRecord`
- **service** (1): `dnsbl`

### caddy

- **diagnostics** (2): `caddyfile, config`
- **reverseproxy** (46): `addAccessList, addBasicAuth, addHandle, addHeader, addLayer4, addLayer4Openvpn, addReverseProxy, addSubdomain, delAccessList, delBasicAuth, delHandle, delHeader, delLayer4, delLayer4Openvpn, delReverseProxy` +31 more
- **service** (1): `validate`

### captiveportal

- **access** (4): `api, logoff, logon, status`
- **service** (4): `delTemplate, getTemplate, saveTemplate, searchTemplates`
- **session** (5): `connect, disconnect, list, search, zones`
- **settings** (6): `addZone, delZone, getZone, searchZones, setZone, toggleZone`
- **voucher** (7): `dropExpiredVouchers, dropVoucherGroup, expireVoucher, generateVouchers, listProviders, listVoucherGroups, listVouchers`

### chrony

- **service** (4): `chronyauthdata, chronysources, chronysourcestats, chronytracking`

### cicap

- **service** (1): `checkclamav`

### clamav

- **service** (2): `freshclam, version`
- **url** (6): `addUrl, delUrl, getUrl, searchUrl, setUrl, toggleUrl`

### collectd

- **general** (2): `get, set`
- **service** (5): `reconfigure, restart, start, status, stop`

### core

- **backup** (6): `backups, deleteBackup, diff, download, providers, revertBackup`
- **dashboard** (5): `getDashboard, picture, productInfoFeed, restoreDefaults, saveWidgets`
- **defaults** (4): `factoryDefaults, get, getInstalledSections, reset`
- **firmware** (26): `audit, changelog, check, cleanup, connection, details, getOptions, health, info, install, license, lock, log, poweroff, reboot` +11 more
- **hasync** (1): `reconfigure`
- **hasyncstatus** (6): `restart, restartAll, services, start, stop, version`
- **initialsetup** (1): `configure`
- **menu** (2): `search, tree`
- **service** (4): `restart, search, start, stop`
- **snapshots** (7): `activate, add, del, get, isSupported, search, set`
- **system** (4): `dismissStatus, halt, reboot, status`
- **tunables** (7): `addItem, delItem, getItem, reconfigure, reset, searchItem, setItem`

### cron

- **service** (1): `reconfigure`
- **settings** (6): `addJob, delJob, getJob, searchJobs, setJob, toggleJob`

### crowdsec

- **alerts** (1): `search`
- **appsecconfigs** (1): `search`
- **appsecrules** (1): `search`
- **bouncers** (1): `search`
- **collections** (1): `search`
- **decisions** (2): `del, search`
- **machines** (1): `search`
- **parsers** (1): `search`
- **postoverflows** (1): `search`
- **scenarios** (1): `search`
- **service** (1): `reconfigure`
- **version** (1): `get`

### dechw

- **info** (1): `powerStatus`

### dhcpv4

- **leases** (2): `delLease, searchLease`

### dhcpv6

- **leases** (3): `delLease, searchLease, searchPrefix`

### dhcrelay

- **service** (1): `reconfigure`
- **settings** (11): `addDest, addRelay, delDest, delRelay, getDest, getRelay, searchDest, searchRelay, setDest, setRelay, toggleRelay`

### diagnostics

- **activity** (1): `getActivity`
- **cpuusage** (2): `getCPUType, stream`
- **dns** (1): `reverseLookup`
- **dnsdiagnostics** (1): `set`
- **firewall** (13): `delState, flushSources, flushStates, killStates, listRuleIds, log, logFilters, pfStates, pfStatistics, queryPfTop, queryStates, stats, streamLog`
- **interface** (18): `CarpStatus, delRoute, flushArp, getArp, getBpfStatistics, getInterfaceConfig, getInterfaceNames, getInterfaceStatistics, getMemoryStatistics, getNdp, getNetisrStatistics, getPfsyncNodes, getProtocolStatistics, getRoutes, getSocketStatistics` +3 more
- **lvtemplate** (5): `addItem, delItem, getItem, searchItem, setItem`
- **netflow** (6): `cacheStats, getconfig, isEnabled, reconfigure, setconfig, status`
- **networkinsight** (7): `export, getInterfaces, getMetadata, getProtocols, getServices, timeserie, top`
- **packetcapture** (8): `download, macInfo, remove, searchJobs, set, start, stop, view`
- **ping** (5): `remove, searchJobs, set, start, stop`
- **portprobe** (1): `set`
- **proofpointet** (1): `status`
- **system** (8): `memory, systemDisk, systemInformation, systemMbuf, systemResources, systemSwap, systemTemperature, systemTime`
- **systemhealth** (4): `exportAsCSV, getInterfaces, getRrdList, getSystemHealth`
- **traceroute** (1): `set`
- **traffic** (3): `Interface, Top, stream`

### dmidecode

- **service** (1): `get`

### dnscryptproxy

- **cloak** (6): `addCloak, delCloak, getCloak, searchCloak, setCloak, toggleCloak`
- **forward** (6): `addForward, delForward, getForward, searchForward, setForward, toggleForward`
- **server** (6): `addServer, delServer, getServer, searchServer, setServer, toggleServer`
- **service** (1): `dnsbl`
- **whitelist** (6): `addWhitelist, delWhitelist, getWhitelist, searchWhitelist, setWhitelist, toggleWhitelist`

### dnsmasq

- **leases** (1): `search`
- **settings** (34): `addBoot, addDomain, addHost, addOption, addRange, addTag, delBoot, delDomain, delHost, delOption, delRange, delTag, downloadHosts, get, getBoot` +19 more

### dyndns

- **accounts** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`
- **settings** (1): `get`

### firewall

- **alias** (16): `addItem, delItem, export, getAliasUUID, getGeoIP, getItem, getTableSize, import, listCategories, listCountries, listNetworkAliases, listUserGroups, reconfigure, searchItem, setItem` +1 more
- **aliasutil** (7): `add, aliases, delete, findReferences, flush, list, updateBogons`
- **category** (5): `addItem, delItem, getItem, searchItem, setItem`
- **filter** (10): `addRule, delRule, flushInspectCache, getInterfaceList, getRule, moveRuleBefore, searchRule, setRule, toggleRule, toggleRuleLog`
- **filterbase** (7): `apply, cancelRollback, listCategories, listNetworkSelectOptions, listPortSelectOptions, revert, savepoint`
- **filterutil** (1): `ruleStats`
- **group** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`
- **npt** (6): `addRule, delRule, getRule, searchRule, setRule, toggleRule`
- **onetoone** (6): `addRule, delRule, getRule, searchRule, setRule, toggleRule`
- **sourcenat** (6): `addRule, delRule, getRule, searchRule, setRule, toggleRule`

### freeradius

- **avpair** (6): `addAvpair, delAvpair, getAvpair, searchAvpair, setAvpair, toggleAvpair`
- **client** (8): `addClient, delClient, get, getClient, searchClient, set, setClient, toggleClient`
- **dhcp** (6): `addDhcp, delDhcp, getDhcp, searchDhcp, setDhcp, toggleDhcp`
- **eap** (2): `get, set`
- **general** (2): `get, set`
- **ldapgroup** (8): `addLdapgroup, delLdapgroup, get, getLdapgroup, searchLdapgroup, set, setLdapgroup, toggleLdapgroup`
- **lease** (6): `addLease, delLease, getLease, searchLease, setLease, toggleLease`
- **proxy** (20): `addHomeserver, addHomeserverpool, addRealm, delHomeserver, delHomeserverpool, delRealm, get, getHomeserver, getHomeserverpool, getRealm, searchHomeserver, searchHomeserverpool, searchRealm, set, setHomeserver` +5 more
- **service** (5): `reconfigure, restart, start, status, stop`
- **user** (8): `addUser, delUser, get, getUser, searchUser, set, setUser, toggleUser`

### ftpproxy

- **service** (6): `config, reload, restart, start, status, stop`
- **settings** (6): `addProxy, delProxy, getProxy, searchProxy, setProxy, toggleProxy`

### gridexample

- **service** (1): `reconfigure`
- **settings** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`

### haproxy

- **export** (3): `config, diff, download`
- **maintenance** (11): `certActions, certDiff, certSync, certSyncBulk, fetchCronIntegration, searchCertificateDiff, searchServer, serverState, serverStateBulk, serverWeight, serverWeightBulk`
- **service** (1): `configtest`
- **settings** (84): `addAcl, addAction, addBackend, addCpu, addErrorfile, addFcgi, addFrontend, addGroup, addHealthcheck, addLua, addMapfile, addServer, addUser, addmailer, addresolver` +69 more
- **statistics** (3): `counters, info, tables`

### helloworld

- **service** (2): `reload, test`

### hostdiscovery

- **service** (1): `search`

### hwprobe

- **service** (1): `report`

### ids

- **service** (7): `dropAlertLog, getAlertInfo, getAlertLogs, queryAlerts, reconfigure, reloadRules, updateRules`
- **settings** (30): `addPolicy, addPolicyRule, addUserRule, checkPolicyRule, delPolicy, delPolicyRule, delUserRule, getPolicy, getPolicyRule, getRuleInfo, getRuleset, getRulesetproperties, getUserRule, listRuleMetadata, listRulesets` +15 more

### interfaces

- **bridgesettings** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`
- **gifsettings** (7): `addItem, delItem, getIfOptions, getItem, reconfigure, searchItem, setItem`
- **gresettings** (7): `addItem, delItem, getIfOptions, getItem, reconfigure, searchItem, setItem`
- **laggsettings** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`
- **loopbacksettings** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`
- **neighborsettings** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`
- **overview** (4): `export, getInterface, interfacesInfo, reloadInterface`
- **vipsettings** (7): `addItem, delItem, getItem, getUnusedVhid, reconfigure, searchItem, setItem`
- **vlansettings** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`
- **vxlansettings** (6): `addItem, delItem, getItem, reconfigure, searchItem, setItem`

### iperf

- **instance** (2): `query, set`
- **service** (4): `restart, start, status, stop`

### ipsec

- **connections** (28): `addChild, addConnection, addLocal, addRemote, connectionExists, delChild, delConnection, delLocal, delRemote, getChild, getConnection, getLocal, getRemote, isEnabled, searchChild` +13 more
- **keypairs** (6): `addItem, delItem, genKeyPair, getItem, searchItem, setItem`
- **leases** (2): `pools, search`
- **legacysubsystem** (2): `applyConfig, status`
- **manualspd** (6): `add, del, get, search, set, toggle`
- **pools** (6): `add, del, get, search, set, toggle`
- **presharedkeys** (5): `addItem, delItem, getItem, searchItem, setItem`
- **sad** (2): `delete, search`
- **sessions** (4): `connect, disconnect, searchPhase1, searchPhase2`
- **settings** (1): `get`
- **spd** (2): `delete, search`
- **tunnel** (7): `delPhase1, delPhase2, searchPhase1, searchPhase2, toggle, togglePhase1, togglePhase2`
- **vti** (6): `add, del, get, search, set, toggle`

### kea

- **ctrlagent** (1): `get`
- **dhcpv4** (18): `addPeer, addReservation, addSubnet, delPeer, delReservation, delSubnet, downloadReservations, get, getPeer, getReservation, getSubnet, searchPeer, searchReservation, searchSubnet, setPeer` +3 more
- **dhcpv6** (23): `addPdPool, addPeer, addReservation, addSubnet, delPdPool, delPeer, delReservation, delSubnet, downloadReservations, get, getPdPool, getPeer, getReservation, getSubnet, searchPdPool` +8 more
- **leases** (1): `search`

### lldpd

- **service** (1): `neighbor`

### monit

- **service** (2): `check, reconfigure`
- **settings** (18): `addAlert, addService, addTest, delAlert, delService, delTest, getAlert, getGeneral, getService, getTest, searchAlert, searchService, searchTest, setAlert, setService` +3 more
- **status** (1): `get`

### ndpproxy

- **general** (5): `addAlias, delAlias, getAlias, searchAlias, setAlias`

### netbird

- **authentication** (3): `down, get, up`
- **settings** (1): `sync`
- **status** (1): `status`

### netsnmp

- **user** (6): `addUser, delUser, getUser, searchUser, setUser, toggleUser`

### nginx

- **bans** (2): `delban, searchban`
- **logs** (5): `accesses, errors, streamaccesses, streamerrors, tlsHandshakes`
- **service** (3): `status, stop, vts`
- **settings** (108): `addcachePath, addcredential, addcustompolicy, adderrorpage, addhttprewrite, addhttpserver, addipacl, addlimitRequestConnection, addlimitZone, addlocation, addnaxsirule, addproxyCacheValid, addresolver, addsecurityHeader, addsnifwd` +93 more

### nrpe

- **command** (6): `addCommand, delCommand, getCommand, searchCommand, setCommand, toggleCommand`

### ntopng

- **service** (1): `checkredis`

### ntpd

- **service** (3): `gps, meta, status`

### nut

- **diagnostics** (1): `upsstatus`

### openvpn

- **clientoverwrites** (6): `add, del, get, search, set, toggle`
- **export** (6): `accounts, download, providers, storePresets, templates, validatePresets`
- **instances** (12): `add, addStaticKey, del, delStaticKey, genKey, get, getStaticKey, search, searchStaticKey, set, setStaticKey, toggle`
- **service** (7): `killSession, reconfigure, restartService, searchRoutes, searchSessions, startService, stopService`

### postfix

- **address** (6): `addAddress, delAddress, getAddress, searchAddress, setAddress, toggleAddress`
- **domain** (6): `addDomain, delDomain, getDomain, searchDomain, setDomain, toggleDomain`
- **headerchecks** (6): `addHeadercheck, delHeadercheck, getHeadercheck, searchHeaderchecks, setHeadercheck, toggleHeadercheck`
- **recipient** (6): `addRecipient, delRecipient, getRecipient, searchRecipient, setRecipient, toggleRecipient`
- **recipientbcc** (6): `addRecipientbcc, delRecipientbcc, getRecipientbcc, searchRecipientbcc, setRecipientbcc, toggleRecipientbcc`
- **sender** (6): `addSender, delSender, getSender, searchSender, setSender, toggleSender`
- **senderbcc** (6): `addSenderbcc, delSenderbcc, getSenderbcc, searchSenderbcc, setSenderbcc, toggleSenderbcc`
- **sendercanonical** (6): `addSendercanonical, delSendercanonical, getSendercanonical, searchSendercanonical, setSendercanonical, toggleSendercanonical`
- **service** (2): `checkrspamd, reconfigure`

### proxy

- **acl** (14): `addCustomPolicy, addPolicy, apply, delCustomPolicy, delPolicy, getCustomPolicy, getPolicy, searchCustomPolicy, searchPolicy, setCustomPolicy, setPolicy, test, toggleCustomPolicy, togglePolicy`
- **service** (6): `downloadacls, fetchacls, refreshTemplate, reset, restart, start`
- **settings** (23): `addPACRule, addPacMatch, addPacProxy, addRemoteBlacklist, delPacMatch, delPacProxy, delPacRule, delRemoteBlacklist, fetchRbCron, getPacMatch, getPacProxy, getPacRule, getRemoteBlacklist, searchPacMatch, searchPacProxy` +8 more
- **template** (3): `get, reset, set`

### proxysso

- **service** (5): `createkeytab, deletekeytab, getCheckList, showkeytab, testkerblogin`

### qfeeds

- **settings** (4): `reconfigure, searchEvents, searchFeeds, stats`

### quagga

- **bfd** (6): `addNeighbor, delNeighbor, getNeighbor, searchNeighbor, setNeighbor, toggleNeighbor`
- **bgp** (42): `addAspath, addCommunitylist, addNeighbor, addPeergroup, addPrefixlist, addRedistribution, addRoutemap, delAspath, delCommunitylist, delNeighbor, delPeergroup, delPrefixlist, delRedistribution, delRoutemap, getAspath` +27 more
- **diagnostics** (19): `bfdcounters, bfdneighbors, bfdsummary, bgpneighbors, bgpsummary, generalrunningconfig, ospfdatabase, ospfinterface, ospfoverview, ospfv3interface, ospfv3overview, searchBgproute4, searchBgproute6, searchGeneralroute4, searchGeneralroute6` +4 more
- **ospf6settings** (30): `addInterface, addNetwork, addPrefixlist, addRedistribution, addRoutemap, delInterface, delNetwork, delPrefixlist, delRedistribution, delRoutemap, getInterface, getNetwork, getPrefixlist, getRedistribution, getRoutemap` +15 more
- **ospfsettings** (42): `addArea, addInterface, addNeighbor, addNetwork, addPrefixlist, addRedistribution, addRoutemap, delArea, delInterface, delNeighbor, delNetwork, delPrefixlist, delRedistribution, delRoutemap, getArea` +27 more
- **static** (6): `addRoute, delRoute, getRoute, searchRoute, setRoute, toggleRoute`

### radsecproxy

- **clients** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`
- **realms** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`
- **rewrites** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`
- **servers** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`
- **tls** (6): `addItem, delItem, getItem, searchItem, setItem, toggleItem`

### redis

- **service** (1): `resetdb`

### relayd

- **service** (2): `configtest, reconfigure`
- **settings** (6): `del, dirty, get, search, set, toggle`
- **status** (2): `sum, toggle`

### routes

- **gateway** (1): `status`
- **routes** (7): `addroute, delroute, getroute, reconfigure, searchroute, setroute, toggleroute`

### routing

- **settings** (7): `addGateway, delGateway, getGateway, reconfigure, searchGateway, setGateway, toggleGateway`

### siproxd

- **domain** (8): `addDomain, delDomain, get, getDomain, searchDomain, set, setDomain, toggleDomain`
- **general** (2): `get, set`
- **service** (6): `reconfigure, restart, showregistrations, start, status, stop`
- **user** (8): `addUser, delUser, get, getUser, searchUser, set, setUser, toggleUser`

### smart

- **service** (5): `abort, info, list, logs, test`

### sslh

- **settings** (1): `index`

### stunnel

- **services** (7): `addItem, delItem, get, getItem, searchItem, setItem, toggleItem`

### syslog

- **service** (2): `reset, stats`
- **settings** (6): `addDestination, delDestination, getDestination, searchDestinations, setDestination, toggleDestination`

### tailscale

- **settings** (6): `addSubnet, delSubnet, getSubnet, reload, searchSubnet, setSubnet`
- **status** (3): `ip, net, status`

### tayga

- **mapping** (6): `addStaticmapping, delStaticmapping, getStaticmapping, searchStaticmapping, setStaticmapping, toggleStaticmapping`

### telegraf

- **general** (2): `get, set`
- **input** (2): `get, set`
- **key** (6): `addKey, delKey, getKey, searchKey, setKey, toggleKey`
- **output** (2): `get, set`
- **service** (5): `reconfigure, restart, start, status, stop`

### tinc

- **service** (4): `reconfigure, restart, start, stop`
- **settings** (10): `delHost, delNetwork, getHost, getNetwork, searchHost, searchNetwork, setHost, setNetwork, toggleHost, toggleNetwork`

### tor

- **exitacl** (6): `addacl, delacl, getacl, searchacl, setacl, toggleacl`
- **general** (7): `addhidservauth, delhidservauth, gethidservauth, searchhidservauth, set, sethidservauth, togglehidservauth`
- **hiddenservice** (6): `addservice, delservice, getservice, searchservice, setservice, toggleservice`
- **hiddenserviceacl** (6): `addacl, delacl, getacl, searchacl, setacl, toggleacl`
- **service** (8): `circuits, getHiddenServices, reconfigure, restart, start, status, stop, streams`
- **socksacl** (6): `addacl, delacl, getacl, searchacl, setacl, toggleacl`

### trafficshaper

- **service** (3): `flushreload, reconfigure, statistics`
- **settings** (18): `addPipe, addQueue, addRule, delPipe, delQueue, delRule, getPipe, getQueue, getRule, searchPipes, searchQueues, searchRules, setPipe, setQueue, setRule` +3 more

### trust

- **ca** (9): `add, caInfo, caList, del, generateFile, get, rawDump, search, set`
- **cert** (10): `add, caInfo, caList, del, generateFile, get, rawDump, search, set, userList`
- **crl** (5): `del, get, rawDump, search, set`
- **settings** (1): `reconfigure`

### udpbroadcastrelay

- **service** (6): `config, reload, restart, start, status, stop`
- **settings** (6): `addRelay, delRelay, getRelay, searchRelay, setRelay, toggleRelay`

### unbound

- **diagnostics** (7): `dumpcache, dumpinfra, listinsecure, listlocaldata, listlocalzones, stats, testBlocklist`
- **overview** (6): `Rolling, getPolicies, isBlockListEnabled, isEnabled, searchQueries, totals`
- **service** (2): `dnsbl, reconfigureGeneral`
- **settings** (32): `addAcl, addDnsbl, addForward, addHostAlias, addHostOverride, delAcl, delDnsbl, delForward, delHostAlias, delHostOverride, getAcl, getDnsbl, getForward, getHostAlias, getHostOverride` +17 more

### vnstat

- **service** (5): `daily, hourly, monthly, resetdb, yearly`

### wireguard

- **client** (11): `addClient, addClientBuilder, delClient, getClient, getClientBuilder, getServerInfo, listServers, psk, searchClient, setClient, toggleClient`
- **server** (7): `addServer, delServer, getServer, keyPair, searchServer, setServer, toggleServer`
- **service** (2): `reconfigure, show`

### wol

- **wol** (8): `addHost, delHost, getHost, getwake, searchHost, set, setHost, wakeall`

### zabbixagent

- **settings** (12): `addAlias, addUserparameter, delAlias, delUserparameter, getAlias, getUserparameter, searchAliases, searchUserparameters, setAlias, setUserparameter, toggleAlias, toggleUserparameter`

### zerotier

- **network** (7): `add, del, get, info, search, set, toggle`
- **settings** (3): `get, set, status`

