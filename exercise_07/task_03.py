# Написать функцию, вычисляющую сумму двух переданных чисел.


def sum_num(val_tuple):
    """Функция вычисяет сумму переданных в нее чисел"""
    num_sum = 0
    for i in val_tuple:
        num_sum += i
    return num_sum


def get_num():
    """Функция возвращает введенные с клавиатуры числа"""
    x = int(input('Число A: '))
    y = int(input('Число B: '))
    return x, y


nums = ()
try:
    nums = get_num()
except ValueError:
    print('Введены некорректные числа')
    exit()
print(sum_num(nums))

