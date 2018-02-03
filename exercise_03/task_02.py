# Определить четверть координатной плоскости по координатам x и y.
# Применить минимум два разных подхода в указании условий.

x = y = 0.0
try:
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))
except ValueError:
    print('Введены некорректные числа')
    exit()

if x == 0:
    print('Точка находится на оси Х')
    if y == 0:
        print('Точка находится в центре координат')
        exit()
if y == 0:
    print('Точка находится на оси Y')
    exit()

coord = 1
if x < 0 < y:
    coord = 2
elif x < 0 > y:
    coord = 3
elif x > 0 < y:
    coord = 4

print('Координатная четверть: {}'.format(coord))


