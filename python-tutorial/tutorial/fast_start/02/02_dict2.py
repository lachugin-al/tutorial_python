# Dictionary / Словари 2
dict1 = {
    'key': 1,
    2: 'value',
    True: False
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())  # кортежи ключ: значение

for k, j in dict1.items():
    print('key', k)
    print('value', j)
    # dict1[k] = 1  # заменяем по циклу все значения k на 1
print(dict1)

# генератор словаря
dict_gen = {k: k** 2 for k in range(10)}
print(dict_gen)

# переворот словаря, замена / меняем ключ и значение местами
dict_reverse = {v: k for k, v in dict1.items()}
print(dict1)
print(dict_reverse)

# двойной цикл в словаре
# перебор всех значений от 0 до 4 и вывод суммы этих значений
double_dict = {(k,v): k+v for k in range(4) for v in range(4)}
print(double_dict)

print(dict1.pop('key'))
print(dict1.popitem()) # возвращаем последний ключ и его значение в виде кортежа
print(dict1)

# print(dict1.clear())

dict_copy = dict1.copy()
print(dict_copy)

# создает словарь с ключами и значениями None
# dict_from_keys = dict.fromkeys(['1', '2', 'key', 1])
dict_from_keys = dict.fromkeys('1', '2') # создает словарб ключ: значение
print(dict_from_keys)


print(dict1.setdefault('key', None)) # если ключа нет то выдает None либо другое значение по умолчанию
print(dict1.setdefault('dev', 'prod'))