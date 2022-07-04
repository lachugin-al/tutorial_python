import datetime
import os

print(os.getcwd())
os.chdir('test')
print(os.getcwd())
os.chdir('../')
print(os.getcwd())
os.chdir(os.getcwd() + os.sep + 'test') # os.sep для связывания строк и я вляется "/" в данном примере
print(os.getcwd())
os.chdir('../')
print(os.listdir()) # отобразить список директорий
# os.mkdir('test1') # создать директорию, но если она уже существует будет ошибка
os.makedirs('test1/test2') # создаем дерево директорий, создаст даже если уже есть данная директория
# os.makedirs('test1/test2/test3')

# os.rmdir('test1') # удаляет пустую директорию
os.removedirs('test1/test2') # удаляет все дерево, но в том случае если данная папка пустая

# os.rename('test.txt', 'new_test.txt') # переименование файла или директории
# os.rename('test', 'new_test') # переименование файла или директории

print(os.stat('test1.txt')) # статистика по файлу
print(datetime.datetime.fromtimestamp(os.stat('test1.txt').st_atime)) # распарсиваем дату создания файла

# Выводим содержимое директории и вложенных файлов
for path, dirs, files in os.walk(os.getcwd()): # в метод walk передаем текущую рабочуу директорию
    print('path', path)
    print('dirs', dirs)
    print('files', files)
    print('-----')
    # os.walk возвращает кортеж директорий, если есть вложенные то пройдется по всем директориям и идет далее

# Поиск / создание путей к файлам

file_path = os.path.join(os.getcwd(), 'test') # складывает пути
# file_path = os.path.join(os.getcwd(), '/test') # /test начинает отсчет от корневой директории (ненадо ставить слеш при линковке путей)
print(file_path)
print(os.path.basename(file_path)) # возвращает название директории/файла
print(os.path.dirname(file_path)) # возвращает название директории с путем
print(os.path.exists(file_path)) # возвращает сущетсвует или нет

# абсолютный путь до текущего файлы
print(os.path.dirname(__file__)) # путь до директории файла
print(os.path.join(os.path.dirname(__file__), __file__)) # путь директории + самого файла