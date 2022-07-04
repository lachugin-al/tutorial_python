# *args and **kwargs
# *args - позиционные аргументы
# **kwargs - именованные аргументы

def function4(a, b):
    print(a + b)


def function4_c(a, b, c):
    print(a + b + c)


function4(1, 2)
function4_c(1, 2, 3)


def function_args(*args, **kwargs):  # передаем кортеж key word arguments
    print(args, type(args))
    print(kwargs, type(kwargs))

    result = 0
    for i in args:
        result += i
    print(result)

    action = kwargs.get('action')
    if action and action == 'avg':
        print(action)


function_args(1, 2, 4, 5)
function_args(1, 2, 4, 5, 3, 4, 2, action='avg', action1='max')
