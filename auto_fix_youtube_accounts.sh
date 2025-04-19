#!/bin/bash

# Перевірка наявності файлів акаунтів для YouTube
echo "[INFO] Перевіряємо наявність файлів акаунтів для YouTube..."
if [ ! -f "~/fixbot/Mainingbotrobot/data/accounts_youtube.json" ]; then
  echo "[INFO] Файл accounts_youtube.json не знайдено. Завантажуємо нові акаунти..."
  ./download_accounts.sh
else
  echo "[INFO] Файл accounts_youtube.json знайдено. Перевіряємо кількість акаунтів..."
  youtube_accounts_count=$(cat ~/fixbot/Mainingbotrobot/data/accounts_youtube.json | jq '.accounts | length')
  echo "[INFO] Кількість акаунтів YouTube: $youtube_accounts_count"
fi

# Завантажуємо акаунти для YouTube, якщо їх нема
if [ "$youtube_accounts_count" -eq 0 ]; then
  echo "[INFO] Завантажуємо нові акаунти YouTube..."
  ./download_accounts.sh
fi

# Перевірка і оновлення акаунтів
echo "[INFO] Оновлюємо акаунти YouTube..."
./auto_fix_accounts.sh

echo "[INFO] Все готово! Акаунти оновлені та перевірені."

