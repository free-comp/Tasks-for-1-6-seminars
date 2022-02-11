# 14. Подсчитать сумму цифр в вещественном числе.


# numb =  input('Введите вещественное число, в качестве разделителя используйте точку: ')
# numb_str = numb.replace('.', '')
# sum = 0
# for el in list(numb_str):
#     sum += int(el)
# print ('Сумма цифр в числе равна', sum)



numb =  input('Введите вещественное число, в качестве разделителя используйте точку: ')
numb_str = numb.replace('.', '')
rez = sum([int(i) for i in numb_str])
print ('Сумма цифр в числе равна', rez)