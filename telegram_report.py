import requests

def send_report(message: str):
    TELEGRAM_BOT_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
    TELEGRAM_CHAT_ID = "6821675571"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        print("[Telegram] Статус надсилання:", response.status_code)
    except Exception as e:
        print("[Telegram] Помилка надсилання:", e)
