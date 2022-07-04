# names = str(input().split())
# print(type(names))
# print(names)
# for i in range(0, len(names), 2):
#     print(names[i])
#
# ints1, ints2 = input().split()
#
# print(type(ints1))
# ints1 = int(ints1)
# print(type(ints1))
# print(f'{ints1}, {ints2}')
# print(ints1, ints2)

# a, b, c = map(int, input().split())
# print(a, b, c)
e = list(map(int, input().split()))
print(type(e))
print(sum(e))
print(len(e)) # длинна массива
e.append(4) # добавим в конец массива

y = []
print(y)
y.append(1)
y.append(2)
print(y)

y.append(e[1:3]) # возьмем из массива e объекты по индексу 1-3 (3 не вкл) и добавим как встроенный массив
print(y)
print(type(e[1:3]))

print(e[0:]) # 0,1,2...
print(e[:3]) # 0,1,2
print(e[:]) # 0...
print(e[0:10:2]) # 0, 2, 4, 6, 8 через каждые 2 элемента в массиве
print(e[-1]) # первый с конца в массиве

print(e[::-1]) # перевернуть массив с шагом 1
print(e[::-2]) # перевернуть массив с шагом 2

#sort
e.sort() # сортирует по возрастанию и меняет сам массив
print(e)
# если необходимо вывести копию данного массива не изменяя оригинал
print(sorted(e))

#reverse - разворачиваем массив (можно использовать для сортировки по убыванию)
e.reverse()

# count - возвращает сколько элементов равных какомуто числу
print(e.count(2))

print(y.pop(1)) # возвращает элемент по индексу, Удаляя его из списка
y.remove(1) # удаляет элемент по индексу не возвращая его

# list
# set
# dict

x = int(input())
print(x%2)


# Резюме 1-го урока курса по алгоритмам и структурам данных

"""
Установка Visual Studio Code и Python:
* VS Code на русском языке с Python на Windows, https://www.youtube.com/watch?v=8Kg06eHH6S4, 00:00-12:00
* VS Code на русском языке на MacOS, https://www.youtube.com/watch?v=paA-leudslo 
"""

"""
Веб-сайты, которые будут использованы:
* https://ideone.com - онлайн IDE (среда разработки), где можно запускать Python код.
* https://informatics.mccme.ru - веб-сайт Московского Центра Непрерывного Математического Образования (МЦНМО), где в основном мы будем решать задачи для ознакомления с темами.
* https://www.e-olymp.com/ - украинский веб-сайт, содержащий в себе много задач с различных олимпиад от начинающего до продвинутого уровня, администратором которого является мой учитель с Украины.
* http://leetcode.com - самый популярный веб-сайт для подготовки к техническим интервью в IT-компании.
* https://codeforces.com - самый популярный веб-сайт для изучения спортивного программирования и участия в онлайн-соревнованиях.
"""

"""
На 1-м уроке были пройдены следующие темы:
1. функция print(args..., sep=' ', end='\n')
2. int, float, str
3. функция input()
4. функции int(), float(), str()
5. list и его функции
6. функция split()
7. функция map()
8. if, elif, else; <, >, ==, !=, <=, >=
"""


""" 1. Функция print() """


# вывод строки "Hello World!\n" в консоль ('\n' - это перенос на следующую строку)
print('Hello World!')

# вывод строки "Hello World!\n" в консоль, но строка создана
# с помощью двойных кавычек, а не единичных
print("Hello World!")

# Вывод строки "Hello World!\n" в консоль, т.к. print()
# разделяет заданные через запятую аргументы "Hello" и "World!"
# с помощью пробела по умолчанию.
print("Hello", "World!")

# Вывод строки "Hello_x_World!\n" в консоль, т.к.
# параметр sep (от слова separator, т.е. разделитель [между аргументами])
# функции print() был задан как "_x_"
print("Hello", "World!", sep="_x_")

# Вывод строки "Hello_x_World!_The End." в консоль,
# т.к. параметр end, задающий что выводится в конце строки
# (по умолчанию - это перенос на следующую строку, обозначаемый '\n'),
# задан как "_The End."
print("Hello", "World!", sep="_x_", end="_The End.")


""" 2. int и float """


# int - от слова integer, т.е. целое число, которое
# может быть как отрицательным, нулем, так и положительным.

# float - от слова float, т.е. плавать. Дробные числа в компьютерных
# технологиях (информатике) называются числами с плавающей точкой.
# Подробнее: https://ru.wikipedia.org/wiki/Число_с_плавающей_запятой

