# Структуры данных
# Списки
l = list()
list1 = [1, 2, 3, 4, 5.1]
list2 = ['a', None, True]
string = 'string'

print(list1 + list2)
print(list1 * 2)

list1[0] = 0
# string[0] = 'S' # exception, строки нельзя изменять

list1.append(6)  # добавляет 6 в конец списка
print(list1[0:-1])  # стрез с 0 до последнего не вкл
print(list1[0:len(list1)])

# Списки передаются по ссылке
list3 = list1
list3.append('list3')  # добавляет объект в конец списка
list1.extend([111, 222])  # расширяет список на кол-во элементов
print(list1, list3)
print(id(list1), id(list3))

print(list1 == list2)  # стравнение списков где совпадают форматы данных

print(dir(list1))  # выводит методы объекта list1

list1.insert(0, [1, 2])  # добавляем в список элемент по индексу
list2.clear()  # очищаем весь список
list4 = list1.copy()  # копирует список
list5 = list1[0:len(list1)]  # копирование через срез

list6 = list4 + list5
print(list6, list6.count([1, 2]))  # подсчитывает кол-во элементов

print(list1.index(0))  # возвращает индекс искомого элемента

list2 = ['a', None, True]
pop2 = list2.pop(-1)  # возвращает элемент по индексу и достет его из списка
print(list2.remove('a'))  # удаляет по значению

list1 = [1, 2, 3, 0, 4, 5.1]
list7 = list(reversed(list1))  # возвращает перевернутый список не меняя его оригинал
list8 = list(sorted(list1))  # сортирует список по элементам которые можно сравнить
print(list7, list1, list8, list1)

list1.sort()  # сортирует список
list1.reverse()  # переворачивает список
print(list1)
