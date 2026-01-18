import json
from typing import Any, Dict, List


def load_operations_from_json(filepath: str) -> List[Dict[str, Any]]:
    """Загружает данные из JSON файла."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            if not data:
                print(f"Внимание: файл {filepath} - содержит пустой список")
            return data
        else:
            print(f"Внимание: файл {filepath} не содержит список")
            return []
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: некорректный JSON в файле {filepath}")
        return []
