import secrets
import json
from eth_utils import to_checksum_address
from eth_keys import keys

wallets = []

for _ in range(100):
    priv = secrets.token_bytes(32)
    pk = keys.PrivateKey(priv)
    address = to_checksum_address(pk.public_key.to_address())
    wallets.append({
        "address": address,
        "private_key": pk.to_hex()
    })

with open("wallets_polygon.json", "w") as f:
    json.dump(wallets, f, indent=2)

print("✅ Згенеровано 100 Polygon (EVM) гаманців у wallets_polygon.json")
