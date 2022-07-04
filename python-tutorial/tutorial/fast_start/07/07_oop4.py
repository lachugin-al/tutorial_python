# Статические методы / @staticmethod
# Статические методы принадлежат пространству класса и могут быть вызваны без создания объекта
import random


class Math:
    ARG = 2

    @staticmethod
    def super_sum(a, b):  # перестала принимать self
        return Math.ARG + (a + b) * a * b


# Мы можем обращаться к этому методу 2 способами
m = Math()
print(m.super_sum(10, 20))

# либо без создания объекта
print(Math.super_sum(10, 20))


class A(Math):
    pass


print(A.super_sum(10, 20))


class B(Math):
    def super_sum(a, b):  # данный метод статический хотя он полиморфлен
        return a + b

    pass


print(B.super_sum(10, 20))


# Класс методы / @classmethod

class Car:
    __COUNT = 0
    __BRAND = 'toyota'

    def __init__(self, color, price):
        self.color = color
        self.price = price
        self.__up_counter()

    @property
    def brand(self):
        return self.__BRAND

    def set_brand(self, name):
        self.__BRAND = name

    @classmethod
    def set_brand_for_all(cls, name):  # cls - ссылаемся на класс
        cls.__BRAND = name

    # создаем конструктор при создании объекта класса через метод
    @classmethod
    def random_car(cls):
        return cls(color=random.choice(['red', 'white', 'black', 'blue', 'grey', 'blue', 'yellow']),
                   price=random.randint(10000, 1000000))

    # создаем счетчик
    @classmethod
    def __up_counter(cls):
        cls.__COUNT += 1
        print('создали новую машину')
        print(cls.__COUNT)
        if cls.__COUNT > 5:
            raise Exception('максимум машин')
        # cls.__COUNT += 1

    @property
    def count(self):
        return self.__COUNT


class OneCar(Car):
    pass


onecar1 = OneCar('onecar1', 123)
onecar1.set_brand_for_all('onecar')
"""
значение класса __BRAND поменяется только у наследника, так как
у родителя обозначен для функции def set_brand_for_all декоратор @classmethod 
если бы его небыло, то поменял бы у всех
"""
print(onecar1.brand)

car1 = Car('foo', 123)
car2 = Car('foo2', 456)
print(car1.brand)
print(car2.brand + '\n')

car2.set_brand_for_all('mini')  # поменяли для класса
print(car1.brand)
print(car2.brand + '\n')

car1.set_brand('bmw')  # поменяли для конкретного объекта
print(car1.brand)
print(car2.brand + '\n')

car3 = Car('foo3', 123)  # создали объект с уже измененным значением brand
print(car3.brand + '\n')

print(onecar1.brand)

rand_car1 = Car.random_car()
rand_car2 = Car.random_car()
rand_car6 = Car.random_car()
print(rand_car1.brand, rand_car1.color, rand_car1.price)
print(rand_car2.brand, rand_car2.color, rand_car2.price)

print(car3.count)
