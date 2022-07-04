# Dictionary / Словари

dict1 = {'key': 'value'}
dict2 = dict()
dict3 = dict(key='value')
dict4 = dict([('key1', 'value1'), ('ky2', 'value2')])

print(dict1)
print(dict2)
print(dict3)
print(dict4)

print(dict4['key1'])
print(dict4.get('key1'))  # при проверки ключей лучше использовать функцию get

dict5 = {(100, 50): 'value'}
print(dict5.get((100, 50)))

# ключами могут быть только неизменяемые структуры данных
# dict6 = {['1']: 'value1'}  # exception, list - изменяемая страуктура данных

dict7 = {1: {2: {3: '1'}}}
print(dict7.get(1).get(2).get(3))
