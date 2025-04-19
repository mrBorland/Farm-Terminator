#!/data/data/com.termux/files/usr/bin/bash

echo "[DNS FIX] Очищаю попередній конфігураційний файл DNS..."
rm -f $PREFIX/etc/resolv.conf

echo "[DNS FIX] Встановлюю стабільні DNS (1.1.1.1, 8.8.8.8)..."
echo -e "nameserver 1.1.1.1\nnameserver 8.8.8.8" > $PREFIX/etc/resolv.conf

echo "[DNS FIX] Вимикаю IPv6 (опційно)..."
echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6 2>/dev/null || echo "[!] IPv6 disable not supported"

echo "[DNS FIX] Перевіряю доступ до Galxe..."
curl -I https://graphigo.prd.galxe.com/query
