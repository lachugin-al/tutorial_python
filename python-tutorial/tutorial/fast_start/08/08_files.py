file = open('file.txt')
file = open('file.txt', mode='wt+')
# r - чтение
# r+ - чтение и перезапись (по аналогии с insert на клавиатуре)
# w - запись со стиранием всего текста
# w+ - запись с возможностью чтения того что записали
# t - по умолчанию как текстовый файл
# b - если надо открыть к примеру картинку - то позволяет читать в binary mode

file.write('some text 1')
file.seek(0) # перевод каретки в начало списка с элемента 0
print(file.read())
file.close() # обязательно закрываем файл после

file = open('logo.png', mode='rb+')
print(file.read())
file.close()

# копирование файлов через бинарную запись
file = open('logo.png', mode='rb+')
file_copy = open('logo_copy.png', mode='wb+')
file_copy.write(file.read())
file.close()
file_copy.close()

# дописывание в запись нового текста
file = open('file.txt', mode='a')
file.write('\nsome text 2')
file.close()

# можно создать через mode = xb в бинарном режиме
file2 = open('file.txt', mode='rb+')
file_copy2 = open('file_copy2.txt', mode='xb+')
file_copy2.write(file2.read())
file2.close()
file_copy2.close()