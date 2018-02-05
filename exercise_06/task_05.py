# Заполнить список из десяти элементов произвольными целочисленными значениями.
# Получить список из элементов певрого списка, стоящих на четных местах.

import random

startList = []
ARR_LEN = 10
for i in range(0, ARR_LEN):
    startList.append(random.randint(0, 1000))

print('Начальный список: ', startList)
evenDigitsList = []
# Первый способ
for i in range(0, ARR_LEN):
    if not i % 2:
        evenDigitsList.append(startList[i])
print('Список из четных индексов: ', evenDigitsList)
