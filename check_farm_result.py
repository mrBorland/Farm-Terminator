
import re

LOG_FILE = 'logs/farm_log.txt'

try:
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("❌ Лог-файл не знайдено.")
    exit()

# Знайдемо всі рядки з USDT прибутком
profit_lines = [line for line in lines if '→ +' in line and 'USDT' in line]
total_profit = 0

print("===== Звіт GalxeFarm (останній запуск) =====")
for line in profit_lines[-50:]:  # останні 50 дій
    print(line.strip())
    match = re.search(r'→ \+([0-9.]+) USDT', line)
    if match:
        total_profit += float(match.group(1))

print(f"---------------------------------------------")
print(f"Загальний прибуток за звіт: {round(total_profit, 2)} USDT")
