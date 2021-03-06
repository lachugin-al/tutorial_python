# Массивы


a = [1, 2, 3, 4, 5]
# a1 = ['a','b','c','d','e']

# Можно прочитать значения в массиве по элемента
# Поменять значения не получится так как ссылаемся на временный обьект при присвоении
for i in a:
    print(i, type(i))  # выводит 1 элемент в массиве и его тип
    i = i + 1  # присваивает ссылку на временный объект равный сумме значения 1-го элемена и 1
    # по обьектам str так сделать не получится так как: can only concatenate str (not "int") to str
    print(i)

# Значение в массиве возможно поменять если обращаться по индексу
for i in range(len(a)):
    print(a[i])
    a[i] = a[i] * a[i]
    print(a[i])

l = [0] * 1000  # создаем массив из 1000 элементов
top = 0  # уровень заполненности кол-во элементов
x = int(input())
while x != 0:
    l[top] = x
    top += 1
    x = int(input())
for k in range(top - 1, -1, -1):  # в обратном порядке выводим список
    print(l[k])

# Копирование массива
n = int(input())  # array len
arr1 = [0] * n
arr2 = [0] * n
for i in range(n):
    arr1[i] = i + 1

arr3 = arr1 # просто ссылаемся на объект
arr3 = list(arr1) # создаем через конструктор копию списка arr1

# копируем
for i in range(n):
    arr2[i] = arr1[i] # присваиваем значения