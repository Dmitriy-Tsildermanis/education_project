import pytest
from src.masks import get_mask_account, get_mask_card_number
from tests.constants import INVALID_TYPE_NUMBERS, INVALID_LENGTHS


def test_get_mask_card_number_valid_int(valid_number_int):
    assert get_mask_card_number(valid_number_int) == '1234 56** **** 3456'


def test_get_mask_card_number_valid_str(valid_number_str):
    assert get_mask_card_number(valid_number_str) == "1234 56** **** 3456"


@pytest.mark.parametrize('edge_cases, expected_mask', [(1000000000000000, "1000 00** **** 0000"),
                                                       ('0000000000000000', "0000 00** **** 0000"),
                                                       (9999999999999999, "9999 99** **** 9999"),
                                                       ("9999999999999999", "9999 99** **** 9999")])
def test_get_mask_card_number_edge_cases(edge_cases, expected_mask):
    assert get_mask_card_number(edge_cases) == expected_mask


@pytest.mark.parametrize("invalid_length", INVALID_LENGTHS)
def test_get_mask_card_number_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_length)
    assert str(exc_info.value) == "Не верный формат данных"


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_NUMBERS)
def test_get_mask_card_number_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(invalid_type)
    assert str(exc_info.value) == "Не верный тип данных"


@pytest.mark.parametrize('number_with_spaces', [' 1234567890123456', '1234567890123456 ', ' 1234567890123456 '])
def test_get_mask_card_number_with_spaces(number_with_spaces):
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(number_with_spaces)
    assert str(exc_info.value) == "Не верный тип данных"


def test_get_mask_card_number_negative_integer(negative_number_int):
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(negative_number_int)
    assert str(exc_info.value) == "Не верный тип данных"


def test_get_mask_account_valid_int(valid_number_int):
    assert get_mask_account(valid_number_int) == "**3456"


def test_get_mask_account_valid_str(valid_number_str):
    assert get_mask_account(valid_number_str) == "**3456"


@pytest.mark.parametrize('edge_cases, expected_mask', [(1000000000000000, "**0000"),
                                                       ('0000000000000000', "**0000"),
                                                       (9999999999999999, "**9999"),
                                                       ("9999999999999999", "**9999")])
def test_get_mask_account_edge_cases(edge_cases, expected_mask):
    assert get_mask_account(edge_cases) == expected_mask


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_NUMBERS)
def test_get_mask_account_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        get_mask_account(invalid_type)
    assert str(exc_info.value) == "Не верный тип данных"


@pytest.mark.parametrize("invalid_length", INVALID_LENGTHS)
def test_get_mask_account_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_length)
    assert str(exc_info.value) == "Не верный формат данных"


@pytest.mark.parametrize('number_with_spaces', [' 1234567890123456', '1234567890123456 ', ' 1234567890123456 '])
def test_get_mask_account_with_spaces(number_with_spaces):
    with pytest.raises(TypeError) as exc_info:
        get_mask_account(number_with_spaces)
    assert str(exc_info.value) == "Не верный тип данных"


def test_get_mask_account_negative_integer(negative_number_int):
    with pytest.raises(TypeError) as exc_info:
        get_mask_account(negative_number_int)
    assert str(exc_info.value) == "Не верный тип данных"
