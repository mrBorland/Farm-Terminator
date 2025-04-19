import json
import requests
import time
import hashlib
import rlp
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_der_canonize
from binascii import hexlify, unhexlify

RPC = "https://bsc-dataseed.binance.org/"
GAS_PRICE = 5_000_000_000  # 5 Gwei
GAS_LIMIT = 21000
AMOUNT_TO_KEEP = 0.0003
TO_ADDRESS = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"
WALLETS_FILE = "wallets_bnb.json"

def keccak256(data):
    return hashlib.new("sha3_256", data).digest()

def to_checksum(address):
    address = address.lower().replace("0x", "")
    hashed = hashlib.sha3_256(address.encode()).hexdigest()
    result = "0x"
    for i, c in enumerate(address):
        result += c.upper() if int(hashed[i], 16) >= 8 else c
    return result

def get_nonce(address):
    payload = {
        "jsonrpc": "2.0", "method": "eth_getTransactionCount",
        "params": [address, "pending"], "id": 1
    }
    res = requests.post(RPC, json=payload).json()
    return int(res.get("result", "0x0"), 16)

def get_balance(address):
    payload = {
        "jsonrpc": "2.0", "method": "eth_getBalance",
        "params": [address, "latest"], "id": 1
    }
    res = requests.post(RPC, json=payload).json()
    return int(res.get("result", "0x0"), 16)

def sign_tx(private_key, tx_dict, chain_id=56):
    tx = [
        tx_dict["nonce"],
        tx_dict["gasPrice"],
        tx_dict["gas"],
        bytes.fromhex(tx_dict["to"][2:]),
        tx_dict["value"],
        b"",
        b""
    ]
    tx_raw = rlp.encode(tx)
    h = keccak256(tx_raw)

    sk = SigningKey.from_string(unhexlify(private_key[2:]), curve=SECP256k1)
    signature = sk.sign_digest(h, sigencode=sigencode_der_canonize)
    r = int.from_bytes(signature[4:36], byteorder="big")
    s = int.from_bytes(signature[36:], byteorder="big")

    v = chain_id * 2 + 35
    tx_signed = [
        tx_dict["nonce"],
        tx_dict["gasPrice"],
        tx_dict["gas"],
        bytes.fromhex(tx_dict["to"][2:]),
        tx_dict["value"],
        b"",
        b"",
        v,
        r,
        s
    ]
    raw_tx = rlp.encode(tx_signed)
    return "0x" + raw_tx.hex()

def send_raw_tx(signed_tx):
    payload = {"jsonrpc": "2.0", "method": "eth_sendRawTransaction", "params": [signed_tx], "id": 1}
    res = requests.post(RPC, json=payload).json()
    return res.get("result")

def main():
    with open(WALLETS_FILE, "r") as f:
        wallets = json.load(f)

    print("===== Старт виводу з BNB-гаманців =====")
    total_sent = 0
    for i, w in enumerate(wallets, 1):
        addr = to_checksum(w["address"])
        key = w["private_key"]
        try:
            balance = get_balance(addr)
            bnb = balance / 10**18
            if bnb < AMOUNT_TO_KEEP + 0.0002:
                print(f"[{i}] {addr} недостатньо балансу ({bnb:.6f} BNB)")
                continue

            value = int((bnb - AMOUNT_TO_KEEP) * 10**18)
            tx = {
                "nonce": get_nonce(addr),
                "gasPrice": GAS_PRICE,
                "gas": GAS_LIMIT,
                "to": TO_ADDRESS,
                "value": value
            }
            signed = sign_tx(key, tx)
            tx_hash = send_raw_tx(signed)
            if tx_hash:
                print(f"[{i}] {addr} → {TO_ADDRESS} | {bnb:.6f} BNB | TX: {tx_hash[:12]}...")
                total_sent += value / 10**18
            else:
                print(f"[{i}] {addr} → Помилка надсилання")
        except Exception as e:
            print(f"[{i}] {addr} → Помилка: {str(e)}")
        time.sleep(0.5)

    print(f"💸 Успішно виведено: {total_sent:.6f} BNB")

if __name__ == "__main__":
    main()
