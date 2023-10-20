def card_mask(card_number: int) -> str:
    """Принимает номер карты и возвращает замаскированую и обработаную версию"""
    # Превращаем номер карты в список строк для замены символов на '*'
    digit_list = list(str(card_number))
    digit_list[6:-4] = "*" * len(digit_list[6:-4])
    # Разделяем номер на сегменты по 4 цифры
    separated_list = []
    for i in range(0, len(digit_list), 4):
       separated_list.extend([digit_list[i:i + 4]])
    separated_list = [''.join(item) for item in separated_list]
    return ' '.join(separated_list[:])
if __name__ == "__main__":
    print(card_mask(int(input('Введите 16-ти значный номер карты: \n'))))
