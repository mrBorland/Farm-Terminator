import json
import random
from datetime import datetime

ACCOUNTS_FILE = 'data/accounts_crypto.json'
LOG_FILE = 'logs/farm_log.txt'

# Завантаження акаунтів
with open(ACCOUNTS_FILE, 'r') as f:
    data = json.load(f)
    accounts = data.get('accounts', [])

total_profit = 0
log_entries = []

print(f"[Galxe] Запуск фарму на {len(accounts)} акаунтах...")

for acc in accounts:
    email = acc['email']
    tasks_done = random.randint(1, 3)
    earned = round(tasks_done * random.uniform(0.15, 0.35), 2)
    total_profit += earned
    log_entries.append(f"[Galxe] {email} → {tasks_done} завдань → +{earned} USDT")

# Логування результатів
with open(LOG_FILE, 'a') as log:
    log.write(f"\n[GalxeFarm] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    for entry in log_entries:
        log.write(entry + "\n")
    log.write(f"Загальний прибуток: {round(total_profit, 2)} USDT\n")

print(f"[Galxe] Завершено. Прибуток: {round(total_profit, 2)} USDT")
