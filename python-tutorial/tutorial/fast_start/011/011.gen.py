# Генераторы
import random


def gen():
    yield 10


print(next(gen()))  # next итерируется по объекту пока есть следующий элемент

g = gen()

print(next(g))


# print(next(g)) #StopIteration нет следующего значения

def gen2():
    yield 11
    yield 12
    yield 23


g2 = gen2()
next_el = next(g2)

# for el in g2:
#     print(el)

for el in 'HELLO':
    print(el)
    print(next_el)  # всега 11 пока не будет применен следующий итерируемый g2


# Рандомный генератор чисел (числа не повторяются если уже сгенерированы)
def randon_gen(amount):
    memory = []
    while True:
        n = random.randint(1, amount)
        if n in memory:  # если уже есть число ранее в памяти, вернусь в начало цикла и сгенерируем новое
            continue
        yield n  # иначе верну число
        memory.append(n)
        if len(memory) == amount:  # вернул все числа в заданном диапазоне
            return StopIteration


ran_gen = randon_gen(10)  # генерируем числа 1-10

for el in ran_gen:
    print(el)

# итерируемся по hello и добавляем рандомное число от 1-10
# el = next(ran_gen)
# for el in 'hello':
#     print(el+ str(next(ran_gen)))
# el1 = next(ran_gen)

print('--------------------------------\n')
# Протокол итерации и итераторы
l = ['1', '2', '3']

for i in l:
    print(i)
print('\n')
# print(next(l)) # TypeError: 'list' object is not an iterator

l = iter(l)  # преобразуем список в итерируемый объект
print(next(l))

print('\n')


# Создаем класс который поддерживает протокол итерации

class RndNums:

    def __init__(self, amount):
        self.amount = amount
        self.memory = []

    def __iter__(self):
        return self

    def __next__(self):  # возвращаем сгенерированный объект
        print('NEXT')
        n = random.randint(1, self.amount)

        while n in self.memory:  # пока сгенерированный n есть в memory, то генерируем новое рандомное число
            n = random.randint(1, self.amount)

        self.memory.append(n)

        if len(self.memory) == self.amount:
            print('STOP')
            raise StopIteration
        return n


rn = RndNums(11)

# print(next(rn))  # возвращаем следующий итерируемый объект от 1-10
for i in rn:
    print(i)

# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
