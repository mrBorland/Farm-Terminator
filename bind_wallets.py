import json

# Завантажуємо акаунти та гаманці
with open("data/accounts_crypto_autogen.json") as f:
    accounts = json.load(f)

with open("wallets_bnb.json") as f:
    wallets = json.load(f)

# Перевірка кількості гаманців та акаунтів
assert len(wallets) >= len(accounts), "Недостатньо гаманців для всіх акаунтів!"

# Прив'язуємо гаманці до акаунтів
for i, account in enumerate(accounts):
    account['wallet'] = wallets[i]['address']

# Зберігаємо оновлені акаунти
with open("data/accounts_crypto_bound.json", "w") as f:
    json.dump(accounts, f, indent=4)

print(f"Прив'язано {len(accounts)} акаунтів до справжніх гаманців.")
