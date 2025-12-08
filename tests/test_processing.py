import pytest
from src.processing import filter_by_state, sort_by_date
from tests.constants import INVALID_TYPE_CASES, INVALID_VALUE_CASES


def test_filter_by_state_valid_executed(valid_dict_of_processing, state_executed):
    assert filter_by_state(valid_dict_of_processing, state='EXECUTED') == state_executed


def test_filter_by_state_valid_canceled(valid_dict_of_processing, state_canceled):
    assert filter_by_state(valid_dict_of_processing, state='CANCELED') == state_canceled


@pytest.mark.parametrize("invalid_state", INVALID_TYPE_CASES)
def test_filter_by_state_invalid(invalid_state):
    with pytest.raises(TypeError) as exc_info:
        filter_by_state([{'id': 939719570, 'state': invalid_state, 'date': '2018-06-30T02:08:58.425572'}, ])
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize("invalid_value", INVALID_VALUE_CASES)
def test_filter_by_state_invalid_invalid(invalid_value):
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([{'id': 939719570, 'state': invalid_value, 'date': '2018-06-30T02:08:58.425572'}, ])
    assert str(exc_info.value) == "Неверный формат данных"


def test_filter_by_state_with_no_state():
    with pytest.raises(TypeError) as exc_info:
        filter_by_state([{'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}, ])
    assert str(exc_info.value) == "Неверный тип данных"


def test_sort_by_date_valid_increase(valid_dict_of_processing, valid_dict_of_processing_sorted_increase):
    assert sort_by_date(valid_dict_of_processing, sort_revers=False) == valid_dict_of_processing_sorted_increase


def test_sort_by_date_valid_decrease(valid_dict_of_processing, valid_dict_of_processing_sorted_decrease):
    assert sort_by_date(valid_dict_of_processing) == valid_dict_of_processing_sorted_decrease


def test_sort_by_date_same_date(valid_dict_of_processing_same_date):
    assert sort_by_date(valid_dict_of_processing_same_date) == valid_dict_of_processing_same_date


@pytest.mark.parametrize('invalid_type', INVALID_TYPE_CASES)
def test_sort_by_date_invalid_type(invalid_type):
    with pytest.raises(TypeError) as exc_info:
        sort_by_date([{'id': 939719570, 'date': invalid_type}, ])
    assert str(exc_info.value) == "Неверный тип данных"


@pytest.mark.parametrize('invalid_value', INVALID_VALUE_CASES)
def test_sort_by_date_invalid_value(invalid_value):
    with pytest.raises(ValueError) as exc_info:
        sort_by_date([{'id': 939719570, 'date': invalid_value}, ])
    assert str(exc_info.value) == "Неверный формат данных"
