import os
import subprocess
from datetime import datetime

project_dir = "/data/data/com.termux/files/home/fixbot/Mainingbotrobot"
log_path = os.path.join(project_dir, "farm_log.txt")
farm_launcher_path = os.path.join(project_dir, "farm_launcher.py")

# Створення лог-файлу, якщо його нема
if not os.path.exists(log_path):
    with open(log_path, "w") as f:
        f.write("")

# Запуск farm_launcher.py
timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
command = f"python3 {farm_launcher_path}"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Запис результату в лог
with open(log_path, "a") as log_file:
    log_file.write(f"{timestamp} [LAUNCH]\n")
    log_file.write(result.stdout)
    log_file.write(result.stderr)
    log_file.write("\n")

print("[+] Запуск завершено. Лог оновлено.")
