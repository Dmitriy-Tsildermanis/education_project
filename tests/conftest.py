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
