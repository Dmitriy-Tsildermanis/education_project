import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid(valid_number_int):
    assert get_mask_card_number(valid_number_int) == '1234 56** **** 3456'


@pytest.mark.parametrize('edge_cases, expected_mask', [(1000000000000000, "1000 00** **** 0000"),
                                                       ('0000000000000000', "0000 00** **** 0000"),
                                                       (9999999999999999, "9999 99** **** 9999"),
                                                       ("9999999999999999", "9999 99** **** 9999")])
def test_get_mask_card_number_edge_cases(edge_cases, expected_mask):
    assert get_mask_card_number(edge_cases) == expected_mask


@pytest.mark.parametrize("invalid_length", [1234,
                                            '1234',
                                            0,
                                            12345678901234567890,
                                            '12345678901234567890'])
def test_get_mask_card_number_invalid_length(invalid_length):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_length)
    assert str(exc_info.value) == "Не верный формат данных"


@pytest.mark.parametrize('invalid_type', [12.45,
                                          [123, [123, 123]],
                                          [[1], [2], [3], [4], [4], 3, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7],
                                          {},
                                          (),
                                          '',
                                          '1234 5678 9012 3456',
                                          '1234-5679-0123-4567',
                                          'asdfqwerasdfqwer',
                                          '1234qwer5678qwer',
                                          None])
def test_get_mask_card_number_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(invalid_type)
    assert str(exc_info.value) == "Не верный тип данных"
