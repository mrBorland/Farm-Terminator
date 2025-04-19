import json
import time
import hmac
import base64
import hashlib
import requests

# === OKX API доступ ===
API_KEY = "8ce4bd62-9328-495e-9556-2bf1107b3ac2"
API_SECRET = "AB2C36344430A6080F3C5645155074B3"
PASSPHRASE = "Slipknot221989@"

# === Конфіг ===
TARGET_CHAIN = "Polygon"
TOKEN = "MATIC"
AMOUNT = "0.01"
WALLETS_FILE = "wallets_polygon.json"
TO_ADDRESS = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"  # Основний гаманець

# === Підпис запиту OKX ===
def sign_request(timestamp, method, path, body=""):
    msg = f"{timestamp}{method.upper()}{path}{body}"
    return base64.b64encode(hmac.new(API_SECRET.encode(), msg.encode(), hashlib.sha256).digest()).decode()

# === Виконати запит до OKX ===
def okx_request(method, endpoint, payload=""):
    url = f"https://www.okx.com{endpoint}"
    timestamp = str(time.time())
    signature = sign_request(timestamp, method, endpoint, json.dumps(payload) if payload else "")
    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": signature,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json"
    }
    r = requests.request(method, url, headers=headers, json=payload if payload else None)
    return r.json()

# === Отримати баланс MATIC ===
def get_matic_balance():
    res = okx_request("GET", "/api/v5/asset/balances?ccy=MATIC")
    return float(res["data"][0]["availBal"])

# === Надіслати транзакцію на один гаманець ===
def transfer_to_wallet(address, amount):
    data = {
        "ccy": TOKEN,
        "amt": amount,
        "dest": "4",  # external address
        "toAddr": address,
        "chain": "MATIC-Polygon",
        "fee": "0.0005",
        "pwd": "",  # якщо не потрібно — залишити порожнім
    }
    res = okx_request("POST", "/api/v5/asset/withdrawal", data)
    return res

# === Запуск ===
print("===== Початок поповнення з OKX до Polygon-гаманців =====")
try:
    with open(WALLETS_FILE) as f:
        wallets = json.load(f)
except Exception as e:
    print(f"[X] Не вдалося відкрити {WALLETS_FILE}:", e)
    exit()

matic_balance = get_matic_balance()
print(f"[✓] Доступно на OKX: {matic_balance:.4f} MATIC")

count = 0
for w in wallets:
    if matic_balance < float(AMOUNT): break
    r = transfer_to_wallet(w["address"], AMOUNT)
    if r.get("code") == "0":
        print(f"[{count+1}] {w['address']} → Успішно надіслано {AMOUNT} MATIC")
        count += 1
        matic_balance -= float(AMOUNT)
    else:
        print(f"[{count+1}] {w['address']} → Помилка: {r.get('msg')}")

print(f"✅ Успішно поповнено: {count} гаманців")
