# Найдите количество четных цифр введёного натурального числа.

x = input('Введите число: ')
try:
    int(x)
except ValueError:
    print('Введено некорректное число')
    exit()

evenCount = 0
for v in tuple(x):
    if not int(v) % 2:
        evenCount += 1
print(evenCount)

