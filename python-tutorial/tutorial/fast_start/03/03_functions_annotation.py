# Аннотации типов
# Область видимости

def foo(a: int, b: str, c: list) -> complex:
    pass


foo(1, 'string', [1, 2])


def bar(a: int, b: int, c: tuple[(int, int)]) -> complex:
    return a, b, c,


bar_obj = bar(1, 2, (3, "a"))
print(bar_obj)

global_var = 1


def foo2():
    # global global_var
    # global дает доступ к глобальной переменной и
    # возможности ее менять в области видимости функции когда есть одинаковые имена
    # global_var
    global_var = 10
    print('global var: ', global_var)
    global_var = 11


foo2()
print('global_var', global_var)


def foo3():
    # global global_var
    global_var = 20

    def inner():
        nonlocal global_var  # позволяет обращаться к функции на уровень выше
        global_var += 1
        print('global_var from inner', global_var)

    inner()


foo3()
