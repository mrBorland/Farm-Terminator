import requests
import time
from config import OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE, TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN

WITHDRAW_ADDRESS = "TTb8QfyLAsXtTyZZ1SZiCUZt6H6PfJb3Wo"
CHAIN = "TRC20"
CURRENCY = "USDT"
FEE = "1"  # фіксована комісія TRC20 на OKX
MIN_WITHDRAW_AMOUNT = 2  # мінімальна сума для виводу

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})

def withdraw_from_account(account_id, amount):
    if amount < MIN_WITHDRAW_AMOUNT:
        send_telegram(f"На акаунті {account_id} замало для виводу: {amount} USDT")
        return

    url = "https://www.okx.com/api/v5/asset/withdrawal"
    headers = {
        "OK-ACCESS-KEY": OKX_API_KEY,
        "OK-ACCESS-SIGN": "SIGN_HERE",  # тут потрібно поставити підпис через HMAC
        "OK-ACCESS-TIMESTAMP": str(time.time()),
        "OK-ACCESS-PASSPHRASE": OKX_PASSPHRASE,
        "Content-Type": "application/json"
    }

    data = {
        "ccy": CURRENCY,
        "amt": str(amount - float(FEE)),
        "dest": "4",
        "toAddr": WITHDRAW_ADDRESS,
        "fee": FEE,
        "chain": f"{CURRENCY}-{CHAIN}"
    }

    # Тут має бути реальна генерація підпису + логіка перевірки балансу
    send_telegram(f"Мок-вивід {amount} USDT з акаунту {account_id} на {WITHDRAW_ADDRESS}")

# Тест
if __name__ == "__main__":
    withdraw_from_account("Account#1", 5.5)
