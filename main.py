from utils import get_usdt_balance
from config import TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN
import requests

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})

def farm_galxe():
    print("Фарм на Galxe...")
    send_telegram("✅ Galxe фарм завершено (тест).")

def farm_okx():
    print("Фарм на OKX...")
    send_telegram("✅ OKX фарм завершено (тест).")

def farm_taskon():
    print("Фарм на TaskOn...")
    send_telegram("✅ TaskOn фарм завершено (тест).")

if __name__ == "__main__":
    send_telegram("🚀 Починаю фарм на всіх платформах...")
    farm_galxe()
    farm_okx()
    farm_taskon()
    balance = get_usdt_balance()
    send_telegram(f"💰 Поточний баланс після фарму: {balance} USDT")
