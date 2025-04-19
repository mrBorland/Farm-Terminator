import time
import json
import random
from utils.nft_market import get_best_price, sell_nft
from utils.wallet import withdraw_to_wallet

NFT_STORAGE = "data/farmed_nfts.json"
WALLETS = ["4441111073415832", "TTb8QfyLAsXtTyZZ1SZiCUZt6H6PfJb3Wo"]

def load_nfts():
    try:
        with open(NFT_STORAGE, "r") as f:
            return json.load(f)
    except:
        return []

def save_nfts(nfts):
    with open(NFT_STORAGE, "w") as f:
        json.dump(nfts, f)

def process_nfts():
    nfts = load_nfts()
    if not nfts:
        print("[NFT] Немає нових NFT для обробки.")
        return
    for nft in nfts:
        print(f"[NFT] Обробка {nft['name']}...")
        price = get_best_price(nft)
        if price:
            print(f"[NFT] Знайдена ціна {price} USDT — продаємо!")
            sell_nft(nft, price)
            withdraw_to_wallet(price, random.choice(WALLETS))
        else:
            print("[NFT] Не вдалося знайти ціну.")
    save_nfts([])

if __name__ == "__main__":
    process_nfts()