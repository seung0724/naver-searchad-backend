from .auth import SearchAdClient

def list_adgroups(client: SearchAdClient, campaign_id: int):
    """GET /ncc/adgroups – list adgroups in a campaign"""
    return client.request("GET", "/ncc/adgroups", params={"campaignId": campaign_id})

def create_adgroup(client: SearchAdClient, body: dict):
    """POST /ncc/adgroups"""
    return client.request("POST", "/ncc/adgroups", data=body)
