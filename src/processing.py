def filter_by_state(list_of_dict: list[dict[str, str | int]],
                    state_name: str = 'EXECUTED'
                    ) -> list[dict[str, str | int]]:
    new_list = []
    for dict_ in list_of_dict:
        if state_name in dict_.values():
            new_list.append(dict_)
    return new_list
