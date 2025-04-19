#!/bin/bash

# 1/4: Оновлюємо код з GitHub
echo "[1/4] Оновлюємо код із GitHub..."
git fetch origin main
git reset --hard origin/main

# 2/4: Завантажуємо нові акаунти
echo "[2/4] Завантажуємо нові акаунти..."
mkdir -p data
wget -qO data/accounts_crypto_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_crypto_autogen.json

# Завантажуємо акаунти YouTube
echo "[2/4] Завантажуємо акаунти YOUTUBE..."
wget -qO data/accounts_youtube_autogen.json https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_youtube_autogen.json

# 3/4: Оновлюємо акаунти
echo "[3/4] Оновлюємо акаунти..."
./auto_fix_accounts.sh

# 4/4: Запускаємо AutoFarmBot
echo "[4/4] Запускаємо AutoFarmBot..."
python3 main_autofarm.py

# Аналіз заробітку
echo "Оцінка заробітку..."
python3 account_analysis.py

echo "[INFO] Усі платформи проаналізовано і фарминг успішно виконано."
