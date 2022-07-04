#!/usr/bin/python3

# Парсер аргументов для командной строки
import argparse

parcer = argparse.ArgumentParser(description='Python example script')

parcer.add_argument('a', type=int)  # указываем тип для аргемунта
parcer.add_argument('b', type=int)
parcer.add_argument('action', choices=['+', '-'])  # добавляем фильтрацию аргументо которые пришли на фход
# parcer.add_argument('--action', default='+') # добавляем фильтрацию аргументо которые пришли на фход и добавляем дефолтное значение

argv = parcer.parse_args()

print(argv)

# ./012_par2.py
# usage: 012_par2.py [-h] a b action
# 012_par2.py: error: the following arguments are required: a, b, action

# ./012_par2.py 10 100 +
# Namespace(a='10', action='+', b='100')

# использоуем аргументы через точку
a = argv.a
b = argv.b
action = argv.action

if action == '+':
    print('Sum is: ', a + b)
else:
    print('Diff is: ', a - b)
