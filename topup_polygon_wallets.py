import json
import time
import requests
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import to_checksum_address, to_hex
from hexbytes import HexBytes

OKX_PRIVATE_KEY = "0x577e129ba842539db6a4cd7ae814b7bb2e0343fe77c1cf695e0c54c268c538d8"
RPC = "https://polygon-rpc.com"
WALLETS_FILE = "wallets_polygon.json"
AMOUNT_TO_SEND = 0.001  # MATIC (мінімум для gas)

def get_nonce(address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionCount",
        "params": [address, "latest"],
        "id": 1
    }
    res = requests.post(RPC, json=payload).json()
    return int(res["result"], 16)

def get_gas_price():
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_gasPrice",
        "params": [],
        "id": 1
    }
    res = requests.post(RPC, json=payload).json()
    return int(res["result"], 16)

def send_tx(to_address, nonce, gas_price):
    from_address = Account.from_key(OKX_PRIVATE_KEY).address
    tx = {
        "to": to_checksum_address(to_address),
        "value": hex(int(AMOUNT_TO_SEND * 10**18)),
        "gas": 21000,
        "gasPrice": gas_price,
        "nonce": nonce,
        "chainId": 137,
    }
    signed_tx = Account.sign_transaction(tx, OKX_PRIVATE_KEY)
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_sendRawTransaction",
        "params": [to_hex(signed_tx.rawTransaction)],
        "id": 1
    }
    res = requests.post(RPC, json=payload).json()
    return res.get("result", res)

def main():
    print("===== Поповнення Polygon-гаманців з OKX =====")
    with open(WALLETS_FILE, "r") as f:
        wallets = json.load(f)

    from_address = Account.from_key(OKX_PRIVATE_KEY).address
    gas_price = get_gas_price()
    nonce = get_nonce(from_address)

    success = 0
    for wallet in wallets:
        try:
            tx_hash = send_tx(wallet["address"], nonce, gas_price)
            print(f"[+] {wallet['address']} → {AMOUNT_TO_SEND} MATIC | TX: {tx_hash}")
            success += 1
            nonce += 1
            time.sleep(1)
        except Exception as e:
            print(f"[!] {wallet['address']} → Помилка: {e}")

    print(f"✅ Успішно поповнено: {success} гаманців")

if __name__ == "__main__":
    main()
