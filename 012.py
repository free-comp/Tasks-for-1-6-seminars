# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов 
# последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def seq(n):
    return 3*n + 1

dict = {}
col = int (input ('Введите n: '))

key = range(1, col+1)
for i in key:
    dict[i] = seq(i)
print(dict)


# второй вариант:

# def seq(n):
#     return 3*n + 1

# col = int (input ('Введите n: '))
# dict = {key: seq(key) for key in range(1, col+1)}

# print(dict)
    
