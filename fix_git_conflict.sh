#!/bin/bash

echo "[FIX] Автоматичне вирішення конфлікту..."

# Підтягуємо правильну версію
echo "[FIX] Вставляємо версію з репозиторію..."
curl -s https://raw.githubusercontent.com/mrBorland/Mainingbotrobot/main/fix_git_checkout.sh -o fix_git_checkout.sh

# Додаємо і комітимо з повідомленням
git add fix_git_checkout.sh
GIT_EDITOR=true git rebase --continue || git commit -m "Auto-resolved conflict in fix_git_checkout.sh"

# Пул щоб уникнути non-fast-forward
echo "[GIT] Оновлюємо локальну гілку..."
git pull origin main --rebase

# Пуш
echo "[GIT] Пуш в main..."
git push origin main --force

echo "[DONE] Все оновлено і запушено!"
