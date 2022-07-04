print(range(20))

for el in range(0, 20, 1):
    print(el)

# обращаемся по элементам
t = [el ** 2 for el in range(20) if el % 2 == 0]
print(t)

# обращаемся по индексам
some_list = [1, 2, 3, 5, 2, 3, 5]
t1 = [some_list[i] for i in range(len(some_list)) if i % 2 == 0]
print(t1)

# обращаемся по элементу по индексу
some_list = [1, 2, 3, 5, 2, 3, 5]
t1 = [some_list[i] for i in range(len(some_list)) if some_list[i] % 2 == 0]
print(t1)
