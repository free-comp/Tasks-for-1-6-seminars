# 16.Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

from tkinter import N


def seq(x):
    return (1+(1/x))**x


count = int (input('Введите количество членов для последовательности N: '))

list = [seq(n) for n in range(1,count+1)]
print ('Последовательность: ', list)

print (f'Сумма {count} чисел последовательности: ', round (sum(list), 2))
