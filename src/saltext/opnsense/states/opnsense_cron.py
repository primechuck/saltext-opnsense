# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense cron state wrappers.

Generated from controllers.json for module cron.
Do not edit manually; run tools/generate_wrappers.py.

Uses opnsense.item_present/absent which work in proxy and direct modes.
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_cron"


def __virtual__():
    if "opnsense.item_present" in __salt__ or "opnsense.call" in __salt__:
        return __virtualname__
    return (False, "opnsense state module not loaded: opnsense execution module missing")


# --- settings controller ---

def job_present(name, data=None, match=None, reconfigure="cron/service/reconfigure", search_field=None):
    """
    Ensure job settings present in cron.

    Wraps opnsense.item_present for /api/cron/settings/searchJob

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default cron/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "cron", "settings", "job", data, match=match, reconfigure=reconfigure, search_field=search_field)


def job_absent(name, match=None, reconfigure="cron/service/reconfigure", search_field=None):
    """
    Ensure job settings absent in cron.

    Wraps opnsense.item_absent for /api/cron/settings/searchJob

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "cron", "settings", "job", match=match, reconfigure=reconfigure, search_field=search_field)


def jobs_present(name, data=None, match=None, reconfigure="cron/service/reconfigure", search_field=None):
    """
    Ensure jobs settings present in cron.

    Wraps opnsense.item_present for /api/cron/settings/searchJobs

    :param name: Identifier for state, used for matching if match not given
    :param data: Dict of fields to set
    :param match: Dict to identify existing entry, e.g. {"hostname": "grafana"}
    :param reconfigure: Reconfigure path, default cron/service/reconfigure
    :param search_field: Optional field to use as match if match not supplied
    :return: State result dict
    """
    return __salt__["opnsense.item_present"](name, "cron", "settings", "jobs", data, match=match, reconfigure=reconfigure, search_field=search_field)


def jobs_absent(name, match=None, reconfigure="cron/service/reconfigure", search_field=None):
    """
    Ensure jobs settings absent in cron.

    Wraps opnsense.item_absent for /api/cron/settings/searchJobs

    :param name: Identifier
    :param match: Dict to identify entry to delete
    :param reconfigure: Reconfigure path
    :param search_field: Optional search field
    :return: State result
    """
    return __salt__["opnsense.item_absent"](name, "cron", "settings", "jobs", match=match, reconfigure=reconfigure, search_field=search_field)



def reconfigured(name, controller="service", action="reconfigure"):
    """
    Trigger reconfigure for cron.

    Wraps opnsense.reconfigured state.

    :param name: State name
    :param controller: Controller to reconfigure
    :param action: Action, default reconfigure
    """
    ret = {"name": name, "result": False, "changes": {}, "comment": ""}
    try:
        __salt__["opnsense.reconfigure"]("cron", controller, action)
        ret["result"] = True
        ret["comment"] = f"reconfigured cron/{controller}/{action}"
        ret["changes"] = {"reconfigured": f"cron/{controller}/{action}"}
    except Exception as exc:
        ret["comment"] = f"reconfigure failed: {exc}"
    return ret
