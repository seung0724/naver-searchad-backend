# main.py

from fastapi import FastAPI
from naver_searchad import (
    SearchAdClient,
    list_campaigns,
    suggest_keywords,
    get_stat,
    fetch_release_notes,
)
from naver_searchad.schemas import (
    Credentials,
    SuggestKeywordRequest,
    GetStatRequest
)

app = FastAPI(title="Naver Search Ads API")

@app.post("/list_campaigns")
def api_list_campaigns(req: Credentials):
    client = SearchAdClient(req.access_key, req.secret_key, req.customer_id)
    return list_campaigns(client)

@app.post("/suggest_keywords")
def api_suggest_keywords(req: SuggestKeywordRequest):
    client = SearchAdClient(req.access_key, req.secret_key, req.customer_id)
    return suggest_keywords(client, term=req.term)

@app.post("/get_stat")
def api_get_stat(req: GetStatRequest):
    client = SearchAdClient(req.access_key, req.secret_key, req.customer_id)
    return get_stat(client, entity=req.entity, entity_ids=req.entity_ids)

@app.post("/fetch_release_notes")
def api_fetch_release_notes():
    return fetch_release_notes()
