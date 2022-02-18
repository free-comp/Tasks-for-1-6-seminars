# 18. Реализовать алгоритм перемешивания списка. 

import random

list = [i  for i in range(0, 11)]
print('Дан список:', list)
random.shuffle(list)
print('Перемешанный список:', list)

# rez = sorted (list, key = lambda a: random.random()) # с использованием случайного ключа для сорт.
# print ('Перемешанный список:', rez)