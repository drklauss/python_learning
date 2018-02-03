# Найдите произведение цифр трехзначного числа, введёного с клавиатуре.

x = input('Введите число: ')
try:
    int(x)
except ValueError:
    print('Введено некорректное число')
    exit()
multiply = 1
for v in tuple(x):
    multiply *= int(v)
print(multiply)

