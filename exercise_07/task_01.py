# Написать функцию, вычисляющую сумму двух переданных чисел.


def sum_num(*args):
    """Функция вычисяет сумму переданных в нее чисел"""
    num_sum = 0
    for i in args:
        num_sum += i
    return num_sum


print(sum_num(5, 8))
