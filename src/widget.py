from src import masks
from tests.constants import CARD_TYPES


def mask_account_card(type_and_number_card: str) -> str:
    """Функция принимает на вход строку с типом карты или счетом и её номером.
    Возвращает строку с типом карты или счетом и маской номера"""
    if not isinstance(type_and_number_card, str):
        raise TypeError("Неверный тип данных")
    list_of_data_card = type_and_number_card.split()
    if len(list_of_data_card) == 0:
        raise ValueError("Неверный формат данных")
    card_type = ' '.join(list_of_data_card[:-1])
    card_number = list_of_data_card[-1]
    if not str(card_number).isdigit() or not card_type.replace(" ", "").isalpha():
        raise ValueError("Неверный формат данных")
    if card_type == "Счет":
        mask_number = masks.get_mask_account(card_number)
        return f"{card_type} {mask_number}"
    if card_type in CARD_TYPES:
        mask_number = masks.get_mask_card_number(card_number)
        return f"{card_type} {mask_number}"


def get_date(date_string: str) -> str:
    """Получает на вход строку с датой и возвращает дату по образцу ДД.ММ.ГГГГ"""

    if not isinstance(date_string, str | int):
        raise TypeError("Неверный тип данных")
    if str(date_string).count("-") != 2:
        raise ValueError("Неверный формат данных")
    if not is_valid_date(date_string):
        raise TypeError("Неверный тип данных")

    data = str(date_string)[0:10]
    year_str, month_str, day_str = data.split("-")

    return f"{day_str}.{month_str}.{year_str}"


def is_valid_date(date_string: str) -> bool:
    """Получает на вход строку и проверяет корректность введеного года, месяца и дня"""
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    data = str(date_string)[0:10]
    year_str, month_str, day_str = data.split("-")
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    month_days[2] = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    if year < 1900 or year > 2100:
        raise ValueError("Неверный формат данных")
    if month < 1 or month > 12:
        raise ValueError("Неверный формат данных")
    if day < 1 or day > month_days[month]:
        raise ValueError("Неверный формат данных")
    return True
