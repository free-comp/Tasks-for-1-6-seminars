# 1.	По двум заданным числам проверить является ли одно квадратом второго

# a = int(input('Введите а: '))
# b = int(input('Введите b: '))

# if a == b ** 2:
#     print (f'Число {a} является квадратом {b}')
# elif b == a ** 2:
#     print (f'Число {b} является квадратом {a}')
# else:
#     print ('Ни одно из чисел не является квадратом другого')

def sq (x):
    return x ** 2

a = int(input('Введите а: '))
b = int(input('Введите b: '))

if a == sq (b):
    print (f'Число {a} является квадратом {b}')
elif b == sq (a):
     print (f'Число {b} является квадратом {a}')
else:
     print ('Ни одно из чисел не является квадратом другого')