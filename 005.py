# 5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# непонятное условие

numb = int (input ('введите число: '))
if (numb % 5 == 0 and numb % 10 == 0 or numb % 15 == 0) and numb % 30 != 0:
    print ('Число кратно 5 и (10 или 15), но не 30')
else:
    print ('Условие не выполнено')