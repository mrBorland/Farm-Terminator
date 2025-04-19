import requests
import json
import time

BSC_API_KEY = "FIJE4FIC166ANVPX6ZQVP3CMDBHND4S256"  # твій ключ
ACCOUNTS_FILE = "data/accounts_crypto_bound.json"
SLEEP_TIME = 0.2  # затримка між запитами
OUTPUT_LOG = "logs/wallet_balances.log"

def get_bnb_balance(address):
    url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&apikey={BSC_API_KEY}"
    try:
        response = requests.get(url)
        result = response.json()
        if result["status"] == "1":
            return int(result["result"]) / 1e18
        else:
            return None
    except:
        return None

def main():
    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
        wallets = json.load(f)

    total_balance = 0
    lines = []
    for acc in wallets:
        address = acc.get("wallet")
        if not address:
            continue
        balance = get_bnb_balance(address)
        if balance is not None:
            lines.append(f"{address} → {balance:.6f} BNB")
            total_balance += balance
        else:
            lines.append(f"{address} → Помилка запиту")
        time.sleep(SLEEP_TIME)

    with open(OUTPUT_LOG, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
        f.write(f"\nЗагальний баланс: {total_balance:.6f} BNB\n")

    print(f"[✓] Баланси зібрано. Загальний: {total_balance:.6f} BNB")

if __name__ == "__main__":
    main()
