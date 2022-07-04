# Контестный менеджер with
# file = open('file.txt')
# print(file.read())
# file.close()

files = []
for x in range(100):
    print(len(files))
    files.append(open('file.txt').close())


# чтобы постоянно не вспоминать что необходимо открытый файл закрывать, существует контекстный менеджер
# with open('file.txt', 'r+') as file:
#     file.write('diojfosmfs')
#     file.seek(0)
#     data = file.read()
#
# print(data)

class Contex:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


exaple_object = Contex()
with exaple_object:
    print('inside')

# Удобно использовать с базами данных или соединениями
