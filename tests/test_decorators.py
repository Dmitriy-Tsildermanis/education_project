import os
import tempfile

import pytest

from src.decorators import log


# функция для успешного выполнения
@log()
def add(a, b):
    return a + b


# функция, которая вызывает ошибку
@log()
def divide(a, b):
    return a / b


# функция без аргументов
@log()
def get_answer():
    return 42


# функция с разными типами аргументов
@log()
def process_data(data, multiplier=1):
    if not data:
        raise ValueError("Пустые данные")
    return [x * multiplier for x in data]


def test_log_to_console(capsys):
    # вызываем функцию
    result = add(10, 20)

    # получаем вывод из консоли
    captured = capsys.readouterr()
    console_output = captured.out

    # проверяем результат функции
    assert result == 30

    # проверяем логи в консоли
    assert "Function add started with args: (10, 20)" in console_output
    assert "add ok." in console_output
    assert "Time:" in console_output


def test_log_error_to_console(capsys):
    # проверяем, что функция вызывает ошибку
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # получаем вывод из консоли
    captured = capsys.readouterr()
    console_output = captured.out

    # проверяем логи ошибки
    assert "Function divide started with args: (10, 0)" in console_output
    assert "divide error: ZeroDivisionError" in console_output
    assert "Inputs: (10, 0)" in console_output
    assert "Time:" in console_output


def test_log_function_without_args_to_console(capsys):
    result = get_answer()

    captured = capsys.readouterr()
    console_output = captured.out

    assert result == 42
    assert "Function get_answer started with args: (), {}" in console_output
    assert "get_answer ok." in console_output


def test_log_with_complex_args_to_console(capsys):
    result = process_data([1, 2, 3], multiplier=2)

    captured = capsys.readouterr()
    console_output = captured.out

    assert result == [2, 4, 6]
    assert "Function process_data started with args: ([1, 2, 3],)" in console_output
    assert "process_data ok." in console_output


def test_log_with_custom_message_to_console(capsys):
    with pytest.raises(ValueError, match="Пустые данные"):
        process_data([], multiplier=2)

    captured = capsys.readouterr()
    console_output = captured.out

    assert "process_data error: ValueError" in console_output
    assert "Inputs: ([],)" in console_output


def test_log_to_file_success():
    # создаём временный файл
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log") as f:
        temp_path = f.name

    try:
        # создаём декорированную функцию
        @log(filename=temp_path)
        def multiply(x, y):
            return x * y

        # вызываем функцию
        result = multiply(5, 10)

        # проверяем результат
        assert result == 50

        # читаем и проверяем файл
        with open(temp_path, "r") as f:
            log_content = f.read()

        assert "Function multiply started with args: (5, 10)" in log_content
        assert "multiply ok." in log_content
        assert "Time:" in log_content

    finally:
        # очищаем
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_log_to_file_error():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log") as f:
        temp_path = f.name

    try:

        @log(filename=temp_path)
        def risky_operation(value):
            if value < 0:
                raise ValueError("Отрицательное значение")
            return value * 2

        # тест с ошибкой
        with pytest.raises(ValueError):
            risky_operation(-5)

        # тест без ошибки
        risky_operation(10)

        # читаем файл
        with open(temp_path, "r") as file:
            log_content = file.read()

        # Проверяем оба случая
        assert "risky_operation error: ValueError" in log_content
        assert "Inputs: (-5,)" in log_content
        assert "risky_operation ok." in log_content
        assert "Function risky_operation started with args: (10,)" in log_content

    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
