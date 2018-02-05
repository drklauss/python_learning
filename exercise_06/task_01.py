# Заполнить список из шести элементов произвольными целочисленными значениями. Вывести список на экран.

import random

myList = list()
for i in range(0, 6):
    myList.append(random.randint(0, 1000))
print(myList)
