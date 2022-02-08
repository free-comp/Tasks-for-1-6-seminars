# 10.	Найти расстояние между двумя точками пространства

import math

def distance (x1, y1, z1, x2, y2, z2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist

print ('Задайте координаты для точки в пространстве: ')
x1 = int (input(f'x1: '))
y1 = int (input(f'y1: '))
z1 = int (input(f'z1: '))
x2 = int (input(f'x2: '))
y2 = int (input(f'y2: '))
z2 = int (input(f'z2: '))

result = distance (x1, y1, z1, x2, y2, z2)
print ('Расстоние между двумя точками в пространстве равно', round(result, 3))