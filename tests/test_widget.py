import pytest
from src.widget import get_date, mask_account_card
from tests.constants import (INVALID_LENGTH_CASES,
                             INVALID_TYPE_CASES,
                             CARD_TYPES,
                             VALID_EDGE_CASES_CARD,
                             VALID_EDGE_CASES_ACCOUNT,
                             INVALID_VALUE_CASES)


@pytest.mark.parametrize("card_type", CARD_TYPES)
def test_mask_account_card_valid(valid_number_int, valid_number_str, valid_card_mask, card_type):
    for number in (valid_number_int, valid_number_str):
        expected = f"{card_type} {valid_card_mask}"
        result = mask_account_card(f"{card_type} {str(number)}")
        assert result == expected


def test_mask_account_valid(valid_number_int, valid_number_str, valid_account_mask):
    for number in (valid_number_int, valid_number_str):
        expected = f"Счет {valid_account_mask}"
        result = mask_account_card(f"Счет {str(number)}")
        assert result == expected


@pytest.mark.parametrize("edge_case, expected", VALID_EDGE_CASES_CARD)
def test_mask_account_card_edge_cases(edge_case, expected):
    assert mask_account_card(f"Visa {edge_case}") == f"Visa {expected}"


@pytest.mark.parametrize("edge_case, expected", VALID_EDGE_CASES_ACCOUNT)
def test_mask_account_edge_cases(edge_case, expected):
    assert mask_account_card(f"Счет {edge_case}") == f"Счет {expected}"


@pytest.mark.parametrize("invalid_type", INVALID_TYPE_CASES)
def test_mask_account_invalid_type(invalid_type):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(f"Visa {str(invalid_type)}")
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize("invalid_value", INVALID_VALUE_CASES)
def test_mask_account_invalid_value(invalid_value):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(invalid_value)
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize("invalid_length", INVALID_LENGTH_CASES)
def test_mask_account_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(f"Visa {str(invalid_length)}")
    assert str(exc_info.value) == "Неверный формат данных"


def test_mask_account_negative_value(negative_number_int):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(f"Visa {str(negative_number_int)}")
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-12-31T23:59:59.999999", "31.12.2024"),
    ("2024-01-01T00:00:00.000000", "01.01.2024"),
    ("2024-03-11", "11.03.2024"),
    ("2024-03-11Tanything", "11.03.2024")])
def test_get_date_valid(input_date, expected):
    assert get_date(input_date) == expected


@pytest.mark.parametrize("invalid_length", INVALID_LENGTH_CASES)
def test_get_date_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        get_date(invalid_length)
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize("invalid_type", INVALID_TYPE_CASES)
def test_get_date_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        get_date(invalid_type)
    assert str(exc_info.value) == "Неверный тип данных"
