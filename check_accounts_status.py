import requests
import json
import time

with open("data/accounts_crypto.json", "r") as f:
    accounts = json.load(f)["accounts"]

def check_galxe_profile(wallet):
    url = "https://graphigo.prd.galxe.com/query"
    query = {
        "operationName": "userProfile",
        "variables": {"id": wallet},
        "query": "query userProfile($id: String!) { userProfile(id: $id) { id name avatar } }"
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.post(url, json=query, headers=headers, timeout=10)
        print(f"[CHECK] {wallet[:10]}... -> {r.status_code}")
        if r.status_code == 200 and "userProfile" in r.json().get("data", {}):
            return True
        return False
    except Exception as e:
        print(f"[ERROR] {wallet[:10]}... -> {e}")
        return False

def main():
    for acc in accounts:
        wallet = acc["wallet"]
        active = check_galxe_profile(wallet)
        print(f"Account: {acc['username']} | Wallet: {wallet} | Active: {active}")
        time.sleep(1)

if __name__ == "__main__":
    main()
