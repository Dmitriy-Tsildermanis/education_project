import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_convert(amount: int | float, currency_from: str, currency_to: str = "RUB") -> float:
    """Запрашивает с сайта с помощью API курс валют и конвертирует из USD и EUR в рубли"""
    api_key = os.getenv("EXCHANGE_API_KEY")

    if not api_key:
        raise ValueError("EXCHANGE_API_KEY не установлен в .env файле")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

    headers = {"apikey": api_key}

    response = requests.request("GET", url, headers=headers)

    return float(response.json()["result"])


def amount_transaction(transaction: dict) -> float:
    """На вход получает транзакцию и возвращает сумму операции - amount"""
    if not transaction:
        raise ValueError
    if not isinstance(transaction["operationAmount"]["amount"], int | float | str):
        raise TypeError
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if not currency == "RUB":
        result = get_convert(amount, currency)
        return round(result, 2)
    return amount
