import json
import time
import requests

BSCSCAN_API_KEY = "FIJE4FIC166ANVPX6ZQVP3CMDBHND4S256"
START_TIME = int(time.time()) - 50 * 3600
END_TIME = int(time.time())

with open("wallets_bnb.json") as f:
    wallets = json.load(f)

def get_token_transfers(address):
    url = (
        f"https://api.bscscan.com/api"
        f"?module=account&action=tokentx&address={address}"
        f"&starttimestamp={START_TIME}&endtimestamp={END_TIME}"
        f"&sort=asc&apikey={BSCSCAN_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    if data["status"] != "1":
        return []
    return data["result"]

print(f"[+] Перевірка токенів з {len(wallets)} гаманців за останні 50 годин\n")

for wallet in wallets:
    address = wallet["address"]
    print(f"[{address}]")
    try:
        tokens = get_token_transfers(address)
        if not tokens:
            print("  [-] Нічого не отримано.")
            continue
        for tx in tokens:
            if tx["to"].lower() == address.lower():
                print(f"  [+] {tx['value']} {tx['tokenSymbol']} від {tx['from']}")
    except Exception as e:
        print(f"  [!] Помилка: {e}")
