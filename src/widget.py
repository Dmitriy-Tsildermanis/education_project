from src import masks


def mask_account_card(type_and_number_card: str) -> str:
    """Функция принимает на вход строку с типом карты или счетом и её номером.
    Возвращает строку с типом карты или счетом и маской номера"""
    list_of_data_card = type_and_number_card.split()
    if list_of_data_card[0] == "Счет":
        mask_number = masks.get_mask_account(int(list_of_data_card[-1]))
        return f"{list_of_data_card[0]} {mask_number}"
    else:
        mask_number = masks.get_mask_card_number(int(list_of_data_card[-1]))
        return f"{' '.join(list_of_data_card[0:-1])} {mask_number}"


def get_date(date_string: str) -> str:
    """Получает на вход строку с датой и возвращает дату по образцу ДД.ММ.ГГГГ"""
    data = date_string[0:10]
    year, month, day = data.split("-")
    return f"{day}.{month}.{year}"
