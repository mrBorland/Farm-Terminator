#!/bin/bash
echo "===== Старт повного фарму ====="
date

# Запуск Galxe фарму
python3 modules/crypto/galxe_farm.py

# Перевірка балансу Polygon
python3 check_polygon_balance_auto.py

# Вивід MATIC
python3 withdraw_polygon_auto.py

# Автоматичний звіт
python3 auto_reporter.py

echo "===== Фарм завершено ====="
date
