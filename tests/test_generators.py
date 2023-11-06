from _pytest import fixtures
from _pytest.fixtures import fix_cache_order, fixture
import src.generators
import pytest


@pytest.fixture
def data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def correct_answer_filter_usd():
    return [939719570, 142264268]


@pytest.fixture
def correct_answer_filter_rub():
    return [873106923, 594226727]


def test_card_generator():
    assert next(src.generators.card_number_generator(1, 5)) == "0000 0000 0000 0001"
    assert next(src.generators.card_number_generator(2, 5)) == "0000 0000 0000 0002"
    assert next(src.generators.card_number_generator(3, 5)) == "0000 0000 0000 0003"


def test_filter_by_currency_usd(data, correct_answer_filter_usd):
    filtered_usd = src.generators.filter_by_currency(data, "USD")
    for _ in range(2):
        assert next(filtered_usd)["id"] == correct_answer_filter_usd[_]


def test_filter_by_currency_rub(data, correct_answer_filter_rub):
    filtered_rub = src.generators.filter_by_currency(data, "RUB")
    for _ in range(2):
        assert next(filtered_rub)["id"] == correct_answer_filter_rub[_]


def test_descriptions(data):
    descriptions = src.generators.transactions_description(data)
    for _ in range(5):
        assert next(descriptions) == data[_]["description"]
