# 11. Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.


count = int (input('Введите количество членов для последовательности N: '))

list = [(-3)**n for n in range(0,count)]
print ('Последовательность: ', list)


# второй вариант
# def res (n):
#     return (-3)**n

# count = int (input('Введите количество членов для последовательности N: '))

# list = []
# for i in range(0,count):
#     list.append(res(i))
 
# print(list)



