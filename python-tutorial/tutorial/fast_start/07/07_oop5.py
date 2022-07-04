# Абстрактные классы и модуль ABC
from abc import ABC, abstractmethod


# абстрактным класс может называться когда есть хотябы один абстрактный метод
# нельзя создать инстанс абстрактного класса
class Figure(ABC):  # необходимо унаследоваться от класса ABC

    # @property # можно задекорировать и так и все равно будет работать
    @abstractmethod
    def area(self):
        # raise NotImplementedError
        pass

    def name(self):
        pass


class Circle(Figure):

    def area(self):
        return ''


f = Circle()
