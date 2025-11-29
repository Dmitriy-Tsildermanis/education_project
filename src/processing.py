from typing import Any


def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "CANCELED") -> list[dict[str, Any]]:
    """Функция фильтрующая в соответствии с указанным параметром 'state'"""
    return [item for item in list_of_dict if item.get("state") == state]
