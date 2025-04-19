import time
import json
import requests

API_KEY = "8ce4bd62-9328-495e-9556-2bf1107b3ac2"
API_SECRET = "AB2C36344430A6080F3C5645155074B3"
API_PASSPHRASE = "Slipknot221989@"

WITHDRAW_AMOUNT = "0.01"  # MATIC
FEE = "0.1"  # фіксована комісія OKX
CHAIN = "Polygon"  # мережа
TOKEN = "MATIC"

WALLETS_FILE = "wallets_polygon.json"

def sign_headers(endpoint, body=""):
    import base64
    import hmac
    import hashlib
    import datetime

    timestamp = datetime.datetime.utcnow().isoformat("T", "seconds") + "Z"
    method = "POST"
    message = timestamp + method + endpoint + body
    signature = base64.b64encode(
        hmac.new(
            API_SECRET.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256
        ).digest()
    ).decode()

    return {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": signature,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": API_PASSPHRASE,
        "Content-Type": "application/json"
    }

def send_matic(to_address):
    url = "https://www.okx.com/api/v5/asset/withdrawal"
    data = {
        "ccy": TOKEN,
        "amt": WITHDRAW_AMOUNT,
        "fee": FEE,
        "dest": "4",  # on-chain
        "toAddr": to_address,
        "chain": f"{TOKEN}-{CHAIN}"
    }
    body = json.dumps(data)
    headers = sign_headers("/api/v5/asset/withdrawal", body)
    r = requests.post(url, headers=headers, data=body)
    return r.json()

def main():
    print("===== Розподіл газу через OKX =====")
    with open(WALLETS_FILE, "r") as f:
        wallets = json.load(f)

    success, failed = 0, 0
    for i, wallet in enumerate(wallets):
        print(f"[{i+1}] Поповнення {wallet['address']}...")
        res = send_matic(wallet['address'])

        if res.get("code") == "0":
            print(f" → Успіх!")
            success += 1
        else:
            print(f" → Помилка: {res.get('msg')}")
            failed += 1
        time.sleep(2)

    print("=====================================")
    print(f"✅ Успішно поповнено: {success}")
    print(f"❌ Не вдалося: {failed}")

if __name__ == "__main__":
    main()
