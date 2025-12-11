# education project

## Описание:

education project - это учебный проект, в котором я изучаю инструменты разработчика Python, Github, и прочие.
Цель проекта: повысить профессиональные навыки.

## Установка:

1. Клонируйте репозиторий:
```
[git clone https://github.com/username/project-x.git](https://github.com/Dmitriy-Tsildermanis/education_project.git)
```
2. Установите зависимости:
```
poetry install      # Установит всё
poetry shell        # Активирует окружение
poetry show         # Покажет что установилось
```
## Использование:

На данный момент реализовано несколько функций:
1. get_mask_card_number - Функция принимает на вход номер карты и возвращает маску по образцу ХХХХ ХХ** **** ХХХХ, где Х - цифра номера.
2. get_mask_account - Функция принимает на вход номер счета и возвращает маску по образцу **ХХХХ, где Х - цифра номера
3. mask_account_card - Функция принимает на вход строку с типом карты или счетом и её номером. Возвращает строку с типом карты или счетом и маской номера
4. get_date - Получает на вход строку с датой и возвращает дату по образцу ДД.ММ.ГГГГ
5. filter_by_state - Функция фильтрующая в соответствии с указанным параметром 'state'
6. sort_by_date - Функция сортирующая в соответствии с датой и указаным направляенем по убыванию или возрастанию
7. filter_by_currency - Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
8. transaction_descriptions - Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
9. card_number_generator - Генератор номеров банковских карт от стартового значения до конечного.
    Может генерировать значения от 0000 0000 0000 0001 до 9999 9999 9999 9999.


### Примеры использования

#### Модуль masks.py
функция get_mask_card_number:
```python
number = 1000000000000000
print(get_mask_card_number(number))
```
результат:  
```python
1000 00** **** 0000
```
---
функция get_mask_account:
```python
number = 1000000000000000
print(get_mask_account(number))
```
результат:  
```python
**0000
```
---
#### Модуль widget.py
функция mask_account_card:
```python
type_and_number_card = "Visa 1234567890123456"
print(mask_account_card(type_and_number_card))
```
результат:  
```python
Visa 1234 56** **** 3456
```
---
функция get_date:
```python
data = "2019-07-03T18:35:29.512364"
print(get_date(data))
```
результат:  
```
03.07.2019
```
---
#### Модуль processing.py
пример тестовых данных:
```python
list_of_dict = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
```
---
функция filter_by_state:
```python
state = 'EXECUTED'
filter_list = filter_by_state(list_of_dict, state)
for dict_ in filter_list:
    print(dict_)
```
результат:  
```
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}  
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
```
---
функция sort_by_date:
```python
sort_revers = True
sorted_list = sort_by_date(list_of_dict, sort_revers)
for dict_ in sorted_list:
    print(dict_)
```

результат:  
```python
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
```
---
#### Модуль generators.py
пример тестовых данных:
```python
list_of_transactions = [
        # USD транзакции (3 штуки)
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T00:00:00.000000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "Доллар США", "code": "USD"}
            },
            "description": "Test USD 1",
            "from": "Счет 1",
            "to": "Счет 2"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-01-02T00:00:00.000000",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "USD"}  # Только code, нет name
            },
            "description": "Test USD 2",
            "from": "Счет 3",
            "to": "Счет 4"
        },
        {
            "id": 3,
            "state": "PENDING",  # Другое состояние, но валюта USD
            "date": "2023-01-03T00:00:00.000000",
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "USD"}  # Только name, нет code
            },  # Без описания операции
            "from": "Счет 5",
            "to": "Счет 6"
        }]
```
---
функция filter_by_currency:
```python
currency_name = "USD"
list_of_transactions = filter_by_currency(list_of_dict, currency_name)
for dict_ in list_of_transactions:
    for key, value in dict_.items():
        print(f"{key}: {value}")
    print('\n')
```
результат:  
```python
id: 1
state: EXECUTED
date: 2023-01-01T00:00:00.000000
operationAmount: {'amount': '100.00', 'currency': {'name': 'Доллар США', 'code': 'USD'}}
description: Test USD 1
from: Счет 1
to: Счет 2


id: 2
state: EXECUTED
date: 2023-01-02T00:00:00.000000
operationAmount: {'amount': '200.00', 'currency': {'code': 'USD'}}
description: Test USD 2
from: Счет 3
to: Счет 4


id: 3
state: PENDING
date: 2023-01-03T00:00:00.000000
operationAmount: {'amount': '300.00', 'currency': {'name': 'USD'}}
from: Счет 5
to: Счет 6
```
---
функция transaction_descriptions:
```python
list_of_descriptions = transaction_descriptions(list_of_transactions)
for description in list_of_descriptions:
    print(description)
```
результат:  
```python
Test USD 1
Test USD 2
```
---
функция card_number_generator:
```python
generator_of_numbers_cards = card_number_generator(1, 5)
for number_card in generator_of_numbers_cards:
    print(number_card)
```
результат:
```python
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
```
---
## Тестирование

Проект включает комплексные тесты с покрытием кода 95%:

### Запуск тестов
```bash
# Запуск всех тестов
pytest

# С покрытием кода
pytest --cov=src --cov-report=term-missing

# С HTML-отчетом
pytest --cov=src --cov-report=html
```

### Типы используемых тестов:
✅ **Модульные тесты (Unit Tests)** - проверка отдельных функций  
✅ **Параметризованные тесты** - множественные тест-кейсы через `@pytest.mark.parametrize`  
✅ **Тесты граничных случаев** - минимальные/максимальные значения, специальные случаи  
✅ **Тесты обработки ошибок** - проверка корректных исключений при невалидных данных  

### Статистика покрытия:
- **Общее покрытие**: 95%
- **Модуль `masks.py`**: 100%
- **Модуль `widget.py`**: 91%  
- **Модуль `processing.py`**: 95%
- **Модуль `generators.py`**: 100%

### Особенности тестов:
- Фикстуры для повторного использования тестовых данных
- Отдельные константы для тестовых случаев
- Проверка как валидных, так и невалидных входных данных
- Тестирование всех возможных состояний функций
   
