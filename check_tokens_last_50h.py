import json
import time
from web3 import Web3
from datetime import datetime, timedelta

# Підключення до BSC (можна змінити на інший RPC, якщо треба)
BSC_RPC = "https://bsc-dataseed.binance.org"
web3 = Web3(Web3.HTTPProvider(BSC_RPC))

# Завантаження гаманців
with open("wallets_bnb.json") as f:
    wallets = json.load(f)

# Часова межа — останні 50 годин
current_time = int(time.time())
time_50h_ago = current_time - 50 * 60 * 60

def check_transfers(address):
    print(f"\n[+] Перевірка: {address}")
    # Отримання транзакцій (тільки останні 1000 для оптимізації)
    try:
        url = f"https://api.bscscan.com/api?module=account&action=tokentx&address={address}&sort=desc"
        import requests
        response = requests.get(url)
        data = response.json()
        for tx in data["result"]:
            if int(tx["timeStamp"]) >= time_50h_ago:
                ts = datetime.utcfromtimestamp(int(tx["timeStamp"]))
                print(f"  - {tx['tokenName']} ({tx['tokenSymbol']}): +{int(tx['value']) / 10**int(tx['tokenDecimal'])} at {ts}")
    except Exception as e:
        print("  [!] Помилка:", e)

# Перевірка кожного гаманця
for wallet in wallets:
    check_transfers(wallet["address"])
