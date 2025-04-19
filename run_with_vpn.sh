#!/bin/bash

echo "[VPN] Запускаємо WireGuard..."
bash /data/data/com.termux/files/home/start_vpn.sh

sleep 5

echo "[BALANCE] Перевіряємо баланс Polygon-гаманців..."
python3 check_polygon_balance.py

echo "[WITHDRAW] Виводимо зароблене на основний гаманець..."
python3 withdraw_polygon_nolib.py
