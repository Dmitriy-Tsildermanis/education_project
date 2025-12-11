import pytest
from src.generators import filter_by_currency, transaction_descriptions
from tests.constants import INVALID_TYPE_CASES_WITHOUT_LIST, VALID_BUT_EMPTY_RETERN


def test_filter_by_currency_valid(valid_list_of_transactions):
    generator = filter_by_currency(valid_list_of_transactions, 'RUB')
    result = list(generator)
    assert len(result) == 1
    assert result[0]['id'] == 6
    assert result[0]['operationAmount']['currency']['code'] == 'RUB'


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_CASES_WITHOUT_LIST)
def test_filter_by_currency_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        list(filter_by_currency(invalid_type, 'RUB'))
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize('invalid_value', VALID_BUT_EMPTY_RETERN)
def test_filter_by_currency_invalid_value(invalid_value):
    assert list(filter_by_currency(invalid_value, 'RUB')) == []


def test_transaction_descriptions_valid(valid_list_of_transactions):
    generator = transaction_descriptions(valid_list_of_transactions)
    result = list(generator)
    assert len(result) == 5
    assert result[0] == 'Test USD 1'
    assert result[4] == 'No currency'


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_CASES_WITHOUT_LIST)
def test_transaction_descriptions_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        list(transaction_descriptions(invalid_type))
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize('invalid_value', VALID_BUT_EMPTY_RETERN)
def test_transaction_descriptions_invalid_value(invalid_value):
    assert list(transaction_descriptions(invalid_value)) == []
