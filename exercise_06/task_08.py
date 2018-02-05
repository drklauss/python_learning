# Заполнить список из десяти элементов произвольными целочисленными значениями.
#  Затем четные элементы расположить в начале списка, нечетные - в конце.


import random

ARR_LEN = 10
startList = [random.randint(0, 1000) for _ in range(ARR_LEN)]
result = []
print('Список: ', startList)
for i in startList:
    if i % 2 == 0:
        result.insert(0, i)
    else:
        result.append(i)
print('Сначала четные, потом нечетные: ', result)

