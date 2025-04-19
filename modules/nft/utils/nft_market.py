def get_best_price(nft):
    # Симуляція запиту до OpenSea/Magic Eden
    import random
    return round(random.uniform(3, 30), 2)

def sell_nft(nft, price):
    print(f"[MARKET] NFT '{nft['name']}' продано за {price} USDT")