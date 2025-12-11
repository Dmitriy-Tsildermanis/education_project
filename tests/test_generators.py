import pytest
from src.generators import filter_by_currency
from tests.constants import INVALID_TYPE_CASES_WITHOUT_LIST, VALID_BUT_EMPTY_RETERN


def test_filter_by_currency_valid(transactions_for_currency_filtering):
    generator = filter_by_currency(transactions_for_currency_filtering, 'RUB')
    result = list(generator)
    assert len(result) == 1
    assert result[0]['id'] == 6
    assert result[0]['operationAmount']['currency']['code'] == 'RUB'


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_CASES_WITHOUT_LIST)
def test_filter_by_currency_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        list(filter_by_currency(invalid_type, 'RUB'))
    assert str(exc_info.value) == "Не верный тип данных"


@pytest.mark.parametrize('invalid_value', VALID_BUT_EMPTY_RETERN)
def test_filter_by_currency_invalid_value(invalid_value):
    assert list(filter_by_currency(invalid_value, 'RUB')) == []
