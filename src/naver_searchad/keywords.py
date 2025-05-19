from .auth import SearchAdClient

def list_keywords(client: SearchAdClient, campaign_id: int):
    """GET /ncc/keywords – list keywords in campaign"""
    return client.request("GET", "/ncc/keywords", params={"campaignId": campaign_id})

def suggest_keywords(client: SearchAdClient, term: str, hint: str = None):
    """GET /ncc/keywords/suggestions – keyword ideas & volume"""
    params = {"hintKeywords": term}
    if hint:
        params["includeHintKeywords"] = hint
    return client.request("GET", "/ncc/keywords/suggestions", params=params)
