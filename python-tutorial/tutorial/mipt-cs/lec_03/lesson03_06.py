# Множества
a = set()
print(a)

b = set([1, 2, 5, 'hello'])
print(b, type(b))

c = {4, 5, 6, 'hello', 'hey'}
print(c)

d = set()
print(d)
d.add(1)
d.add('hello')
d.add(10)
print(d)

d.add(1)
print(d)

d1 = set(map(int, input().split()))

for i in d:
    print(i)

my_list = [1, 2, 3, 1, 1, 5, 'hello', 'hello']
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_set)

my_set2 = set(my_list)
print(my_set2)

my_set3 = set([1, 2, 3, 1, 1, 5, 'hello', 'hello'])
print(my_set3)

my_list2 = list(my_set2)
print(my_list2)

a = {'hello', 'anton', 1, 2, 5}
print(5 in a)

# Задача
# Найти сумму уникальных элементов в списке
my_list = [1, 1, 3, 3, 4, 2, 3, 3, 5, 6, 5, 4, 5]
print(sum(set(my_list)))

# or
my_set = set(my_list)
result = 0
for el in my_set:
    result += el
print(result)

# Реализовать функцию где первым аргументов передается множество, а вторым аргументом список
# вернуть True если во множестве есть все значения из списка
a = {1, 2, 3, 6, 7}
b = [1, 2, 3, 6, 0]


def my_func(input_set, input_list):
    for i in input_list:
        if i not in input_set:
            return False
    return True


print(my_func(a, b))
