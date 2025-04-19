import json
import time
import requests
from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3

RPC = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(RPC))

with open("wallets_bnb.json", "r") as f:
    wallets = json.load(f)

TO_ADDRESS = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"

GAS_LIMIT = 21000
GAS_PRICE = web3.toWei("3", "gwei")

def withdraw(wallet):
    address = wallet["address"]
    private_key = wallet["private_key"]

    try:
        balance = web3.eth.get_balance(address)
        if balance == 0:
            print(f"[!] {address} → баланс 0 BNB")
            return 0

        amount = balance - GAS_LIMIT * GAS_PRICE
        if amount <= 0:
            print(f"[!] {address} → недостатньо для комісії")
            return 0

        nonce = web3.eth.get_transaction_count(address)
        tx = {
            "to": TO_ADDRESS,
            "value": amount,
            "gas": GAS_LIMIT,
            "gasPrice": GAS_PRICE,
            "nonce": nonce,
            "chainId": 56,
        }

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"[→] {address} → {web3.fromWei(amount, 'ether')} BNB → {TO_ADDRESS}")
        print(f"     TX: https://bscscan.com/tx/{web3.toHex(tx_hash)}")
        return web3.fromWei(amount, "ether")
    except Exception as e:
        print(f"[X] {address} → Помилка: {e}")
        return 0

print("===== Вивід BNB з усіх акаунтів =====")
total_sent = 0

for wallet in wallets:
    sent = withdraw(wallet)
    total_sent += sent
    time.sleep(1.5)

print(f"===== Готово. Всього виведено: {total_sent:.4f} BNB =====")
