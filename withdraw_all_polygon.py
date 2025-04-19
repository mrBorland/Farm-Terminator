from web3 import Web3
import json
import time
import requests

# Підключення до RPC Polygon
w3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))

# Основна адреса для виводу
recipient_address = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"

# Telegram-бот для сповіщень
TELEGRAM_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
TELEGRAM_CHAT_ID = "6821675571"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        requests.post(url, json=payload)
    except:
        pass

# Завантаження гаманців
with open("wallets_polygon.json") as f:
    wallets = json.load(f)

# Вивід з кожного гаманця
for wallet in wallets:
    private_key = wallet["private_key"]
    address = wallet["address"]

    try:
        balance = w3.eth.get_balance(address)
        if balance > w3.to_wei(0.001, "ether"):
            nonce = w3.eth.get_transaction_count(address)
            tx = {
                'nonce': nonce,
                'to': recipient_address,
                'value': balance - w3.to_wei(0.0005, 'ether'),  # залишаємо трохи на gas
                'gas': 21000,
                'gasPrice': w3.to_wei(30, 'gwei'),
                'chainId': 137
            }
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_url = f"https://polygonscan.com/tx/{w3.to_hex(tx_hash)}"
            message = f"✅ {address} → {recipient_address}\nTX: {tx_url}"
            print("[→]", message)
            send_telegram_message(message)
        else:
            msg = f"[×] {address} → баланс < 0.001 MATIC"
            print(msg)
            send_telegram_message(msg)
    except Exception as e:
        error_msg = f"[!] Помилка з {address}: {e}"
        print(error_msg)
        send_telegram_message(error_msg)

    time.sleep(1)
