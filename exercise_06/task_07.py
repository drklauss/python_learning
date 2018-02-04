# Заполнить список из десяти элементов произвольными целочисленными значениями (без использования цикла).
# Удалить те элементы, значения которых не кратны 3.

import random

ARR_LEN = 10
myList = [random.randint(0, 1000) for _ in range(ARR_LEN)]
print('Список: ', myList)
result = []
for i in myList:
    if i % 3 == 0:
        result.append(i)
print('Список только с кратными 3 числами: ', result)
