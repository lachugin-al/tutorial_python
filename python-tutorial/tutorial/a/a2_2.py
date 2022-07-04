arr = [2, 7, 11, 15]
result = 9

# Решение через массив
for i in range(len(arr)-1):
    i2 = i + 1
    for i2 in range(len(arr)):
        if result - arr[i2] == arr[i]:
            print(i, i2)
            break

# Решение через словарь
d = {}
for i in range(len(arr)):
    d[arr[i]] = i
    if result - arr[i] in d:
        print(i, d[result-arr[i]])
