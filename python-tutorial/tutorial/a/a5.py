# Резюме 5-го урока курса по алгоритмам и структурам данных

"""
На 5-м уроке были пройдены следующие темы:
1. __add__(self, other) на примере Vector
2. ключевое слово global
3. lambda функции (f = lambda x) с map, filter (даёт list)
4. битовые операции и манипуляции
"""


""" 1. __add__(self, other) на примере Vector """


"""
class Vector:
    vectorCounter = 0

    def __init__(self, *args):
        self.args = args
        Vector.vectorCounter += 1

    @staticmethod
    def printVectorCounter():
        print(f"I created {Vector.vectorCounter} vectors")

    def printArguments(self):
        for coor in self.args:
            print(coor, end=" ")
        print()

    def __add__(self, other):
        a = [arg1 + arg2 for arg1, arg2 in zip(self.args, other.args)]
        return self.__class__(*a)

    def __str__(self):
        return self.__class__.__name__ + str(self.args)


v1 = Vector(1, 4, 8, 9)
v2 = Vector(5, 3, 2, 1)

Vector.printVectorCounter()
v1.printArguments()

v1.__str__()

print(v1)
print(v2)
print(v1 + v2)
"""


""" 2. Ключевое слово global """


"""
c = 1

def add():
    print(c)

add()
"""

"""
c = 1
    
def add():
    c = c + 2
    print(c)

add()
"""

"""
c = 0

def add():
    global c
    c = c + 2
    print("Inside add():", c)

add()
print("In main:", c)
"""


""" 3. lambda функции (f = lambda x) с map, filter (даёт list) """


# lambda arguments : expression

"""
mul = lambda a, b : a * b
print(mul(5, 6))
"""

"""
sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
filtered_result = filter(lambda x: x > 4, sequences) 
print(list(filtered_result))
"""

"""
sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
filtered_result = map(lambda x: x * x, sequences)
print(list(filtered_result))
"""


""" 4. Битовые операции и манипуляции """


"""
* Вступление про двоичную систему счисления и системы счисления в целом
* Вступление про and, or, xor, <<, >>, not
* (D) Дано целое число A и натуральное число i. Выведите число, которое получается из числа A установкой значения i-го бита равному 1.
* (F) Дано целое число A и натуральное число i. Выведите число, которое получается из числа A установкой значения i-го бита равному 0.
* (E) Дано целое число A. Выведите число, которое получается из числа A обнулением самого младшего включённого бита.
* (H) Дано целое число A и натуральное число i. Выведите значение i-го бита числа A, то есть 0 или 1.
* (G) Дано целое число A и натуральное число n. Выведите число, которое состоит только из n последних бит числа A (то есть обнулите все биты числа A, кроме последних n).
"""

# base = 10, цифры от 0 до 9
# base = 16, цифры от 0 до 9, A, B, C, D, E
# base = 36, цифры от 0 до 9, A-Z
# base = 2, цифры 0 и 1

# base = 10, 123 = 3 * 10^0 + 2 * 10^1 + 1 * 10^2 = 3 * 1 + 2 * 10 + 1 * 100
# base = 16, 123 = 3 * 16^0 + 2 * 16^1 + 1 * 16^2 = ...
# base = 2, 111 = 1 * 2^0 + 1 * 2^1 + 1 * 2^2 = 1 + 2 + 4 = 7
# base 2 -> 16
# x = 7
# 7 / 2 = 3 (1) ^
# 3 / 2 = 1 (1) ^
# 1 / 2 = 0 (1) ^
# 111
# x = 11
# 11 / 2 = 5 (1) ^
# 5 / 2 = 2  (1) ^
# 2 / 2 = 1  (0) ^
# 1 / 2 = 0  (1) ^
# 11 -> 1011 = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 = 1 + 2 + 0 + 8 = 11
# 11 / 4 = 2 (3)
# 2 / 4 = 0 (2)
# 11 -> 23 = 3 * 4^0 + 2 * 4^1 = 3 * 1 + 2 * 4 = 3 + 8 = 11

# & - операция И
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

# a = 1011
# b = 0110
# a & b = 0010 -> and

# or - операция ИЛИ
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1

# a = 1011
# b = 0110
# a | b = 1111

# xor - exclusive or - исключающее ИЛИ
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

#     3210
# a = 1011
# b = 0110
# a ^ b = 1101

# not - НЕ - операция отрицания
# a = 1011
# not a = 0100
# ~a = 0100

# << - left shift - левый битовый сдвиг
# a = 01011
# a << 1 = 10110
# a = (1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3) * 2^1
# a << x = a * 2^x
# (1 << x) = 1[00..000] -> x нулей
# (1 << 0) = 0001
# (1 << 1) = 0010
# (1 << 2) = 0100

# >> - right shift - правый битовый сдвиг
# a = 1011
# [a >>= 1] = [a //= 2] = 0101
# [a >>= x] = [a //= 2 ** x]

#                6543210
# a            = 0011010
# 1 << 2       = 0000100
# a | (1 << 2) = 0011110

def set_bit(value, bit):
    return value | (1 << bit)

# IN C++
# int       - [-2^31; 2^31 - 1] -> 32
# long long - [-2^63; 2^63 - 1] -> 64

# IN PYTHON
# int - [..., ...] -> 64-битный, но расширяемый

#                64   6543210
# a             =  0...0011010
# 1 << 3       =  0...0001000
# ~(1 << 3)     =  1...1110111
# a & ~(1 << 3) =  0...0010010

def clear_bit(value, bit):
    return value & ~(1 << bit)


#               7654 3210
# a           = 1100 1000
# a - 1       = 1100 0111
# a & (a - 1) = 1100 0000

def clear_last_set_bit(value):
    return value & (value - 1)

#                  3210
# a              = 1101
# 1 << bit       = 0100
# a & (1 << bit) = 0100

def what_bit(value, bit):
    return a & (1 << bit)

#                876543210
# a            = 101001110
# 1 << x       = 000100000
# (1 << x) - 1 = 000011111

# a                  = 101001110
# (1 << x) - 1       = 000011111
# a & ((1 << x) - 1) = 000001110

#                          01110
# x = 5

#     3210
# 8 = 1000
# 7 = 0111

# ans = a & mask
# mask = (1 << x) - 1

def last_x_bits(value, x):
    return a & ((1 << x) - 1)