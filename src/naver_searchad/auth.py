import requests
import time
import hmac
import hashlib
import base64

class SearchAdClient:
    BASE_URL = "https://api.searchad.naver.com"

    def __init__(self, access_key: str, secret_key: str, customer_id: str):
        self.access_key = access_key
        self.secret_key = secret_key.encode('utf-8')
        self.customer_id = customer_id

    def _make_headers(self, method: str, path: str) -> dict:
        timestamp = str(int(time.time() * 1000))
        message = f"{timestamp}.{method}.{path}"
        signature = base64.b64encode(
            hmac.new(self.secret_key, message.encode('utf-8'), hashlib.sha256).digest()
        ).decode()
        return {
            "X-Timestamp": timestamp,
            "X-API-KEY": self.access_key,
            "X-Customer": self.customer_id,
            "X-Signature": signature,
            "Content-Type": "application/json; charset=UTF-8"
        }

    def request(self, method: str, path: str, params=None, data=None):
        url = f"{self.BASE_URL}{path}"
        headers = self._make_headers(method, path)
        resp = requests.request(method, url, headers=headers, params=params, json=data)
        resp.raise_for_status()
        return resp.json()
