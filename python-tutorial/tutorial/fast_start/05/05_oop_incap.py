# Инкапсуляция

class Computer:
    cpu = 1000
    gpu = 8

    def power_on(self):
        print('power_on')

    def power_off(self):
        print('power_off')


class MacBook(Computer):
    owner = None  # public
    _id = None  # protected
    __manufacturer = 'Apple'  # private

    def __init__(self, _id):
        self._id = _id

    # как получать доступ а аттрибутам?
    def get_manufature(self):
        return self.__manufacturer

    def set_id(self, new_id):
        self._id = 'this_id_is_not_original_' + new_id

    # доступ к методам
    def __set_manufacture(self, man):
        self.__manufacturer = 'new_manufacture_' + man

    def change_manufacture(self, man):
        print('Warning')
        self.__set_manufacture(man)

    # переопределение метода / полиморфизм
    def power_on(self):
        print('power_onnnnn')

mac1 = MacBook('1')
mac1.owner = 'A'
mac1.owner = 'B'  # меняет данные

mac1._id = '2'  # так не принято делать
mac1.__manufacturer = 'Microsoft'

# даже если обратиться к приватному имени то поменяв его можно обратиться к тому значению которое бло изначально
# оно будет спрятано в имени _MacBook__manufacturer
# это плохая практика и очень не рекомендуется обращаться к таким аттрибутам
print(dir(mac1))
print(mac1._id, mac1.__manufacturer, mac1._MacBook__manufacturer)

print(mac1.get_manufature())
print(mac1.set_id('100'))
print(mac1._id)

print(mac1.change_manufacture('Samsung'))
print(mac1.get_manufature())


macC = Computer()
macM = MacBook('10')
print(macC.power_on(), macM.power_on())