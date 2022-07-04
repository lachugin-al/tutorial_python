import json

# при помощи нативной библиотеки json можно превратить файл json в объект python

with open("example.json") as file:
    print(file.read())

with open("example.json") as file:
    data = json.loads(file.read())

print(data)

# меняем значения
del data['String']
data['NumberKey'] = 1000

print(data)

# записываем на выход
with open('out.json', 'w+') as file:
    # file.write(str(data).replace("'", "\""))
    # file.write(str(data).replace('\'', '\"'))
    # либо методами json
    file.write(json.dumps(data))