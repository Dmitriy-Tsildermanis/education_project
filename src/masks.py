def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает маску по образцу ХХХХ ХХ** **** ХХХХ, где Х - цифра номера"""
    digit_list = [digit for digit in str(card_number)]
    mask_card_number = f"{''.join(digit_list[0:4])} {''.join(digit_list[4:6])} ** **** {''.join(digit_list[-4:])}"
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает маску по образцу **ХХХХ, где Х - цифра номера"""
    digit_list = [digit for digit in str(account_number)]
    mask_account_number = f"**{''.join(digit_list[-4:])}"
    return mask_account_number
