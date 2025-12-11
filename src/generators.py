from typing import Any, Iterator, TypeAlias

TransactionDict: TypeAlias = dict[str, Any]
TransactionList: TypeAlias = list[TransactionDict]


def filter_by_currency(transactions: TransactionList, currency_name: str) -> Iterator[TransactionDict]:
    if not isinstance(transactions, list):
        raise TypeError("Не верный тип данных")
    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        currency = transaction.get("operationAmount", {}).get("currency", {})
        if not currency:
            continue

        if currency.get("name") == currency_name or currency.get("code") == currency_name:
            yield transaction
