# Резюме 4-го урока курса по алгоритмам и структурам данных

"""
На 4-м уроке были пройдены следующие темы:
1. решение "Котлет" https://informatics.mccme.ru/mod/statements/view3.php?id=276&chapterid=265#1
2. решение "Суммы кубов" https://informatics.mccme.ru/mod/statements/view3.php?id=254&chapterid=158#1
3. решение "Ханойских башен" https://informatics.mccme.ru/mod/statements/view.php?id=2550#1
4. что такое class?
5. __init__(self, ...)
6. объявление функций класса
7. использование класса (создание instance'ов, вызов функций)
8. про то, как сдавать задачи на LeetCode
9. __str__(self)
10. статические (class P: x = 1) и скрытые (self.__variable) variables
11. isinstance(obj, Class), issubclass(sub, sup)
"""


""" 1. Решение "Котлет" https://informatics.mccme.ru/mod/statements/view3.php?id=276&chapterid=265#1 """


def kotlety():
    k = int(input())
    m = int(input())
    n = int(input())

    # k - кол-во котлет, которое помещается на сковороду
    # m - сколько жариться котлета с одной стороны
    # n - сколько всего котлет

    if n <= k:
        print(2 * m)
        return

    n *= 2  # кол-во полу-котлет

    # n поделить на k округлённое вверх
    # формула: (n + k - 1) // k

    # n % k == 0 ->
    #   n // k == (n + k - 1) // k

    # n % k > 0 ->
    #   n // k + 1 == (n + k - 1) // k

    # print((n + k - 1) // k * m) - в одну строку
    if n % k != 0:
        print((n // k + 1) * m)
    else:
        print(n // k * m)


# kotlety()


""" 2. Решение "Суммы кубов" https://informatics.mccme.ru/mod/statements/view3.php?id=254&chapterid=158#1 """


# f(n, k) - надо разложить n, используя не более k кубов
# for x in range(cbrt(n), 0, -1)
#   f(n - x ** 3, k - 1)
# if k == 0 and n > 0: не получилось
# if k >= 0 and n == 0: получилось

def cbrt(x):
    return int(x ** (1 / 3))


def f(n, k=8):
    if n == 0:
        return True
    if k == 0:  # n > 0
        return False

    for x in range(cbrt(n), 0, -1):
        if f(n - x ** 3, k - 1) == True:
            print(x, end=" ")
            return True

    return False


def summaKubov():
    n = int(input())

    if f(n) == False:
        print("IMPOSSIBLE")


# summaKubov()


""" 3. Решение "Ханойских башен" https://informatics.mccme.ru/mod/statements/view.php?id=2550#1 """


# from - откуда, с какого стержня
# to - на какой стержень
# aux - вспомогательный стержень
# n - кол-во дисков

# 1й диск - самый маленький
# 2й диск - средний
# 3й диск - самый большой
# ...

# hanoi(n, from, to, aux):
#   if n == 0:
#     return
#   hanoi(n - 1, from=from, to=aux, aux=to)
#   print(f"{n} {from} {to}")
#   hanoi(n - 1, from=aux, to=to, aux=from)

# hanoi(n, from, to)
# aux = 6 - from - to


def hanoi(n, start, end):
    if n == 0:
        return

    aux = 6 - start - end

    # 1 2 3
    # 1 + 2 + 3 = 6
    # start = 1, end = 3
    # aux = 6 - start - end
    # 1 + 2 + 3 - start - end = aux

    hanoi(n - 1, start, aux)
    print(f"{n} {start} {end}")
    hanoi(n - 1, aux, end)


# n = 1 -> 1
# n = 2 -> 3
# n = 3 -> 7

# f(1) = 1
# f(n) = 2 * f(n - 1) + 1, n >= 2
# f(n) = (2 ** n) - 1

def hanoiSolution():
    n = int(input())
    hanoi(n, 1, 3)

# hanoiSolution()


""" 4. Что такое класс? """
""" 5. __init__(self, ...) """
""" 6. Объявление функций класса """
""" 7. Использование класса (создание instance'ов, вызов функций) """
""" 9. __str__(self) """
""" 10. Статические (class P: x = 1) и скрытые (self.__variable) variables """
""" 11. isinstance(obj, Class), issubclass(sub, sup) """

# Классы используются для организации информации.

person = ("Kairat", 17, 180, 78) # кто потом вспомнит, что 1-й индекс это возраст, 2-й это рост, а 3-й это вес?

# Лучше организуем информацию в класс Person.

class Person:  # или class Person(object):
    # peopleCount - статическая переменная, которая не относится
    # к создаваемым объектам класса Person, а именно к самому классу Person.
    # В ней мы будем считать кол-во созданных объектов класса Person.

    peopleCount = 0

    # Функция инициализации __init__(self, param1, param2, ...) позволит создавать
    # объекты класса Person с помощью вызова Person(param1, param2, ...)
    def __init__(self, name, age, height, weight):  # self позволяет обращаться конкретно к объекту, на котором вызывается функция
        # у создаваемого объекта Person будут объявлены публичные атрибуты name, height, weight
        self.name = name
        self.height = height
        self.weight = weight

        self.__age = age  # атрибут __age (возраст) является скрытым (из-за __) и к нему нельзя получить доступ вне класса

        Person.peopleCount += 1  # при создании объекта класса Person увеличим кол-во созданных объектов на 1

    def sayHello(self):
        print(
            f"Hello! My name is {self.name}. I am {self.__age} years old. "
            f"I am {self.height} cm tall, and my weight is {self.weight} kg."
        )


personObj = Person("Kairat", 17, 180, 78)
print(Person.peopleCount)  # 1

personObj.sayHello()


# Каждый класс наследует функции, атрибуты и свойства у других классов,
# как минимум у базового класса под названием object.
class Animal(object):
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight


class Human(Animal):
    def __init__(self, name, age, height, weight):
        super().__init__(age, weight)  # как бы создаём объект Animal и превращаем его в объект Human
        self.name = name
        self.height = height


obj1 = Human("Kairat", 17, 180, 78)
obj2 = Human("Bayel", 18, 175, 60)

# isinstance(obj, class) - является ли объект obj объектом класса class
# issubclass(subclass, superclass) - является ли класс subclass подклассом класса superclass

print(isinstance(obj1, Human))  # True
print(isinstance(obj1, Animal))  # True
print(issubclass(Human, Animal))  # True
print(issubclass(Animal, Human))  # False

x = 15

if isinstance(x, int):  # является ли x объектом класса int
    print("x is an integer")