# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def expres1(x, y):
    result = not (x or y)
    return result

def expres2(x, y):
    result = not x and not y
    return result

def print_result(x, y):
    print(f'При значении x = {x}, y = {y}')
    if (expres1(x, y) == expres2(x, y)):
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')

print_result(True, True)
print_result(True, False)
print_result(False, True)
print_result(False, False)