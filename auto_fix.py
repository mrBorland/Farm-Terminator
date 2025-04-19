import os
import re
from pathlib import Path

# Функція для виправлення помилок у скриптах
def fix_galxe_script():
    path = Path('modules/galxe/galxe_farm_real.py')
    if not path.exists():
        print(f"[!] Не знайдено {path}")
        return
    
    text = path.read_text(encoding='utf-8')
    
    # Замінити wallet['address'] на wallet.get('address', wallet.get('wallet'))
    new_text = re.sub(r"wallet'address'", "wallet.get('address', wallet.get('wallet'))", text)
    
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f"[+] Оновлено {path}")
    else:
        print(f"[*] {path} вже містить правильний ключ")

# Функція для перевірки наявності файлів
def check_required_files():
    files_to_check = [
        'modules/galxe/galxe_farm_real.py',
        'modules/zealy/zealy_farm.py',
        'modules/layer3/layer3_farm.py'
    ]
    for file in files_to_check:
        if not Path(file).exists():
            print(f"[!] Не знайдено {file}")
        else:
            print(f"[+] {file} знайдено.")

# Виконати всі перевірки та виправлення
def auto_fix():
    fix_galxe_script()
    check_required_files()
    print("[+] Виправлення завершено!")

# Запуск
if __name__ == "__main__":
    auto_fix()
