#!/usr/bin/env python3
# Генерация всех перестановок

# Генерация чисел для n-ричной системы счисления
def generate_numbers(n: int, m: int, prefix=None):
    """ Генерируем все числа (с лидирующими незначащими нулями)
        и N-риной системе счисления (N<=10)
        длинны M
    """
    # параметры:
    # 1 основание системы счисления,
    # 2 длинна числа
    # 3 обновляемая сгенерированная часть числа
    # хотим чтобы рекурсия начала витвиться

    # рассмотрим крайний случай
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return

    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


generate_numbers(4, 3)


# Генератор чисел для двоичной системы счисления

def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    gen_bin(m - 1, prefix + '0')
    gen_bin(m - 1, prefix + '1')


gen_bin(3)


def gen_bin2(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    for digit in '0', '1':
        gen_bin2(m - 1, prefix + digit)


gen_bin2(3)


# Генерация перестановок
def find(number, a):
    """ ищет number в a и возвращает True, если есть такой
        False, если такого нет
        используем чтобы у нас небыло повторения числе
    """
    for x in a:
        if number == x:
            return True


def gen_permutation(n: int, m: int = -1, prefix=None):
    """ Генерация всех перестановок n чисел в m позициях,
        с префиксом prefix
    """
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix, end=', ', sep='')
        return
    for number in range(1, n + 1):
        if find(number, prefix):
            continue
        else:
            prefix.append(number)
            gen_permutation(n, m - 1, prefix)
            prefix.pop()


gen_permutation(3)
