def account_mask(account_number: int) -> str:
    """Принимает номер счета и возвращает замаскированную версию"""
    # Возможно не самое лучшее решение, но это все, что я смог придумать:(
    number = list(str(account_number))
    number_tail = number[-4:]
    masked_number = ('*' * (len(number) - 4))
    return masked_number + ''.join(number_tail)
if __name__ == "__main__":
    print(account_mask(int(input('Введите номер счета \n'))))
