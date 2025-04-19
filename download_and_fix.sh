#!/usr/bin/env bash
set -euo pipefail
set -x

# 1) Оновлюємо код із GitHub
echo "[1/4] Оновлюємо код із GitHub…"
git fetch origin main
git reset --hard origin/main

# 2) Завантажуємо нові акаунти
echo "[2/4] Завантажую акаунти…"
mkdir -p data
wget -qO data/accounts_crypto_autogen.json \
  https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_crypto_autogen.json
wget -qO data/accounts_youtube_autogen.json \
  https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/data/accounts_youtube_autogen.json
echo "[download_accounts] Готово."

# 3) Патчимо auto_fix_accounts.sh, щоб працював з новим JSON
echo "[3/4] Переводжу jq-вирази в auto_fix_accounts.sh…"
# якщо jq не встановлено — ставимо
if ! command -v jq &> /dev/null; then
  echo "  – jq не знайдено, встановлюю…"
  pkg update -y
  pkg install -y jq
fi
# Припустимо, що auto_fix_accounts.sh читає .accounts[] — виправимо на просто []
sed -i 's/\.accounts//g; s/$/,/g' auto_fix_accounts.sh || true
echo "[auto_fix_accounts] Патч застосовано."

# 4) Запускаємо авто‑фікс та стартуємо бота
echo "[4/4] Запускаю auto_fix_accounts.sh та main_autofarm.sh…"
chmod +x auto_fix_accounts.sh main_autofarm.sh
./auto_fix_accounts.sh
./main_autofarm.sh
