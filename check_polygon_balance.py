import json
import requests
from datetime import datetime

RPC = "https://rpc.ankr.com/polygon"
TELEGRAM_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
CHAT_ID = "6821675571"

def get_balance(address):
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    try:
        r = requests.post(RPC, json=data, timeout=10)
        r.raise_for_status()
        result = int(r.json()["result"], 16) / 1e18
        return round(result, 6)
    except Exception as e:
        return f"Error: {str(e)}"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, json=payload)
    except:
        pass

with open("wallets_polygon.json") as f:
    wallets = json.load(f)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log = f"===== Polygon Wallets Balance [{now}] =====\n"
total = 0

for wallet in wallets:
    bal = get_balance(wallet["address"])
    if isinstance(bal, float):
        total += bal
    log += f"{wallet['address'][:12]}... → {bal} MATIC\n"

log += f"-------------------------------------\nЗагальний баланс: {round(total, 4)} MATIC\n"

print(log)

with open("logs/polygon_balances.txt", "a") as f:
    f.write(log + "\n")

send_telegram(log if len(log) < 4000 else log[:3990] + "...")
