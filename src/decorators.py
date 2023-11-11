from datetime import datetime
from functools import wraps
from typing import Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор, который регистрирует выполнение функции.
    :param filename: Имя файла для ведения логов.
    По умолчанию None - вывод в консоль.
    :return:
        inner: Декорированная функция.
    """

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if filename:
                try:
                    with open(filename, "a") as file:
                        file.write(f"{datetime.now()} {func.__name__} ok!\n")
                    return func(*args, **kwargs)
                except Exception as e:
                    file.write(f"{datetime.now()} {func.__name__} error: {e} \n Inputs: {args}, {kwargs}\n")
                    return func(*args, **kwargs)
            else:
                try:
                    print(f"{datetime.now()} {func.__name__} ok!\n")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{datetime.now()} {func.__name__} error: {e} \n Inputs: {args}, {kwargs}\n")
                    return func(*args, **kwargs)

        return inner

    return wrapper
