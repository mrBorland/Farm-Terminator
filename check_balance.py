def check_okx_balance(api_key, secret_key, passphrase):
    import requests
    import time
    import hmac
    import base64
    import hashlib

    url = "https://www.okx.com/api/v5/account/balance"
    timestamp = str(int(time.time()))
    method = "GET"
    request_path = "/api/v5/account/balance"

    prehash_string = f"{timestamp}{method}{request_path}"
    signature = base64.b64encode(
        hmac.new(
            secret_key.encode('utf-8'),
            prehash_string.encode('utf-8'),
            hashlib.sha256
        ).digest()
    ).decode()

    headers = {
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": signature,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": passphrase,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response.json()


# Тест
if __name__ == "__main__":
    from config import OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE

    result = check_okx_balance(OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE)
    print(result)
