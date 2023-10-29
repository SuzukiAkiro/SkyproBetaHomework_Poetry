from src.masks.account import account_mask
from src.masks.card import card_mask


def is_account(info: str) -> bool:
    """
    Проверяет является ли поданная строка номером счета
    :param info: Строка с информацией о карте/счете
    :return: True - на входе счет, False - на входе карта
    """
    return info.lower().startswith("счет")


def is_card_valid(info: str) -> bool:
    """
    Проверяет относится ли карта к одному из существующих производителей карт
    :param info: Информация о карте
    :return: True/False
    """
    if not is_account(info):
        card_vendors = ["maestro", "mastercard", "visa"]
        card_info = info.lower().split(" ")
        return card_info[0] in card_vendors
    return False


def return_masked_info(info: str) -> tuple[str, str] | str:
    """
    Принимает на вход данные карты и счета, возвращает маскированную версию
    :param info: Информация о счете/карте формата 'Счет xxx / Visa xxx'
    :return: Маскированная информация о счете/карте
    """
    if is_account(info):
        account_info = info.split(" ")
        account_number = int(account_info[1])
        return account_info[0], account_mask(account_number)

    if is_card_valid(info):
        card_info = info.split(" ")
        card_vendor = " ".join(card_info[0:-1])
        card_number = int(card_info[-1])
        return card_vendor, card_mask(card_number)
    else:
        return "Вы ввели некорректные данные счета/карты"


def date_from_datetime(datetime: str) -> str:
    """Превращает строку формата YYYY-MM-DDTHH:MM:SSSSSS \
    в строку формата DD.MM.YYYY
    :param datetime: Исходная строка
    :return: Форматированая строка
    """
    if len(datetime) != 26:
        return "Вы ввели некорректные данные!"
    else:
        date = datetime[:10].split("-")
        day = date[-1]
        month = date[1]
        year = date[0]
        return f"{day}.{month}.{year}"


if __name__ == "__main__":
    print(*return_masked_info("Счет 12345678"))
    print(*return_masked_info("Visa Classic 1234123412341234"))
    print(date_from_datetime(str(input("Введите дату в формате YYYY-MM-DDTHH:MM:SSSSSS \n"))))
