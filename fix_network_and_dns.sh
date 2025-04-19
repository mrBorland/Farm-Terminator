#!/data/data/com.termux/files/usr/bin/bash

echo "[DNS FIX] Починаємо виправлення інтернету та DNS..."

# Крок 1: Встановити resolv-conf, якщо не встановлений
pkg install -y resolv-conf

# Крок 2: Записати DNS Google
echo "nameserver 8.8.8.8" > $PREFIX/etc/resolv.conf
echo "[DNS FIX] DNS змінено на 8.8.8.8"

# Крок 3: Перевірити доступ до polygon-rpc.com
ping -c 2 polygon-rpc.com > /dev/null 2>&1

if [ $? -eq 0 ]; then
  echo "[DNS FIX] Успішно! polygon-rpc.com доступний."
else
  echo "[DNS FIX] Помилка! Схоже, що інтернет або DNS ще не працює."
  echo "Можливо, потрібне VPN-з'єднання або стабільне Wi-Fi підключення."
fi
