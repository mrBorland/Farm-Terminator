import os
import json

def find_wallet_file():
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        if "wallets_polygon.json" in files:
            return os.path.join(root, "wallets_polygon.json")
    return None

def analyze_wallet_file(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if isinstance(data, list) and all("address" in w and "private_key" in w for w in data):
                print(f"[✓] Знайдено {len(data)} гаманців.")
                print(f"→ Перший гаманець: {data[0]['address']}")
            else:
                print("[!] Файл не містить валідних гаманців.")
    except Exception as e:
        print(f"[!] Помилка при читанні файлу: {e}")

if __name__ == "__main__":
    print("===== Аналіз wallets_polygon.json =====")
    path = find_wallet_file()
    if path:
        print(f"[✓] Файл знайдено: {path}")
        analyze_wallet_file(path)
    else:
        print("[!] Файл wallets_polygon.json не знайдено.")
        print("→ Хочеш створити новий файл з порожніми гаманцями?")
