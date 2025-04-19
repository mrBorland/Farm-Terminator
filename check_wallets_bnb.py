import json
import os

FILE_PATH = "wallets_bnb.json"

print("===== АвтоПеревірка файлу wallets_bnb.json =====")

# Перевіряємо чи існує файл
if not os.path.exists(FILE_PATH):
    print(f"[!] Файл не знайдено: {FILE_PATH}")
    exit(1)

# Спроба відкрити і прочитати JSON
try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        wallets = json.load(f)
except UnicodeDecodeError:
    print("[!] Помилка: файл не в UTF-8. Виправ у редакторі як plain UTF-8.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"[!] JSON помилка: {e}")
    exit(1)

# Перевірка структури
valid = True
for i, w in enumerate(wallets):
    if not isinstance(w, dict) or "address" not in w or "private_key" not in w:
        print(f"[!] Некоректна структура в об'єкті #{i+1}: {w}")
        valid = False
        break

if not valid:
    exit(1)

# Вивід кількості
print(f"[✓] Валідний файл JSON з {len(wallets)} гаманцями.")
if len(wallets) < 250:
    print("[!] Увага: менше ніж 250 гаманців.")
elif len(wallets) > 250:
    print("[!] Увага: більше ніж 250 гаманців.")
else:
    print("[✓] Все ок: 250 гаманців є.")

print("===============================================")
