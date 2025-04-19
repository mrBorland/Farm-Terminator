import json
import os

# Оновлений список акаунтів
accounts = [
    {"username": "user1", "email": "huntmarcus@daniel.com", "wallet": "0x392af3b647c34bf7dfda95a31f1c96e874adb892", "proxy": "172.17.233.57:6042:user:pass"},
    {"username": "user2", "email": "jellis@acosta.info", "wallet": "0xf86fc79cbf22ccb083fa2b2e4560205a4f5aa5a0", "proxy": "192.168.73.50:7213:user:pass"},
    {"username": "user3", "email": "nedwards@hopkins.com", "wallet": "0x3e0eb7bc1d618300534930e325d8416d07bd0f95", "proxy": "172.27.160.99:9558:user:pass"},
    {"username": "user4", "email": "felicia29@miles.com", "wallet": "0x4387bf9dfe908e536a8b3c92981f6f0b65551d2a", "proxy": "172.28.233.117:6927:user:pass"},
    {"username": "user5", "email": "rachelfinley@manning.com", "wallet": "0x47002fdf71a83aaafe3d55a68482db0235664083", "proxy": "192.168.56.99:6474:user:pass"},
    {"username": "user6", "email": "curtis69@hotmail.com", "wallet": "0xb0eccb11aa282f0d34c4a5c6ddaa81de364c21bc", "proxy": "192.168.171.174:8955:user:pass"},
    {"username": "user7", "email": "grice@norris.net", "wallet": "0x4992e79a0c78bded5eb2033e737c29afea0683d1", "proxy": "10.215.146.250:6794:user:pass"},
    {"username": "user8", "email": "veronica70@hotmail.com", "wallet": "0xf1d7fb1f1967017702083125b9decddbf7135369", "proxy": "10.255.110.91:9700:user:pass"},
    {"username": "user9", "email": "michelle24@hotmail.com", "wallet": "0xd5eb9f6750b5efb01a21936193adb8bf74fee41e", "proxy": "10.85.240.110:9621:user:pass"},
    {"username": "user10", "email": "fletchermatthew@jensen.com", "wallet": "0xefec13a75e12b5ec22daf68e277b610d9d368d79", "proxy": "172.29.25.148:8299:user:pass"},
    {"username": "user11", "email": "williamdelgado@hotmail.com", "wallet": "0x8c79ace10b771ffe122fd0fdd9b971b0c7bd7c58", "proxy": "172.28.127.42:8924:user:pass"},
    {"username": "user12", "email": "colebarbara@white.biz", "wallet": "0x1f8388733f2beb91a5575b5269feea4e284a8af8", "proxy": "172.20.11.206:6286:user:pass"},
    {"username": "user13", "email": "amy68@horn.info", "wallet": "0x223fe7425403df4d61d9c75730a45f4dfd0ffe58", "proxy": "192.168.106.81:6079:user:pass"},
    {"username": "user14", "email": "loveanthony@yahoo.com", "wallet": "0xb1dfce7032cc48b4daef5dac7bf7dc90f2af3e2d", "proxy": "192.168.64.43:9919:user:pass"},
    {"username": "user15", "email": "gvazquez@yahoo.com", "wallet": "0xf055ba15117bd2765e456e5d87bfe254641c319b", "proxy": "10.66.27.124:5261:user:pass"},
    {"username": "user16", "email": "ptorres@garcia-morton.com", "wallet": "0xbb6480b6fe98956f5b9385a5d13df2ff5b9f54ce", "proxy": "192.168.58.38:8943:user:pass"},
    {"username": "user17", "email": "hayesdeanna@hotmail.com", "wallet": "0xefd2bdb58b586e5ac80b6c07c9eb8ad2750b27dc", "proxy": "192.168.210.0:5107:user:pass"},
    {"username": "user18", "email": "aguilarwilliam@hotmail.com", "wallet": "0x7ee5c8a19c142d9a54cbd0d568b240fe1f136e2e", "proxy": "192.168.75.207:8774:user:pass"},
    {"username": "user19", "email": "dking@fischer.org", "wallet": "0x8c920b66e99a640f2b6dc6038dd581929e3784f3", "proxy": "172.26.155.103:6262:user:pass"},
    {"username": "user20", "email": "leejoshua@gmail.com", "wallet": "0x4c0b5ac32e0770dc72fc4ff30c89bf2cbf0248e5", "proxy": "192.168.107.35:6323:user:pass"},
    {"username": "user21", "email": "sburke@johnson-harper.biz", "wallet": "0xefa8624f3b9d245b71bb31eb4cd9c21f3d93d580", "proxy": "192.168.145.173:8506:user:pass"},
    {"username": "user22", "email": "ayalapaul@vasquez.com", "wallet": "0x5508f461d07c70c3bdb4037673a4a6fbb00f4973", "proxy": "192.168.42.28:8899:user:pass"},
    {"username": "user23", "email": "michaelcuevas@cooper.com", "wallet": "0x41454a47735cb745ebc74d3d535f072e005e3c72", "proxy": "192.168.178.92:7785:user:pass"},
    {"username": "user24", "email": "heidiluna@hotmail.com", "wallet": "0x544c02293cfa3783eb07d285668325d516cde9ac", "proxy": "10.127.230.143:9333:user:pass"},
    {"username": "user25", "email": "terribrowning@hotmail.com", "wallet": "0xec7098c858535b0cf3ae501ebab9fed06a504d3e", "proxy": "192.168.208.19:8595:user:pass"},
    # Add more accounts here if needed
]

# Файл для збереження акаунтів
file_path = "data/accounts_crypto.json"

# Функція для додавання акаунтів до файлу
def add_accounts_to_file(file_path, accounts):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
            data['accounts'].extend(accounts)
        else:
            data = {'accounts': accounts}

        # Записуємо оновлені акаунти назад у файл
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"У файлі {file_path} додано {len(accounts)} акаунтів.")
    except Exception as e:
        print(f"Помилка при додаванні акаунтів у {file_path}: {e}")

# Додаємо акаунти до файлу
add_accounts_to_file(file_path, accounts)

print("Акаунти успішно додано до всіх платформ!")
