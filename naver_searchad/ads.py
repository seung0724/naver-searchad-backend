from .auth import SearchAdClient

def list_ads(client: SearchAdClient, adgroup_id: int):
    """GET /ncc/ads – list ads under an adgroup"""
    return client.request("GET", "/ncc/ads", params={"adgroupId": adgroup_id})

def create_ad(client: SearchAdClient, body: dict):
    """POST /ncc/ads"""
    return client.request("POST", "/ncc/ads", data=body)
