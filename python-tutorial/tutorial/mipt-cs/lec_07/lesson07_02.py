# Factorial

def fact(n: int):
    assert n >= 0, 'factorial not found'  # if assert False print text
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(5))


# Алгоритм Евклида (наибольший общий делитель)
# a = ----------
# b = --
# вычитаем из одного отрезка другой пока не останется общий делитель
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


def gcd1(a, b):
    if a == b:
        return a
    else:
        return gcd1(b, a % b)


def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


# Быстрое возведение в степень
# a ** n = (a ** (n - 1)) * a
def pow(a: float, n: int):
    if n == 0:
        return 1
    else:
        return pow(a, n - 1) * a


# быстрее
# a ** n = (a ** 2) ** n / 2 для четных n
# для нечетный n-1
def pow2(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:  # нечетное
        return pow2(a, n - 1) * a
    else:  # четное
        return pow(a ** 2, n // 2)


# Ханойские башни
numbers = 3


def tower_of_hanoi(numbers, start, auxiliary, end):
    if numbers == 1:
        print('Move disk 1 from rod {} to rod {}'.format(start, end))
    else:
        tower_of_hanoi(numbers - 1, start, end, auxiliary)
        print('Move disk {} from rod {} to rod {}'.format(numbers, start, end))
        tower_of_hanoi(numbers - 1, auxiliary, start, end)


tower_of_hanoi(numbers, 'A', 'B', 'C')

print('-----')


def tower(n, start, finish):
    if n == 1:
        print('Move disk 1 from rod {} to rod {}'.format(start, finish))
    else:
        tmp = 6 - start - finish  # вспомогательный колышек (3) 6 == 1+2+3 номера колышков
        tower(n - 1, start, tmp)
        print('Move disk {} from rod {} to rod {}'.format(n, start, finish))
        tower(n - 1, tmp, finish)


tower(1, 1, 3)
