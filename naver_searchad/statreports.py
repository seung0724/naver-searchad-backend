from .auth import SearchAdClient

def create_statreport(client: SearchAdClient, body: dict):
    """POST /stat-reports – request bulk report"""
    return client.request("POST", "/stat-reports", data=body)

def get_statreport_status(client: SearchAdClient, report_id: int):
    """GET /stat-reports/{reportId}"""
    return client.request("GET", f"/stat-reports/{report_id}")
