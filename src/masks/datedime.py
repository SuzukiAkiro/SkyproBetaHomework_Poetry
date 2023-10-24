def date_from_datetime(datetime: str) -> str:
    """Превращает строку формата YYYY-MM-DDTHH:MM:SSSSSS \
    в строку формата DD.MM.YYYY
    :param datetime: Исходная строка
    :return: Форматированая строка
    """
    date = datetime[:10].split("-")
    day = date[-1]
    month = date[1]
    year = date[0]
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    print(date_from_datetime(str(input("Введите дату в формате YYYY-MM-DDTHH:MM:SSSSSS \n"))))
