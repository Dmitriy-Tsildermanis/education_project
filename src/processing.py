from src.widget import is_valid_date

def filter_by_state(list_of_dict: list[dict[str, str | int]], state: str = "EXECUTED") -> list[dict[str, str | int]]:
    """Функция фильтрующая в соответствии с указанным параметром 'state'"""
    valid_state = ("EXECUTED", "CANCELED")
    for dict_ in list_of_dict:
        item_state = dict_.get("state")
        if not isinstance(item_state, str):
            raise TypeError("Неверный тип данных")
        if item_state not in valid_state:
            raise ValueError("Неверный формат данных")
    return [item for item in list_of_dict if item.get("state") == state]


def sort_by_date(list_of_dict: list[dict[str, str | int]], sort_revers: bool = True) -> list[dict[str, str | int]]:
    """Функция сортирующая в соответствии с датой и указаным направляенем по убыванию или возрастанию"""
    for dict_1 in list_of_dict:
        item_state = dict_1.get("date")
        if not isinstance(item_state, str):
            raise TypeError("Неверный тип данных")
        if str(item_state).count("-") != 2:
            raise ValueError("Неверный формат данных")
        if not is_valid_date(item_state):
            raise ValueError("Неверный формат данных")
    new_list_of_dicts = sorted(list_of_dict, key=lambda dict_2: dict_2["date"], reverse=sort_revers)
    return new_list_of_dicts
