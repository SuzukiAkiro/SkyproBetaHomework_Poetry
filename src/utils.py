import json
from typing import TypeAlias

JsonType: TypeAlias = list[dict]


def json_parser(path: str | None = None) -> JsonType | list:
    """
    Принимает на вход путь до json файла и возвращает его содержимое
    :param path: Путь до json файла
    :return: Содержимое json файла
    """
    if path:
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError or FileNotFoundError:
            return []
    return []


def parse_transaction(transaction: dict) -> float:
    """
    Функция, которая принимает на вход одну транзакцию и возвращает ее сумму, если транзакция совершалась в рублях.
    :param transaction: транзакция
    :return: сумма транзакции в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
