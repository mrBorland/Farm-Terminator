#!/data/data/com.termux/files/usr/bin/bash

echo "[BACKUP] Створюємо резервну копію..."
mkdir -p ~/fixbot/Mainingbotrobot/backup
mv ~/fixbot/Mainingbotrobot/README.md ~/fixbot/Mainingbotrobot/backup/ 2>/dev/null
mv ~/fixbot/Mainingbotrobot/accounts_crypto_autofix.json ~/fixbot/Mainingbotrobot/backup/ 2>/dev/null
mv ~/fixbot/Mainingbotrobot/main_autofarm.py ~/fixbot/Mainingbotrobot/backup/ 2>/dev/null
mv ~/fixbot/Mainingbotrobot/mainingbot_autofix_all_platforms.zip ~/fixbot/Mainingbotrobot/backup/ 2>/dev/null
mv ~/fixbot/Mainingbotrobot/nft_autofix.zip ~/fixbot/Mainingbotrobot/backup/ 2>/dev/null
mv ~/fixbot/Mainingbotrobot/telegram_report.py ~/fixbot/Mainingbotrobot/backup/ 2>/dev/null

echo "[GIT] Перемикаємося на гілку main..."
cd ~/fixbot/Mainingbotrobot
git checkout -t origin/main

echo "[RESTORE] Повертаємо файли назад..."
mv ~/fixbot/Mainingbotrobot/backup/* ~/fixbot/Mainingbotrobot/ 2>/dev/null
rm -r ~/fixbot/Mainingbotrobot/backup

echo "[DONE] Успішно завершено!"
