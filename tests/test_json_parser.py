import json

import pytest

from src.utils.json_parser import json_parser


@pytest.fixture
def valid_json():
    with open("data/operations.json", "r") as f:
        return json.load(f)


def test_json_parser(valid_json):
    assert json_parser("data/operations.json") == valid_json


def test_json_parser_empty():
    assert json_parser() == []
