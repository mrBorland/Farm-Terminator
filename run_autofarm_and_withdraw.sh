#!/data/data/com.termux/files/usr/bin/bash

echo "===== Старт повного фарму ====="
date

# Крок 1: Galxe фарм
python3 modules/crypto/galxe_farm.py

# Крок 2: Перевірка балансу
python3 check_polygon_balance_auto.py

# Крок 3: Автовивід MATIC
python3 withdraw_polygon_auto.py

# Крок 4: Telegram-звіт
python3 auto_reporter.py
