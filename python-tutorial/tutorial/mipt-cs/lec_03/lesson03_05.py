# Генератор списков
a = [1, 2, 3, 4, 5]
print(a)

b = []
for i in a:
    b.append(i * 2)
print(b)

# list comprehension
c = [i * 2 for i in a]
print(c)

d = [num * 3 for num in range(1, 6)]
print(d)

d1 = []
for i in range(1, 6):
    d1.append(i * 3)
print(d1)

# Фильтрация элементов
f = []
for i in a:
    if i < 3:
        f.append(i)
print(f)

f1 = [num for num in a if num < 3]
print(f1)

f_sqr = [num ** 2 for num in a if num < 3]
print(f_sqr)

# Последовательность строк
words = ['hello', 'h', 'he', 'hellooo']
print(words)
word_filtered = [word for word in words if len(word) < 4]
print(word_filtered)

# Задача
"""
Создаем список вида 20, 16, 12, 8, 4
Интервал от 10 до 2
Идем от большего к меньшему
Только четные
каждое из четных умножаем на 2
"""
# list(range(10,1,-1))
print([num * 2 for num in range(10, 1, -1) if num % 2 == 0])

# Каждое слово которое больше 5 поставим точку с запятой
print([word + ';' for word in words if len(word) < 5])
