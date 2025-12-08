def get_mask_card_number(card_number: [int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает маску по образцу ХХХХ ХХ** **** ХХХХ, где Х - цифра номера"""
    if not isinstance(card_number, int | str):
        raise TypeError("Неверный тип данных")
    str_number = str(card_number)
    if not str_number.isdigit():
        raise ValueError('Неверный формат данных')
    if len(str_number) != 16:
        raise ValueError('Неверный формат данных')
    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"


def get_mask_account(account_number: [int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает маску по образцу **ХХХХ, где Х - цифра номера"""
    if not isinstance(account_number, int | str):
        raise TypeError("Неверный тип данных")
    str_number = str(account_number)
    if not str_number.isdigit():
        raise ValueError('Неверный формат данных')
    if len(str_number) != 16:
        raise ValueError('Неверный формат данных')
    mask_account_number = f"**{str_number[-4:]}"
    return mask_account_number
