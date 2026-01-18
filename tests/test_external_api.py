from unittest.mock import patch

import pytest
import requests

from src.external_api import amount_transaction, get_convert


def test_amount_transaction_valid_rub(rub_transaction):
    assert amount_transaction(rub_transaction) == 1500.75


def test_amount_transaction_valid_rub_int():
    transaction = {
        "operationAmount": {
            "amount": 1000,  # int вместо str
            "currency": {"code": "RUB"}
        }
    }
    result = amount_transaction(transaction)
    assert result == 1000.0


@patch('src.external_api.get_convert')
def test_amount_transaction_valid_usd(mock_get_convert, usd_transaction):
    mock_get_convert.return_value = 9000.0
    result = amount_transaction(usd_transaction)

    assert result == 9000.0
    mock_get_convert.assert_called_once_with(100.0, 'USD')


@patch('src.external_api.get_convert')
def test_amount_transaction_valid_eur(mock_get_convert, eur_transaction):
    mock_get_convert.return_value = 5000.0
    result = amount_transaction(eur_transaction)

    assert result == 5000.0
    mock_get_convert.assert_called_once_with(50.0, 'EUR')


def test_amount_transaction_empty_dict():
    with pytest.raises(ValueError):
        amount_transaction({})


def test_amount_transaction_invalid_amount_type():
    transaction = {
        "operationAmount": {
            "amount": [100],  # list вместо int
            "currency": {"code": "RUB"}
        }
    }
    with pytest.raises(TypeError):
        amount_transaction(transaction)


def test_amount_transaction_invalid_amount_string():
    transaction = {
        "operationAmount": {
            "amount": "не число",
            "currency": {"code": "RUB"}
        }
    }
    with pytest.raises(ValueError):
        amount_transaction(transaction)



def test_amount_transaction_missing_currency():
    transaction = {
        "operationAmount": {
            "amount": 100,
            # нет currency
        }
    }
    with pytest.raises(KeyError):
        amount_transaction(transaction)


def test_amount_transaction_missing_fields():
    transaction = {"id": 1}
    with pytest.raises(KeyError):
        amount_transaction(transaction)




@patch('os.getenv', return_value="test_api_key")
@patch('requests.request')
def test_get_convert_success(mock_request, mock_getenv):
    mock_request.return_value.json.return_value = {'result': 7500.5}
    result = get_convert(100, 'USD', 'RUB')

    mock_request.assert_called_once_with(
        'GET',
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": mock_getenv.return_value},
        data={}
    )

    assert result == 7500.5


@patch("os.getenv", return_value=None)
def test_get_convert_api_key_missing(mock_getenv):
    with pytest.raises(ValueError, match="EXCHANGE_API_KEY не установлен в .env файле"):
        get_convert(100, 'USD', 'RUB')



@patch('os.getenv', return_value="test_api_key")
@patch("requests.request")
def test_get_convert_api_error(mock_request, mock_getenv):
    mock_request.side_effect = requests.RequestException("Network error")
    with pytest.raises(requests.RequestException):
        get_convert(100, 'USD', 'RUB')


@patch("os.getenv", return_value='test_api_key')
@patch("requests.request")
def test_get_convert_default_currency(mock_request, mock_getenv):
    mock_request.return_value.json.return_value = {'result': 7500.5}
    result = get_convert(100, 'USD')

    mock_request.assert_called_once_with(
        'GET',
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": mock_getenv.return_value},
        data={}
    )

    assert result == 7500.5


