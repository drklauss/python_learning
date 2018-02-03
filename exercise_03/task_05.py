# Проверить, что введеные три числа (длины сторон) могут образовать треугольник.

a = b = c = 0
try:
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    c = float(input('Введите c: '))
except ValueError:
    print('Введены некорректные числа')
    exit()

if a + b > c and a + c > b and b + c > a:
    print('Треугольник можно построить')
else:
    print('Треугольник нельзя построить')
