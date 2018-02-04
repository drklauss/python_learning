# Найдите произведение цифр трехзначного числа, введёного с клавиатуре.

x = input('Введите число: ')
try:
    x = int(x)
except ValueError:
    print('Введено некорректное число')
    exit()

multiply = 1
while x > 10:
    rest = x % 10
    multiply *= rest
    x = x // 10
multiply *= x
print(multiply)
