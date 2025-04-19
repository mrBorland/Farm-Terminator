#!/data/data/com.termux/files/usr/bin/bash

echo "[DNSProxyFarm] Старт із DNS проксі..."

# Встановлюємо DNS вручну
echo -e "nameserver 1.1.1.1\nnameserver 8.8.8.8" > $PREFIX/etc/resolv.conf

# Перевіряємо доступність Galxe
curl -s --head https://graphigo.prd.galxe.com/query | head -n 1 | grep "200 OK" > /dev/null
if [ $? -ne 0 ]; then
    echo "[DNSProxyFarm] Galxe недоступний. Можлива проблема з DNS."
    termux-notification --title "Farm Bot" --content "Galxe недоступний. DNS не працює." --priority high
    exit 1
fi

echo "[DNSProxyFarm] Galxe доступний. Запускаємо фарм..."

# Запуск Galxe
python3 modules/crypto/galxe_farm.py

# Можеш додати інші платформи, наприклад:
# python3 modules/crypto/zealy_farm.py
# python3 modules/crypto/taskon_farm.py

echo "[DNSProxyFarm] Завершено."
termux-notification --title "Farm Bot" --content "Фарм через DNS проксі завершено!" --priority high
