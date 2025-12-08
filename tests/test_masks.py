import pytest
from src.masks import get_mask_account, get_mask_card_number
from tests.constants import (INVALID_LENGTH_CASES,
                             INVALID_TYPE_CASES,
                             VALID_EDGE_CASES_CARD,
                             VALID_EDGE_CASES_ACCOUNT,
                             INVALID_NUMBERS_WITH_SPACES,
                             INVALID_VALUE_CASES)


def test_get_mask_card_number_valid_int(valid_number_int):
    assert get_mask_card_number(valid_number_int) == '1234 56** **** 3456'


def test_get_mask_card_number_valid_str(valid_number_str):
    assert get_mask_card_number(valid_number_str) == "1234 56** **** 3456"


@pytest.mark.parametrize('edge_cases, expected_mask', VALID_EDGE_CASES_CARD)
def test_get_mask_card_number_edge_cases(edge_cases, expected_mask):
    assert get_mask_card_number(edge_cases) == expected_mask


@pytest.mark.parametrize("invalid_length", INVALID_LENGTH_CASES)
def test_get_mask_card_number_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_length)
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_CASES)
def test_get_mask_card_number_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(invalid_type)
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize('number_with_spaces', INVALID_NUMBERS_WITH_SPACES)
def test_get_mask_card_number_with_spaces(number_with_spaces):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(number_with_spaces)
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize('invalid_value', INVALID_VALUE_CASES)
def test_get_mask_card_number_invalid_value(invalid_value):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_value)
    assert str(exc_info.value) == "Неверный формат данных"


def test_get_mask_card_number_negative_integer(negative_number_int):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(negative_number_int)
    assert str(exc_info.value) == "Неверный формат данных"


def test_get_mask_account_valid_int(valid_number_int):
    assert get_mask_account(valid_number_int) == "**3456"


def test_get_mask_account_valid_str(valid_number_str):
    assert get_mask_account(valid_number_str) == "**3456"


@pytest.mark.parametrize('edge_cases, expected_mask', VALID_EDGE_CASES_ACCOUNT)
def test_get_mask_account_edge_cases(edge_cases, expected_mask):
    assert get_mask_account(edge_cases) == expected_mask


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_CASES)
def test_get_mask_account_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        get_mask_account(invalid_type)
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize("invalid_length", INVALID_LENGTH_CASES)
def test_get_mask_account_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_length)
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize('number_with_spaces', INVALID_NUMBERS_WITH_SPACES)
def test_get_mask_account_with_spaces(number_with_spaces):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(number_with_spaces)
    assert str(exc_info.value) == "Неверный формат данных"


@pytest.mark.parametrize('invalid_value', INVALID_VALUE_CASES)
def test_get_mask_account_invalid_value(invalid_value):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_value)
    assert str(exc_info.value) == "Неверный формат данных"


def test_get_mask_account_negative_integer(negative_number_int):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(negative_number_int)
    assert str(exc_info.value) == "Неверный формат данных"
