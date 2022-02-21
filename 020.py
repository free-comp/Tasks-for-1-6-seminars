# 20. Определить, присутствует ли в заданном списке строк, некоторое число 
# (список: [2, 'aaa', 'htd', 'ty', ‘55’])

list = [2, 'aaa', 'htd', 'ty', '55', 9.5, 'e', 4]

rez = []

for i in list:
    if type(i) == int or type(i) == float:
        rez.append(i)
print ('В списке присутствуют числа:', rez)

    


