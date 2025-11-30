from typing import Any


def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрующая в соответствии с указанным параметром 'state'"""
    return [item for item in list_of_dict if item.get("state") == state]


def sort_by_date(list_of_dict: list[dict[str, Any]], sorted_: bool = True) -> list[dict[str, Any]]:
    """Функция сортирующая в соответствии с датой и указаным направляенем по убыванию или возрастанию"""
    new_list_of_dicts = sorted(list_of_dict, key=lambda dict_: dict_["date"], reverse=sorted_)
    return new_list_of_dicts
