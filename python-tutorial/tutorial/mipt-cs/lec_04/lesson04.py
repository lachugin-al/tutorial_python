def is_simple(x):
    """
        Определяет, является ли число простым (делится только на 1 и на самого себя)
        Простые числа начинаются с 2
    """
    div = 2  # будем увеличивать делитель до числа x
    while div < x:
        if x % div == 0:
            return False
        div += 1
    else:
        return True


def factorize_num(x):
    """
        Раскладывает число на множители
    """
    div = 2
    while x > 1:
        if x % div == 0:
            print(div)  # печатаем делитель
            x //= div
        else:
            div += 1


is_simple(5)
factorize_num(33)
