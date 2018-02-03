# Заполнить список из шести элементов произвольными целочисленными значениями.
# Найти максимальный элемент в списке, вывести его и его номер на экран.
# Два варианта вычисления максимального элемента: с приминением цикла и без него.

import random

myList = []
ARR_LEN = 6
for i in range(0, ARR_LEN):
    myList.append(random.randint(0, 1000))

print('Список: ', myList)
# Первый способ
maxValue = 0
for i in myList:
    if i > maxValue:
        maxValue = i
print('1.Максимальное значение: ', maxValue)
# Второй способ
print('2.Максимальное значение: ', max(myList))
