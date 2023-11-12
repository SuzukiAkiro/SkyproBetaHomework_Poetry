def state_processing(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Получает список словарей и возвращает из него словари с заданным параметром 'state'
    :param data: Список словарей с данными
    :param state: Параметр для фильтрации
    :return: Отфильтрованный список
    """
    processed = []
    for i in range(0, len(data)):
        if data[i]["state"] == state:
            processed.append(dict(data[i].items()))
    return processed


def date_processing(data: list[dict], reverse_sorting: bool = False) -> list[dict]:
    """
    Получает список словарей и сортирует его по ключу 'date'
    :param data: Список словарей с данными
    :param reverse_sorting: Инвертировать сортировку или нет
    :return: Отсортированный список
    """
    sorted_data = sorted(data, key=lambda data: data["date"], reverse=reverse_sorting)
    return sorted_data
