# Программа, которая считывает длины катетов прямоугольного треугольника и вычисляет длину его гипотенузы

import math

firstSide = float(input('Введите первый катет: '))
secondSide = float(input('Введите второй катет: '))
longSide = math.sqrt(firstSide ** 2 + secondSide ** 2)
print('Гипотенуза: {:.2f}'.format(longSide))
