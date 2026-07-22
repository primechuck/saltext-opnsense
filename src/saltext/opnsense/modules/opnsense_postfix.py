# AUTO-GENERATED - DO NOT EDIT - run tools/generate_wrappers.py

"""
Auto-generated OPNsense postfix wrappers.

Generated from controllers.json for module postfix.
Do not edit manually; run tools/generate_wrappers.py to regenerate.

API pattern: /api/postfix/{controller}/{action}[/{uuid}]

This module wraps generic opnsense.* calls, working in both
proxy and direct modes via __salt__['opnsense.*']
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "opnsense_postfix"


def __virtual__():
    if "opnsense.call" in __salt__ or "opnsense.search" in __salt__:
        return __virtualname__
    return (False, "opnsense execution module not loaded")


# --- address controller ---

def search_address(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search address entries in postfix/address.

    Wraps: POST /api/postfix/address/searchAddress

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "address", "address", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_address(uuid=None):
    """
    Get address entry in postfix/address.

    Wraps: GET /api/postfix/address/getAddress/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "address", "address", uuid)


def add_address(data):
    """
    Add address entry in postfix/address.

    Wraps: POST /api/postfix/address/addAddress

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "address", "address", data)


def set_address(uuid, data):
    """
    Set/update address entry in postfix/address.

    Wraps: POST /api/postfix/address/setAddress/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "address", "address", uuid, data)


def del_address(uuid):
    """
    Delete address entry in postfix/address.

    Wraps: POST /api/postfix/address/delAddress/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "address", "address", uuid)


def toggle_address(uuid, enabled=None):
    """
    Toggle address entry in postfix/address.

    Wraps: POST /api/postfix/address/toggleAddress/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "address", "address", uuid, enabled)


# --- domain controller ---

def search_domain(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search domain entries in postfix/domain.

    Wraps: POST /api/postfix/domain/searchDomain

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "domain", "domain", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_domain(uuid=None):
    """
    Get domain entry in postfix/domain.

    Wraps: GET /api/postfix/domain/getDomain/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "domain", "domain", uuid)


def add_domain(data):
    """
    Add domain entry in postfix/domain.

    Wraps: POST /api/postfix/domain/addDomain

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "domain", "domain", data)


def set_domain(uuid, data):
    """
    Set/update domain entry in postfix/domain.

    Wraps: POST /api/postfix/domain/setDomain/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "domain", "domain", uuid, data)


def del_domain(uuid):
    """
    Delete domain entry in postfix/domain.

    Wraps: POST /api/postfix/domain/delDomain/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "domain", "domain", uuid)


def toggle_domain(uuid, enabled=None):
    """
    Toggle domain entry in postfix/domain.

    Wraps: POST /api/postfix/domain/toggleDomain/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "domain", "domain", uuid, enabled)


# --- headerchecks controller ---

def get_headercheck(uuid=None):
    """
    Get headercheck entry in postfix/headerchecks.

    Wraps: GET /api/postfix/headerchecks/getHeadercheck/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "headerchecks", "headercheck", uuid)


def add_headercheck(data):
    """
    Add headercheck entry in postfix/headerchecks.

    Wraps: POST /api/postfix/headerchecks/addHeadercheck

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "headerchecks", "headercheck", data)


def set_headercheck(uuid, data):
    """
    Set/update headercheck entry in postfix/headerchecks.

    Wraps: POST /api/postfix/headerchecks/setHeadercheck/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "headerchecks", "headercheck", uuid, data)


def del_headercheck(uuid):
    """
    Delete headercheck entry in postfix/headerchecks.

    Wraps: POST /api/postfix/headerchecks/delHeadercheck/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "headerchecks", "headercheck", uuid)


def toggle_headercheck(uuid, enabled=None):
    """
    Toggle headercheck entry in postfix/headerchecks.

    Wraps: POST /api/postfix/headerchecks/toggleHeadercheck/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "headerchecks", "headercheck", uuid, enabled)


