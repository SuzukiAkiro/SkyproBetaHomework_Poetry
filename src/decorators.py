from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор, который регистрирует выполнение функции.
    :param filename: Имя файла для ведения логов.
    По умолчанию None - вывод в консоль.
    :return:
        inner: Декорированная функция.
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Callable:
            try:
                result = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} {func.__name__} ok!\n"
            except Exception as e:
                result = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\
                        {func.__name__} Error: {e}\n Inputs: {args}, {kwargs}\n"
            if filename:
                with open(filename, "a") as file:
                    file.write(result)
                    return func(*args, **kwargs)
            else:
                print(result)
                return func(*args, **kwargs)

        return inner

    return wrapper
