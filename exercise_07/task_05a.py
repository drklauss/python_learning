# Написать функцию, приминмающую номер месяца и возвращающую время года, которому принадледжит месяц.
# Не забыть про проверки входных данных в самой функции.
# Вызвать функцию в цикле несколько раз для случайных значений номера месяца.


def get_season_name(month_num):
    if 12 < month_num or month_num < 1:
        raise IndexError('Такого месяца нет')
    """Функция возвращает название времени года по номеру месяца"""
    if month_num in (3, 4, 5):
        return 'Весна'
    if month_num in (6, 7, 8):
        return 'Лето'
    if month_num in (9, 10, 11):
        return 'Осень'
    if month_num in (1, 2, 12):
        return 'Зима'


def get_month_num():
    """Функция возвращает введенное с клавиатуры число"""
    return int(input('Номер месяца: '))


for i in range(5):
    num = 0
    try:
        num = get_month_num()
    except ValueError:
        print('Введено некорректное число')
        exit()
    try:
        print(get_season_name(num))
    except IndexError as index_err:
        print(index_err)
