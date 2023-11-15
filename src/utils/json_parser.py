import json
import os
from typing import TypeAlias

JsonType: TypeAlias = list[dict]


def json_parser(path: str | None = None) -> JsonType | list:
    """
    Принимает на вход путь до json файла и возвращает его содержимое
    :param path: Путь до json файла
    :return: Содержимое json файла
    """
    if path:
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        else:
            return []
    return []
