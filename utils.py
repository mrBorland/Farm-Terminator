import time
import hmac
import base64
import requests
from hashlib import sha256
from config import OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE

def get_timestamp():
    return str(time.time())

def generate_signature(timestamp, method, request_path, body=''):
    message = timestamp + method.upper() + request_path + body
    mac = hmac.new(bytes(OKX_SECRET_KEY, encoding='utf-8'),
                   bytes(message, encoding='utf-8'),
                   digestmod=sha256)
    return base64.b64encode(mac.digest()).decode()

def get_headers(method, path, body=''):
    timestamp = get_timestamp()
    sign = generate_signature(timestamp, method, path, body)
    return {
        'OK-ACCESS-KEY': OKX_API_KEY,
        'OK-ACCESS-SIGN': sign,
        'OK-ACCESS-TIMESTAMP': timestamp,
        'OK-ACCESS-PASSPHRASE': OKX_PASSPHRASE,
        'Content-Type': 'application/json'
    }

def get_usdt_balance():
    url = "https://www.okx.com/api/v5/account/balance"
    headers = get_headers("GET", "/api/v5/account/balance")
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        for asset in data['data'][0]['details']:
            if asset['ccy'] == 'USDT':
                return float(asset['availBal'])
    except Exception as e:
        print("Помилка при отриманні балансу:", e)
    return 0.0
