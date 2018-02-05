# Заполнить список из шести элементов квадратными корнями произвольных целочисленных значений.
# Вывести список на экран через запятую.

import random
import math

ARR_LEN = 6
startList = []
# Я позже увидел как заполняется список генератором, но решил по-старинке
for i in range(0, ARR_LEN):
    startList.append(str(math.sqrt(random.randint(0, 1000))))
print(','.join(startList))


