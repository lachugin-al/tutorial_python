# While

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 'Python: Быстрый старт'

t1 = []

while len(t):
    t1.append(t.pop(0) ** 2)  # достаетм лемент из списка t и добавлем его в список t1 с возведением в степень 2

print(t1)  # вернет массив

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t1.clear()
while len(t):
    el = t.pop(0)
    print(el, el % 2)
    if el % 2:  # 1,3,5 ... (мы ожидаем el%2 == True or False, 1%2 = 1, 2%2 = 0)
        continue  # продолжаем выполнение цикла со следующей итерации
    t1.append(el ** 2)
print(t1)
print(t)

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t1.clear()
while len(t):
    el = t.pop(0)
    if el % 2:
        t1.append(el ** 2)
print(t1)

for i in range(len(s)):
    if s[i] == ':':
        break
    print(s[i], end='')
else:
    print('привет')
print()

for el in s:
    print(el, end="**")
print()

for el in range(0, len(s)):
    print(el, end="")
    print(s[el])

# остаток от деления True/False
# 1%2 = 1 = True
# 2%2 = 0 = False (так как 0 всегда = False)
print(bool(1 % 2)) # True
print(bool(2 % 2)) # False
