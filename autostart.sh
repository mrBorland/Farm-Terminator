#!/usr/bin/env bash
set -e

# Переходимо в каталог скрипта
cd "$(dirname "$0")"

echo "[1/4] Оновлюємо код із GitHub…"
curl -sL https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/auto_fix_accounts.py -o auto_fix_accounts.py
curl -sL https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/main_autofarm.py       -o main_autofarm.py
curl -sL https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/telegram_report.py    -o telegram_report.py

echo "[2/4] Завантажуємо нові акаунти…"
./download_accounts.sh

echo "[3/4] Авто‑фікс акаунтів…"
python3 auto_fix_accounts.py

echo "[4/4] Запускаємо AutoFarmBot…"
python3 main_autofarm.py
