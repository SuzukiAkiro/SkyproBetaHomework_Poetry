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


def date_processing(data: list[dict], reverse_sorting: bool| None = None) -> list[dict]:
    """
    Получает список словарей и сортирует его по ключу 'date'
    :param data: Список словарей с данными
    :param reverse_sorting: Инвертировать сортировку или нет
    :return: Отсортированный список
    """
    if reverse_sorting:
        reverse = True
    else:
        reverse = False
    sorted_data = sorted(data, key=lambda data: data["date"], reverse=reverse)
    return sorted_data


if __name__ == "__main__":
    test_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(state_processing(test_data))
    print(date_processing(test_data))
