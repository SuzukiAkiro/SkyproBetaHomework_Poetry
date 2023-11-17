import json

import pytest

from src import utils


@pytest.fixture
def valid_json():
    with open("data/operations.json", "r") as f:
        return json.load(f)


def test_json_parser(valid_json):
    assert utils.json_parser("data/operations.json") == valid_json


def test_json_parser_empty():
    assert utils.json_parser() == []


def test_json_parser_invalid():
    with pytest.raises(FileNotFoundError):
        assert utils.json_parser("data/invalid_operations.json") == []


@pytest.fixture
def test_data():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


def test_parse_transaction(test_data):
    assert utils.parse_transaction(test_data[0]) == 31957.58


def test_parse_transaction_usd(test_data):
    with pytest.raises(ValueError):
        utils.parse_transaction(test_data[1])
