# Функции и пространства имен (локальность имен)
def foo():
    pass
    return None  # возвращает ничего


def bar() -> None:  # аннотация что вернет None type
    pass


def baz(y) -> int:  # необязательно будет возвращать что написано в аннотации
    return y ** 2


x = baz(2)
print(type(x), x)
# print(y) NameError: name 'y' is not defined


a = [1, 2, 3]
b = 4
print(*a, b)


def change_list(o1, o2):
    o1[0] = 7
    o1 = [5, 6, 7]
    print(o1)


change_list(a, b)
print(*a, b)  # 7 2 3


# контракт функций (аннотации не обязательные)
def foo2(x: str, y: int) -> str:
    result = x
    for i in range(y):
        result += x
    return result

print(foo2(2, 5))
print(foo2('foo', 5))

# Параметры по умолчанию

