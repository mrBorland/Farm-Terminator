#!/data/data/com.termux/files/usr/bin/bash

echo "[AutoCycle] Старт циклу фарму..."

total_usdt=0
report=""

accounts_file=~/fixbot/Mainingbotrobot/data/accounts_crypto.json
report_file=~/fixbot/Mainingbotrobot/logs/auto_cycle_log.txt

if [ ! -f "$accounts_file" ]; then
  echo "[ERROR] Файл акаунтів не знайдено: $accounts_file"
  exit 1
fi

length=$(cat $accounts_file | jq length)

for (( i=0; i<$length; i++ ))
do
  username=$(jq -r ".[$i].username" $accounts_file)
  wallet=$(jq -r ".[$i].wallet" $accounts_file)

  echo "[AutoCycle] Фарм для $username ($wallet)..."

  usdt=$(python3 ~/fixbot/Mainingbotrobot/auto_farm_reporter.py "$wallet" | grep "USDT:" | awk '{print $NF}')
  report+="Акаунт: $username | $usdt USDT\n"

  total_usdt=$(echo "$total_usdt + $usdt" | bc)
done

final_msg="[AutoCycle] Звіт фарму\n$report\nЗагалом: $total_usdt USDT"

echo -e "$final_msg" | tee -a "$report_file"

# Надсилання в Telegram
curl -s -X POST https://api.telegram.org/bot7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI/sendMessage \
  -d chat_id=6821675571 \
  -d text="$final_msg"
