#!/usr/bin/env bash
set -e

# Шляхи до вихідних та цільових файлів
SRC_CRYPTO="data/accounts_crypto_autogen.json"
DST_CRYPTO="data/accounts_crypto.json"
SRC_YT="data/accounts_youtube_autogen.json"
DST_YT="data/accounts_youtube.json"

echo "[auto_fix_accounts] Старт…"

if [[ -f "$SRC_CRYPTO" ]]; then
  echo "[auto_fix_accounts] Оновлюю CRYPTO акаунти..."
  # Витягуємо масив "accounts" і записуємо у dst
  jq '.accounts' "$SRC_CRYPTO" > "$DST_CRYPTO"
  echo "[auto_fix_accounts] Записано $DST_CRYPTO"
else
  echo "[auto_fix_accounts] Помилка: $SRC_CRYPTO не знайдено" >&2
fi

if [[ -f "$SRC_YT" ]]; then
  echo "[auto_fix_accounts] Оновлюю YOUTUBE акаунти..."
  jq '.accounts' "$SRC_YT" > "$DST_YT"
  echo "[auto_fix_accounts] Записано $DST_YT"
else
  echo "[auto_fix_accounts] Помилка: $SRC_YT не знайдено" >&2
fi

echo "[auto_fix_accounts] Готово."
