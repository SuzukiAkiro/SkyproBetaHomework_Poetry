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
