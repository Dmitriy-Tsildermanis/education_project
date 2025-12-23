from functools import wraps
from time import time
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Если указан, логи пишутся в файл, иначе в консоль.

    Returns:
        Декорированную функцию.
    """

    def write_log(message: str) -> None:
        """Вспомогательная функция для записи лога"""
        if filename:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(message + "\n")
        else:
            print(message)

    def wrap(func: F) -> F:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_start = time()
            write_log(f"Function {func.__name__} started with args: {args}, {kwargs}.")

            try:
                result = func(*args, **kwargs)

                duration = time() - time_start
                write_log(f"{func.__name__} ok. Time: {duration:.4f}s")

                return result

            except Exception as e:
                duration = time() - time_start
                write_log(
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}. " f"Time: {duration:.4f}s"
                )
                raise

        return cast(F, inner)

    return wrap
