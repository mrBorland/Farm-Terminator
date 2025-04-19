import json, time, requests, random
from eth_utils import to_checksum_address
from eth_keys import keys
from hexbytes import HexBytes
from rlp import encode as rlp_encode
from eth_rlp import transactions

RPC = "https://polygon-rpc.com"
PRIVATE_KEY = "577e129ba842539db6a4cd7ae814b7bb2e0343fe77c1cf695e0c54c268c538d8"  # OKX
FROM_ADDR = to_checksum_address("0xf75137f855377b37d79fa8e470d2f6512361f2e6")  # OKX

def get_nonce(addr):
    r = requests.post(RPC, json={
        "jsonrpc": "2.0", "method": "eth_getTransactionCount",
        "params": [addr, "latest"], "id": 1
    }).json()
    return int(r["result"], 16)

def get_gas_price():
    r = requests.post(RPC, json={
        "jsonrpc": "2.0", "method": "eth_gasPrice",
        "params": [], "id": 1
    }).json()
    return int(r["result"], 16)

def send_tx(to_addr, value, nonce, gas_price):
    tx = transactions.Transaction(
        nonce=nonce,
        gasPrice=gas_price,
        gas=21000,
        to=HexBytes(to_addr),
        value=int(value * 1e18),
        data=b'',
    )
    pk = keys.PrivateKey(HexBytes(PRIVATE_KEY))
    signed_tx = tx.sign(pk)
    raw_tx = HexBytes(rlp_encode(signed_tx)).hex()
    r = requests.post(RPC, json={
        "jsonrpc": "2.0", "method": "eth_sendRawTransaction",
        "params": [f"0x{raw_tx}"], "id": 1
    }).json()
    return r.get("result", r)

def main():
    print("===== Поповнення Polygon-гаманців без Web3 =====")
    with open("wallets_polygon.json", "r") as f:
        wallets = json.load(f)

    nonce = get_nonce(FROM_ADDR)
    gas_price = get_gas_price()
    success = 0

    for w in wallets:
        try:
            to = to_checksum_address(w["address"])
            tx_hash = send_tx(to, 0.001, nonce, gas_price)
            print(f"[+] {to} → TX: {tx_hash}")
            nonce += 1
            success += 1
            time.sleep(1)
        except Exception as e:
            print(f"[!] {w['address']} → Помилка: {e}")

    print(f"✅ Успішно поповнено: {success} гаманців")

if __name__ == "__main__":
    main()
