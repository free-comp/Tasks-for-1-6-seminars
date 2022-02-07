# 3.	Вывести на экран числа от -N до N

numb = int (input('Введите положительное число: '))
if numb < 0:
    print('Попробуйте снова.')
    quit()
else:
    print(f'Числа от -{numb} до {numb}: ')
    r = range(-numb, numb+1)
    for i in r:
        print (i, end = ' ')
    print()


