from .auth import SearchAdClient

def get_campaign(client: SearchAdClient, campaign_id: int):
    """GET /ncc/campaigns/{campaignId}"""
    return client.request("GET", f"/ncc/campaigns/{campaign_id}")

def create_campaign(client: SearchAdClient, body: dict):
    """POST /ncc/campaigns"""
    return client.request("POST", "/ncc/campaigns", data=body)

def update_campaign(client: SearchAdClient, campaign_id: int, body: dict):
    """PUT /ncc/campaigns/{campaignId}"""
    return client.request("PUT", f"/ncc/campaigns/{campaign_id}", data=body)

def delete_campaign(client: SearchAdClient, campaign_id: int):
    """DELETE /ncc/campaigns/{campaignId}"""
    return client.request("DELETE", f"/ncc/campaigns/{campaign_id}")
