from .auth import SearchAdClient

def list_targets(client: SearchAdClient, owner_id: int, types: list = None):
    """GET /ncc/targets – retrieves targeting info"""
    params = {"ownerId": owner_id}
    if types:
        params["types"] = ",".join(types)
    return client.request("GET", "/ncc/targets", params=params)
