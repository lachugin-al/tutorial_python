# Recursion
"""
    Перед написание рекурсии необходимо решить 2 условия
    1) рекурентный случай
    2) крайний крайний
    Иначе писать рекурсию нельзя!
"""

n = int(input())


def matrioshka(n):
    if n == 1:
        print('матрешка n = 1')
    else:
        print('матрешка n =', n)
        matrioshka(n - 1)
        print('низ матрешки n = ', n)


matrioshka(n)
