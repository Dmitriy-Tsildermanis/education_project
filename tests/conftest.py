import json
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def valid_number_int():
    return 1234567890123456


@pytest.fixture
def valid_number_str():
    return "1234567890123456"


@pytest.fixture
def valid_card_mask():
    return "1234 56** **** 3456"


@pytest.fixture
def valid_account_mask():
    return "**3456"


@pytest.fixture
def negative_number_int():
    return -1234567890123456


@pytest.fixture
def state_executed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def state_canceled():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def valid_dict_of_processing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def valid_dict_of_processing_sorted_decrease():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def valid_dict_of_processing_sorted_increase():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def valid_dict_of_processing_same_date():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def over_max_number_int():
    return 100_000_000_000_000_000_000


@pytest.fixture
def valid_list_of_transactions():
    return [
        # USD транзакции (3 штуки)
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T00:00:00.000000",
            "operationAmount": {"amount": "100.00", "currency": {"name": "Доллар США", "code": "USD"}},
            "description": "Test USD 1",
            "from": "Счет 1",
            "to": "Счет 2",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-01-02T00:00:00.000000",
            "operationAmount": {"amount": "200.00", "currency": {"code": "USD"}},  # Только code, нет name
            "description": "Test USD 2",
            "from": "Счет 3",
            "to": "Счет 4",
        },
        {
            "id": 3,
            "state": "PENDING",  # Другое состояние, но валюта USD
            "date": "2023-01-03T00:00:00.000000",
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "USD"},  # Только name, нет code
            },  # Без описания операции
            "from": "Счет 5",
            "to": "Счет 6",
        },
        # EUR транзакции (2 штуки)
        {
            "id": 4,
            "state": "EXECUTED",
            "date": "2023-01-04T00:00:00.000000",
            "operationAmount": {"amount": "400.00", "currency": {"name": "Евро", "code": "EUR"}},
            "description": "Test EUR 1",
            "from": "Счет 7",
            "to": "Счет 8",
        },
        {
            "id": 5,
            "state": "EXECUTED",
            "date": "2023-01-05T00:00:00.000000",
            "operationAmount": {
                "amount": "500.00",
                "currency": {"name": "Euro", "code": "EUR"},
            },  # Пустая строка в описании
            "description": "",
            "from": "Счет 9",
            "to": "Счет 10",
        },
        # RUB транзакция (1 штука)
        {
            "id": 6,
            "state": "EXECUTED",
            "date": "2023-01-06T00:00:00.000000",
            "operationAmount": {"amount": "600.00", "currency": {"name": "Российский рубль", "code": "RUB"}},
            "description": "Test RUB",
            "from": "Счет 11",
            "to": "Счет 12",
        },
        # Без валюты
        {
            "id": 7,
            "state": "EXECUTED",
            "date": "2023-01-07T00:00:00.000000",
            "operationAmount": {
                "amount": "700.00",
                # Нет currency!
            },
            "description": "No currency",
            "from": "Счет 13",
            "to": "Счет 14",
        },
    ]


@pytest.fixture
def valid_json_file():
    """Создает временный файл с корректным JSON."""
    data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as file:
        json.dump(data, file)
        temp_path = file.name

    yield temp_path
    Path(temp_path).unlink()


@pytest.fixture
def invalid_json_file():
    """Создает временный файл с некорректным JSON."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as file:
        file.write('{invalid json}')
        temp_path = file.name

    yield temp_path
    Path(temp_path).unlink()


@pytest.fixture
def dict_json_file():
    """Создает временный файл с корректным JSON, но в виде словаря"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as file:
        json.dump({'key': 'value'}, file)
        temp_path = file.name

    yield temp_path
    Path(temp_path).unlink()


@pytest.fixture
def empty_json_file():
    """Создает временный файл с пустым JSON"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as file:
        json.dump([], file)
        temp_path = file.name

    yield temp_path
    Path(temp_path).unlink()


@pytest.fixture
def rub_transaction():
    """Транзакция в рублях"""
    return {
        "operationAmount": {
            "amount": "1500.75",
            "currency": {"code": "RUB"}
        }
    }

@pytest.fixture
def usd_transaction():
    """Транзакция в USD"""
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }

@pytest.fixture
def eur_transaction():
    """Транзакция в EUR"""
    return {
        "operationAmount": {
            "amount": "50.00",
            "currency": {"code": "EUR"}
        }
    }
