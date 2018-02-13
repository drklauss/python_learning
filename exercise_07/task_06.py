# Пользователь вводит любое целое положительное число (сделать проверку).
# Программа должна просуммировать все числа от 1 до введенного пользователем числа (не включая его).


def sum_numbers(range_end):
    """ Функция суммирует значения от 1 до переданного """
    global sumNumbers
    for i in range(1, range_end):
        sumNumbers += i


x = input('Введите целое положительное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 1:
    print("Число не положительное")
    exit()

sumNumbers = 0
sum_numbers(xInt)
print("Сумма", sumNumbers)

sumNumbers = 0
sum_numbers(xInt)
print("Сумма", sumNumbers)
