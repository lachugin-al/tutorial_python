# MRO / Method resolution order
# super() / метод супер
# Волшебные методы __*__

class A:
    VAR = 'A'
    VAR2 = 'A2'

    def method(self):
        pass


class B:
    VAR = 'B'

    def method(self):
        pass


class C(B, A):
    def method(self):
        print(self.VAR + self.VAR2)


class D(C):
    pass


d = D()
d.method()

print(D.__mro__)
print(D.mro())


# ======================

# h - высота
# w - ширина

class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w


class Square(Rectangle):
    def __init__(self, s):
        # Rectangle.__init__(self, s, s) # можно переопределить конструктор родителя
        # либо через super
        super().__init__(h=s, w=s)


class Cube(Square):

    def area(self):
        return super().area() * 6

    def volume(self):
        return self.h ** 3  # используем переменную self.h родилея


sq = Square(10)
print(sq.area())

c = Cube(10)
print(c.area())
print(c.volume())


# =======================

class Magic:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # аналог toString
    def __str__(self):
        return '{}: {} power'.format(self.name, self.power)

    # toString для list
    def __repr__(self):
        return '{}: {} power'.format(self.name, self.power)

    # даем возможность обращаться к объекту как к функции
    def __call__(self, *args, **kwargs):
        return '{}: is calling'.format(self.name)

    # даем возможность складывать объекты
    def __add__(self, other):
        return Magic(self.name + other.name, self.power + other.power)




human = Magic('Gendalf', 100)
print(human)

legion = [human, human, human]
print(legion)

print(human())

superhuman = human + human
print(superhuman)
print([superhuman, superhuman])