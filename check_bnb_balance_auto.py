import json
import requests
from datetime import datetime
import os

WALLETS_FILE = "wallets_bnb.json"
RPC = "https://bsc-dataseed.binance.org/"
LOG_FILE = "logs/bnb_balance.log"

def get_balance(address):
    try:
        data = {
            "jsonrpc":"2.0",
            "method":"eth_getBalance",
            "params":[address, "latest"],
            "id":1
        }
        r = requests.post(RPC, json=data, timeout=10)
        result = int(r.json()["result"], 16) / 1e18
        return round(result, 6)
    except:
        return 0.0

def check_all():
    if not os.path.exists("logs"):
        os.mkdir("logs")
    with open(WALLETS_FILE, "r") as f:
        wallets = json.load(f)
    total = 0.0
    log_lines = []
    for i, w in enumerate(wallets, 1):
        bal = get_balance(w["address"])
        total += bal
        line = f"[{i}] {w['address']} → {bal} BNB"
        print(line)
        log_lines.append(line)

    summary = f"\n===== Звіт BNB Balance =====\nДата: {datetime.now()}\nЗагальна кількість: {len(wallets)}\nЗагальний баланс: {total:.6f} BNB\n"
    print(summary)
    log_lines.append(summary)

    with open(LOG_FILE, "a") as f:
        f.write("\n".join(log_lines) + "\n")

if __name__ == "__main__":
    print("===== Запуск перевірки балансу BNB-гаманців =====")
    check_all()
