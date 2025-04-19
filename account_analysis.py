import json

def load_accounts(file_path):
    """
    Завантажує акаунти з JSON файлу
    :param file_path: шлях до JSON файлу з акаунтами
    :return: список акаунтів
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get("accounts", [])

def check_earnings(account):
    """
    Перевіряє зароблені гроші для акаунта
    :param account: акаунт з інформацією про баланс
    :return: зароблені гроші (наприклад, у вигляді строки з числом)
    """
    # Тут може бути API запит або логіка для перевірки балансу акаунта
    # Поки що просто повертаємо фіксовану суму для демонстрації
    return 20  # Це просто демонстраційний приклад

def analyze_accounts():
    # Шляхи до файлів акаунтів
    crypto_accounts_file = 'data/accounts_crypto.json'
    youtube_accounts_file = 'data/accounts_youtube.json'

    # Завантаження акаунтів з файлів
    crypto_accounts = load_accounts(crypto_accounts_file)
    youtube_accounts = load_accounts(youtube_accounts_file)

    # Аналіз акаунтів і зароблених грошей
    print("[INFO] Аналізую акаунти CRYPTO...")
    for account in crypto_accounts:
        earnings = check_earnings(account)
        print(f"Акаунт: {account['username']}\nГроші: {earnings} USDT")

    print("[INFO] Аналізую акаунти YouTube...")
    for account in youtube_accounts:
        earnings = check_earnings(account)
        print(f"Акаунт: {account['username']}\nГроші: {earnings} USDT")

if __name__ == "__main__":
    analyze_accounts()