# str - от слова string, т.е. цепочка или серия.
# В программировании, string - это тип данных, значениями
# которого является произвольная последовательность (цепочка) символов.

# константа - от слова constant, т.е. нечто неизменное, постоянное.
# переменная - от слова variable, т.е. нечто варирующееся, непостоянное.

x = 15  # объявление переменной типа int
y = -20.3  # объявление переменной типа float
s = 'qwe'  # объявление переменной типа str
f = "asd"  # объявление переменной типа str с помощью двойных кавычек

# функция type(объект) позволяет узнать
# тип данных объекта
print(type(x))  # class 'int'
print(type(y))  # class 'float'

x = 21.0  # можно менять тип переменных на ходу (здесь, int -> float)
x, y = 21, 3  # можно присваивать значения переменным, объявлять их по нескольку за раз
z = 4.0

# см. ниже, арифметические операции
print(x + y)  # сумма двух чисел, 24
print(x - y)  # разница двух чисел, 18
print(x * y)  # перемножение двух чисел, 63
print(x / y)  # частное двух чисел (дробное, тип float), 7.0
print(x // y)  # частное двух чисел (целочисленное, тип int), 7
print(x % 4)  # взятие остатка от деления, 21 % 4 = 1
print(x ** y)  # возведение в степень, 21 в степени 3, т.е. 21 * 21 * 21 = 9261
print(x + z)  # арифметические операции int и float дают тип float, 25.0

# Конкатенация двух строк, т.е. склеивание.
print(s + f)  # "qweasd"
print(s + " " + f)  # можно склеивать строки подряд, "qwe asd"


""" 3. Функция input() """


s = input()  # ввод одной линии/строки с консоли, тип str
print(s)  # вывод считанной строки для проверки


""" 4. Функции int(), str(), float() """


# функции int(), str(), float() преобразуют объект
# в int, str или float, соответственно,
# если это возможно, иначе выдают ошибку
s = "123"
s = int(s)
print(s + 123)  # 123 + 123 = 246

s = float(s)
print(s)  # 123.0

s = str(s)  # "123.0"
print(s)  # 123.0

# если ввести одно число (к примеру, 5) и нажать enter, то оно считается в переменную s
s = int(input())
print(s)  # 5


""" 5. list и его функции """


# list - в переводе, список или же массив.
# Объект типа list может хранить в себе упорядоченный список
# объектов различных типов, в т.ч. другие list'ы.

l = []  # объявление пустого list'а
print(len(l))  # len() позволяет узнать размер list'а - в данном случае, 0

# функция append(), с английского переводится как "добавлять".
l.append(123)  # [123]
l.append("234")  # [123, "234"]
l.append(345.0)  # [123, "234", 345.0]

# К элементам массива можно обращаться по индексу.
# Элементы массива нумеруются с нуля. См. ниже.
l[0] = 567  # новое значение 567 было присвоено нулевому индексу массива
print(str(l[0]) + " " + l[1])  # 567 234

x, y = l[0], l[2]  # значения l[0] и l[2] были скопированы в x и y, соответственно
print(x + y)  # 567 + 345.0 = 912.0

# если индекс отрицательный, то элемент отсчитывается с конца.
# См. ниже.
x, y = l[-1], l[-2]  # последний и предпоследний элементы массива
print(x, y)  # 345.0, 234

l = [1, 2, 3]  # объявление массива с тремя элементами-константами
l = [l[0], l[2]]  # объявление массива с двумя элементами, уже содержащимися в нём, [1, 3]

# функция pop(индекс) удаляет элемент, стоящий на заданном индексе.
# Если задан несуществующий индекс, то выдаётся ошибка.
l.pop(0)
print(l)  # [3]

l.pop(0)  # []
l.append(1)  # [1]
l.append(2)  # [1, 2]
l.append(3)  # [1, 2, 3]
l.append(9)  # [1, 2, 3, 9]
l.append(8)  # [1, 2, 3, 9, 8]
l.append(7)  # [1, 2, 3, 9, 8, 7]
l.append(6)  # [1, 2, 3, 9, 8, 7, 6]
l.append(5)  # [1, 2, 3, 9, 8, 7, 6, 5]
l.append(4)  # [1, 2, 3, 9, 8, 7, 6, 5, 4]

# slicing (срез) - способ сделать копию массива,
# содержащий только некоторые из его элементов. См. ниже.

# индексы: 0  1  2  3  4  5  6  7  8
# массив: [1, 2, 3, 9, 8, 7, 6, 5, 4]

# суффиксный срез:
# l[start:] - даёт копию массива из всех элементов, начиная с
# элемента с индексом start. См. ниже.

t = l[5:]  # [7, 6, 5, 4]

# префиксный срез:
# l[:end] - даёт копию массива из всех элементов до end'того,
# не включая end'тый. См. ниже.

t = l[:5]  # [1, 2, 3, 9, 8]

# срез отрезка:
# l[start:end] - даёт копию массива из всех элементов с индексом от start до end,
# не включая end.

t = l[2:4]  # [3, 9]

# полная форма среза:
# l[start:end:step] - сделать копию массива из элементов
# [
#  l[start],
#  l[start + step],
#  l[start + 2 * step],
#  l[start + 3 * step],
#  ...,
#  l[start + k * step]
# ], где start + k * step < end,
# то есть из каждого step'того элемента на отрезке [start, end),
# начиная с элемента с индексом start до end, не включая end.
# См. примеры ниже.

t = l[1:7:2]  # [l[1], l[3], l[5]]
t = l[:7:2]  # [l[0], l[2], l[4], l[6]]
t = l[5::2]  # [l[5], l[7]]

# если step отрицательный, то копирование делается так:
t = l[3::-1]  # [l[3], l[2], l[1], l[0]]
t = l[:3:-2]  # с конца до 3-го индекса, невключительно, т.е. [l[8], l[6], l[4]]
t = l[::-1]  # копия развернутого массива [4, 5, 6, 7, 8, 9, 3, 2, 1]

# функция sort() сортирует массив объектов так, что соблюдается
# l[0] <= l[1] <= l[2] <= l[3] <= ... <= l[len(l) - 1].
l.sort()  # l равно [1, 2, 3, 4, 5, 6, 7, 8, 9]

# функция sorted() возвращает отсортированную копию массива,
# но не меняет сам массив. См. ниже.
l = sorted(t)  # l равно [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(t)  # до сих пор равен [4, 5, 6, 7, 8, 9, 3, 2, 1]

t.reverse()  # разворачивает массив
print(t)  # [1, 2, 3, 9, 8, 7, 6, 5, 4]

# функция count() считает кол-во элементов,
# равных заданному значению. См. ниже.

print(t.count(10))  # 0, так как в массиве нет числа 10
print(t.count(9))  # 1, так как есть одна 9

t.append(9)
print(t.count(9))  # 2, так как после вставки ещё одной 9 их стало 2 шт.

# функция sum() выдаёт сумму/конкатенацию всех элементов,
# т.е. t[0] + t[1] + ... + t[len(l)-1]

print(sum(t))  # сумма от 1 до 9 плюс ещё одна 9 = 54


""" 6. Функция split() """


# у объекта класса str есть встроенная функция split(),
# которая разделяет str на list str'ов по заданному разделителю
# (пробел ' ' по умолчанию). См. ниже.

s = "123 234 345"
l = s.split()  # ["123", "234", "345"]
print(l)


""" 7. Функция map() """


# функция map() возвращает map-объект, содержащий
# результаты функции, применённой ко всем элементам
# массива. См. ниже.

# возвращается map-объект, содержащий
# результаты функции int(), примененной к каждому элементу в массиве l
l = map(int, l)  # map-объект содержащий числа 123, 234, 345
l = list(l)  # преобразуем map-объект в list и получаем [123, 234, 345]

# особенно удобно применять split и map, чтобы считывать массивы чисел с консоли.
# Допустим нам необходимо ввести одну строку, в которой будет задано несколько целых чисел.
# Затем, скажем нам нужно посчитать сумму этих целых чисел и вывести на экран.
# См. решение ниже.

print(sum(list(map(int, input().split()))))


""" 8. if, elif, else; <, >, ==, !=, <=, >= """


# с помощью операторов проверки if, elif (else if) и else
# можно контролировать выполнение программы.
# Для эффективного пользования операторами if, elif, else
# понадобятся операторы сравнения <, > (меньше/больше),
# ==, != (равны?/не равны?), <= (меньше или равно/больше и равно).
# См. ниже.

age_A = 30  # возраст человека A
age_B = 20  # возраст человека B

name_A = "Arstan"  # имя человека A
name_B = "Bolot"  # имя человека B

if age_A < age_B:  # всегда необходимо ставить двоеточие
    # ставить здесь tab для корректной работы необходимо,
    # чтобы Python мог различать, что является частью if'а,
    # а что нет
    print(name_A)  # выведем имя человека A, если он младше
elif age_B < age_A:
    print(name_B)  # выведем имя человека B, если он младше
else:
    print(name_A, name_B)  # выведем имена обоих людей, если их возраст совпадает