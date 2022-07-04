# Functions / Функции
# с функциями можно обращаться как с любыми другими объектами

def function(arg):
    print(arg)
    # return # чтобы функция что ли бо возвращала иначе она ничего не будет возвращать будет None
    # pass # ничего не делает функция


# function()
# print(function)

l = [function, function]

variable = function

variable('hello')


def function1(a, b, c):
    print(a)


function1(b='a', a='b', c='c')  # если хотябы один из аргументов именованный то все они должны быть именованы тоже


def function2(my_list=[]):  # пустой изначально список по умолчанию будет кочевать везде где он создан по умолчанию
    my_list.append(1)
    print(my_list)


function2()  # [1]
function2()  # [1, 1]
function2()  # [1, 1, 1]


def function3(my_list2=[]):
    my_list2.append(1)
    print(my_list2)


function2()  # [1, 1, 1, 1]
function2()  # [1, 1, 1, 1, 1]
function2()  # [1, 1, 1, 1, 1, 1]


# Как обойти это
def function3(my_list3=None):
    if my_list3 is None:
        my_list3 = []
    my_list3.append(1)
    print(my_list3)


function3()
function3()
function3()
