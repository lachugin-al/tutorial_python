# comma separated values
import csv

with open('small.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)

"""
['name', 'phone', 'age']
['Misha', '8911111110', '20']
['Masha', '8911111111', '21']
['Mosha', '8911111112', '22']
"""

# создаем csv файлы
with open('small.csv', 'r') as file:
    reader = csv.reader(file)

    with open('new.csv', 'w') as file:
        writer = csv.writer(file)
        # writer = csv.writer(file, delimiter='+')

        for line in reader:
            writer.writerow(line)