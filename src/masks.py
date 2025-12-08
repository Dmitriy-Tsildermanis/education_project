def get_mask_card_number(card_number: [int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает маску по образцу ХХХХ ХХ** **** ХХХХ, где Х - цифра номера"""
    str_number = str(card_number)
    if not str_number.isdigit():
        raise TypeError('Не верный тип данных')
    if len(str_number) != 16:
        raise ValueError('Не верный формат данных')
    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"

def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает маску по образцу **ХХХХ, где Х - цифра номера"""
    digit_list = [digit for digit in str(account_number)]
    mask_account_number = f"**{''.join(digit_list[-4:])}"
    return mask_account_number


print(isinstance('1234', int), len('asdfqwerasdfqwer'), 'asdfqwerasdfqwer'.isdigit(), type(''), '1234'.isdigit())