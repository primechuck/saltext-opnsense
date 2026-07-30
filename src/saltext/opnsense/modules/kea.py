import logging

from saltext.opnsense.utils.common import is_uuid

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_kea"


def __virtual__():
    if "opnsense.search" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


def _search(controller, type_name, search_phrase="", row_count=-1):
    try:
        fn = __salt__["opnsense.search"]
        res = fn("kea", controller, type_name, search_phrase=search_phrase, row_count=row_count)
        if isinstance(res, dict):
            return res.get("rows", [])
        return []
    except Exception as exc:
        log.debug("kea search %s/%s failed: %s", controller, type_name, exc)
        return []


def list_subnets(version="v4"):
    ctrl = "dhcpv4" if version in ("v4", "4", "dhcpv4") else "dhcpv6"
    rows = _search(ctrl, "subnet", row_count=-1)
    result = {}
    for r in rows:
        subnet = r.get("subnet") or ""
        if not subnet:
            continue
        result[subnet] = {
            "subnet": subnet,
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "pools": r.get("pools") or r.get("pool") or "",
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_subnets_pretty(version="v4"):
    data = list_subnets(version=version)
    lines = []
    for cidr in sorted(data):
        info = data[cidr]
        lines.append(f"{cidr} [{info.get('description', '')}] {info.get('uuid', '')[:8]}")
    return lines


def list_subnets_simple(version="v4"):
    return {cidr: info["uuid"] for cidr, info in list_subnets(version=version).items()}


def list_reservations(subnet=None, version="v4", search_phrase=""):
    ctrl = "dhcpv4" if version in ("v4", "4", "dhcpv4") else "dhcpv6"
    rows = _search(ctrl, "reservation", search_phrase=search_phrase, row_count=-1)

    subnet_uuid_map = {}
    if subnet:
        if not is_uuid(subnet):
            subnets = list_subnets(version=version)
            for s_cidr, s_info in subnets.items():
                if s_cidr == subnet:
                    subnet_uuid_map[subnet] = s_info["uuid"]
                    break
            if subnet in subnet_uuid_map:
                filter_uuid = subnet_uuid_map[subnet]
            else:
                filter_uuid = subnet
        else:
            filter_uuid = subnet
    else:
        filter_uuid = None

    uuid_to_subnet = {}
    for cidr, info in list_subnets(version=version).items():
        if info.get("uuid"):
            uuid_to_subnet[info["uuid"]] = cidr

    result = {}
    for r in rows:
        r_subnet = r.get("subnet") or ""
        if filter_uuid and r_subnet != filter_uuid and r_subnet != subnet:
            continue
        ip = r.get("ip_address") or r.get("ip") or ""
        hw = r.get("hw_address") or r.get("hwaddr") or ""
        hostname = r.get("hostname") or ""
        key = hostname or hw or ip or r.get("uuid")
        result[key] = {
            "hostname": hostname,
            "ip_address": ip,
            "hw_address": hw,
            "subnet": r_subnet,
            "subnet_cidr": uuid_to_subnet.get(r_subnet, r_subnet),
            "uuid": r.get("uuid"),
            "description": r.get("description", ""),
            "raw": r,
        }
    return dict(sorted(result.items()))


def list_reservations_pretty(subnet=None, version="v4"):
    data = list_reservations(subnet=subnet, version=version)
    lines = []
    for key in sorted(data):
        info = data[key]
        lines.append(
            f"{info.get('hostname')} {info.get('ip_address')} {info.get('hw_address')} subnet={info.get('subnet_cidr')} [{info.get('uuid', '')[:8]}]"
        )
    return lines


def list_reservations_simple(subnet=None, version="v4"):
    data = list_reservations(subnet=subnet, version=version)
    return {k: v["ip_address"] for k, v in data.items()}


def list_leases(version="v4"):
    if version in ("v4", "4"):
        action = "searchLease4"
        controller = "leases"
    else:
        action = "searchLease6"
        controller = "leases"
    try:
        res = __salt__["opnsense.call"](
            "kea",
            controller,
            action,
            data={"current": 1, "rowCount": -1, "searchPhrase": ""},
            method="POST",
        )
        if isinstance(res, dict):
            rows = res.get("rows", []) or res.get("leases", [])
            if isinstance(rows, dict):
                rows = list(rows.values())
            result = {}
            for r in rows:
                if not isinstance(r, dict):
                    continue
                key = (
                    r.get("hostname")
                    or r.get("hwaddr")
                    or r.get("ip_address")
                    or r.get("uuid")
                    or str(id(r))
                )
                result[key] = r
            return dict(sorted(result.items()))
        return {}
    except Exception as exc:
        log.debug("kea leases failed: %s", exc)
        return {}


def list_leases_pretty(version="v4"):
    data = list_leases(version=version)
    lines = []
    for key in sorted(data):
        r = data[key]
        if isinstance(r, dict):
            lines.append(
                f"{r.get('hostname', '')} {r.get('address', '') or r.get('ip_address', '')} {r.get('hwaddr', '')}"
            )
        else:
            lines.append(str(r))
    return lines


def list_options(subnet=None, version="v4"):
    ctrl = "dhcpv4" if version in ("v4", "4") else "dhcpv6"
    rows = _search(ctrl, "option", row_count=-1)
    result = {}
    for r in rows:
        name = r.get("option_name") or r.get("name") or r.get("uuid") or ""
        if not name:
            continue
        result[name] = {
            "name": name,
            "uuid": r.get("uuid"),
            "value": r.get("option_value") or r.get("value") or "",
            "raw": r,
        }
    return dict(sorted(result.items()))


def resolve_subnet(subnet_cidr_or_uuid, version="v4"):
    if not subnet_cidr_or_uuid:
        return None
    if is_uuid(subnet_cidr_or_uuid):
        return subnet_cidr_or_uuid
    subnets = list_subnets(version=version)
    if subnet_cidr_or_uuid in subnets:
        return subnets[subnet_cidr_or_uuid]["uuid"]
    rows = _search(
        "dhcpv4" if version == "v4" else "dhcpv6",
        "subnet",
        search_phrase=subnet_cidr_or_uuid,
        row_count=-1,
    )
    for r in rows:
        if r.get("subnet") == subnet_cidr_or_uuid:
            return r.get("uuid")
    return None


def get_subnet(cidr_or_uuid, version="v4"):
    return list_subnets(version=version).get(cidr_or_uuid) or list_subnets(version=version).get(
        resolve_subnet(cidr_or_uuid, version=version) or ""
    )
