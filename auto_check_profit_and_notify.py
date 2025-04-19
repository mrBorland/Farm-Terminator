import json
import requests
from datetime import datetime

# Файли та налаштування
accounts_file = "data/accounts_crypto.json"
telegram_token = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
chat_id = "6821675571"
log_file = "logs/profit_report.log"

# Завантаження акаунтів
with open(accounts_file, "r") as f:
    data = json.load(f)

accounts = data.get("accounts", [])
total_profit = 0.0
report_lines = ["[AutoProfit Report]"]

# Оновлення balance та підрахунок
for acc in accounts:
    balance = acc.get("balance", 0.0)
    acc["balance"] = float(balance)
    total_profit += acc["balance"]
    report_lines.append(f"Акаунт: {acc['username']} | {acc['balance']} USDT")

report_lines.append(f"\nЗагалом: {round(total_profit, 2)} USDT")
final_report = "\n".join(report_lines)

# Надсилання в Telegram
requests.post(f"https://api.telegram.org/bot{telegram_token}/sendMessage", data={
    "chat_id": chat_id,
    "text": final_report[:4000]  # обмеження на довжину
})

# Збереження логів
with open(log_file, "a") as log:
    log.write(f"\n{datetime.now()}\n{final_report}\n")

# Оновлення accounts.json
with open(accounts_file, "w") as f:
    json.dump({"accounts": accounts}, f, indent=4)
