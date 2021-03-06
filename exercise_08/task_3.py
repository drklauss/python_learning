# Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке,
# разделяя их пробелами или новыми строками.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).


def print_n_recurse(n):
    """Выводит на экран все цифры числа по одной в обратном порядке"""
    if n // 10 > 0:
        print(n % 10, end=" ")
        print_n_recurse(n // 10)
    else:
        print(n % 10)
        exit()


print_n_recurse(185998798797)
