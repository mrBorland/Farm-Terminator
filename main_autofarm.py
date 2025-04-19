from telegram_report import send_report
import os
import time

print("[START] AutoFarmBot — запуск усіх напрямків")

print("[RUN] modules/crypto/galxe_farm.py")
os.system("python modules/crypto/galxe_farm.py")

print("[RUN] modules/crypto/zealy_farm.py")
os.system("python modules/crypto/zealy_farm.py")

print("[RUN] modules/crypto/taskon_farm.py")
os.system("python modules/crypto/taskon_farm.py")

print("[RUN] modules/crypto/questn_farm.py")
os.system("python modules/crypto/questn_farm.py")

print("[RUN] modules/crypto/port3_farm.py")
os.system("python modules/crypto/port3_farm.py")

print("[RUN] modules/crypto/openblock_farm.py")
os.system("python modules/crypto/openblock_farm.py")

print("[RUN] modules/clickfarm/smart_click_farm_v2.py")
os.system("python modules/clickfarm/smart_click_farm_v2.py")

print("[RUN] modules/youtube/youtube_smart_bot_v3.py")
os.system("python modules/youtube/youtube_smart_bot_v3.py")

print("[RUN] modules/nft/nft_monitor.py")
os.system("python modules/nft/nft_monitor.py")

# Telegram звіт
try:
    with open("modules/youtube/youtube_view_log.txt", "r") as f:
        log_content = f.read()
except:
    log_content = "Звіт: немає даних з YouTube Smart Bot"

send_report(f"Звіт AutoFarmBot (усі платформи)\n\n{log_content}")

print("[WAIT] Чекаємо 6 годин до наступного запуску...")
time.sleep(21600)
