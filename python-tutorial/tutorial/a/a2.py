
# Резюме 2-го урока курса по алгоритмам и структурам данных

"""
На 2-м уроке были пройдены следующие темы:
1. функция range()
2. цикл while
3. and, or, in для проверок с помощью if/elif/else и решение задачи http://www.e-olymp.com/ru/problems/1623
4. решение задачи https://www.e-olymp.com/ru/problems/128
5. dict - описание и функции
6. решение задачи https://leetcode.com/problems/valid-anagram/
7. решение задачи https://leetcode.com/problems/two-sum/
8. Решение задачи https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


""" 1. Функция range() """


# объявление массива с числами от 1 до 10 (индексы от 0 до 9, len(l) равно 10)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range(begin, end, step) - выдаёт все целые числа от begin до end,
# end не включительно, через step, т.е. все целые числа
# begin, begin + step, begin + 2 * step, ..., begin + k * step,
# где begin + k * step < end.

# i будет итерироваться по 0, 1, 2, ..., len(l) - 1
# этот код выводит все числа из l по порядку
for i in range(len(l)):
    print(l[i])

# i будет итерироваться по 1, 2, ..., len(l) - 2
# этот код выводит все числа из l, кроме первого и последнего
for i in range(1, len(l) - 1):
    print(l[i])

# i будет итерироваться по 0, 1, 2, ..., len(l) - 1
# этот код выводит все числа из l, который делятся на 2
for i in range(len(l)):
    if l[i] % 2 == 0:
        print(l[i])

# i будет итерироваться по 1, 3, 5, 7, ..., до len(l) - 1 или len(l) - 2,
# в зависимости от четности
# этот код выводит все числа из l через один, начиная с 1-го индекса
for i in range(1, len(l), 2):
    print(l[i])

# i будет итерироваться по len(l) - 1, len(l) - 2, ..., 2, 1, 0
# этот код выводит все числа из l, начиная с последнего, заканчивая первым
for i in range(len(l) - 1, -1, -1):
    print(l[i])


""" 2. Цикл while """


# while выполняется до тех пор, пока заданное условие является верным
i = 0
while i < len(l):
    print(l[i])
    i += 1


""" 3. and, or, in для проверок с помощью if/elif/else и решение задачи http://www.e-olymp.com/ru/problems/1623 """


# and и or на примере решения задачи http://www.e-olymp.com/ru/problems/1623
a, b, c = map(int, input().split())

even = 0
odd = 0

# если среди a, b или c есть чётное число
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    even = 1

# если среди a, b или c есть нечётное число
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    odd = 1

# если есть хотя бы одно чётное и одно нечётное число
if even == 1 and odd == 1:
    print("YES")
else:
    print("NO")

# пример использования in
l = [1, 2, 3]

# читается как "если 3 есть в l"
if 3 in l:
    print("3 est' v l")

# примечание - оператор not является оператором логического отрицания
# читается как "если 4 нет в l"
if 4 not in l:
    print("4 net v l")


""" 4. Решение задачи https://www.e-olymp.com/ru/problems/128 """


n = int(input())

# Замечание 1:
# чтобы разделить число на цифры, можно в цикле брать
# последнюю цифру числа с помощью взятия числа по модулю 10
# и затем стирать её с помощью деления на 10. См. пример ниже.
# 123 => 123 % 10 = 3 => 12
# 12 => 12 % 10 = 2 => 1
# 1 => 1 % 10 => 1 => 0

# Для решения задачи, пройдёмся по всем числам от 0 до 999999
# и представим все числа как 6-ти значные, то есть мысленно дописывая
# нули, где необходимо:
# 000000
# 000001
# 000002
# ...
# 999999
# Каждое из этих чисел разобьём на два числа. Первое будет
# образовано из первых трёх цифр (число // 1000), а второе из последних
# трёх цифр (число % 1000). Посчитаем для каждого из них сумму цифр и
# прибавим к ответу 1, если сумма цифр совпадает и равна n. В конце, выводим ответ.

ans = 0

for i in range(1000000):  # от [00000]0 до 999999
    first_three = i // 1000  # число, образованное из последних трёх цифр i
    last_three = i % 1000  # число, образованное из первых трёх цифр i

    first_sum = 0  # считаем сумму первых трёх цифр i в эту переменную
    while first_three > 0:  # пока число больше 0
        first_sum += first_three % 10  # берём последнюю цифру first_three и прибавляем к сумме
        first_three //= 10  # стираем последнюю цифру first_three

    last_sum = 0  # считаем сумму последних трёх цифр i в эту переменную
    while last_three > 0:
        last_sum += last_three % 10
        last_three //= 10

    if first_sum == last_sum and first_sum == n:  # делаем сравнение по условию задачи
        ans += 1  # если это нужное нам число, то засчитываем его в ответ

print(ans)


""" 5. dict - описание и функции """


# dict - ассоциативный контейнер, в котором можно хранить
# пары-ассоциации (ключ, значение).

# базовая инициализация
d = {}

# инициализация c начальными значениями
d = {"Timur bayke": "Coordinator", "Azret": "Teacher"}  # (key, value)

# создание новой пары (ключ, значение)
d["Tilek bayke"] = "Coordinator"

# выдаёт все ключи из d - dict_keys("Timur bayke", "Azret", "Tilek bayke")
print(d.keys())

# выдаёт все значения из d - dict_values("Coordinator", "Teacher", "Coordinator")
print(d.values())

# element in d по умолчанию проверяет наличие element среди d.keys(),
# т.е. среди ключей d
if "Timur bayke" in d:  # эквивалентно "Timur bayke" in d.keys()
    print("Timur bayke yavlyaetsya:", d["Timur bayke"])


""" 6. Решение задачи https://leetcode.com/problems/valid-anagram/ """


# первое решение (с помощью dict)
"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):  # если длина строк неодинаковая
            return False
        
        d1 = {}
        d2 = {}
        
        for c in s:  # считаем кол-во каждого символа в s
            if c in d1:  # если ключ c был создан ранее, то прибавляем к его значению 1 
                d1[c] += 1
            else:  # если ключа c нет в d1, то создаём пару (c, 1)
                d1[c] = 1

        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
                
        for key in d1.keys():
            # если символа из первой строки нет во второй
            if key not in d2.keys():
                return False

            # если символ key встречается в строках неодинаковое кол-во раз
            if d2[key] != d1[key]:
                return False

        return True
"""

# второе решение
"""
class Solution(object):
    def isAnagram(self, s, t):        
        return sorted(s) == sorted(t)  # возвращает ответ, True или False
"""


""" 7. Решение задачи https://leetcode.com/problems/two-sum/ """


"""
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        
        d = {}
        
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]

            d[nums[i]] = i
"""


""" 8. Решение задачи https://leetcode.com/problems/intersection-of-two-arrays-ii/ """


"""
class Solution(object):
    def intersect(self, nums1, nums2):
        d1 = {}
        
        for x in nums1:
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] += 1
        
        d2 = {}
        for x in nums2:
            if x not in d2:
                d2[x] = 1
            else:
                d2[x] += 1
        
        # Input:
        # nums1 = [4,9,5], 
        # nums2 = [9,4,9,8,4]

        # {4: 1, 9: 1, 5: 1}
        # {9: 2, 4: 2, 8: 1}
        
        ans = []
        for x in d1.keys():  # (4, 1), (9, 1), (5, 1)
            if x in d2:
                occurences = min(d1[x], d2[x])
                
                while occurences > 0:
                    ans.append(x)
                    occurences -= 1
                
        return ans
"""