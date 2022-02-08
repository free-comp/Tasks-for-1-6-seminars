# 10.	Найти расстояние между двумя точками пространства

import math

def distance (x1, y1, z1, x2, y2, z2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist

print ('Задайте координаты для точки в пространстве: ')
x1 = int (input('x1: '))
y1 = int (input('y1: '))
z1 = int (input('z1: '))
x2 = int (input('x2: '))
y2 = int (input('y2: '))
z2 = int (input('z2: '))

result = distance (x1, y1, z1, x2, y2, z2)
print ('Расстоние между двумя точками в пространстве равно', round(result, 3))