def search_headerchecks(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search headerchecks entries in postfix/headerchecks.

    Wraps: POST /api/postfix/headerchecks/searchHeaderchecks

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "headerchecks", "headerchecks", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


# --- recipient controller ---

def search_recipient(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search recipient entries in postfix/recipient.

    Wraps: POST /api/postfix/recipient/searchRecipient

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "recipient", "recipient", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_recipient(uuid=None):
    """
    Get recipient entry in postfix/recipient.

    Wraps: GET /api/postfix/recipient/getRecipient/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "recipient", "recipient", uuid)


def add_recipient(data):
    """
    Add recipient entry in postfix/recipient.

    Wraps: POST /api/postfix/recipient/addRecipient

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "recipient", "recipient", data)


def set_recipient(uuid, data):
    """
    Set/update recipient entry in postfix/recipient.

    Wraps: POST /api/postfix/recipient/setRecipient/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "recipient", "recipient", uuid, data)


def del_recipient(uuid):
    """
    Delete recipient entry in postfix/recipient.

    Wraps: POST /api/postfix/recipient/delRecipient/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "recipient", "recipient", uuid)


def toggle_recipient(uuid, enabled=None):
    """
    Toggle recipient entry in postfix/recipient.

    Wraps: POST /api/postfix/recipient/toggleRecipient/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "recipient", "recipient", uuid, enabled)


# --- recipientbcc controller ---

def search_recipientbcc(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search recipientbcc entries in postfix/recipientbcc.

    Wraps: POST /api/postfix/recipientbcc/searchRecipientbcc

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "recipientbcc", "recipientbcc", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_recipientbcc(uuid=None):
    """
    Get recipientbcc entry in postfix/recipientbcc.

    Wraps: GET /api/postfix/recipientbcc/getRecipientbcc/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "recipientbcc", "recipientbcc", uuid)


def add_recipientbcc(data):
    """
    Add recipientbcc entry in postfix/recipientbcc.

    Wraps: POST /api/postfix/recipientbcc/addRecipientbcc

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "recipientbcc", "recipientbcc", data)


def set_recipientbcc(uuid, data):
    """
    Set/update recipientbcc entry in postfix/recipientbcc.

    Wraps: POST /api/postfix/recipientbcc/setRecipientbcc/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "recipientbcc", "recipientbcc", uuid, data)


def del_recipientbcc(uuid):
    """
    Delete recipientbcc entry in postfix/recipientbcc.

    Wraps: POST /api/postfix/recipientbcc/delRecipientbcc/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "recipientbcc", "recipientbcc", uuid)


def toggle_recipientbcc(uuid, enabled=None):
    """
    Toggle recipientbcc entry in postfix/recipientbcc.

    Wraps: POST /api/postfix/recipientbcc/toggleRecipientbcc/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "recipientbcc", "recipientbcc", uuid, enabled)


# --- sender controller ---

def search_sender(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search sender entries in postfix/sender.

    Wraps: POST /api/postfix/sender/searchSender

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "sender", "sender", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_sender(uuid=None):
    """
    Get sender entry in postfix/sender.

    Wraps: GET /api/postfix/sender/getSender/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "sender", "sender", uuid)


def add_sender(data):
    """
    Add sender entry in postfix/sender.

    Wraps: POST /api/postfix/sender/addSender

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "sender", "sender", data)


def set_sender(uuid, data):
    """
    Set/update sender entry in postfix/sender.

    Wraps: POST /api/postfix/sender/setSender/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "sender", "sender", uuid, data)


def del_sender(uuid):
    """
    Delete sender entry in postfix/sender.

    Wraps: POST /api/postfix/sender/delSender/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "sender", "sender", uuid)


def toggle_sender(uuid, enabled=None):
    """
    Toggle sender entry in postfix/sender.

    Wraps: POST /api/postfix/sender/toggleSender/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "sender", "sender", uuid, enabled)


# --- senderbcc controller ---

def search_senderbcc(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search senderbcc entries in postfix/senderbcc.

    Wraps: POST /api/postfix/senderbcc/searchSenderbcc

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "senderbcc", "senderbcc", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_senderbcc(uuid=None):
    """
    Get senderbcc entry in postfix/senderbcc.

    Wraps: GET /api/postfix/senderbcc/getSenderbcc/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "senderbcc", "senderbcc", uuid)


def add_senderbcc(data):
    """
    Add senderbcc entry in postfix/senderbcc.

    Wraps: POST /api/postfix/senderbcc/addSenderbcc

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "senderbcc", "senderbcc", data)


def set_senderbcc(uuid, data):
    """
    Set/update senderbcc entry in postfix/senderbcc.

    Wraps: POST /api/postfix/senderbcc/setSenderbcc/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "senderbcc", "senderbcc", uuid, data)


