# ООП

# Наследование
class Moving:
    def __init__(self, name='vehicle', wheels=20):
        self.name = name
        self.wheels = wheels
    # wheels = None

    def move(self):
        print('{} make move on {} wheels'.format(self.name, self.wheels))

class Mechanics:
    pass


# Наследование
class Vehicle(Mechanics):
    def __init__(self, name='vehicle', wheels=10):
        self.name = name
        self.wheels = wheels

    def stop(self):
        print('{} stoped'.format(self.name))
    # pass


class Car(Vehicle):
    wheels = 4

    def move(self):  # self - ссылка объект на самого себя - т.е. конкретный объект
        print('make move on {} wheels'.format(self.wheels))  # обращаемся к аттрибуту объекта
        # print('make move on {} wheels'.format(Car.wheels)) # обращаемся к аттрибуту класса

    def change(self, wheels):  # пришло 3
        print('change wheels from {} to {}'.format(self.wheels, wheels))  # от класса было 4, пришло 3
        self.wheels = wheels  # меняем у объекта на 3
        Car.wheels = wheels  # меняем у всех объектов данного класса
    # pass


# Наследование
class Bike(Vehicle, Moving):
    # по умолчанию проинициализируется классы от которых наследуется
    # и создается объект и если инициализации у нас в каждом классе, то
    # аттрибуты будут использоваться вот класса который идет первый в родителях
    pass


# Конструктор класса + наследование от класса Vehicle
class Train(Vehicle):
    # def __init__(self, name, wheels=10):
    #     self.name = name
    #     self.wheels = wheels

    def move(self):
        print('{} make move on {} wheels'.format(self.name, self.wheels))

    def change(self, wheels):
        print('{} change wheels from {} to {}'.format(self.name, self.wheels, wheels))
        self.wheels = wheels

    # pass

class SuperTrain(Train):
    pass


toyota = Car()
honda = Car()

print(toyota is honda)  # разные обьекты одного класса
print(toyota.wheels)  # доступ к аттрибуту класса

toyota.move()
honda.move()
toyota.change(3)
toyota.move()
honda.move()

train1 = Train(name='poezd', wheels=20)
train2 = Train(name='parovoz')
train1.move()
train2.change(30)
train2.stop()

print(issubclass(Train, Vehicle))
print(issubclass(SuperTrain, Vehicle))

print(isinstance(train1, Vehicle))
print(isinstance(train1, Car))

bike = Bike()
bike.move()