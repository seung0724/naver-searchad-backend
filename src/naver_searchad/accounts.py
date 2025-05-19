from .auth import SearchAdClient

def list_accounts(client: SearchAdClient):
    """GET /ncc/campaigns – list all campaigns under account"""
    return client.request("GET", "/ncc/campaigns")
