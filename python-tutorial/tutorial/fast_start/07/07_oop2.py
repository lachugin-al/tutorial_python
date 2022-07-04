# Property, позволяет делать из методов свойства

class Car:
    __wheels = 4

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter  # позволет получить доступ к приватному аттрибуту
    def wheels(self, num):
        print('устанавливаем колеса')
        if num > 5:
            num = 4
        self.__wheels = num

    @wheels.deleter
    def wheels(self):
        print('снимаем колеса')
        self.__wheels = 0

car = Car()

# значение возвращается через метод
# print(car.wheels())

# если указано property то позволяет доступ к закрытому свойству
# созраняю аттрибут приватным, созраняю ограниченный доступ но обращаюсь к этому свойству
print(car.wheels)

car.wheels = -10

print(car.wheels)
