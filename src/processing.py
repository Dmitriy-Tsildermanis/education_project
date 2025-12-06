def filter_by_state(list_of_dict: list[dict[str, str | int]],
                    state_name: str = 'EXECUTED'
                    ) -> list[dict[str, str | int]]:
    """Фильтрует входящие данные по параметру state_name и выдает отфильтрованный список"""
    new_list = []
    for dict_ in list_of_dict:
        if state_name in dict_.values():
            new_list.append(dict_)
    return new_list


def sort_by_date(list_of_dict: list[dict[str, str | int]], revers_sort: bool = True) -> list[dict[str, str | int]]:
    """Сортирует список словарей по дате, по умолчанию - по убыванию и возвращает отсортированный список словарей"""
    new_list = sorted(list_of_dict, key=lambda x: x['date'], reverse=revers_sort)
    return new_list