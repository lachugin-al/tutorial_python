a = 'anagram'
b = 'margana'

# Решение через сортировку
if sorted(a) == sorted(b):
    print(True)
else:
    print(False)

#
a1 = [a]
print(type(a1))
a1.reverse()
print(a1)