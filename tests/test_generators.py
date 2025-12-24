import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.constants import INVALID_TYPE_CASES, INVALID_TYPE_CASES_WITHOUT_LIST, VALID_BUT_EMPTY_RETERN


def test_filter_by_currency_valid(valid_list_of_transactions):
    generator = filter_by_currency(valid_list_of_transactions, "RUB")
    result = list(generator)
    assert len(result) == 1
    assert result[0]["id"] == 6
    assert result[0]["operationAmount"]["currency"]["code"] == "RUB"


@pytest.mark.parametrize("invalid_type", INVALID_TYPE_CASES_WITHOUT_LIST)
def test_filter_by_currency_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        list(filter_by_currency(invalid_type, "RUB"))
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize("invalid_value", VALID_BUT_EMPTY_RETERN)
def test_filter_by_currency_invalid_value(invalid_value):
    assert list(filter_by_currency(invalid_value, "RUB")) == []


def test_transaction_descriptions_valid(valid_list_of_transactions):
    generator = transaction_descriptions(valid_list_of_transactions)
    result = list(generator)
    assert len(result) == 5
    assert result[0] == "Test USD 1"
    assert result[4] == "No currency"


@pytest.mark.parametrize("invalid_type", INVALID_TYPE_CASES_WITHOUT_LIST)
def test_transaction_descriptions_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        list(transaction_descriptions(invalid_type))
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize("invalid_value", VALID_BUT_EMPTY_RETERN)
def test_transaction_descriptions_invalid_value(invalid_value):
    assert list(transaction_descriptions(invalid_value)) == []


def test_card_number_generator_valid():
    assert list(card_number_generator(1, 5)) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_edge_case():
    assert list(card_number_generator(999999999999995, 999999999999999)) == [
        "0999 9999 9999 9995",
        "0999 9999 9999 9996",
        "0999 9999 9999 9997",
        "0999 9999 9999 9998",
        "0999 9999 9999 9999",
    ]


@pytest.mark.parametrize("invalid_type", INVALID_TYPE_CASES)
def test_card_number_generator_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        list(card_number_generator(invalid_type, invalid_type))
    assert str(exc_info.value) == "Неверный тип данных"


def test_card_number_generator_negative_numbers(negative_number_int):
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(negative_number_int, 1))
    assert str(exc_info.value) == "Числа должны быть неотрицательными"


def test_card_number_generator_over_max_numbers(over_max_number_int):
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(1, over_max_number_int))
    assert str(exc_info.value) == "Числа не должны превышать 9999999999999999"


def test_card_number_generator_start_is_greater():
    assert list(card_number_generator(5, 1)) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
