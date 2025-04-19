import requests
import time
import hmac
import hashlib
import base64
import json

API_KEY = "8ce4bd62-9328-495e-9556-2bf1107b3ac2"
API_SECRET = "AB2C36344430A6080F3C5645155074B3"
PASSPHRASE = "Slipknot221989@"
BASE_URL = "https://www.okx.com"

def get_iso_timestamp():
    return time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())

def sign_request(timestamp, method, path, body=""):
    message = f"{timestamp}{method}{path}{body}"
    signature = hmac.new(
        API_SECRET.encode(),
        message.encode(),
        hashlib.sha256
    ).digest()
    return base64.b64encode(signature).decode()

def okx_request(method, path, body=""):
    timestamp = get_iso_timestamp()
    body_str = json.dumps(body) if body else ""
    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-SIGN": sign_request(timestamp, method, path, body_str),
        "Content-Type": "application/json"
    }
    response = requests.request(method, BASE_URL + path, headers=headers, data=body_str)
    return response.json()

print("===== Перевірка всіх активів OKX =====")
balances = okx_request("GET", "/api/v5/asset/balances")
print(json.dumps(balances, indent=2))
