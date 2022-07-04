class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
        self.cash = {}

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):  # если хотим обгулить уже посчитанные значения, которые уже есть в кеше
        if self.cash != {}:
            print('drop cash')
            self.cash = {}
        self._celsius = value

    @property
    def kelvin(self):
        if 'kelvin' not in self.cash.keys():
            self.cash['kelvin'] = self._celsius - 273.15  # не будет вычисляться если его хоть раз считали
        return self.cash['kelvin']

    @property
    def fahrengeight(self):
        if 'fahrengeight' not in self.cash.keys():
            self.cash['fahrengeight'] = self._celsius * 9 / 5 + 32  # не будет вычисляться если его хоть раз считали
        return self.cash['fahrengeight']


t = Temperature(20)

print(t.kelvin)
print(t.fahrengeight)
print(t.cash)

t.celsius = 10

print(t.kelvin)
print(t.fahrengeight)
print(t.cash)
