# 21.	Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


from itertools import count


def get_index(lst, el):
    return [i for i in range(len(lst)) if lst[i] == el]
    

#дано:
given_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"] 
str = 'qwe'
pos = 2


posit = get_index(given_list, str) # ищем все вхождения, делаем из них список
print (posit)

posit = get_index(given_list, str)  # ищем все вхождения, делаем из них список
if len(posit) < pos:
    print(-1)
else:
    print (posit[pos-1])
