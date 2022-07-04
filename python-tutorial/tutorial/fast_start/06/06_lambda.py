# Lambda / Лямбда

x = lambda a: a + 50
y = lambda a, b: a + b
print(x(1))  # 51
print(y(1, 2))  # 3


def foo(n):
    return lambda a: a * n

# аналог
def foo1(n):
    def wrap(a):
        return a*n
    return wrap # возвращаем объект wrap, а не wrap() - т.к. это вызов функции


# возвращаем объект фукции где результат умножение на 10
mod10 = foo(10)

print(foo(10)(2))  # 20
print(mod10(3))  # 30 при результате 3*10
