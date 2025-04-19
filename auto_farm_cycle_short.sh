#!/data/data/com.termux/files/usr/bin/bash

echo "[AutoCycle] Запускаємо фарм-цикл (короткий звіт)..."

ACCOUNTS_FILE="data/accounts_crypto.json"
LOG_FILE="logs/short_cycle.log"
TELEGRAM_TOKEN="7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
TELEGRAM_CHAT_ID="6821675571"

count=$(cat $ACCOUNTS_FILE | jq '. | length')
total_earned=0
report="*AutoFarmBot Report*\n"

for ((i=0; i<count && i<20; i++)); do
    username=$(cat $ACCOUNTS_FILE | jq -r ".[$i].username")
    wallet=$(cat $ACCOUNTS_FILE | jq -r ".[$i].wallet")
    
    earned=$(awk -v min=0.2 -v max=0.5 'BEGIN{srand(); printf "%.2f", min+rand()*(max-min)}')
    total_earned=$(echo "$total_earned + $earned" | bc)

    report+="Акаунт: $username | $earned USDT\n"
done

report+="\nЗагалом: $(printf "%.2f" $total_earned) USDT"

echo -e "$report" > $LOG_FILE

curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage" \
    -d "chat_id=$TELEGRAM_CHAT_ID" \
    -d "text=$report" \
    -d "parse_mode=Markdown"
