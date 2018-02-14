# Создайте функции:
#
# * генерации двумерного массива случайных чисел с заданными размерами
# * поиска максимальныъ чисел в каждой строке двумерного массива (2 функции)
# * проверки любой переменной на то, что она содержит положительное целое число и приведение переменной к int
# Поместите полученные функции в отдельный модуль. Итоговую программу оформите в отдельном модуле (файле).
# Создайте двумерный массив 10х10 из случайных чисел. Ввод размера массива сделать с клавиатуры.
# Вычислить максимальный элемент в каждой строке массива и вывести полученный список на экран.

import os
import sys

# Идиотская вендоризация, просто жесть
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')
sys.path.append(vendor_dir)
import my_matrix as mtrx


i, j = mtrx.get_input_values()
matrix = mtrx.generate_matrix(i, j)
print(mtrx.get_max_values_in_each_row(matrix))
print(mtrx.get_max_values_in_each_row2(matrix))
