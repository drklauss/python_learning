# Проверить, что хотя бы одно из чисел a или b оканчивается на 0.

a = b = 0
try:
    a = float(input('Введите A: '))
    b = float(input('Введите B: '))
except ValueError:
    print('Введены некорректные числа')
    exit()

if a % 10 == 0 or b % 10 == 0:
    print('Одно из чисел оканчивается на 0')
else:
    print('Ни одно из чисел не оканчивается на 0')

