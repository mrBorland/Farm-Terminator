import os, json

def is_valid_address(addr):
    return addr.startswith("0x") and len(addr) == 42 and addr != "0x0000000000000000000000000000000000000000"

folder = "/data/data/com.termux/files/home/fixbot/Mainingbotrobot"
wallet_files = [f for f in os.listdir(folder) if f.endswith(".json")]

for filename in wallet_files:
    path = os.path.join(folder, filename)
    try:
        with open(path, "r") as f:
            data = json.load(f)
        addresses = [w["address"] for w in data if is_valid_address(w["address"])]
        print(f"[✓] {filename}: {len(addresses)} валідних адрес")
    except Exception as e:
        print(f"[!] {filename}: помилка читання - {e}")
