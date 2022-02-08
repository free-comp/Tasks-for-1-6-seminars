# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с 
# координатами Х и У

x = int (input('Задайте значение х: '))
y = int (input('Задайте значение y: '))

if x > 0 and y > 0:
    print (f'Точка с координатами х = {x} и у = {y} находится в I четверти')
elif x > 0 and y < 0:
    print (f'Точка с координатами х = {x} и у = {y} находится в II четверти')
elif x < 0 and y < 0:
    print (f'Точка с координатами х = {x} и у = {y} находится в III четверти')
elif x < 0 and y > 0:
    print (f'Точка с координатами х = {x} и у = {y} находится в IV четверти')
elif (x > 0 and y == 0) or (x < 0 and y == 0):
    print (f'Точка с координатами х = {x} и у = {y} находится на оси Х')
elif (x == 0 and y > 0) or (x == 0 and y < 0):
    print (f'Точка с координатами х = {x} и у = {y} находится на оси Y')
else:
    print (f'Точка с координатами х = {x} и у = {y} находится в начале координат')