# 4.	Показать первую цифру дробной части числа

def dig (x):
    x = (abs(x) * 10) % 10
    return x

numb = float(input('Введите число: '))

first_digit = dig (numb)
print (f'Первая цифра дробной части числа {numb}:', int(first_digit))