# src/naver_searchad/__init__.py

from .auth import SearchAdClient

# accounts.py 의 list_accounts 함수를 list_campaigns 라는 이름으로도 사용하도록 alias 걸기
from .accounts import list_accounts, list_accounts as list_campaigns

from .campaigns import (
    get_campaign,
    create_campaign,
    update_campaign,
    delete_campaign
)
from .adgroups import list_adgroups, create_adgroup
from .ads import list_ads, create_ad
from .keywords import list_keywords, suggest_keywords
from .targets import list_targets
from .stats import get_stat
from .statreports import create_statreport, get_statreport_status
from .updates import fetch_release_notes, fetch_notices

__all__ = [
    "SearchAdClient",
    "list_accounts",      # 원래 이름
    "list_campaigns",     # alias 이름
    "get_campaign", "create_campaign", "update_campaign", "delete_campaign",
    "list_adgroups", "create_adgroup",
    "list_ads", "create_ad",
    "list_keywords", "suggest_keywords",
    "list_targets",
    "get_stat",
    "create_statreport", "get_statreport_status",
    "fetch_release_notes", "fetch_notices",
]
