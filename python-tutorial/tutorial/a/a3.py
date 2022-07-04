# Удаление элемента из списка в Python (clear, pop, remove, del)
my_list = ['Python', 50, 11.50, 'Alex', 50, ['A', 'B', 'C']]
"""Метод remove() — это встроенный метод, который удаляет первый совпадающий элемент из списка.
Синтаксис: list.remove(element).
Передается элемент, который нужно удалить из списка.
Метод не возвращает значений.
"""

my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']
my_list.remove(12)  # удаляем элемент 12 в начале
print(my_list)
my_list.remove('Mars')  # удаляем первый Mars из списка
print(my_list)
my_list.remove(100)  # ошибка
print(my_list)

"""
Метод pop()
Этот метод удаляет элемент на основе переданного индекса.
Синтаксис: list.pop(index).
Принимает лишь один аргумент — индекс.
Для удаления элемента списка нужно передать его индекс. Индексы в списках стартуют с 0. Для получения первого передайте 0. Для удаления последнего передайте -1.
Этот аргумент не является обязательным. Значение по умолчанию равно -1, поэтому по умолчанию будет удален последний элемент.
Если этот индекс не найден или он вне диапазона, то метод выбросит исключение IndexError: pop index.
Возвращает элемент, удаленный из списка по индексу. Сам же список обновляется и больше не содержит этот элемент.
"""

my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']

# Передавая индекс как 2, чтобы удалить Sun
name = my_list.pop(2)
print(name)
print(my_list)

# метод pop() без индекса - возвращает последний элемент
item = my_list.pop()
print(item)
print(my_list)

# передача индекса за пределами списка
item = my_list.pop(15)
print(item)
print(my_list)

"""
Метод clear()
Метод clear() удаляет все элементы из списка.
Синтаксис: list.clear().
Нет ни параметров, ни возвращаемого значения.
"""

my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']

element = my_list.clear()
print(element)
print(my_list)


"""
Ключевое слово del
Для удаления элемента из списка можно использовать ключевое слово del с названием списка после него. Также потребуется передать индекс того элемента, который нужно удалить.
Синтаксис: del list[index].
Также можно выбрать элементы в определенном диапазоне и удалить их с помощью del. Для этого нужно передать начальное и конечное значение диапазона.
Синтаксис: del list[start:stop].
Вот пример того как с помощью del можно удалить первый, последний и сразу несколько элементов списка:
"""

my_list = list(range(7))
print("Исходный список", my_list)

# Чтобы удалить первый элемент
del my_list[0]
print("После удаления первого элемента", my_list)

# Чтобы удалить элемент по индексу
del my_list[5]
print("После удаления элемента", my_list)

# Чтобы удалить несколько элементов
del my_list[1:5]
print("После удаления нескольких элементов", my_list)





l = [1, 3, 5, 2, 6, 4, 9, 11]

for i in range(len(l)):
    if l[i] >= 10:
        print(f'number {l[i]} and index {i}')
        break # выходит из цикла

for i in range(len(l)):
    if l[i] % 2 ==0:
        continue # пропускает итерацию и возвращается к началу выполнения следующей итерации
    print('index ', i)

print(
    f'1\n'
    f'2')
print('''3
4''')

# List соединение
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)

# Резюме 3-го урока курса по алгоритмам и структурам данных

"""
На 3-м уроке были пройдены следующие темы:
1. break в цикле
2. continue в цикле
3. format strings: name = "Azret"; print(f“My name is {name}”)
4. конкатенация list'ов: list3 = list1 + list2
5. del для list: del some_list[index]
6. tuple: t = (1, 2, 3)
7. dict.items(): даёт все (key, value) из словаря dict
8. for x, y in zip(list1, list2): создаёт tuple'ы из (list1[i], list2[i])
9. for i, o in enumerate(some_list): создаёт tuple'ы (i, some_list[i])
10. функции, решение задачи https://informatics.mccme.ru/mod/statements/view3.php?id=277&chapterid=311
11. рекурсия, решение задачи https://informatics.mccme.ru/moodle/mod/statements/view3.php?chapterid=1414 
"""


""" 1. break в цикле """


l = [1, 2, 3, 4, 5, 6, 10, 9, 11, 6]

for i in range(len(l)):
    if l[i] >= 10:
        print(i)
        break  # выходит из цикла


""" 2. continue в цикле """


for i in range(len(l)):
    if l[i] % 2 != 0:
        continue  # пропускает одну итерацию цикла
    print(i)


""" 3. Format strings """


name = "Azret"
age = "xx"

print(
    f"My name is {name}. I am {age} years old."
    f"My name is {name}. I am {age} years old."
)  # пример использования format strings

print("Hello" " World")  # две строки записанные друг за другом конкатинируются


""" 4. конкатенация list'ов """


l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 + l2
l1 += l2

print(l1, l3)  # выдаст эквивалентные результаты


""" 5. del для list """


del l2[1]  # удалит элемент на индексе 1 из l2
print(l2)  # [4, 6]


""" 6. tuple """


t = (1, 2, 3)
print(t[0], t[1], t[2])

a, b, c = t[0], t[1], t[2]


""" 7. for x, y in zip(list1, list2) """


l2 = [4, 5, 6]

for x, y in zip(l1, l2):
    print(x, y)


""" 8. for i, o in enumerate(some_list) """


for i, x in enumerate(l1):
    print(f"l1[{i}] = {x}")


