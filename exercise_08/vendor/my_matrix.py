#!/usr/bin/python
# -*- coding: utf-8 -*-
# Пользователь вводит два целых числа x и y  > 1 (проверки на числа, целые, > 1).
# Нужно создать матрицу размером (x, y). Т.е. один список размером x, состоящий из списков размером y.
# Заполнить матрицу случайными числами в диапазоне от 0 до 1000.
# Найти номера столбцов, в которых содержатся числа в интервале от 90 до 100.

import random


def get_input_values() -> tuple:
    """Считывает введенные значения"""
    x = y = 0
    try:
        x = int(input('Число строк: '))
        y = int(input('Число столбцов: '))
    except ValueError:
        print('Введены некорректные числа')
        exit()
    if x <= 0 or y <= 0:
        print('Введены отрицательные числа')
        exit()
    return x, y


def generate_matrix(x: int, y: int) -> list(tuple()):
    """Создает и возвращает матрицу"""
    the_matrix = []
    for _ in range(x):
        the_matrix.append(tuple(random.randint(0, 1000) for _ in range(y)))
    return the_matrix


def get_max_values_in_each_row(a: list) -> list:
    """Возвращает максимальное значение каждой строки матрицы"""
    max_values = []
    for row in a:
        max_values.append(max(row))
    return max_values


def get_max_values_in_each_row2(a: list) -> list:
    """Возвращает максимальное значение каждой строки матрицы. Вариант 2"""
    max_values = []
    for row in a:
        max_value = 0
        for value in row:
            max_value = value if value > max_value else max_value
        max_values.append(max_value)
    return max_values
