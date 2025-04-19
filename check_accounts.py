import json

# Завантажуємо акаунти
with open("data/accounts_crypto_autogen.json", "r") as file:
    accounts = json.load(file)

# Перевірка акаунтів
for account in accounts:
    print(f"Перевіряємо акаунт: {account['username']}")
    # Додайте тут перевірку балансу або іншого функціоналу для перевірки акаунтів
    # Це може бути API запит або перевірка через платформу
