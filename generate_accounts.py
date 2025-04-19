import requests
import random
import string
import time
import json
from concurrent.futures import ThreadPoolExecutor

OUTPUT_FILE = 'accounts.json'
ACCOUNTS_TO_CREATE = 250

EMAIL_DOMAIN = '1secmail.com'
EMAIL_API = 'https://www.1secmail.com/api/v1/'

PROXIES = [
    "user1:pass1@192.0.2.1:8080",
    "user2:pass2@192.0.2.2:8080",
    "user3:pass3@192.0.2.3:8080"
]

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{name}@{EMAIL_DOMAIN}", name

def get_mailbox_messages(login):
    try:
        time.sleep(5)
        response = requests.get(EMAIL_API + f'?action=getMessages&login={login}&domain={EMAIL_DOMAIN}')
        return response.json()
    except:
        return []

def read_email(login, message_id):
    try:
        response = requests.get(EMAIL_API + f'?action=readMessage&login={login}&domain={EMAIL_DOMAIN}&id={message_id}')
        return response.json()
    except:
        return None

def extract_okx_code(email_body):
    import re
    match = re.search(r'code is (\d{6})', email_body)
    return match.group(1) if match else None

def register_account(email, login, proxy):
    session = requests.Session()
    session.proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    try:
        session.post("https://www.okx.com/api/auth/send-email-code", json={"email": email})
        for _ in range(10):
            messages = get_mailbox_messages(login)
            if messages:
                body = read_email(login, messages[0]['id'])
                if body:
                    code = extract_okx_code(body.get('body', ''))
                    if code:
                        break
            time.sleep(5)
        else:
            print(f"[!] Не вдалося отримати код для {email}")
            return

        payload = {
            "email": email,
            "password": password,
            "emailCode": code
        }
        response = session.post("https://www.okx.com/api/auth/register", json=payload)
        if response.status_code == 200:
            print(f"[+] Створено: {email}:{password}")
            with open(OUTPUT_FILE, 'a') as f:
                json.dump({"email": email, "password": password, "proxy": proxy}, f)
                f.write('\n')
        else:
            print(f"[-] Помилка при реєстрації: {response.text}")
    except Exception as e:
        print(f"[X] {email} — помилка: {str(e)}")

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(ACCOUNTS_TO_CREATE):
            email, login = generate_random_email()
            proxy = random.choice(PROXIES)
            executor.submit(register_account, email, login, proxy)

if __name__ == "__main__":
    main()