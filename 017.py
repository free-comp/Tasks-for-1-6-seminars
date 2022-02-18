# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file_017.txt 
# в одной строке одно число

n = int (input ('Укажите число n: '))

list_el = [n for n in range(-n, n + 1)] # список из N элементов
print(f'Имеется список чисел от {-n} до {n}:', list_el)

path = 'file_017.txt'
data = open (path, 'r') # открыли, прочитали
list_pos_ch = []
for line in data:
    list_pos_ch.append(line) # заполнили список строками из файла file_017.txt  
data.close()

list_position = [int(i) for i in list_pos_ch] # перевели список строк в список чисел
print('Найдем произведение чисел списка на позициях: ', list_position) # самопроверка

res = 1
for i in list_position:
   res *= list_el[i]
print('Произведение элементов на данных позициях равно', res)












