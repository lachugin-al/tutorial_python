file = open('file.txt', mode='w+')
file_text = open('file.txt', mode='r+')
file_bin = open('logo.png', mode='rb')
this_file = open('08_files2.py', mode='r')

# уникальный идентификатор файла
print(file.fileno())
print(file_text.fileno())
print(file_bin.fileno())
print(this_file.fileno())

# доступный для чтения True / False
print(file.readable())

# доступный для записи True / False
print(file.writable())

# доступный для доступа к файлу и мы можем с ним оперировать True / False
print(file.seekable())
# std_out = open('dev/stdout', 'w')


# получение информации о положении каретки
file.write('hello ' + 'anton ' + '\n' + 'привет')
print(file.tell())
file.seek(0)
print(file.tell())


print(file.readline()) # прочитает только первую строку
file.seek(0)
print(file.readlines()) # выведет массив из строк вместе с переносами

file.seek(0)
file.writelines(['hello', ' anton ']) # не стирает весь файл а заменяет построчно

file.seek(0)
file.truncate(255) # обрезает информацию по размеру а остальное заполняет  

print(file.read())

file.close()
file_text.close()
file_bin.close()
this_file.close()