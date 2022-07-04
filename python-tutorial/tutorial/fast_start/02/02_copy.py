# Тонкости копирования
list1 = [[1,2],3]
list2 = [[1,2],3]

# копирование
list3 = list1.copy()

print(list3 == list1) # True
print(list3 is list1) # False

"""Происходит копирования списка но не происходит копирования вложенных ссылок
поэтому при сравнении первого элемента они будут указывать на одну и ту же область
в памяти"""
print(list3[0] == list1[0])
print(list3[0] is list1[0], 'ссылка на туже область памяти')

# Решение находится в библиотеке
from copy import deepcopy

list4 = deepcopy(list1)
print(list4 == list1) # True
print(list4 is list1) # False

print(list4[0] == list1[0])
print(list4[0] is list1[0], 'ссылка на туже область памяти')
