# naver_searchad/schemas.py

from pydantic import BaseModel
from typing import List, Literal


class Credentials(BaseModel):
    access_key: str
    secret_key: str
    customer_id: str


class SuggestKeywordRequest(BaseModel):
    access_key: str
    secret_key: str
    customer_id: str
    term: str


class GetStatRequest(BaseModel):
    access_key: str
    secret_key: str
    customer_id: str
    entity: Literal["CAMPAIGN", "ADGROUP", "KEYWORD"]
    entity_ids: List[int]
