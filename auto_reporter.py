import json
from datetime import datetime

# Шляхи до логів
polygon_log = "logs/polygon_balance.log"
galxe_log = "logs/galxe_farm.log"
youtube_log = "logs/youtube_farm.log"

def read_last_balance(log_path):
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in reversed(lines):
                if "Загальний баланс:" in line:
                    return float(line.split(":")[1].strip().split()[0])
    except:
        return 0.0
    return 0.0

def read_last_profit(log_path):
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in reversed(lines):
                if "Загальний прибуток за звіт:" in line:
                    return float(line.split(":")[1].strip().split()[0])
    except:
        return 0.0
    return 0.0

polygon_balance = read_last_balance(polygon_log)
galxe_profit = read_last_profit(galxe_log)
youtube_profit = read_last_profit(youtube_log)

total_profit = polygon_balance + galxe_profit + youtube_profit

# Формування фінального звіту
report = f"""===== АвтоЗвіт за {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} =====
→ [Galxe] Прибуток: {galxe_profit:.2f} USDT
→ [YouTube] Прибуток: {youtube_profit:.2f} USDT
→ [Polygon] Баланс: {polygon_balance:.2f} MATIC

💰 Загальний прибуток: {total_profit:.2f} USDT (з урахуванням балансу)
====================================================
"""

# Збереження
with open("logs/auto_profit_report.log", "a", encoding="utf-8") as f:
    f.write(report + "\n")

# Вивід
print(report)
