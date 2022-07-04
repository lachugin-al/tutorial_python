import csv

with open('big.csv', 'r') as f:
    reader = csv.DictReader(f) # чтение и преобразование в виде словаря

    for line in reader:
        print(dict(line))

    for line in reader:
        print(line['date'])

# создаем новый файл с использованием DictWriter
with open('small.csv', 'r') as f:
    reader = csv.DictReader(f)

    with open('new.csv', 'w') as f:
        header = ['name','phone','age']
        writer = csv.DictWriter(f, fieldnames=header)

        # необходимо записать header в новый файл
        writer.writeheader()

        for line in reader:
            writer.writerow(line)

# посчитать price для city
with open('big.csv', 'r') as f:
    reader = csv.DictReader(f)

    result = {}

    # for line in reader:
    # print(line['Price'], line['City'])

    # одинаковые города
    for line in reader:
        city = line['City'].strip() # убираем пробелы если они есть после названия
        price = int(line['Price'])

        # проверяем если в ловаре есть такое ключ (city) то прибавляем туда price
        try:
            result[city] += price
        except KeyError: # если нет такого ключа то добавляем ключи и стоимость
            result[city] = price

    # преобразуем в отсортированный список
    result = sorted(result.items(), key=lambda item: item[1], reverse=True )

    # print(result)
    for el in result:
        print(el)