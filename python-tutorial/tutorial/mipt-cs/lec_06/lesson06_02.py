# Квадратичные сортировки
# значит что кол-во операций чтобы его отсортировать = n**2
# O(n**2)

# Сортировка вставками (insert sort)
# кол-во сравнений в массиве из 5 элементов
# 1+2+3+4

# Сортировка методом выбора (choise sort)
# кол-во сравнений в массиве из 5 элементов
# 1+2+3+4

# Сортировка методом пузырька (bubble sort)
# кол-во сравнений в массиве из 5 элементов
# 4+3+2+1

def insert_sort(a):
    """ Сортировка списка a вставками """
    n = len(a)
    for top in range(1, n):
        tmp = top
        while tmp > 0 and a[tmp - 1] > a[tmp]:
            a[tmp], a[tmp - 1] = a[tmp - 1], a[tmp]
            tmp -= 1    # если происходит обмен переменными, то самая меньшее число будет перемещено на tmp -1 (то есть в самое начало списка)


def choise_sort(a):
    """ Сортировка списка a выбором """
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    """ Сортировка списка a методом пузырька """
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def test_sort(sort_algo):
    print('Тестируем: ', sort_algo.__doc__)  # достучимся до документ строки метода выше
    print('testcase #1: ', end='')
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algo(a)
    # сравнение массивов очень затратно
    # if a == a_sorted:
    #     print('ok')
    # else:
    #     print('fail')
    print('ok' if a == a_sorted else 'fail')

    print('testcase #2: ', end='')
    a = [1, 3, 2, 3, 2]
    a_sorted = [1, 2, 2, 3, 3]
    sort_algo(a)
    print('ok' if a == a_sorted else 'fail')

    print('testcase #3: ', end='')
    a = list(range(10, 20)) + list(range(0, 10))  # арифметическая прогрессия
    a_sorted = list(range(20))
    sort_algo(a)
    print('ok' if a == a_sorted else 'fail')


test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)

# Сортировка подсчетом O(n) времени,
# а по памяти O(m), где m кол-во отдельных элементов
# Алгоритм однопроходный
# необходимо знать диапазон допустимых значений (тоесть только цифры например)
a = [1, 2, 3, 2, 3, 4, 5, 3, 4, 9]
n = len(a)
f = [0] * 10
for i in range(n):
    x = int(input())
    f[x] += 1
