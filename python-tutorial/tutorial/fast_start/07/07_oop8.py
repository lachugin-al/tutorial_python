# __slots__
import timeit

class A:
    pass


a = A()

a.at = 1
a.at1 = 1

print(a.at)
print(a.__dict__)


class B:
    __slots__ = ('a', 'b')

class C(B):
    __slots__ = ('a', 'b', 'c') # необходимо наследовать слотсы родителя иначе будет и аттрибут и слотс

b = B()
b.a = 1
# b.c = 2 # нельзя добавить аттрибут c

def actions(e):
    e.a = 1000
    e.b = 2000
    e.a
    e.b
    del e.a
    del e.b

def testA():
    actions(A())

def testB():
    actions(B())

print(timeit.repeat(testA))
print(timeit.repeat(testB)) # работает быстрее из-за __slots__