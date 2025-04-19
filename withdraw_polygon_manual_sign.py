import json, requests, time
from eth_keys import keys
from eth_utils import to_checksum_address, keccak, to_hex
import rlp
from rlp.sedes import big_endian_int, Binary, binary

# RPC та основні параметри
RPC = "https://polygon-rpc.com"
TO = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"  # Сюди виводимо
GAS_LIMIT = 21000
GAS_PRICE = int(30e9)  # 30 Gwei
CHAIN_ID = 137

# Формат транзакції
class Transaction(rlp.Serializable):
    fields = [
        ('nonce', big_endian_int),
        ('gas_price', big_endian_int),
        ('gas', big_endian_int),
        ('to', Binary.fixed_length(20, allow_empty=True)),
        ('value', big_endian_int),
        ('data', binary),
        ('v', big_endian_int),
        ('r', big_endian_int),
        ('s', big_endian_int),
    ]

# Функції
def get_nonce(address):
    data = {
        "jsonrpc":"2.0","id":1,
        "method":"eth_getTransactionCount",
        "params":[address, "latest"]
    }
    r = requests.post(RPC, json=data).json()
    return int(r["result"], 16)

def get_balance(address):
    data = {
        "jsonrpc":"2.0","id":1,
        "method":"eth_getBalance",
        "params":[address, "latest"]
    }
    r = requests.post(RPC, json=data).json()
    return int(r["result"], 16)

def send_raw_tx(signed_tx_hex):
    data = {
        "jsonrpc":"2.0","id":1,
        "method":"eth_sendRawTransaction",
        "params":[signed_tx_hex]
    }
    return requests.post(RPC, json=data).json()

def build_and_send_tx(wallet):
    pk = keys.PrivateKey(bytes.fromhex(wallet["private_key"][2:]))
    addr = to_checksum_address(pk.public_key.to_address())
    nonce = get_nonce(addr)
    balance = get_balance(addr)

    if balance < GAS_LIMIT * GAS_PRICE:
        print(f"[!] {addr} недостатньо для комісії")
        return 0

    value = balance - GAS_LIMIT * GAS_PRICE
    tx = Transaction(nonce, GAS_PRICE, GAS_LIMIT, bytes.fromhex(TO[2:]), value, b'', 0, 0, 0)
    tx_parts = rlp.encode(tx, Transaction.exclude(['v','r','s']))
    msg_hash = keccak(tx_parts + bytes([CHAIN_ID, 0, 0]))
    sig = pk.sign_msg_hash(msg_hash)
    v = sig.v + CHAIN_ID * 2 + 35
    signed_tx = Transaction(nonce, GAS_PRICE, GAS_LIMIT, bytes.fromhex(TO[2:]), value, b'', v, int.from_bytes(sig.r, 'big'), int.from_bytes(sig.s, 'big'))
    raw_tx = rlp.encode(signed_tx)
    tx_hash = send_raw_tx("0x" + raw_tx.hex())
    print(f"[+] {addr} → {TO} | TX: {tx_hash}")
    return value / 1e18

# Основний цикл
with open("wallets_polygon.json") as f:
    wallets = json.load(f)

total = 0
print("===== Зняття коштів Polygon (без web3) =====")
for wallet in wallets:
    try:
        total += build_and_send_tx(wallet)
        time.sleep(1)
    except Exception as e:
        print(f"[x] Помилка: {e}")

print(f"💸 Загалом виведено: {total:.4f} MATIC")
