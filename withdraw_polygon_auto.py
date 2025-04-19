
import json
import requests
import time
from datetime import datetime

RPC = "https://polygon-rpc.com"
DESTINATION = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"
MIN_BALANCE = 0.05
LOG_FILE = "logs/polygon_withdraw.log"

def get_balance(address):
    data = {
        "jsonrpc":"2.0",
        "method":"eth_getBalance",
        "params":[address, "latest"],
        "id":1
    }
    try:
        r = requests.post(RPC, json=data, timeout=10).json()
        balance_wei = int(r["result"], 16)
        return balance_wei / 1e18
    except Exception as e:
        return -1

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def simulate_withdraw(from_address, privkey, amount):
    log(f"→ (SIMULATED) Вивід {amount:.4f} MATIC з {from_address} → {DESTINATION}")

def main():
    with open("wallets_polygon.json") as f:
        wallets = json.load(f)

    total_balance = 0
    total_withdrawn = 0
    count = 0

    print("===== Старт автозняття MATIC =====")
    for w in wallets:
        address = w["address"]
        privkey = w["private_key"]
        balance = get_balance(address)
        if balance == -1:
            log(f"✖ {address}: неможливо отримати баланс.")
            continue
        total_balance += balance
        if balance >= MIN_BALANCE:
            simulate_withdraw(address, privkey, balance - 0.001)
            total_withdrawn += balance - 0.001
            count += 1
        else:
            log(f"• {address}: баланс {balance:.4f} MATIC (менше {MIN_BALANCE})")

    print(f"→ Оброблено: {len(wallets)} гаманців")
    print(f"→ Загальний баланс: {total_balance:.4f} MATIC")
    print(f"→ Виведено: {total_withdrawn:.4f} MATIC з {count} гаманців")
    log(f"Завершено: {count} виводів, {total_withdrawn:.4f} MATIC виведено.")

if __name__ == "__main__":
    main()
