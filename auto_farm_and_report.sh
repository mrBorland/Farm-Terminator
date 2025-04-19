#!/bin/bash

# Оновлення коду з GitHub
echo "[1/4] Оновлюємо код із GitHub..."
git fetch origin main
git reset --hard origin/main

# Завантаження акаунтів
echo "[2/4] Завантажуємо нові акаунти..."
mkdir -p data
wget -qO data/accounts_crypto_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_crypto_autogen.json
wget -qO data/accounts_youtube_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_youtube_autogen.json

# Оновлення акаунтів
echo "[3/4] Оновлюємо акаунти..."
python3 ./auto_fix_accounts.py

# Запуск AutoFarmBot
echo "[4/4] Запускаємо AutoFarmBot..."
python3 main_autofarm.py

# Підрахунок заробленого
echo "[INFO] Підраховуємо прибуток..."
# Додати код для підрахунку прибутку з ваших платформ (якщо є логіка для цього)
#!/bin/bash

# Дані для Telegram
TELEGRAM_TOKEN="7626770291:AAG3UC1h3vt1aR9h0ALAqg3oo9RlvsMGSzI"
CHAT_ID="6821675571"
API_URL="https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage"

# Оновлення коду з GitHub
echo "[1/4] Оновлюємо код із GitHub..."
git fetch origin main
git reset --hard origin/main

# Завантаження нових акаунтів
echo "[2/4] Завантажуємо нові акаунти..."
mkdir -p data
wget -qO data/accounts_crypto_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_crypto_autogen.json
wget -qO data/accounts_youtube_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_youtube_autogen.json

# Оновлення акаунтів
echo "[3/4] Оновлюємо акаунти..."
python3 auto_fix_accounts.py

# Запуск AutoFarmBot
echo "[4/4] Запускаємо AutoFarmBot..."
python3 main_autofarm.py

# Перевірка прибутку
echo "[INFO] Перевіряємо прибуток..."

# Приклад підрахунку балансу (потрібно замінити на реальну логіку)
# Для демонстрації ми просто рахуємо кількість акаунтів на крипто-платформі
CRYPTO_ACCOUNTS=$(cat data/accounts_crypto.json | jq '.accounts | length')
YOUTUBE_ACCOUNTS=$(cat data/accounts_youtube.json | jq '.accounts | length')

# Припустимо, що для кожного акаунту ми отримуємо певну суму (наприклад, $0.5 за акаунт)
CRYPTO_PROFIT=$(($CRYPTO_ACCOUNTS * 0.5))  # Для прикладу $0.5 за акаунт
YOUTUBE_PROFIT=$(($YOUTUBE_ACCOUNTS * 0.3))  # Для прикладу $0.3 за акаунт

# Загальний прибуток
TOTAL_PROFIT=$(($CRYPTO_PROFIT + $YOUTUBE_PROFIT))

# Створення повідомлення для Telegram
SEND_MESSAGE="Звіт AutoFarmBot:\n\n- Кількість акаунтів на Crypto платформі: $CRYPTO_ACCOUNTS\n- Прибуток від Crypto: \$${CRYPTO_PROFIT}\n\n- Кількість акаунтів на YouTube: $YOUTUBE_ACCOUNTS\n- Прибуток від YouTube: \$${YOUTUBE_PROFIT}\n\nЗагальний прибуток: \$${TOTAL_PROFIT}"

# Надсилаємо повідомлення в Telegram
curl -s -X POST $API_URL -d "chat_id=$CHAT_ID" -d "text=$SEND_MESSAGE"

echo "[INFO] Завершено!"
