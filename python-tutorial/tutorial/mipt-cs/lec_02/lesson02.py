# Тип bool
flag = False
# flag = True

# n = int(input())
# for i in range(n):
#     x = int(input())
#     # if x% 10 == 0:
#     #     flag = True
#     flag = (x % 10 == 0) or flag

# если все будут делиться на 10 то flag будет True наче будет False
flag = True
n = int(input())
for i in range(n):
    x = int(input())
    flag = (flag and
            x % 10 == 0)
    # y=x%10
    # print(y, flag)

# Вложенные и последовательные if-ы
# хотим распечатать да если число делится на 2 и на 3
x = int(input())
if x % 2 == 0:
    print('да')
if x % 3 == 0:
    print('да')

if x == 1 or x == 2:
    print('yes')

if x % 2 == 0:
    if x % 3 == 0:
        print('/на 6')
# ==
if x % 2 == 0 and x % 3 == 0:
    print('/на 6')
else:
    print('not 6')

# Каскадная условная конструкция
# Дано целое число , предстоит напечатать букву в зависимости от числа
# Если отрицательные то A, если 0-5 не вкл то B, если 5-10 то C, если 10+ то D
x = int(input())
if x < 0:
    print('A')
elif x < 5:  # x >=0
    print('B')
elif x < 10:  # x > 5
    print('C')
else:  # x >= 10
    print('D')

# Необходимо определить четвердь I, II, III, IV (поделить на квадрат с осями x/y и отсекать по частям)
y, x = int(input())
if y > 0:
    if x > 0:
        print('I')
    else:
        print('II')
else:
    if x < 0:
        print('III')
    else:
        print('IV')
