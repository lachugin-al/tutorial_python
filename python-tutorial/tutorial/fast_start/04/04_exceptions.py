# Exceptions / Исключения

class MyCustomExceptions(Exception):
    def __init__(self, message):
        self.message = message


while True:
    arg1 = input('input arg 1: ')
    arg2 = input('input arg 2: ')
    action = input('choose action: ')

    statement = 'print({}{}{})'.format(arg1, action, arg2)

    if int(arg1) < 0:
        raise MyCustomExceptions('аргумент {} < 0'.format(arg1))

    # вызываем исключения
    try:
        if int(arg1) > 0:
            raise MyCustomExceptions('аргумент {} > 0'.format(arg1))
    except MyCustomExceptions as e:
        print(e, 'нормально')
    finally:
        print('done')

    try:
        eval(statement)  # преобразует в код Питона и выполнит его
        # input 1 - 1, input 2 - 2, action - /

    # Иерархия и каскады исключений
    except ZeroDivisionError:
        print('на ноль делить нельзя')
    except NameError as e:
        raise AssertionError('ну такое')  # вызываем исключения
        print('недопустимые имена переменных')
    except TypeError as error:  # перехватываем исключение через as и сохраняем в обьект error
        print(error)
        print('что-то не так с приведением типов')
    except Exception:
        print('остальные исключения')
    else:  # если не сработало ни одно из исключений то вызовется else
        print('all ok')
    finally:  # не смотря ни на что, выполнить этот код
        print('finaly allways')
