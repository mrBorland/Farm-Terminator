
import requests

TELEGRAM_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
CHAT_ID = "6821675571"

def send_report():
    try:
        with open("youtube_view_log.txt", "r") as f:
            log_content = f.read()
    except:
        log_content = "Лог не знайдено або порожній."

    report_text = f"[YouTube Bot Report]\n{log_content}"

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": report_text
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("[Telegram] Помилка надсилання звіту:", e)
