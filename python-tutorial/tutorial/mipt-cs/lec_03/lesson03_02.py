def foo(x, y, z):
    return 100 * x + 10 * y + 1 * z


print(foo(1, 2, 3))
print(foo(z=1, x=2, y=3))  # named parameters


# print(foo(1,2)) #TypeError: foo() missing 1 required positional argument: 'z'

# параметры по умолчанию в функции
def foo2(x, y, z=0):
    return 100 * x + 10 * y + 1 * z


print(foo2(1, 2))
print(foo(1, 2, 3))


def bar(args):  # чтобы ожидать произвольное кол-во аргументов то добавляет *
    for arg in args:
        print('bar arg = ', arg)


bar([1, 2, 3, 4, 5])
bar(['jelly', 'fish'])


# если убрать скобки []
# bar('jelly', 'fish') TypeError: bar() takes 1 positional argument but 2 were given
# мы кладем 2 аргумента в функцию, а она ждет 1


# добавляем возможность произвольного кол-ва параметров на вход и добавление
# именнованого параметра
def bar2(*args, named_parametr="*bar"):
    for arg in args:
        print(named_parametr, 'arg = ', arg)


bar2('jelly', 'fish', named_parametr='separator')
# если именованный параметр не пришел то используется по умолчанию
# и он не попадает в список аргументов и существует отдельно


# тройные кавычки
stroka = '''многострочная 
строка'''
print(stroka)
