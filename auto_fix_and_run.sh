#!/bin/bash

echo "[INFO] Оновлюємо код із GitHub..."
git fetch origin main
git reset --hard origin/main

echo "[INFO] Завантажуємо нові акаунти..."
# Перевіряємо наявність акаунтів і завантажуємо їх, якщо їх нема
if [ ! -f "~/fixbot/Mainingbotrobot/data/accounts_crypto_autogen.json" ]; then
    echo "[INFO] Завантаження акаунтів CRYPTO..."
    wget -qO ~/fixbot/Mainingbotrobot/data/accounts_crypto_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_crypto_autogen.json
else
    echo "[INFO] Акаунти CRYPTO вже є. Продовжуємо..."
fi

if [ ! -f "~/fixbot/Mainingbotrobot/data/accounts_youtube_autogen.json" ]; then
    echo "[INFO] Завантаження акаунтів YOUTUBE..."
    wget -qO ~/fixbot/Mainingbotrobot/data/accounts_youtube_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_youtube_autogen.json
else
    echo "[INFO] Акаунти YOUTUBE вже є. Продовжуємо..."
fi

# Оновлюємо акаунти
echo "[INFO] Оновлюємо акаунти..."
./auto_fix_accounts.sh

# Запуск AutoFarmBot
echo "[INFO] Запускаємо AutoFarmBot..."
python3 main_autofarm.py

# Логування
echo "[INFO] Перевірка логів..."
cat logs/farm_log.txt

# Завершення
echo "[INFO] Все готово! Фарм запущений."
