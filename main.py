# main.py

import os
from fastapi import FastAPI
from pydantic import BaseModel
from naver_searchad import (
    SearchAdClient,
    list_campaigns,
    suggest_keywords,
    get_stat,
    fetch_release_notes,
)

app = FastAPI(title="Naver Search Ads API")

# 공통으로 쓰는 모델
class Credentials(BaseModel):
    access_key: str
    secret_key: str
    customer_id: str

class Term(BaseModel):
    term: str

class StatRequest(BaseModel):
    entity: str
    entity_ids: list[int]


def _make_client(creds: Credentials):
    return SearchAdClient(creds.access_key, creds.secret_key, creds.customer_id)


@app.post("/list_campaigns")
def api_list_campaigns(creds: Credentials):
    client = _make_client(creds)
    return list_campaigns(client)


@app.post("/suggest_keywords")
def api_suggest_keywords(req: Term, creds: Credentials):
    client = _make_client(creds)
    return suggest_keywords(client, term=req.term)


@app.post("/get_stat")
def api_get_stat(req: StatRequest, creds: Credentials):
    client = _make_client(creds)
    return get_stat(client, entity=req.entity, entity_ids=req.entity_ids)


@app.post("/fetch_release_notes")
def api_fetch_release_notes():
    return fetch_release_notes()
