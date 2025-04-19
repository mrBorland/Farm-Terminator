#!/usr/bin/env bash
set -e

# Переконаємось, що є каталог data/
mkdir -p data

echo "[download_accounts] Завантажую акаунти CRYPTO…"
curl -sL \
  https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/accounts_crypto_autogen.json \
  -o data/accounts_crypto_autogen.json

echo "[download_accounts] Завантажую акаунти YOUTUBE…"
curl -sL \
  https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/accounts_youtube_autogen.json \
  -o data/accounts_youtube_autogen.json

echo "[download_accounts] Готово."
