from functools import wraps
from time import time


def log(filename=None):
    def write_log(message):
        """Вспомогательная функция для записи лога"""
        if filename:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(message + "\n")
        else:
            print(message)

    def wrap(func):
        @wraps(func)
        def inner(*args, **kwargs):
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

        return inner

    return wrap
