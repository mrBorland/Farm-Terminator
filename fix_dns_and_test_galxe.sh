#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Встановлюємо залежності..."
pkg update -y && pkg install -y resolv-conf dnsutils curl

echo "[+] Видаляємо старий resolv.conf..."
rm -f $PREFIX/etc/resolv.conf

echo "[+] Створюємо новий resolv.conf..."
echo -e "nameserver 1.1.1.1\nnameserver 8.8.8.8" > $PREFIX/etc/resolv.conf

echo "[+] Перевіряємо DNS доступність graphigo.prd.galxe.com..."
if curl -s --head https://graphigo.prd.galxe.com/query | grep "200 OK" > /dev/null; then
    echo "[OK] graphigo.prd.galxe.com доступний!" | tee -a logs/network_fix.log
else
    echo "[ERROR] graphigo.prd.galxe.com НЕ доступний! DNS все ще не працює!" | tee -a logs/network_fix.log
    echo "Можливо, потрібен VPN або проксі."
fi

echo "[✓] Скрипт завершено."
