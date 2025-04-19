import re 
import os 
from pathlib import Path

def fix_galxe_script(): path = Path('modules/galxe/galxe_farm_real.py') if not path.exists(): print(f"[!] Не знайдено {path}") return text = path.read_text(encoding='utf-8') # Замінити wallet['address'] на wallet.get('address', wallet.get('wallet')) new_text = re.sub(r"wallet'address'", "wallet.get('address', wallet.get('wallet'))", text) if new_text != text: path.write_text(new_text, encoding='utf-8') print(f"[+] Оновлено {path}") else: print(f"[*] {path} вже містить правильний ключ");

def fix_farm_launcher(): path = Path('farm_launcher.py') template = '''#!/usr/bin/env python3 import os import subprocess import json from datetime import datetime

LOG_FILE = 'farm_log.txt' WALLETS_FILE = 'data/accounts_crypto_bound.json' MODULES = [ ('Galxe', 'modules/galxe/galxe_farm_real.py', True), ('Zealy', 'modules/zealy/zealy_farm.py', False), ('Layer3', 'modules/layer3/layer3_farm.py', False), ('Smart Click Farm', 'modules/clickfarm/smart_click_farm_v2.py', False), ]

def log(msg): timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]') line = f"{timestamp} {msg}\n" with open(LOG_FILE, 'a') as f: f.write(line) print(line, end='')

def run_module(name, path, needs_wallets): if not os.path.isfile(path): log(f"[RUN] {name}") log(f"[{name}] Помилка: файл не знайдено — {path}") return cmd = ['python3', path] log(f"[RUN] {name}") if needs_wallets: wallets = json.load(open(WALLETS_FILE)) for idx, wallet in enumerate(wallets): full_cmd = cmd + ['--wallet-index', str(idx), '--wallets-file', WALLETS_FILE] try: subprocess.run(full_cmd, check=True) addr = wallet.get('wallet') or wallet.get('address') log(f"[{name}] Успішно для {addr}") except subprocess.CalledProcessError as e: addr = wallet.get('wallet') or wallet.get('address') log(f"[{name}] Помилка для {addr}: {e}") else: try: subprocess.run(cmd, check=True) log(f"[{name}] Виконано успішно") except subprocess.CalledProcessError as e: log(f"[{name}] Помилка виконання: {e}")

if name == 'main': open(LOG_FILE, 'a').write(f"--- FARM START --- {datetime.now()}\n") log("[START] AutoFarmBot — запуск усіх напрямків") for name, path, needs_wallets in MODULES: run_module(name, path, needs_wallets) log("[DONE] Усі модулі завершено.") ''' path.write_text(template, encoding='utf-8') os.chmod(path, 0o755) print(f"[+] Створено новий {path}")

if name == 'main': os.chdir(Path(file).parent) fix_galxe_script() fix_farm_launcher() print("[+] Усі виправлення застосовано!")

