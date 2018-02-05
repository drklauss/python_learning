# Заполнить список из шести элементов произвольными целочисленными значениями.
# Вывести список на экран в обратной последовательности.
# Два варианта получения обратной последовательности: с приминением цикла и без него.

import random

myList = []
ARR_LEN = 6
for i in range(0, ARR_LEN):
    myList.append(random.randint(0, 1000))

# Первый способ
result = []
for i in range(1, ARR_LEN + 1):
    result.append(myList[-i])
print(result)
# Второй способ
print(list(reversed(myList)))
