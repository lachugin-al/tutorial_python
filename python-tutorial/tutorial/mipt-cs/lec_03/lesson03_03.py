my_text = 'Робот живёт живёт на прямоугольном клеточном поле по периметру огороженном стенами Между клетками тоже могут встречаться стены'

# Возвращает словарь и кол-во повторяющихся слов в строке
my_dict = {}
for i in my_text.split(): # возвращаем массив и итерируемся по значениям массива
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

print(my_dict)

#
my_dict2 = {}
for i in my_text.split():
    my_dict2[i] = my_dict2.get(i, 0) + 1 # получаем значение по i, если его нет то добавляем новый ключ с значением 0 +1

print(my_dict2)
