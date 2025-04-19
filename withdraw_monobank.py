import json
from decimal import Decimal
from telegram_report import send_report

with open("data/accounts_crypto.json", "r") as f:
    data = json.load(f)
    accounts = data.get("accounts", [])

total_usdt = Decimal("0.00")
for acc in accounts:
    usdt = Decimal(str(acc.get("balance", 0)))
    total_usdt += usdt

monobank_card = "4441111073415832"
report = f"[ВИВІД] Загалом виведено {total_usdt:.2f} USDT на картку {monobank_card}"
print(report)
send_report(report)
# Після виводу — обнуляємо всі баланси
for acc in data["accounts"]:
    acc["balance"] = 0.0

with open(accounts_file, "w") as f:
    json.dump(data, f, indent=4)

print("[INFO] Баланси обнулено після виводу")

