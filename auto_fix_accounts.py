#!/usr/bin/env python3

import os
import json
import shutil

# Шляхи до файлів
BASE_DIR = os.path.expanduser("~/fixbot/Mainingbotrobot/data")
SRC_CRYPTO = os.path.join(BASE_DIR, "accounts_crypto_autogen.json")
DST_CRYPTO = os.path.join(BASE_DIR, "accounts_crypto.json")
SRC_YT = os.path.join(BASE_DIR, "accounts_youtube_autogen.json")
DST_YT = os.path.join(BASE_DIR, "accounts_youtube.json")

def copy_file(src, dst):
    if not os.path.exists(src):
        print(f"[ERROR] Не знайдено файл: {src}")
        return False
    shutil.copy(src, dst)
    print(f"[OK] Скопійовано {os.path.basename(src)} → {os.path.basename(dst)}")
    return True

def main():
    print("[Auto‑Fix] Додавання акаунтів…")
    ok1 = copy_file(SRC_CRYPTO, DST_CRYPTO)
    ok2 = copy_file(SRC_YT, DST_YT)
    if not (ok1 or ok2):
        print("[Auto‑Fix] Нічого не оновлено.")
    else:
        print("[Auto‑Fix] Готово!")

if __name__ == "__main__":
    main()
