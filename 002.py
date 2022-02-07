# 2.	Найти максимальное из пяти чисел

def max (arg_1, arg_2):
    result = arg_1
    if arg_2 > result:
        result = arg_2
    return result

a = int (input ('Введите число а: '))
b = int (input ('Введите число b: '))
c = int (input ('Введите число c: '))
d = int (input ('Введите число d: '))
e = int (input ('Введите число e: '))

max_1 = max (a, b)
max_2 = max (c, d)
max_3 = max (max_1, max_2)
maximum = max (max_3, e)

print(f'Maximum = {maximum}')

## для любого количества чисел (через список)
# def max (array):
#     max = array[0]
#     for i in array:
#         if i > max:
#             max = i
#     return max

# list_1 = [11, 6, -6, -44, 647, 23, 87]
# list_1 = [int(i) for i in input('Введите значения через пробел ').split()]
# result = max(list_1)
# print ('Maximum = ', result)

