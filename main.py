# 수정된 main.py 예외 처리 포함 버전 생성

main_code = """from fastapi import FastAPI, HTTPException
from naver_searchad import (
    SearchAdClient,
    list_campaigns,
    suggest_keywords,
    get_stat,
    fetch_release_notes,
)
from naver_searchad.schemas import (
    Credentials,
)

from pydantic import BaseModel
from typing import List, Literal

class SuggestKeywordRequest(Credentials):
    term: str

class GetStatRequest(Credentials):
    entity: Literal["CAMPAIGN", "ADGROUP", "KEYWORD"]
    entity_ids: List[int]

app = FastAPI(title="Naver Search Ads API")

@app.post("/list_campaigns")
def api_list_campaigns(req: Credentials):
    try:
        client = SearchAdClient(req.access_key, req.secret_key, req.customer_id)
        return list_campaigns(client)
    except Exception as e:
        print("❗ Error in /list_campaigns:", e)
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

@app.post("/suggest_keywords")
def api_suggest_keywords(req: SuggestKeywordRequest):
    try:
        client = SearchAdClient(req.access_key, req.secret_key, req.customer_id)
        return suggest_keywords(client, term=req.term)
    except Exception as e:
        print("❗ Error in /suggest_keywords:", e)
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

@app.post("/get_stat")
def api_get_stat(req: GetStatRequest):
    try:
        client = SearchAdClient(req.access_key, req.secret_key, req.customer_id)
        return get_stat(client, entity=req.entity, entity_ids=req.entity_ids)
    except Exception as e:
        print("❗ Error in /get_stat:", e)
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

@app.post("/fetch_release_notes")
def api_fetch_release_notes():
    try:
        return fetch_release_notes()
    except Exception as e:
        print("❗ Error in /fetch_release_notes:", e)
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
"""

main_file_path = "/mnt/data/main.py"
with open(main_file_path, "w", encoding="utf-8") as f:
    f.write(main_code)

main_file_path