def del_senderbcc(uuid):
    """
    Delete senderbcc entry in postfix/senderbcc.

    Wraps: POST /api/postfix/senderbcc/delSenderbcc/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "senderbcc", "senderbcc", uuid)


def toggle_senderbcc(uuid, enabled=None):
    """
    Toggle senderbcc entry in postfix/senderbcc.

    Wraps: POST /api/postfix/senderbcc/toggleSenderbcc/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "senderbcc", "senderbcc", uuid, enabled)


# --- sendercanonical controller ---

def search_sendercanonical(search_phrase="", row_count=-1, current=1, sort=None, **kwargs):
    """
    Search sendercanonical entries in postfix/sendercanonical.

    Wraps: POST /api/postfix/sendercanonical/searchSendercanonical

    :param search_phrase: Optional search phrase
    :param row_count: Rows per page, -1 for all
    :param current: Current page
    :param sort: Sort dict
    :param kwargs: Additional filters
    :return: API response with rows
    """
    return __salt__["opnsense.search"]("postfix", "sendercanonical", "sendercanonical", search_phrase=search_phrase, row_count=row_count, current=current, sort=sort, **kwargs)


def get_sendercanonical(uuid=None):
    """
    Get sendercanonical entry in postfix/sendercanonical.

    Wraps: GET /api/postfix/sendercanonical/getSendercanonical/{uuid}

    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.get"]("postfix", "sendercanonical", "sendercanonical", uuid)


def add_sendercanonical(data):
    """
    Add sendercanonical entry in postfix/sendercanonical.

    Wraps: POST /api/postfix/sendercanonical/addSendercanonical

    :param data: Dict with entry data
    :return: API response with uuid
    """
    return __salt__["opnsense.add"]("postfix", "sendercanonical", "sendercanonical", data)


def set_sendercanonical(uuid, data):
    """
    Set/update sendercanonical entry in postfix/sendercanonical.

    Wraps: POST /api/postfix/sendercanonical/setSendercanonical/{uuid}

    :param uuid: UUID of existing entry
    :param data: Updated data
    :return: API response
    """
    return __salt__["opnsense.set_item"]("postfix", "sendercanonical", "sendercanonical", uuid, data)


def del_sendercanonical(uuid):
    """
    Delete sendercanonical entry in postfix/sendercanonical.

    Wraps: POST /api/postfix/sendercanonical/delSendercanonical/{uuid}

    :param uuid: UUID to delete
    :return: API response
    """
    return __salt__["opnsense.delete"]("postfix", "sendercanonical", "sendercanonical", uuid)


def toggle_sendercanonical(uuid, enabled=None):
    """
    Toggle sendercanonical entry in postfix/sendercanonical.

    Wraps: POST /api/postfix/sendercanonical/toggleSendercanonical/{uuid}[/{enabled}]

    :param uuid: UUID
    :param enabled: Optional 0/1 to force state
    :return: API response
    """
    return __salt__["opnsense.toggle"]("postfix", "sendercanonical", "sendercanonical", uuid, enabled)


# --- service controller ---

def service_checkrspamd(data=None, uuid=None):
    """
    Execute checkrspamd in postfix/service.

    Wraps: /api/postfix/service/checkrspamd

    :param data: Optional data
    :param uuid: Optional UUID
    :return: API response
    """
    return __salt__["opnsense.call"]("postfix", "service", "checkrspamd", uuid=uuid, data=data)


def service_reconfigure(action="reconfigure", data=None):
    """
    reconfigure action in postfix/service.

    Wraps: POST /api/postfix/service/reconfigure

    :param action: Action override, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("postfix", "service", action, data)



# Generic module-level helpers

def reconfigure(controller="service", action="reconfigure", data=None):
    """
    Generic reconfigure for postfix.

    Wraps: POST /api/postfix/{controller}/{action}

    :param controller: Controller name, default service
    :param action: Action name, default reconfigure
    :param data: Optional data
    :return: API response
    """
    return __salt__["opnsense.reconfigure"]("postfix", controller, action, data)
