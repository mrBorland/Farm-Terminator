<<<<<<< HEAD
import json
import os
from telegram_report import send_report

# Шлях до логів та акаунтів
crypto_file = "data/accounts_crypto.json"
youtube_file = "data/accounts_youtube.json"
log_file = "logs/farm_log.txt"

def count_accounts(filepath):
    if not os.path.exists(filepath):
        return 0
    with open(filepath, "r") as f:
        try:
            data = json.load(f)
            return len(data.get("accounts", []))
        except:
            return 0

def parse_profit(log_path):
    total = 0
    if not os.path.exists(log_path):
        return 0
    with open(log_path, "r") as f:
        for line in f:
            if "Зароблено" in line:
                parts = line.strip().split()
                for p in parts:
                    if "USDT" in p or "$" in p:
                        try:
                            num = float(p.replace("USDT", "").replace("$", "").replace(",", ""))
                            total += num
                        except:
                            continue
    return total

def main():
    crypto_count = count_accounts(crypto_file)
    youtube_count = count_accounts(youtube_file)
    profit = parse_profit(log_file)

    message = (
        f"[Звіт AutoFarmBot]\n"
        f"- Крипто акаунтів: {crypto_count}\n"
        f"- YouTube акаунтів: {youtube_count}\n"
        f"- Загальний прибуток: {profit:.2f} USDT"
    )

    print(message)
    send_report(message)

if __name__ == "__main__":
    main()
=======
import os import json import datetime from telegram_report import send_report

def run_script(script_path): print(f"[RUN] {script_path}") result = os.system(f"python {script_path}") return result

def count_accounts(): count = 0 if os.path.exists("data/accounts_crypto.json"): with open("data/accounts_crypto.json") as f: try: data = json.load(f) if isinstance(data, dict) and "accounts" in data: count += len(data["accounts"]) except json.JSONDecodeError: pass if os.path.exists("data/accounts_youtube.json"): with open("data/accounts_youtube.json") as f: try: data = json.load(f) if isinstance(data, dict) and "accounts" in data: count += len(data["accounts"]) except json.JSONDecodeError: pass return count

def parse_earnings(): total = 0.0 if os.path.exists("logs/farm_log.txt"): with open("logs/farm_log.txt", "r") as f: for line in f: if "Earned:" in line: try: amount = float(line.strip().split("Earned:")[-1].replace("$", "").strip()) total += amount except: continue return round(total, 2)

def append_log(text): with open("logs/farm_log.txt", "a") as log: log.write(f"{datetime.datetime.now()} - {text}\n")

print("[START] AutoFarmBot — запуск усiх напрямкiв")

platforms = [ "modules/crypto/galxe_farm.py", "modules/crypto/zealy_farm.py", "modules/crypto/taskon_farm.py", "modules/crypto/questn_farm.py", "modules/crypto/port3_farm.py", "modules/crypto/openblock_farm.py", "modules/clickfarm/smart_click_farm_v2.py", "modules/youtube/youtube_smart_bot_v3.py", "modules/nft/nft_monitor.py", ]

for script in platforms: run_script(script)

accounts_total = count_accounts() earnings_total = parse_earnings()

report = f"[AutoFarmBot ✨]\n\n🔢 Кiлькiсть акаунтiв: {accounts_total}\n💰 Загальний прибуток: ${earnings_total}" send_report(report) append_log(f"Accounts: {accounts_total}, Earned: ${earnings_total}")

print("[WAIT] Чекаємо 6 годин до наступного запуску...")

>>>>>>> d49b200 (Create auto_farm_reporter.py)
