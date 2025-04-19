import json
from web3 import Web3

# Налаштування
BSC_RPC = "https://bsc-dataseed.binance.org/"
USDT_CONTRACT = "0x55d398326f99059fF775485246999027B3197955"  # BEP20 USDT
ABI = '[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]'

W3 = Web3(Web3.HTTPProvider(BSC_RPC))
contract = W3.eth.contract(address=Web3.to_checksum_address(USDT_CONTRACT), abi=ABI)

# Завантаження гаманців
with open("wallets_bnb.json") as f:
    wallets = json.load(f)

print("===== Баланс USDT на BNB-гаманцях =====")
total = 0
for w in wallets:
    address = w["address"]
    try:
        balance = contract.functions.balanceOf(Web3.to_checksum_address(address)).call()
        usdt = balance / 10**18
        if usdt > 0:
            print(f"{address}: {usdt:.2f} USDT")
            total += usdt
    except Exception as e:
        print(f"Помилка для {address}: {e}")

print("========================================")
print(f"Загальний баланс USDT: {total:.2f}")
