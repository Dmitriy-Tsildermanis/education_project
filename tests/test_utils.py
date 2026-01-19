import json
from unittest.mock import mock_open, patch

from src.utils import load_operations_from_json


def test_load_operations_valid_json():
    mock_data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    mock_json = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = load_operations_from_json("test.json")

    assert result == mock_data


def test_load_operations_empty_list():
    mock_json = "[]"

    with patch("builtins.open", mock_open(read_data=mock_json)), \
            patch("builtins.print") as mock_print:
        result = load_operations_from_json("test.json")

    assert result == []
    mock_print.assert_called_with("Внимание: файл test.json - содержит пустой список")


def test_load_operations_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError), \
            patch("builtins.print") as mock_print:
        result = load_operations_from_json("nonexistent.json")

    assert result == []
    mock_print.assert_called_with("Ошибка: файл nonexistent.json не найден")


def test_load_operations_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")), \
            patch("builtins.print") as mock_print:
        result = load_operations_from_json("invalid.json")

    assert result == []
    mock_print.assert_called_with("Ошибка: некорректный JSON в файле invalid.json")


def test_load_operations_not_a_list():
    mock_json = '{"key": "value"}'

    with patch("builtins.open", mock_open(read_data=mock_json)), \
            patch("builtins.print") as mock_print:
        result = load_operations_from_json("dict.json")

    assert result == []
    mock_print.assert_called_with("Внимание: файл dict.json не содержит список")