""" 9. dict.items() """


d = {
    "key1": "value1",
    "key2": "value2"
}

for key in d.keys():
    print(f"value = {d[key]}")

for key, value in d.items():
    print(key, value)


""" 10. функции, решение задачи https://informatics.mccme.ru/mod/statements/view3.php?id=277&chapterid=311 """


def pown(a, n):  # итеративное возведение a в степень n
    res = 1
    for i in range(n):
        res *= a
    return res


def pown_rec(a, n):  # рекурсивное возведение a в степень n
    if n == 0:
        return 1
    return pown_rec(a, n - 1) * a


"""
a^n = a^(n-1) * a, a^0 = 1  # обычное тождество
Позволяет считать a ** n за кол-во операций пропорциональное n.

# более эффективное тождество
if n == 0:
  a^n = 1
elif n % 2 == 0:
  a^n = (a^(n/2))^2 = a^(n/2) * a^(n/2)
else:
  a^n = a^(n-1) * a

2^6 = (2^3)^2
2^3 = 2^2 * 2
2^2 = (2^1)^2
2^1 = 2^0 * 2
2^0 = 1

2^15 = 2^14 * 2^1

log_2(x) = в какую степень надо возвести два, чтобы получить x.
Возьмём log_2 с обоих сторон.. получаем:

15 = 14 + 1
14 = 7 * 2
7 = 6 + 1
6 = 3 * 2
3 = 2 + 1
2 = 1 * 2
1 = 0 + 1
0 => 1

7 операций, log_2(15) = ~4

129 = 128 + 1
128 = 64 * 2
64 = 32 * 2
32 = 16 * 2
16 = 8 * 2
8 = 4 * 2
4 = 2 * 2
2 = 1 * 2
1 = 0 + 1
0 => 1

9 операций, log_2(129) = ~7

С помощью более эффективного тождества получаем алгоритм
работающий пропорционально log_2(n), а не n.
"""

# используется значение по умолчанию для параметра depth
def pown_eff(a, n, depth=0):  # реализация эффективного (быстрого) возведения в степень
    if n == 0:
        print(f"n = {n}, res = 1, depth = {depth}")
        return 1

    if n % 2 == 0:
        x = pown_eff(a, n // 2, depth + 1)
        x *= x

        print(f"n = {n}, res = {x}, depth = {depth}")
        return x

    x = pown_eff(a, n - 1, depth + 1) * a
    print(f"n = {n}, res = {x}, depth = {depth}")

    return x


"""
a, n = map(int, input().split())

# depth=0 по умолчанию, его не нужно прописывать третьим аргументом для функции, 
# только если вы не хотите иное значение
print(a ** n, pown_eff(a, n))  # эквивалентные результаты
"""


""" 11. рекурсия, решение задачи https://informatics.mccme.ru/moodle/mod/statements/view3.php?chapterid=1414 """

# 1 <= n <= 10
# Есть n пустых ячеек. Например, n = 3, [] [] [].
# 1. Мы можем поставить фишку на ячейку номер 1, если она свободна
# 2. [] [O] [], мы можем поставить фишку на ячейку после самой первой фишки,
#    если там свободно.
#    [O] [] [O]
# 3. Мы можем снимать только фишку на 1-й ячейке (если есть) или
#    мы можем снимать фишку, следующую за самой первой фишкой.
#    [] [O] [O] [] -> [] [O] [] []
#    [O] [] [] [O] -> [] [] [] [O]
# Необходимо заполнить все ячейки.

# 3
# [] [] []
# 1 [O] [] []
# 2 [O] [O] []
# -1 [] [O] []
# 3 [] [O] [O]
# 1 [O] [O] [O]
# 1 2 -1 3 1

# Замечания (observations):
# 1. В каком случае мы можем поставить фишку на позицию X?
#    Мы можем это сделать, если на позиции X - 1 стоит фишка
#    и до неё нет других фишек.
# 2. Нам нужно заполнять (или по крайней мере это логично)
#    ячейки с конца, то есть
#    допустим если у нас 4 ячейки, то сначала поставим
#    ровно одну фишку на 4-ю позицию, затем
#    на 3-ю, затем на 2-ю и затем на 1-ю.
# 3. Допустим на позиции X - 1 уже стоит ровно одна фишка.
#    Теперь мы ставим на позицию X фишку.
#    Теперь нам нужно снять фишку на позиции X - 1.
#    Как нам снять фишку на позиции X-1?
#    Две фишки: X-1 и X
#    Нам нужно поставить (!) фишку на X-2, чтобы снять X-1
#    чтобы снять с X-2 нужно поставить на X-1
#    и так далее...

def put(n):
    if n == 1:
        print(1, end=" ")
        return

    put(n - 1)
    print(n, end=" ")
    take(n - 1)


def take(n):
    if n == 1:
        print(-1, end=" ")
        return

    put(n - 1)
    print(-n, end=" ")
    take(n - 1)


n = int(input())
for i in range(n, 0, -1):
    put(i)

# n = 3
# 1 2 -1 3 1 -2 -1 1 2 -1 1
# put(3):
#  1, O _ _
#  2, O O _
# -1, _ O _
#  3, _ O O
#  1, O O O
# -2, O _ O
# -1, _ _ O
# put(2):
#  1, O _ O
#  2, O O O
# -1, _ O O
# put(1):
#  1, O O O