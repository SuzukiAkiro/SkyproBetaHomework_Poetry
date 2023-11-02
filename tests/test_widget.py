import pytest
import src.widget


@pytest.fixture
def card_visa():
    return "Visa Classic 1234567890123456"


@pytest.fixture
def incorrect_input():
    return "Абра-кадабра!"


@pytest.fixture
def card_mastercard():
    return "MasterCard 1234567890123456"


@pytest.fixture
def account():
    return "Счет 1234567890"


@pytest.fixture
def correct_datetime():
    return "2018-07-11T02:26:18.671407", "11.07.2018"


def test_is_account(account, card_visa, card_mastercard):
    assert src.widget.is_account(card_visa) is False
    assert src.widget.is_account(card_mastercard) is False
    assert src.widget.is_account(account) is True


@pytest.mark.parametrize(
    "card, expected_result",
    [("Visa Classic 1234567890123456", True), ("Счет 328430928594858", False), ("MasterCard 1234123412341234", True)],
)
def test_is_card_valid(card, expected_result):
    assert src.widget.is_card_valid(card) == expected_result


@pytest.mark.parametrize(
    "card, expected_result",
    [
        ("card_visa", "Visa Classic 123456******3456"),
        ("account", "Счет **7890"),
        ("card_mastercard", "MasterCard 123456******3456"),
        ("incorrect_input", "Вы ввели некорректные данные счета/карты"),
    ],
)
def test_return_masked_info(card, expected_result, request: pytest.FixtureRequest):
    data = request.getfixturevalue(card)
    assert src.widget.return_masked_info(data) == expected_result


def test_date_from_datetime(correct_datetime, incorrect_input):
    assert src.widget.date_from_datetime(correct_datetime[0]) == correct_datetime[1]
