d = {'1': 4,
     '2': 5,
     '3': 6}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

print(d)


l = [11,12,13]
for i in l:
    print(i) # получаем значение по индексу

for i in range(len(l)):
    print(i) # получаем индекс по длинне массива
    print(l[i]) # получаем значение по индексу