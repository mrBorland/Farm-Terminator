#!/bin/bash

# Створюємо директорію data, якщо вона не існує
mkdir -p data

# Створюємо файл accounts_youtube.json
cat <<EOL > data/accounts_youtube.json
{
  "accounts": [
    {
      "username": "user1_youtube",
      "email": "user1_youtube@example.com",
      "wallet": "0x392af3b647c34bf7dfda95a31f1c96e874adb892",
      "proxy": "172.17.233.57:6042:user:pass"
    },
    {
      "username": "user2_youtube",
      "email": "user2_youtube@example.com",
      "wallet": "0xf86fc79cbf22ccb083fa2b2e4560205a4f5aa5a0",
      "proxy": "192.168.73.50:7213:user:pass"
    },
    {
      "username": "user3_youtube",
      "email": "user3_youtube@example.com",
      "wallet": "0x3e0eb7bc1d618300534930e325d8416d07bd0f95",
      "proxy": "172.27.160.99:9558:user:pass"
    },
    {
      "username": "user4_youtube",
      "email": "user4_youtube@example.com",
      "wallet": "0x4387bf9dfe908e536a8b3c92981f6f0b65551d2a",
      "proxy": "172.28.233.117:6927:user:pass"
    }
  ]
}
EOL

echo "Файл accounts_youtube.json успішно створено з акаунтами для YouTube."
