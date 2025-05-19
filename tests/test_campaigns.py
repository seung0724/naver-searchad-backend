import pytest
from naver_searchad.campaigns import get_campaign

class DummyClient:
    def __init__(self):
        self.called = False
        self.method = None
        self.path = None
        self.data = None

    def request(self, method, path, params=None, data=None):
        self.called = True
        self.method = method
        self.path = path
        self.data = data
        return {"dummy": True}

def test_get_campaign():
    client = DummyClient()
    response = get_campaign(client, campaign_id=123)
    assert client.called
    assert client.method == "GET"
    assert client.path == "/ncc/campaigns/123"
    assert response == {"dummy": True}
