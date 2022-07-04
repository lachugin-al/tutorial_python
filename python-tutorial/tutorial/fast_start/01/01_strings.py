# Строки

string1 = "Python \nfast \n\t\r start"
"""
\n - перенос строки
\t - табуляция
\r - возврат каретки
"""
string2 = r"Python \nfast \n\t\r start"  # спецсимволы не обрабатываются
print(string1)
print(string2)

print(string1[0:-1])
print(string1[0:len(string1)])
print(string1[0:3])  # не включая элемент по индексу 3

name = input("Input name: ")
s = "Hello, %s %d %f" % (name, 10, 10.1)
s1 = "Hello {} {}".format(name, 10)
s2 = "Hello {greet_name} {greet_number}".format(greet_name=name, greet_number=10)
s3 = f"Hello, {name}"

print("Модификация регистра")
print(s1.lower())  # hello anton 10
print(s1.upper())  # HELLO ANTON 10
print(s1.capitalize())  # Hello anton 10
print(s1.title())  # Hello Anton 10
print(s1.swapcase())  # hELLO ANTON 10

print("Очистка строк")
word = "   !..,,Hello?..,,  "
print(word.strip())  # !..,,Hello?..,,
print(word.strip(".! ,?"))  # Hello
print(word.lstrip(".! ,?"))  # Hello?..,,
print(word.rstrip(".! ,?"))  # !..,,Hello

print("Проверка строк")
word1 = "Alpha12"
print(word1.isalnum())
print(word1.isalpha())
print(word1.islower())
print(word1.istitle())  # слова в строке начинаются все с заглавной буквы
print(word1.isdigit())  # строку возможно привести к цифре? True / False

print("Модификаторы длинны")
a = "test"
b = "some words"
c = "10.00"
print(a.zfill(10))  # заполняет 0000 слева, считат все символы в строке (000000test)
print(b.zfill(10))  # some words
print(c.zfill(10))  # 0000010.00
print(a.center(10, " "))  # отцентрирует строку и добавит по 3 пробела справа и слева

print("Методы поиска")
word = "Python: 'Быстрый старт'"
print(word.endswith("арт", 0, -1))  # True
print(word.endswith("арт", 0, -5))  # False
print(word.startswith("Pyt", 0, len(word)))  # True
print("Python" in word)  # True
print(word.find("Быстрый"))  # 9 index
print(word.index("старт"))
# print(word.index("старт1"))  # exception

print("Полезные методы")
print(word.replace("т", "Т"))  # заменяет все т на Т
print(word.replace("т", "Т", 1))  # заменяет только 1 первое т на Т

print("Замена конкретных буекв в виде словаря")
word_trans = word.maketrans("PБ:", "GB.")
"""Заменит
P --> G
Б --> B
: --> ."""
print(word.translate(word_trans))

word2 = "Python: 'Быстрый старт'"
print(word2.split())  # разбивает по пробелам ['Python:', '"Быстрый', 'старт"']
print(word2.split("т"))  # разбивает по т ['Python: "Быс', 'рый с', 'ар', '"']
print(list(word2))  # разбивает строку на символы
print(word2.partition("Быстрый"))  # разбить строку на 3 части по конкретному элементу и возвращаем кортеж

l = ["П", "р", "и", "в", "е", "т"]
print("*".join(l))  # П*р*и*в*е*т
print("".join(l))  # Привет

l2 = "".join(l)
print(type(l2))



