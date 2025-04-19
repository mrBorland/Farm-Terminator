import subprocess
import datetime
import requests

# === Налаштування ===
TELEGRAM_BOT_TOKEN = "6490535850:AAF2SR-NkkGJ4uPGtSdyW_4Ifwbi0Pr2lBE"
TELEGRAM_CHAT_ID = "592531953"
FARM_LOG_PATH = "/data/data/com.termux/files/home/fixbot/Mainingbotrobot/farm_log.txt"
FARM_SCRIPT_PATH = "/data/data/com.termux/files/home/fixbot/Mainingbotrobot/run_autofarm.sh"

# === Запускаємо фарм ===
with open(FARM_LOG_PATH, "a") as log:
    log.write(f"\n[{datetime.datetime.now()}] --- FARM START ---\n")

subprocess.run(["bash", FARM_SCRIPT_PATH])

# === Отримуємо останній рядок логів ===
try:
    with open(FARM_LOG_PATH, "r") as f:
        lines = f.readlines()
        last_lines = "".join(lines[-20:])  # останні 20 рядків
except FileNotFoundError:
    last_lines = "farm_log.txt не знайдено"

# === Надсилаємо в Telegram ===
message = f"[AutoFarmBot] Фарм завершено:\n\n{last_lines}"
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})
