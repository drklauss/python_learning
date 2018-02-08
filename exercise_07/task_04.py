# Написать функцию, принимающую длину стороны квадрата и рассчитывающую периметр квадрата, его площадь и диагональ.
# Сделать два и более варианта функции, которые должна отличаться количеством возвращаемых переменных.
# Не забыть про проверки входных данных в самой функции.


def square_calc(sides_tup):
    """Функция вычисляет периметр квадрата, его площадь и диагональ"""
    perimeter = 2 * (sides_tup[0] + sides[1])
    square = sides_tup[0] * sides[1]
    diagonal = (sides_tup[0] ** 2 + sides[1] ** 2) ** 0.5

    return perimeter, square, diagonal


def get_sides():
    """Функция возвращает введенные с клавиатуры числа"""
    x = int(input('Сторона A: '))
    y = int(input('Сторона B: '))
    return x, y


sides = ()
try:
    sides = get_sides()
except ValueError:
    print('Введены некорректные числа')
    exit()
per, sq, diag = square_calc(sides)
print('Периметр: {}, Площадь: {}, Диагональ: {:.2f}'.format(per, sq, diag))
