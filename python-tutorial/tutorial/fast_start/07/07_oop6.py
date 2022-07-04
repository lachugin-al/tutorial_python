# Множественное наследование
import random


class Animal:

    def sound(self):
        raise NotImplementedError

class Swimming:
    name = None

    def swim(self):
        print(self.name + ' is swiming')

    def run(self):
        print(self.name + ' is not running')

class Running:
    name = None

    def run(self):
        print(self.name + ' is running')

class Fish(Animal, Swimming, Running):

    def __init__(self, name):
        self.name = name

    def sound(self):
        print('sound')

fish = Fish('Fish' + str(random.randint(1,10)))
fish.sound()
fish.swim()
fish.run()