from .auth import SearchAdClient

def get_stat(client: SearchAdClient, entity: str, entity_ids: list):
    """GET /stats – retrieve performance metrics"""
    return client.request("GET", "/stats", params={
        "entity": entity,
        "ids": ",".join(map(str, entity_ids))
    })
