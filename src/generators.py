from typing import Any, Iterator, TypeAlias

TransactionDict: TypeAlias = dict[str, Any]
TransactionList: TypeAlias = list[TransactionDict]


def filter_by_currency(transactions: TransactionList, currency_name: str) -> Iterator[TransactionDict]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if not isinstance(transactions, list):
        raise TypeError("Неверный тип данных")
    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        currency = transaction.get("operationAmount", {}).get("currency", {})
        if not currency:
            continue

        if currency.get("name") == currency_name or currency.get("code") == currency_name:
            yield transaction
    return


def transaction_descriptions(transactions: TransactionList) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not isinstance(transactions, list):
        raise TypeError("Неверный тип данных")
    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        description = transaction.get("description")
        if not description:
            continue

        yield description
    return


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров банковских карт от стартового значения до конечного.
    Может генерировать значения от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Неверный тип данных")
    if start < 0 or end < 0:
        raise ValueError("Числа должны быть неотрицательными")
    if start > 9999999999999999 or end > 9999999999999999:
        raise ValueError("Числа не должны превышать 9999999999999999")
    if start > end:
        start, end = end, start

    for i in range(start, end + 1):
        len_digits = len(str(i))
        str_digits = str(i)
        str_number = (16 - len_digits) * "0" + str_digits
        yield f"{str_number[:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:]}"

