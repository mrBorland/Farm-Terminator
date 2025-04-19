import json, time, random, requests

TELEGRAM_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
TELEGRAM_CHAT_ID = "6821675571"
WITHDRAW_ADDRESS = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"

# Список RPC для резерву
RPC_LIST = [
    "https://rpc.ankr.com/polygon",
    "https://polygon-bor.publicnode.com",
    "https://polygon.llamarpc.com"
]

def send_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
    except Exception as e:
        print(f"[Telegram Error] {e}")

def get_balance(address):
    for rpc in RPC_LIST:
        try:
            data = {
                "jsonrpc": "2.0", "id": 1, "method": "eth_getBalance",
                "params": [address, "latest"]
            }
            r = requests.post(rpc, json=data, timeout=10)
            if r.status_code == 200 and "result" in r.json():
                return int(r.json()["result"], 16)
        except Exception as e:
            print(f"[!] RPC error: {rpc} → {str(e)}")
            continue
    return 0

def report(wallets):
    total = 0
    messages = []
    for i, w in enumerate(wallets, 1):
        balance = get_balance(w["address"])
        matic = balance / 1e18
        total += matic
        messages.append(f'{i:03d}. {w["address"]} → {matic:.4f} MATIC')
        time.sleep(0.3)
    result = f"===== Polygon Wallets =====\nTotal: {total:.4f} MATIC\n\n" + "\n".join(messages)
    with open("logs/polygon_balances.txt", "w") as f:
        f.write(result)
    send_telegram(result[:4096])
    print(result)

# Завантаження гаманців
with open("wallets_polygon.json") as f:
    wallets = json.load(f)

report(wallets)
