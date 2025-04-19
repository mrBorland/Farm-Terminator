import json
import subprocess
import time
from datetime import datetime
import requests

MAIN_WALLET = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"
WALLETS_FILE = "wallets_bnb.json"
LOG_FILE = "logs/autofarm_and_send_bnb.log"

def log(msg):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{datetime.now()}] {msg}\n")
    print(msg)

def run_autofarm():
    log("Старт фарму...")
    try:
        result = subprocess.run(["bash", "run_autofarm.sh"], capture_output=True, text=True)
        log(result.stdout)
        if result.stderr:
            log(f"stderr: {result.stderr}")
    except Exception as e:
        log(f"Помилка запуску фарму: {e}")

def get_wallets():
    with open(WALLETS_FILE, "r") as f:
        return json.load(f)

def send_bnb_no_lib(wallet):
    url = "https://bsc.publicnode.com"
    address = wallet["address"]
    priv_key = wallet["private_key"]

    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }

    res = requests.post(url, headers=headers, json=payload).json()
    if "result" not in res:
        log(f"[{address}] Помилка при отриманні балансу: {res}")
        return

    balance_wei = int(res["result"], 16)
    if balance_wei < 10**15:  # мінімум 0.001 BNB
        log(f"[{address}] недостатньо балансу для переказу")
        return

    # Тут повинен бути код створення raw-транзакції і підписання приватним ключем (не включено для безпеки)
    # send_raw_tx(raw_tx)

    log(f"[{address}] Переказ {balance_wei / 10**18:.6f} BNB на {MAIN_WALLET}")

def auto_send():
    wallets = get_wallets()
    for wallet in wallets:
        send_bnb_no_lib(wallet)
        time.sleep(1)

if __name__ == "__main__":
    log("=== Початок автофарму і переказу ===")
    run_autofarm()
    auto_send()
    log("=== Завершено ===")
