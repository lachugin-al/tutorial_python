# Многомерные массивы
arr_2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(arr_2d)


def print_matrix_by_el(arr):
    for el in arr:
        for element_in in el:
            print(element_in, end=' ')
        print()
    print('-----')


def print_matrix_by_index(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


print_matrix_by_el(arr_2d)
print_matrix_by_index(arr_2d)

arr_2d.append([0, 0])

# Задачи
# Создать многомерный массив и заполнить значениями None
print('Input m n:', end='')
m, n = map(int, input().split())


def create_a2_arr(m, n):
    arr_2d = []
    for i in range(m):
        arr_2d_in = []
        for j in range(n):
            arr_2d_in.append(None)
        arr_2d.append(arr_2d_in)
    return arr_2d


print_matrix_index(create_a2_arr(m, n))

# Отобразить зеркально двухмерный массив
arr_2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def swap(i, j, arr_end):
    tmp = i[j]
    i[j] = i[arr_end]
    i[arr_end] = tmp


def mirror_2d_array(arr):
    for i in arr_2d:
        for j in range(len(i) // 2):
            # Меняем элементы местами
            # tmp = i[j]
            # i[j] = i[len(i) - 1 - j]
            # i[len(i) - 1 - j] = tmp

            # i1 = i[j]
            # i2 = i[len(i) - 1 - j]
            # print(i1,i2)
            # i1 , i2 = i2, i1
            # print(i1, i2)

            i[j], i[len(i) - 1 - j] = i[len(i) - 1 - j], i[j]

            # swap(i, j, len(i) -1 -j)

        print(i)


mirror_2d_array(arr_2d)
