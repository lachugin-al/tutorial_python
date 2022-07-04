#!/usr/bin/env python3 #делаем запускаемым в Питоне
# import this

# В Питоне нет переменных, есть имена объектов
a = 179
b = 197
c = (a ** 2 + b ** 2) ** 0.5
print(c)

type(a)  # отображает что за тип
dir(a)  # отображает что умеет этот объект

type(2 + 2 == 4)  # bool

a is b  # a есть b? False

"Hello" == 'Hello'  # True
print('Hello' * 2)  # HelloHello

s = '111.2'
s1 = float(s)
s2 = int(s1)

# print format
name = input('What is your name? ')
print(f'Hello, {name}!')

surname, surname2 = input('1'), input('2')
print(f'Hello, {surname}, {surname2}')
print(surname + ' ' + surname2)

# при равенстве приоритетов операции вычисления выполняются слева на право (возведение в степено справа налево)
x = int(input())
y = x + 7 > x + 2 * x ** 3 ** x
# 7  5  6  4 3  2  1

x = 10
while True:
    x -= 1  # x = x//2 тоже самое что и x //=2
    if x < 0:
        break
    print(x)
else:
    print('end')  # не выполнится так как мы выйдем из цикла по break

x = 10
while x >= 0:
    print(x)
    x -= 1
else:
    print('end')  # выполнится в конце цикла

for x in 5, 3, 7:
    print(x ** 2)

a = range(start, stop, step)  # необходима функция арифметической прогрессии
for x in a:
    print(x)

# логическая арифметика
# унарная операция not (приоритет выше чем у бинарных операций)
# бинарная and or

#     y
#     ^
#  2  | 1
# ----|---->x
#  3  | 4

if y > 0:
    if x > 0:
        print(1)
    else:
        print(2)
else:
    if x > 0:
        print(4)
    else:
        print(3)

if x > 0 and y > 0:
    print(1)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print(2)

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y < 0:
    print(4)
else:
    print('if x or y == 0')  # если 0
