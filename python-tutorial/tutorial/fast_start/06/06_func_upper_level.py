from functools import reduce

# map

l = ['Python', 'quick', 'start1', '1']

# переворачиваем слова в списке
l1 = []
for el in l:
    l1.append(el[::-1])
print(l1)


# переворачиваем список в функциональном стиле
# функция которая возвращает объект с конца
def rev(n: str):
    return n[::-1]


print(list(map(rev, l)))  # ['nohtyP', 'kciuq', 'trats']

# через лямбду
print(list(map(lambda n: n[::-1], l)))

# пример с несколькими списками и аргументами
l2 = l.copy()
print(list(map(lambda n, a: a + ':' + n[::-1], l, l2)))  # ['Python:nohtyP', 'quick:kciuq', 'start:trats']

f = lambda n, a: a + ':' + n[::-1]
print(list(map(f, l, l2)))  # ['Python:nohtyP', 'quick:kciuq', 'start:trats']


# filter - отфильтровывает значения в итерируемых структурах данных
def foo_str(n):
    return n.isalpha()


def foo_digit(n):
    return n.isdigit()


print(list(filter(foo_str, l)))  # ['Python', 'quick']

print(list(filter(foo_digit, l)))  # ['1']
print(list(filter(lambda n: n.isdigit(), l)))  # ['1']

# reduce
# получить агрегирующий результат
nums = [1, 2, 3, 4, 5]


def foo_reduce(a, b):
    print('{} + {} = {}'.format(a, b, a + b))
    return a + b


reduce(foo_reduce, nums)  # 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15

reduce(foo_reduce, nums, 100)  # 100 + 1 = 101


# 101 + 2 = 103
# 103 + 3 = 106
# 106 + 4 = 110
# 110 + 5 = 115
def foo5(a, b):
    return a + b


print(reduce(lambda a, b: a + b, nums, 100))  # 115
print(reduce(lambda a, b: foo5(a, b), nums, 100))  # 115


# Recursion / Рекурсия
# 5! = 5*4*3*2*1 * 0(1)
# 0! = 1

def factorial(n):
    if n == 0:
        return 1
    print('{} * {}'.format(n, n - 1))
    return n * factorial(n - 1)
    # return 5 * factorial(4 * factorial(3 * factorial(2 * factorial(1* factorial(0 == 1)))))
    # pass


print(factorial(5))

s = 'abcde'


def fact_str(n):
    if len(n) == 0:
        return ':end'
    return n[0] + ' ' + fact_str(n[1:])  # abcde -> a b c d e :end


print(fact_str(s))

# Каррирование и функция partial
# преобразование функций с многими аргументами в функции с некоторыми аргументами
from functools import partial


def tax_for_purchase(product, amount, tax):
    return product * amount * tax


MILK_PRICE = 10
MILK_TAX = 0.1

BEEF_PRICE = 30
BEEF_TAX = 0.15

tax_to_milk = partial(tax_for_purchase, tax=MILK_TAX, product=MILK_PRICE)
tax_to_beef = partial(tax_for_purchase, tax=BEEF_TAX, product=BEEF_PRICE)

print(tax_to_milk(amount=10))  # 10.0
print(tax_to_beef(amount=10))  # 45.0

# Переопределение встроенных функций
my_print = partial(print, sep='**', end='\t')  # end='\t' табуляция
my_print('Hello', 'World')


# Замыкания (спосбоность функций сохранять внутренний контест для вложенных в нее функций)
def my_foo(num):
    def my_wrap(n):
        print('n value is {}'.format(num))
        return n * num

    return my_wrap


print(my_foo(100))  # <function my_foo.<locals>.my_wrap at 0x7f8b001963a0>
print(my_foo(100)(10))  # n value is 100 # 1000

multi100 = my_foo(100)
multi50 = my_foo(50)
print(multi100(100))
print(multi50(50))


# Декораторы
# функция принимает аргуемент функцию, которая возвращает hello
def make_cool(fun):
    def wrap(*args, **kwargs):  # принимаем аргументы
        return '-={ ' + str(fun(*args, **kwargs)) + ' }=-'  # распаковываем кортеж аргументов

    return wrap


@make_cool
def hello(name, times):
    return times * 'hello, {}'.format(name)


# тоже что и декоратор
# cool_hello = make_cool(hello)
# print(cool_hello('mike'))

# либо с декоратором выше
# print(hello('mike'))
print(hello('mike', times=10))



# =====
def test1(arg):
    def my_wrap(n):
        print('n value is {}'.format(arg))
        return n * arg

    return my_wrap

test10 = test1(2) # возвращаем функцию my_wrap в переменную test10
test10(10) # вызываем my_wrap м возвращаем результат выполнения фнкции
