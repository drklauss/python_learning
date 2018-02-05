# Пользователь вводит два целых числа x и y  > 1 (проверки на числа, целые, > 1).
# Нужно создать матрицу размером (x, y). Т.е. один список размером x, состоящий из списков размером y.
# Заполнить матрицу случайными числами в диапазоне от 0 до 1000.
# Найти номера столбцов, в которых содержатся числа в интервале от 90 до 100.

import random

x = y = 0.0
INTERVAL = range(90, 100)

try:
    x = int(input('Число строк: '))
    y = int(input('Число столбцов: '))
except ValueError:
    print('Введены некорректные числа')
    exit()
if x <= 0 or y <= 0:
    print('Введены отрицательные числа')
    exit()

the_matrix_has_you = []
res_columns = []
for _ in range(x):
    the_matrix_has_you.append([random.randint(0, 1000) for _ in range(y)])

for row in the_matrix_has_you:
    for value in row:
        if value in INTERVAL:
            res_columns.append(row.index(value) + 1)
print(set(res_columns))
