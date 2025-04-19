import json
import os
from datetime import datetime
import random
import time

LOG_FILE = "farm_log.txt"
ACCOUNTS_FILE = "accounts_galxe.json"

def log(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{datetime.now()}] {message}\n")
    print(message)

def simulate_task(account):
    # Тут вставляється реальна логіка фарму
    time.sleep(random.uniform(0.5, 1.5))  # симуляція затримки
    success = random.choice([True, False, False])  # 33% шанс на успіх
    return "SUCCESS" if success else "FAILED"

def main():
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()
    log("--- GALXE FARM SESSION STARTED ---")

    if not os.path.exists(ACCOUNTS_FILE):
        log("ERROR: accounts_galxe.json not found!")
        return

    with open(ACCOUNTS_FILE, "r") as f:
        accounts = json.load(f)

    for idx, account in enumerate(accounts):
        username = account.get("username", f"acc_{idx}")
        wallet = account.get("wallet", "N/A")
        proxy = account.get("proxy", "N/A")

        try:
            result = simulate_task(account)
            log(f"{username} | Wallet: {wallet} | Proxy: {proxy} -> {result}")
        except Exception as e:
            log(f"{username} -> ERROR: {str(e)}")

    log("--- GALXE FARM SESSION ENDED ---\n")

if __name__ == "__main__":
    main()
