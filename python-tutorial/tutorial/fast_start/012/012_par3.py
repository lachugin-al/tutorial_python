#!/usr/bin/python3

# Парсер аргументов для командной строки
# Улучшаем до состояния библиотеки
import argparse


def my_sum(a, b):
    return a + b


def my_dif(a, b):
    return a - b


def my_mult(a, b):
    return a * b


if __name__ == '__main__':

    parcer = argparse.ArgumentParser(description='Python example script')

    # ./ 012_par3.py -h, --help
    # ./ 012_par3.py 10 100 - a + -v
    parcer.add_argument('a', type=int, help='First argument')
    parcer.add_argument('b', type=int, help='Second argument')  # позиционный аргумент не может быть False
    parcer.add_argument('--action', '-a', choices=['+', '-', '*'], help='Action argument',
                        required=True)  # required обязательность аргумента
    parcer.add_argument('--verbose', '-v', help='Show or not message',
                        action='store_true')  # аргумент без значения превращаем во флаг True / False
    parcer.add_argument('--all', nargs=3, type=int)  # позволяет передавать аргументы в качестве последовательности

    argv = parcer.parse_args()

    print(argv)
    a = argv.a
    b = argv.b
    action = argv.action
    verbose = argv.verbose

    # print('Solution for: {} {} {}'.format(a, action, b) if verbose else '')
    if verbose:
        print('Solution for: {} {} {}'.format(a, action, b))

    if action == '+':
        print('Sum is: ' if verbose else '', my_sum(a, b))
    elif action == '-':
        print('Diff is: ' if verbose else '', my_dif(a, b))
    elif action == '*':
        print('Multi is: ' if verbose else '', my_dif(a, b))
