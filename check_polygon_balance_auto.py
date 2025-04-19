import json
import requests
import time
from datetime import datetime

RPC = "https://rpc-mainnet.matic.quiknode.pro"  # Резервний RPC
WALLETS_FILE = "wallets_polygon.json"
LOG_FILE = "logs/polygon_balance.log"

def get_balance(address):
    try:
        data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getBalance",
            "params": [address, "latest"]
        }
        r = requests.post(RPC, json=data, timeout=10).json()
        if "result" in r:
            return round(int(r["result"], 16) / 10**18, 6)
        else:
            return "error"
    except Exception as e:
        return f"error: {str(e)}"

def main():
    print("Запуск перевірки балансу Polygon-гаманців...")
    with open(WALLETS_FILE, "r") as f:
        wallets = json.load(f)

    total = 0
    lines = []
    for i, wallet in enumerate(wallets, 1):
        addr = wallet["address"]
        bal = get_balance(addr)
        if isinstance(bal, float):
            total += bal
        msg = f"[{i}] {addr} → {bal} MATIC"
        print(msg)
        lines.append(msg)
        time.sleep(0.5)

    report = f"\n===== Звіт Polygon Balance =====\nДата: {datetime.now()}\nЗагальна кількість: {len(wallets)}\nЗагальний баланс: {round(total, 6)} MATIC\n"
    print(report)

    with open(LOG_FILE, "a") as f:
        f.write(report + "\n".join(lines) + "\n\n")

    # Telegram сповіщення (опціонально)
    try:
        TELEGRAM_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
        CHAT_ID = "6821675571"
        message = f"[Polygon] Баланс: {round(total, 6)} MATIC ({len(wallets)} гаманців)"
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params={
            "chat_id": CHAT_ID,
            "text": message
        })
    except:
        pass

if __name__ == "__main__":
    main()
