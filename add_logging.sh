#!/bin/bash

# Шлях до вашого проєкту
PROJECT_DIR=~/fixbot/Mainingbotrobot

# Додаємо логування для всіх файлів
echo "[INFO] Додаємо логування у файли..."

# Додаємо логування в Galxe
sed -i '1s/^/import logging\nlogging.basicConfig(filename="logs/galxe_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n\n/' "$PROJECT_DIR/modules/crypto/galxe_farm.py"

# Додаємо логування в Zealy
sed -i '1s/^/import logging\nlogging.basicConfig(filename="logs/zealy_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n\n/' "$PROJECT_DIR/modules/crypto/zealy_farm.py"
#!/bin/bash

# Шлях до вашого проєкту
PROJECT_DIR=~/fixbot/Mainingbotrobot

# Додаємо логування для всіх файлів
echo "[INFO] Додаємо логування у файли..."

# Додаємо логування в Galxe
sed -i '1i import logging\nlogging.basicConfig(filename="logs/galxe_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/crypto/galxe_farm.py"

# Додаємо логування в Zealy
sed -i '1i import logging\nlogging.basicConfig(filename="logs/zealy_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/crypto/zealy_farm.py"

# Додаємо логування в TaskOn
sed -i '1i import logging\nlogging.basicConfig(filename="logs/taskon_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/crypto/taskon_farm.py"

# Додаємо логування в QuestN
sed -i '1i import logging\nlogging.basicConfig(filename="logs/questn_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/crypto/questn_farm.py"

# Додаємо логування в OpenBlock
sed -i '1i import logging\nlogging.basicConfig(filename="logs/openblock_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/crypto/openblock_farm.py"

# Додаємо логування в YouTube
sed -i '1i import logging\nlogging.basicConfig(filename="logs/youtube_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/youtube/youtube_smart_bot_v3.py"

# Додаємо логування в ClickFarm
sed -i '1i import logging\nlogging.basicConfig(filename="logs/clickfarm_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/clickfarm/smart_click_farm_v2.py"

# Додаємо логування в NFT
sed -i '1i import logging\nlogging.basicConfig(filename="logs/nft_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/modules/nft/nft_monitor.py"

# Оновлюємо основний скрипт запуску
sed -i '1i import logging\nlogging.basicConfig(filename="logs/main_farm.log", level=logging.INFO, format="%(asctime)s - %(message)s")\n' "$PROJECT_DIR/main_autofarm.py"

echo "[INFO] Логування додано до всіх платформ."
