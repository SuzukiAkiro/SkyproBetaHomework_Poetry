from typing import Generator


def filter_by_currency(data: list[dict], currency: str) -> Generator:
    for item in data:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transactions_description(data: list[dict]) -> Generator:
    for item in data:
        yield item["description"]


def card_number_generator(start_number, end_number):
    for card_number in range(start_number, end_number + 1):
        card_number_str = f"{card_number:016d}"
        formatted_number = " ".join([card_number_str[i : i + 4] for i in range(0, len(card_number_str), 4)])
        yield formatted_number
